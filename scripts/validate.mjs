#!/usr/bin/env node
// Validiert data/foods.json. Exit-Code 1 bei Fehlern. Keine Abhängigkeiten.
import { readFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';
import { isValidEan } from '../src/search.mjs';

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
const CUISINES = 'tr de it fr es pt gr gb ie nl be at ch se no dk fi is pl cz sk hu rs hr ba bg al mk si ro ee lv lt ua ru cy mt lu ge am az md by me xk ad li mc sm int'.split(' ');
const QUALITIES = ['estimate', 'verified', 'reference'];
const STATES = ['raw', 'cooked', 'dry', 'dried', 'processed'];
const isNum = (v) => typeof v === 'number' && Number.isFinite(v);
const ids = new Map();
const barcodes = new Map();
const MACROS = ['protein', 'carbs', 'fat', 'fiber'];
data.forEach((e, i) => {
  const ctx = `Eintrag #${i} (${e && e.id ? e.id : '?'})`;
  if (!e || typeof e !== 'object' || Array.isArray(e)) return err(ctx, 'ist kein Objekt');

  if (typeof e.id !== 'string' || !/^[a-z0-9]+(-[a-z0-9]+)*$/.test(e.id)) err(ctx, 'id fehlt oder ist nicht im Format "klein-mit-bindestrich"');
  else if (ids.has(e.id)) err(ctx, `doppelte id (auch Eintrag #${ids.get(e.id)})`);
  else ids.set(e.id, i);

  if (typeof e.name !== 'string' || !e.name.trim()) err(ctx, 'name fehlt');
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
    if (!isNum(p.kcal) || p.kcal < 0 || p.kcal > 950) err(ctx, `kcal ${p.kcal} ungültig (0–950)`);
    for (const m of MACROS) {
      if (!isNum(p[m]) || p[m] < 0 || p[m] > 100) err(ctx, `${m} ${p[m]} ungültig (0–100 pro 100 g)`);
    }
    if ('sugar' in p) {
      // Optional. Bei USDA-Daten kann Zucker (gemessen) leicht über Kohlenhydraten (Differenzrechnung) liegen, z. B. Milch.
      if (!isNum(p.sugar) || p.sugar < 0 || p.sugar > 100) err(ctx, `sugar ${p.sugar} ungültig (0–100 pro 100 g)`);
    }
    if (MACROS.every((m) => isNum(p[m]))) {
      // 0,15 g Rundungstoleranz: Referenzdaten (z. B. USDA Leinöl 0,11 g Eiweiß + 99,98 g Fett) summieren teils knapp über 100 g.
      if (p.protein + p.carbs + p.fat > 100.15) err(ctx, `Protein+Kohlenhydrate+Fett = ${(p.protein + p.carbs + p.fat).toFixed(1)} g > 100 g`);
      if (p.fiber > p.carbs + 0.0001 && p.fiber > 0) {
        // Ballaststoffe zählen oft separat; nur Warnung, kein Fehler
        console.warn(`! ${ctx}: Ballaststoffe (${p.fiber}) > Kohlenhydrate (${p.carbs}) – bitte prüfen`);
      }
      if (isNum(p.kcal)) {
        const est = p.protein * 4 + p.carbs * 4 + p.fat * 9;
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
  if ('source_missing' in e && (!Array.isArray(e.source_missing) || e.source_missing.some((k) => !['fiber', 'sugar'].includes(k)))) err(ctx, 'source_missing darf nur "fiber"/"sugar" enthalten');
  if ('is_packaged_product' in e && typeof e.is_packaged_product !== 'boolean') err(ctx, 'is_packaged_product muss true/false sein');
  if (e.is_packaged_product === true && e.type === 'dish') err(ctx, 'ein Gericht (type "dish") darf nicht is_packaged_product=true sein');
  if ('off_similar' in e) {
    if (!Array.isArray(e.off_similar) || e.off_similar.length > 3 || e.off_similar.some((c) => typeof c !== 'string' || !/^\d{6,14}$/.test(c))) err(ctx, 'off_similar muss ein Array von höchstens 3 Barcode-Strings (nur Ziffern) sein');
  }

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
