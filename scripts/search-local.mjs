#!/usr/bin/env node
// Lokale Suche per CLI mit demselben Modul wie die API.
//   node scripts/search-local.mjs karniyarik
//   node scripts/search-local.mjs "Karnıyarık"
//   node scripts/search-local.mjs karniyark --limit 3 --json
import { readFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';
import { buildIndex, search, findByBarcode, isValidEan } from '../src/search.mjs';

const root = join(dirname(fileURLToPath(import.meta.url)), '..');
const foods = JSON.parse(readFileSync(join(root, 'data', 'foods.json'), 'utf8'));

const args = process.argv.slice(2);
let limit = 10, json = false, barcode = null;
const words = [];
for (let i = 0; i < args.length; i++) {
  if (args[i] === '--limit') limit = Number(args[++i]) || 10;
  else if (args[i] === '--json') json = true;
  else if (args[i] === '--barcode') barcode = args[++i];
  else words.push(args[i]);
}

const fmt = (f) => `${f.name} [${f.cuisine || '?'} · ${f.category || f.type}${f.prepared ? ' · ' + f.prepared : ''}]${f.barcode ? ' ' + f.barcode : ''} – ${f.per100g.kcal} kcal | P ${f.per100g.protein} | KH ${f.per100g.carbs} | F ${f.per100g.fat} | BS ${f.per100g.fiber} (pro 100 g)${f.quality ? ' · ' + f.quality : ''}`;

let results;
if (barcode) {
  if (!isValidEan(barcode)) console.error(`Hinweis: "${barcode}" hat keine gültige EAN-Prüfziffer.`);
  const hit = findByBarcode(foods, barcode);
  results = hit ? [hit] : [];
} else {
  if (!words.length) { console.error('Nutzung: node scripts/search-local.mjs <suchbegriff> [--limit N] [--json] | --barcode <EAN>'); process.exit(2); }
  results = search(buildIndex(foods), words.join(' '), limit);
}

if (json) console.log(JSON.stringify(results, null, 2));
else if (!results.length) console.log('Keine Treffer.');
else results.forEach((f) => console.log('• ' + fmt(f)));
