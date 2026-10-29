// Gemeinsames Such-Modul: wird von der Cloudflare-Worker-API UND der lokalen CLI genutzt.
// Keine Abhängigkeiten, reines ES-Modul.

/**
 * Normalisiert Text für die Suche: klein, ohne Akzente, Umlaute vereinheitlicht.
 * ä/ae -> a, ö/oe -> o, ü/ue -> u, ß/ss -> ss, türkisches ı/İ -> i.
 * ş, ğ, ç und weitere Akzente fallen über NFD weg (ş -> s, ğ -> g, ç -> c).
 * ø/æ/œ/đ/ł/þ werden ebenfalls auf lateinische Grundbuchstaben gefaltet.
 * So findet "karniyarik" auch "Karnıyarık", "aepfel" auch "Äpfel" und "calabacin" auch "Calabacín".
 * Die Normalisierung ist verlustbehaftet, aber auf beiden Seiten (Daten + Suchbegriff) gleich.
 */
export function normalize(text) {
  return String(text ?? '')
    .replace(/İ/g, 'i').replace(/ı/g, 'i')
    .toLowerCase()
    .replace(/ß/g, 'ss')
    .replace(/ä/g, 'ae').replace(/ö/g, 'oe').replace(/ü/g, 'ue')
    .replace(/ı/g, 'i')
    .replace(/ø/g, 'o').replace(/æ/g, 'ae').replace(/œ/g, 'oe').replace(/đ/g, 'd').replace(/ł/g, 'l').replace(/þ/g, 'th')
    .normalize('NFD').replace(/[\u0300-\u036f]/g, '') // übrige Akzente (é, è, ş, ğ, ç, ...)
    .replace(/ae/g, 'a').replace(/oe/g, 'o').replace(/ue/g, 'u')
    // Buchstaben/Ziffern aller Schriften bleiben erhalten (z. B. Chinesisch 番茄), Satzzeichen werden zu Leerzeichen.
    .replace(/[^\p{L}\p{N}]+/gu, ' ')
    .trim();
}

/** Levenshtein-Distanz mit frühem Abbruch (max). Gibt max+1 zurück, wenn größer. */
export function levenshtein(a, b, max = 2) {
  if (a === b) return 0;
  if (Math.abs(a.length - b.length) > max) return max + 1;
  let prev = Array.from({ length: b.length + 1 }, (_, i) => i);
  for (let i = 1; i <= a.length; i++) {
    const cur = [i];
    let rowMin = i;
    for (let j = 1; j <= b.length; j++) {
      const cost = a[i - 1] === b[j - 1] ? 0 : 1;
      cur[j] = Math.min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + cost);
      if (cur[j] < rowMin) rowMin = cur[j];
    }
    if (rowMin > max) return max + 1;
    prev = cur;
  }
  return prev[b.length];
}

/** Erlaubte Tippfehler je nach Länge des Suchbegriffs. */
export function maxTypos(len) {
  if (len < 3) return 0;
  if (len < 6) return 1;
  return 2;
}

/**
 * Bewertet einen Suchbegriff-Token gegen einen normalisierten Text.
 * Rückgabe: Rang (kleiner = besser) oder null.
 *  0 = exakt, 1 = Präfix des ganzen Textes, 2 = Präfix eines Wortes,
 *  3 = Teilstring, 4+ = Tippfehler (4 + Distanz)
 */
export function scoreToken(token, text) {
  if (!token || !text) return null;
  if (text === token) return 0;
  if (text.startsWith(token)) return 1;
  const words = text.split(' ');
  if (words.some((w) => w.startsWith(token))) return 2;
  if (text.includes(token)) return 3;
  const allowed = maxTypos(token.length);
  if (allowed === 0) return null;
  let best = Infinity;
  for (const w of words) {
    // Ganzes Wort ODER gleich langer Wortanfang (so passt "apfl" auch zu "apfelmus")
    const d = Math.min(
      levenshtein(token, w, allowed),
      w.length > token.length ? levenshtein(token, w.slice(0, token.length), allowed) : Infinity,
      w.length > token.length ? levenshtein(token, w.slice(0, token.length + 1), allowed) : Infinity,
    );
    if (d < best) best = d;
  }
  return best <= allowed ? 4 + best : null;
}

/**
 * Wort-Rang für die mehrsprachige Suche: 0 = ganzes Wort, 1 = Wortanfang, 2 = Teilstring, 3+ = Tippfehler.
 * (Feiner als scoreToken bei ganzen Wörtern: "Reis" passt besser zu "Reis, gekocht" als zu "Reisnudeln".)
 */
export function wordRank(token, text) {
  const sc = scoreToken(token, text);
  if (sc === null) return null;
  if (sc <= 2) return sc === 0 || text.split(' ').includes(token) ? 0 : 1;
  return sc - 1;
}

/** Sprachen der mehrsprachigen Namen (`names`); die ersten sechs sind Pflicht. */
export const LANGS = ['de', 'en', 'tr', 'fr', 'es', 'pt', 'it', 'zh'];
export const REQUIRED_LANGS = ['de', 'en', 'tr', 'fr', 'es', 'pt'];

const uniq = (arr) => [...new Set(arr.filter(Boolean))];

/**
 * Bereitet die Daten einmalig auf (normalisierte Texte).
 * Haupttexte: `name` + alle `names.*`; Nebentexte: `synonyms` + alle `aliases.*`.
 */
export function buildIndex(foods) {
  const index = foods.map((food) => {
    const names = Object.values(food.names || {}).map(normalize);
    const aliases = Object.values(food.aliases || {}).flat().map(normalize);
    const name = normalize(food.name);
    const primary = uniq([name, ...names]);
    // Kopfwort = Teil vor Komma/Klammer: "Tomate, roh" → "tomate", "番茄（生）" → "番茄".
    const head = (t) => normalize(String(t).split(/[,，(（]/)[0]);
    const heads = uniq([food.name, ...Object.values(food.names || {})].map(head));
    return {
      food,
      name,
      primary,
      heads,
      raw: food.state === 'raw',
      synonyms: uniq([...(food.synonyms || []).map(normalize), ...aliases]).filter((t) => !primary.includes(t)),
    };
  });
  // Wortverzeichnis: Wort → Einträge. Die Suche prüft Tippfehler einmal pro Wort statt pro Eintrag und Sprache.
  const vocab = new Map();
  index.forEach((entry, i) => {
    for (const t of [...entry.primary, ...entry.synonyms]) {
      for (const w of t.split(' ')) {
        if (!w) continue;
        let set = vocab.get(w);
        if (!set) vocab.set(w, (set = new Set()));
        set.add(i);
      }
    }
  });
  Object.defineProperty(index, 'vocab', { value: vocab, enumerable: false });
  return index;
}

/** Anzeigename in einer Sprache (Fallback: `name`). */
export function displayName(food, lang) {
  return (lang && food.names && food.names[lang]) || food.name;
}

/**
 * Suche über alle Sprachen. Sortierung: exakt, Präfix, Teilstring, dann Tippfehler.
 * Bei mehreren Wörtern müssen alle Wörter treffen (in Name, einem Sprachnamen, Alias oder Synonym).
 * Optional `lang`: Treffer im Namen dieser Sprache werden bei Gleichstand bevorzugt.
 */
export function search(index, query, limit = 10, lang = null) {
  const q = normalize(query);
  if (!q) return [];
  const tokens = q.split(' ');
  const results = [];
  // Kandidaten: Einträge, in denen jedes Wort des Suchbegriffs zu mindestens einem Wort passt.
  let candidates = null;
  if (index.vocab) {
    for (const token of tokens) {
      const hits = new Set();
      for (const [w, set] of index.vocab) {
        if (scoreToken(token, w) !== null) for (const i of set) hits.add(i);
      }
      candidates = candidates ? new Set([...candidates].filter((i) => hits.has(i))) : hits;
      if (!candidates.size) return [];
    }
  }
  const pool = candidates ? [...candidates].sort((a, b) => a - b).map((i) => index[i]) : index;
  for (const entry of pool) {
    let total = 0;
    let viaSynonym = false;
    let ok = true;
    for (const token of tokens) {
      let best = null;
      let syn = false;
      for (const t of entry.primary) {
        const sc = wordRank(token, t);
        if (sc !== null && (best === null || sc < best)) best = sc;
        if (best === 0) break;
      }
      if (best !== 0) {
        for (const s of entry.synonyms) {
          const sc = wordRank(token, s);
          if (sc !== null && (best === null || sc < best)) { best = sc; syn = true; }
        }
      }
      if (best === null) { ok = false; break; }
      total = Math.max(total, best);
      if (syn) viaSynonym = true;
    }
    if (!ok) continue;
    // Stufen: 0 = ganzer Begriff gleich einem Namen, 1 = gleich dem Kopfwort eines Namens ("Domates" → "Domates, çiğ"),
    // 2 = gleich einem Synonym/Alias, sonst nach Wort-Rang (Präfix, Teilstring, Tippfehler).
    let score;
    if (entry.primary.includes(q)) score = 0;
    else if (entry.heads.includes(q)) score = 1;
    else if (entry.synonyms.includes(q)) score = 2;
    else score = 10 + total * 10 + (viaSynonym ? 1 : 0);
    const shown = lang ? normalize(displayName(entry.food, lang)) : entry.name;
    if (lang && !tokens.every((tk) => { const sc = scoreToken(tk, shown); return sc !== null && sc <= 3; })) score += 5;
    // Länge des kürzesten Namens, in dem alle Wörter vorkommen (sonst Anzeigename).
    let len = shown.length;
    for (const t of entry.primary) {
      if (t.length < len && tokens.every((tk) => { const sc = scoreToken(tk, t); return sc !== null && sc <= 3; })) len = t.length;
    }
    // Bei Gleichstand: rohe Grundzutat vor anderen Grundzutaten vor Gerichten.
    const kind = entry.food.prepared === 'base_ingredient' ? (entry.raw ? 0 : 1) : 2;
    results.push({ food: entry.food, score, kind, len });
  }
  results.sort((a, b) => a.score - b.score || a.kind - b.kind || a.len - b.len || a.food.name.localeCompare(b.food.name, 'de'));
  return results.slice(0, Math.max(1, Math.min(limit, 50))).map((r) => r.food);
}

/** Prüfziffer für EAN-8 / EAN-13 (GTIN). */
export function isValidEan(code) {
  if (typeof code !== 'string' || !/^(\d{8}|\d{13})$/.test(code)) return false;
  const digits = code.split('').map(Number);
  const check = digits.pop();
  let sum = 0;
  digits.reverse().forEach((d, i) => { sum += d * (i % 2 === 0 ? 3 : 1); });
  return (10 - (sum % 10)) % 10 === check;
}

export function findByBarcode(foods, code) {
  const c = String(code ?? '').replace(/\s+/g, '');
  return foods.find((f) => f.barcode === c) || null;
}
