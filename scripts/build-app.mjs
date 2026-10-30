#!/usr/bin/env node
// Erzeugt data/foods.app.json (kompakte App-Datei, Format A4) aus data/foods.json.
//   npm run build:app            -> schreibt data/foods.app.json
//   node scripts/build-app.mjs --check  -> prüft nur, ob data/foods.app.json dem Build entspricht (Exit 1 sonst)
// Inhalt je Eintrag: id, Namen de/en/tr, kcal/Eiweiß/Kohlenhydrate/Fett/Ballaststoffe, Art, Küche und alles, was die Suche braucht
// (Originalname, aliases, synonyms). Synonyme, die nach normalize() einem Namen, Alias oder früheren Synonym gleichen, entfallen
// (für die Suche wirkungslos). Gelesen wird die Datei mit src/app-decoder.mjs.
import { readFileSync, writeFileSync, existsSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { normalize } from '../src/search.mjs';

const ROOT = fileURLToPath(new URL('..', import.meta.url));
const SRC = ROOT + 'data/foods.json';
const OUT = ROOT + 'data/foods.app.json';
export const FMT = '[id, de, en (0 = wie de), tr (0 = wie de, 1 = wie en), kcal, protein, carbs, fat, fiber (g/100 g), ' +
  'art (0 rohe Grundzutat, 1 Grundzutat, 2 Gericht, 3 sonstiger Artikel z. B. Getränk), cuisine, ' +
  '{o: Originalname (1 = wie en, 2 = wie tr, sonst Text; nur wenn ≠ de), a: aliases {de,en,tr}, s: synonyms}?]';

const r1 = (v) => Math.round(v * 10) / 10;

export function row(e) {
  const n = e.names;
  const en = n.en === n.de ? 0 : n.en;
  const tr = n.tr === n.de ? 0 : n.tr === n.en ? 1 : n.tr;
  const art = e.prepared === 'base_ingredient' ? (e.state === 'raw' ? 0 : 1) : e.type === 'dish' ? 2 : 3;
  const p = e.per100g;
  const r = [e.id, n.de, en, tr, Math.round(p.kcal), r1(p.protein), r1(p.carbs), r1(p.fat), r1(p.fiber), art, e.cuisine];
  const x = {};
  if (e.name !== n.de) x.o = e.name === n.en ? 1 : e.name === n.tr ? 2 : e.name;
  if (e.aliases && Object.keys(e.aliases).length) x.a = e.aliases;
  const seen = new Set([e.name, ...Object.values(n), ...Object.values(e.aliases || {}).flat()].map(normalize));
  const syn = [];
  for (const s of e.synonyms || []) { const k = normalize(s); if (!k || seen.has(k)) continue; seen.add(k); syn.push(s); }
  if (syn.length) x.s = syn;
  if (Object.keys(x).length) r.push(x);
  return r;
}

export function build(foods) {
  return JSON.stringify({ v: 1, f: FMT, d: foods.map(row) }) + '\n';
}

if (import.meta.url === `file://${process.argv[1]}`) {
  const out = build(JSON.parse(readFileSync(SRC, 'utf8')));
  if (process.argv.includes('--check')) {
    if (!existsSync(OUT) || readFileSync(OUT, 'utf8') !== out) {
      console.error('✗ data/foods.app.json ist nicht aktuell. Bitte `npm run build:app` ausführen und die Datei mitcommitten.');
      process.exit(1);
    }
    console.log(`✓ data/foods.app.json entspricht dem Build (${Buffer.byteLength(out)} Bytes)`);
  } else {
    writeFileSync(OUT, out);
    console.log(`data/foods.app.json geschrieben (${Buffer.byteLength(out)} Bytes)`);
  }
}
