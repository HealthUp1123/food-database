// Gemeinsames Such-Modul: wird von der Cloudflare-Worker-API UND der lokalen CLI genutzt.
// Keine Abhängigkeiten, reines ES-Modul.

/**
 * Normalisiert Text für die Suche: klein, ohne Akzente, Umlaute vereinheitlicht.
 * ä/ae -> a, ö/oe -> o, ü/ue -> u, ß/ss -> ss. So findet "aepfel" auch "Äpfel"/"Apfel".
 * Die Normalisierung ist verlustbehaftet, aber auf beiden Seiten (Daten + Suchbegriff) gleich.
 */
export function normalize(text) {
  return String(text ?? '')
    .toLowerCase()
    .replace(/ß/g, 'ss')
    .replace(/ä/g, 'ae').replace(/ö/g, 'oe').replace(/ü/g, 'ue')
    .normalize('NFD').replace(/[\u0300-\u036f]/g, '') // übrige Akzente (é, è, ...)
    .replace(/ae/g, 'a').replace(/oe/g, 'o').replace(/ue/g, 'u')
    .replace(/[^a-z0-9]+/g, ' ')
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

/** Bereitet die Daten einmalig auf (normalisierte Namen/Synonyme). */
export function buildIndex(foods) {
  return foods.map((food) => ({
    food,
    name: normalize(food.name),
    synonyms: (food.synonyms || []).map(normalize).filter(Boolean),
  }));
}

/**
 * Suche. Sortierung: Präfix-Treffer zuerst, dann Teilstring, dann Tippfehler.
 * Bei mehreren Wörtern müssen alle Wörter treffen.
 */
export function search(index, query, limit = 10) {
  const q = normalize(query);
  if (!q) return [];
  const tokens = q.split(' ');
  const results = [];
  for (const entry of index) {
    let total = 0;
    let viaSynonym = false;
    let ok = true;
    for (const token of tokens) {
      const nameScore = scoreToken(token, entry.name);
      let best = nameScore;
      let syn = false;
      for (const s of entry.synonyms) {
        const sc = scoreToken(token, s);
        if (sc !== null && (best === null || sc < best)) { best = sc; syn = true; }
      }
      if (best === null) { ok = false; break; }
      total = Math.max(total, best);
      if (syn) viaSynonym = true;
    }
    if (!ok) continue;
    results.push({ food: entry.food, score: total * 10 + (viaSynonym ? 1 : 0), len: entry.name.length });
  }
  results.sort((a, b) => a.score - b.score || a.len - b.len || a.food.name.localeCompare(b.food.name, 'de'));
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
