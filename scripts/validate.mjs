#!/usr/bin/env node
// Validiert data/foods.json. Exit-Code 1 bei Fehlern. Keine Abhängigkeiten.
import { readFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';
import { isValidEan, LANGS, REQUIRED_LANGS } from '../src/search.mjs';

const root = join(dirname(fileURLToPath(import.meta.url)), '..');
const file = process.argv[2] || join(root, 'data', 'foods.json');
const errors = [];
const err = (ctx, msg) => errors.push(`${ctx}: ${msg}`);

let data;
try {
  data = JSON.parse(readFileSync(file, 'utf8'));
} catch (e) {
  console.error(`✗ ${file} konnte nicht gelesen/geparst werden: ${e.message}`);
  process.exit(1);
}
if (!Array.isArray(data)) {
  console.error('✗ foods.json muss ein Array sein.');
  process.exit(1);
}

// "int" = international/ohne Landesküche (Grundzutaten wie Tomate, Reis, Hähnchenbrust).
const CUISINES = 'tr de it fr es pt gr gb ie nl be at ch se no dk fi is pl cz sk hu rs hr ba bg al mk si ro ee lv lt ua ru cy mt lu ge am az md by me xk ad li mc sm cn jp kr th vn in id int'.split(' ');
const QUALITIES = ['estimate', 'verified', 'reference'];
// Zubereitungszustand: roh/trocken, gegart (cooked = gekocht/gedünstet/gedämpft/geschmort), gegrillt, gebraten/frittiert,
// im Ofen gebacken/gebraten, geröstet, getrocknet, tiefgekühlt, Konserve (Dose/Glas), geräuchert, verarbeitet (Saft, Mark, Püree, Pulver).
const STATES = ['raw', 'cooked', 'grilled', 'fried', 'baked', 'roasted', 'dry', 'dried', 'frozen', 'canned', 'smoked', 'processed'];
const isNum = (v) => typeof v === 'number' && Number.isFinite(v);
const ids = new Map();
const barcodes = new Map();
const MACROS = ['protein', 'carbs', 'fat', 'fiber'];
const allIds = new Set(data.map((e) => e && e.id));
data.forEach((e, i) => {
  const ctx = `Eintrag #${i} (${e && e.id ? e.id : '?'})`;
  if (!e || typeof e !== 'object' || Array.isArray(e)) return err(ctx, 'ist kein Objekt');

  if (typeof e.id !== 'string' || !/^[a-z0-9]+(-[a-z0-9]+)*$/.test(e.id)) err(ctx, 'id fehlt oder ist nicht im Format "klein-mit-bindestrich"');
  else if (ids.has(e.id)) err(ctx, `doppelte id (auch Eintrag #${ids.get(e.id)})`);
  else ids.set(e.id, i);

  if (typeof e.name !== 'string' || !e.name.trim()) err(ctx, 'name fehlt');
  // Mehrsprachige Namen: nur de/en/tr, alle drei Pflicht (andere Sprachen sind nicht erlaubt). Etablierte Gerichtsnamen dürfen in allen Sprachen gleich sein.
  if (!e.names || typeof e.names !== 'object' || Array.isArray(e.names)) err(ctx, `names fehlt (Objekt mit ${REQUIRED_LANGS.join('/')})`);
  else {
    for (const l of REQUIRED_LANGS) if (typeof e.names[l] !== 'string' || !e.names[l].trim()) err(ctx, `names.${l} fehlt oder ist leer`);
    for (const [l, v] of Object.entries(e.names)) {
      if (!LANGS.includes(l)) err(ctx, `names.${l}: unbekannte Sprache (erlaubt: ${LANGS.join(', ')})`);
      else if (typeof v !== 'string' || !v.trim() || v !== v.trim()) err(ctx, `names.${l} muss ein nicht-leerer String ohne Rand-Leerzeichen sein`);
    }
  }
  if ('aliases' in e) {
    if (!e.aliases || typeof e.aliases !== 'object' || Array.isArray(e.aliases)) err(ctx, 'aliases muss ein Objekt {sprache: [..]} sein');
    else for (const [l, arr] of Object.entries(e.aliases)) {
      if (!LANGS.includes(l)) err(ctx, `aliases.${l}: unbekannte Sprache`);
      else if (!Array.isArray(arr) || !arr.length || arr.some((a) => typeof a !== 'string' || !a.trim())) err(ctx, `aliases.${l} muss ein nicht-leeres Array nicht-leerer Strings sein`);
      else if (new Set(arr).size !== arr.length) err(ctx, `aliases.${l} enthält Duplikate`);
    }
  }
  if (!['item', 'dish'].includes(e.type)) err(ctx, 'type muss "item" oder "dish" sein');

  if (!('barcode' in e)) err(ctx, 'barcode fehlt (string oder null)');
  else if (e.barcode !== null) {
    if (typeof e.barcode !== 'string') err(ctx, 'barcode muss String oder null sein');
    else if (!isValidEan(e.barcode)) err(ctx, `barcode "${e.barcode}" ist kein gültiger EAN-8/EAN-13 (Länge oder Prüfziffer)`);
    else if (barcodes.has(e.barcode)) err(ctx, `doppelter barcode ${e.barcode} (auch Eintrag #${barcodes.get(e.barcode)})`);
    else barcodes.set(e.barcode, i);
  }

  if (!Array.isArray(e.synonyms) || e.synonyms.some((s) => typeof s !== 'string' || !s.trim())) err(ctx, 'synonyms muss ein Array nicht-leerer Strings sein');

  if (!CUISINES.includes(e.cuisine)) err(ctx, `cuisine "${e.cuisine}" unbekannt (erlaubte Ländercodes)`);
  if (typeof e.category !== 'string' || !e.category.trim()) err(ctx, 'category fehlt');

  if (!Array.isArray(e.ingredients) || e.ingredients.length === 0) err(ctx, 'ingredients muss ein nicht-leeres Array sein');
  else e.ingredients.forEach((ing, j) => {
    if (!ing || typeof ing !== 'object' || Array.isArray(ing)) return err(ctx, `ingredients[${j}] ist kein Objekt`);
    if (typeof ing.name !== 'string' || !ing.name.trim()) err(ctx, `ingredients[${j}].name fehlt`);
    if (!isNum(ing.grams) || ing.grams <= 0) err(ctx, `ingredients[${j}].grams muss eine Zahl > 0 sein`);
  });

  if (!QUALITIES.includes(e.quality)) err(ctx, 'quality muss "estimate", "verified" oder "reference" sein');
  if (typeof e.source !== 'string' || !e.source.trim()) err(ctx, 'source fehlt (Herkunft der Nährwerte)');

  const p = e.per100g;
  if (!p || typeof p !== 'object') err(ctx, 'per100g fehlt');
  else {
    // Pflicht: kcal, protein, carbs, fat, fiber sind in JEDEM Eintrag vorhanden und Zahlen (null/fehlend = Fehler).
    for (const k of ['kcal', ...MACROS]) if (!(k in p) || !isNum(p[k])) err(ctx, `per100g.${k} fehlt oder ist keine Zahl (Pflichtfeld)`);
    if (isNum(p.kcal) && (p.kcal < 0 || p.kcal > 950)) err(ctx, `kcal ${p.kcal} ungültig (0–950)`);
    for (const m of MACROS) {
      if (isNum(p[m]) && (p[m] < 0 || p[m] > 100)) err(ctx, `${m} ${p[m]} ungültig (0–100 pro 100 g)`);
    }
    if ('sugar' in p) {
      // Optional. Bei USDA-Daten kann Zucker (gemessen) leicht über Kohlenhydraten (Differenzrechnung) liegen, z. B. Milch.
      if (!isNum(p.sugar) || p.sugar < 0 || p.sugar > 100) err(ctx, `sugar ${p.sugar} ungültig (0–100 pro 100 g)`);
    }
    if ('alcohol' in p) {
      // Optional: Alkohol (Ethanol) in g pro 100 g, z. B. Bier ≈ 3,8, Wein ≈ 9–10, Spirituosen ≈ 30–35.
      if (!isNum(p.alcohol) || p.alcohol < 0 || p.alcohol > 100) err(ctx, `alcohol ${p.alcohol} ungültig (0–100 g pro 100 g)`);
    }
    if (MACROS.every((m) => isNum(p[m]))) {
      // 0,15 g Rundungstoleranz: Referenzdaten (z. B. USDA Leinöl 0,11 g Eiweiß + 99,98 g Fett) summieren teils knapp über 100 g.
      if (p.protein + p.carbs + p.fat > 100.15) err(ctx, `Protein+Kohlenhydrate+Fett = ${(p.protein + p.carbs + p.fat).toFixed(1)} g > 100 g`);
      if (p.fiber > p.carbs + 0.0001 && p.fiber > 0) {
        // Ballaststoffe zählen oft separat; nur Warnung, kein Fehler
        console.warn(`! ${ctx}: Ballaststoffe (${p.fiber}) > Kohlenhydrate (${p.carbs}) – bitte prüfen`);
      }
      if (isNum(p.kcal)) {
        // Ist per100g.alcohol gesetzt, zählt Ethanol mit 7 kcal/g in die Schätzung.
        const est = p.protein * 4 + p.carbs * 4 + p.fat * 9 + (isNum(p.alcohol) ? p.alcohol * 7 : 0);
        // Alkohol (Wein, Spirituosen) liegt oft über der 4/4/9-Schätzung (Ethanol ≈ 7 kcal/g).
        // Das ist eine Warnung, kein Fehler.
        if (Math.abs(est - p.kcal) > Math.max(60, p.kcal * 0.35)) console.warn(`! ${ctx}: kcal (${p.kcal}) weicht stark von Makro-Schätzung (${est.toFixed(0)}) ab – bitte prüfen`);
      }
    }
  }

  // Optionale Felder (Gericht vs. Fertigprodukt, Hinweis auf ähnliche OFF-Produkte)
  if ('prepared' in e && !['homemade', 'restaurant', 'base_ingredient'].includes(e.prepared)) err(ctx, 'prepared muss "homemade", "restaurant" oder "base_ingredient" sein');
  if (e.prepared === 'base_ingredient') {
    // Grundzutat (z. B. Tomate roh, Reis gekocht): kein Gericht, kein Fertigprodukt, Referenzwerte pro 100 g.
    if (e.type !== 'item') err(ctx, 'Grundzutat (prepared "base_ingredient") braucht type "item"');
    if (e.is_packaged_product !== false) err(ctx, 'Grundzutat braucht is_packaged_product: false');
    if (e.barcode !== null) err(ctx, 'Grundzutat hat keinen Barcode (barcode: null)');
  }
  if ('state' in e && !STATES.includes(e.state)) err(ctx, `state muss einer von ${STATES.join(', ')} sein`);
  if ('unit' in e && e.unit !== 'g') err(ctx, 'unit muss "g" sein (Nährwerte pro 100 g)');
  if ('note' in e && (typeof e.note !== 'string' || !e.note.trim())) err(ctx, 'note muss ein nicht-leerer String sein');
  if ('fdc_id' in e && (!Number.isInteger(e.fdc_id) || e.fdc_id <= 0)) err(ctx, 'fdc_id muss eine positive Ganzzahl sein (USDA FoodData Central)');
  if ('source_id' in e && (typeof e.source_id !== 'string' || !e.source_id.trim())) err(ctx, 'source_id muss ein nicht-leerer String sein (Datenbank:Code, z. B. "BLS 4.0:G582172")');
  // Fehlt ein Wert in der Quelle, steht er hier (bei protein/fat/fiber ist dann 0 eingetragen, sugar fehlt dann ganz).
  if ('source_missing' in e && (!Array.isArray(e.source_missing) || e.source_missing.some((k) => !['protein', 'fat', 'fiber', 'sugar'].includes(k)))) err(ctx, 'source_missing darf nur "protein"/"fat"/"fiber"/"sugar" enthalten');
  if ('derived_from' in e) {
    const d = e.derived_from;
    const ok = (v) => typeof v === 'string' && v.trim() !== '';
    if (!(ok(d) || (Array.isArray(d) && d.length > 0 && d.every(ok)))) err(ctx, 'derived_from muss eine ID/Quellkennung (String) oder ein nicht-leeres Array davon sein');
    if (e.quality !== 'estimate') err(ctx, 'derived_from nur bei quality "estimate"');
  }
  if ('method' in e && !['yield_factor', 'similar_food', 'recipe'].includes(e.method)) err(ctx, 'method muss "yield_factor", "similar_food" oder "recipe" sein');
  if ('is_packaged_product' in e && typeof e.is_packaged_product !== 'boolean') err(ctx, 'is_packaged_product muss true/false sein');
  if (e.is_packaged_product === true && e.type === 'dish') err(ctx, 'ein Gericht (type "dish") darf nicht is_packaged_product=true sein');
  if ('off_similar' in e) {
    if (!Array.isArray(e.off_similar) || e.off_similar.length > 3 || e.off_similar.some((c) => typeof c !== 'string' || !/^\d{6,14}$/.test(c))) err(ctx, 'off_similar muss ein Array von höchstens 3 Barcode-Strings (nur Ziffern) sein');
  }

  // ---- Welle 5: Ausbeute roh→gekocht, Salz/ges. Fettsäuren (alle optional) ----
  if ('portions' in e) err(ctx, 'portions wird nicht mehr verwendet (entfernt); typische Portion steht in portion');
  if ('yield' in e) {
    const y = e.yield;
    if (!y || !isNum(y.factor) || y.factor <= 0 || y.factor > 15 || y.from !== 'raw' || y.to !== 'cooked' || typeof y.source !== 'string' || !y.source.trim()) err(ctx, 'yield braucht {factor: Zahl > 0, from: "raw", to: "cooked", source}');
    if (!('cooked_id' in e)) err(ctx, 'yield braucht cooked_id');
  }
  for (const k of ['raw_id', 'cooked_id']) {
    if (k in e && (typeof e[k] !== 'string' || !allIds.has(e[k]) || e[k] === e.id)) err(ctx, `${k} "${e[k]}" verweist auf keine andere vorhandene id`);
  }
  if (p && typeof p === 'object') {
    if ('salt' in p && (!isNum(p.salt) || p.salt < 0 || p.salt > 100)) err(ctx, `salt ${p.salt} ungültig (0–100 g pro 100 g)`);
    if ('sat_fat' in p && (!isNum(p.sat_fat) || p.sat_fat < 0 || p.sat_fat > p.fat + 0.05)) err(ctx, `sat_fat ${p.sat_fat} ungültig (0 bis fat)`);
  }
  if ('nutrient_basis' in e) {
    const nb = e.nutrient_basis;
    if (!nb || typeof nb !== 'object' || Array.isArray(nb) || !Object.keys(nb).length) err(ctx, 'nutrient_basis muss ein nicht-leeres Objekt sein');
    else for (const [k, v] of Object.entries(nb)) {
      if (!['salt', 'sat_fat', 'sugar'].includes(k)) err(ctx, `nutrient_basis.${k}: unbekanntes Feld`);
      else if (!['source', 'recipe_estimate'].includes(v)) err(ctx, `nutrient_basis.${k} muss "source" oder "recipe_estimate" sein`);
      else if (!(p && k in p)) err(ctx, `nutrient_basis.${k} ohne Wert in per100g`);
    }
  }
  for (const k of ['salt', 'sat_fat']) if (p && k in p && !(e.nutrient_basis && e.nutrient_basis[k])) err(ctx, `per100g.${k} braucht nutrient_basis.${k}`);
  // Seit der schlanken Welle 5 entfernt: Allergene und redaktionelle Beliebtheit.
  for (const k of ['allergens', 'allergens_basis', 'popularity']) if (k in e) err(ctx, `${k} wird nicht mehr verwendet (entfernt)`);
  // Fehlt protein/fat/fiber in der Quelle, steht 0 in per100g (nur bei Getränken bzw. ballaststofffreien Tierprodukten).
  if (p && Array.isArray(e.source_missing)) for (const k of ['protein', 'fat', 'fiber']) if (e.source_missing.includes(k) && p[k] !== 0) err(ctx, `source_missing enthält ${k}, dann muss per100g.${k} 0 sein`);

  if ('portion' in e && e.portion !== undefined) {
    const po = e.portion;
    if (!po || typeof po.label !== 'string' || !po.label.trim() || !isNum(po.grams) || po.grams <= 0 || po.grams > 5000) err(ctx, 'portion braucht {label: string, grams: Zahl > 0}');
  }
});

if (errors.length) {
  console.error(`✗ ${errors.length} Fehler in ${data.length} Einträgen:`);
  errors.forEach((m) => console.error('  - ' + m));
  process.exit(1);
}
console.log(`✓ ${data.length} Einträge gültig (${ids.size} IDs, ${barcodes.size} Barcodes).`);
