#!/usr/bin/env node
// Prüft die App-Datei: (1) entspricht exakt dem Build aus foods.json, (2) decode() liefert dieselben Kernwerte,
// (3) die Suche über die dekodierten Einträge liefert dieselben Top 10 wie über foods.json (Stichprobe, alle Sprachen).
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { build } from './build-app.mjs';
import { decode } from '../src/app-decoder.mjs';
import { buildIndex, search } from '../src/search.mjs';

const root = new URL('..', import.meta.url);
const full = JSON.parse(readFileSync(new URL('data/foods.json', root), 'utf8'));
const appText = readFileSync(new URL('data/foods.app.json', root), 'utf8');
assert.equal(appText, build(full), 'data/foods.app.json ist nicht aktuell – `npm run build:app` ausführen');

const app = decode(JSON.parse(appText));
assert.equal(app.length, full.length);
const r1 = (v) => Math.round(v * 10) / 10;
full.forEach((f, i) => {
  const a = app[i];
  assert.equal(a.id, f.id); assert.equal(a.name, f.name); assert.deepEqual(a.names, f.names);
  assert.equal(a.type, f.type); assert.equal(a.cuisine, f.cuisine);
  assert.equal(a.per100g.kcal, Math.round(f.per100g.kcal));
  for (const k of ['protein', 'carbs', 'fat', 'fiber']) assert.equal(a.per100g[k], r1(f.per100g[k]), `${f.id} ${k}`);
  assert.deepEqual(a.aliases, f.aliases || {});
  assert.equal(a.prepared === 'base_ingredient', f.prepared === 'base_ingredient');
  assert.equal(a.state === 'raw', f.state === 'raw');
});

const A = buildIndex(full), B = buildIndex(app);
const STEP = Number(process.env.APP_TEST_STEP || 400); // jeder 400. Eintrag; APP_TEST_STEP=1 prüft alle
const qs = ['Fritten', 'Kartoffelpuffer', 'Reibekuchen', 'Tomatte', 'domates', 'Semmel', 'Schrippe', 'Topfen', 'Bulette', 'Kartofel',
  'Patates mücveri', 'Köfte', 'Döner', 'apfel', 'reis gekocht', 'pomes', 'brot', 'milch', 'käse', 'ayran', 'lahmacun', 'knoblauch'];
full.forEach((f, i) => { if (i % STEP === 0) for (const l of ['de', 'en', 'tr']) {
  const n = f.names[l]; qs.push(n); if (n.length > 4) qs.push(n.slice(0, 2) + n[3] + n[2] + n.slice(4));
} });
let n = 0;
for (const q of qs) for (const lang of ['de', 'tr', 'en', null]) {
  n++;
  const a = search(A, q, 10, lang).map((r) => (r.food || r).id), b = search(B, q, 10, lang).map((r) => (r.food || r).id);
  assert.deepEqual(b, a, `Suche "${q}" (${lang}): Top 10 weichen ab`);
}
console.log(`✓ App-Datei aktuell, ${app.length} Einträge dekodiert, ${n} Suchen mit identischen Top 10`);
