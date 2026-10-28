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

  const p = e.per100g;
  if (!p || typeof p !== 'object') err(ctx, 'per100g fehlt');
  else {
    if (!isNum(p.kcal) || p.kcal < 0 || p.kcal > 950) err(ctx, `kcal ${p.kcal} ungültig (0–950)`);
    for (const m of MACROS) {
      if (!isNum(p[m]) || p[m] < 0 || p[m] > 100) err(ctx, `${m} ${p[m]} ungültig (0–100 pro 100 g)`);
    }
    if (MACROS.every((m) => isNum(p[m]))) {
      if (p.protein + p.carbs + p.fat > 100.0001) err(ctx, `Protein+Kohlenhydrate+Fett = ${(p.protein + p.carbs + p.fat).toFixed(1)} g > 100 g`);
      if (p.fiber > p.carbs + 0.0001 && p.fiber > 0) {
        // Ballaststoffe zählen oft separat; nur Warnung, kein Fehler
        console.warn(`! ${ctx}: Ballaststoffe (${p.fiber}) > Kohlenhydrate (${p.carbs}) – bitte prüfen`);
      }
      if (isNum(p.kcal)) {
        const est = p.protein * 4 + p.carbs * 4 + p.fat * 9;
        if (Math.abs(est - p.kcal) > Math.max(60, p.kcal * 0.35)) console.warn(`! ${ctx}: kcal (${p.kcal}) weicht stark von Makro-Schätzung (${est.toFixed(0)}) ab – bitte prüfen`);
      }
    }
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
