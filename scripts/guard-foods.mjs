// Schutztest: Build darf gegenüber data/foods.json nichts verlieren.
// Exit-Code 1 bei Verlust. Keine Abhängigkeiten. Node >= 20.10, python3.
import { spawnSync } from 'node:child_process';
import { readFileSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const root = join(dirname(fileURLToPath(import.meta.url)), '..');
const NAME_LANGS = ['de', 'tr', 'en'];
const NUTRIENTS = [
  ['kcal', 'kcal'],
  ['carbs', 'Kohlenhydrate'],
  ['protein', 'Eiweiß'],
  ['fat', 'Fett'],
  ['fiber', 'Ballaststoffe'],
];

const run = spawnSync('python3', ['tools/dishes/build.py'], { cwd: root, encoding: 'utf8' });
if (run.stdout) process.stdout.write(run.stdout);
if (run.status !== 0) {
  if (run.stderr) process.stderr.write(run.stderr);
  console.error('✗ build.py ist fehlgeschlagen');
  process.exit(1);
}

const data = JSON.parse(readFileSync(join(root, 'data', 'foods.json'), 'utf8'));
const built = JSON.parse(readFileSync(join(root, 'tools', 'dishes', 'foods.json'), 'utf8'));
const minEntries = JSON.parse(readFileSync(join(root, 'data', 'min-entries.json'), 'utf8')).minEntries;
const errors = [];

if (!Array.isArray(data) || !Array.isArray(built)) {
  console.error('✗ foods.json muss ein Array sein');
  process.exit(1);
}
if (!Number.isInteger(minEntries) || minEntries < 1) {
  console.error('✗ data/min-entries.json: minEntries fehlt');
  process.exit(1);
}
if (data.length < minEntries) {
  errors.push(`data/foods.json hat ${data.length} Einträge, Mindestzahl ist ${minEntries}`);
}

const nameProblems = (e) => {
  const names = e && e.names;
  if (!names || typeof names !== 'object' || Array.isArray(names)) return ['names fehlt'];
  return NAME_LANGS.filter((l) => typeof names[l] !== 'string' || !names[l].trim()).map((l) => `names.${l} fehlt oder ist leer`);
};

const fieldProblems = (e) => {
  const problems = [];
  const p = e && e.per100g;
  if (!p || typeof p !== 'object' || Array.isArray(p)) problems.push('per100g fehlt');
  else {
    for (const [key, label] of NUTRIENTS) {
      if (typeof p[key] !== 'number' || !Number.isFinite(p[key])) problems.push(`${label} (${key}) fehlt`);
    }
  }
  if (typeof e.is_packaged_product !== 'boolean') problems.push('is_packaged_product fehlt');
  if (!Array.isArray(e.synonyms)) problems.push('synonyms fehlt');
  return problems;
};

for (const e of data) {
  const id = e && e.id ? e.id : '?';
  for (const p of nameProblems(e)) errors.push(`${id}: Bestand ${p}`);
  for (const p of fieldProblems(e)) errors.push(`${id}: Bestand ${p}`);
}

const builtById = new Map();
for (const e of built) {
  if (!e || !e.id) continue;
  if (builtById.has(e.id)) errors.push(`${e.id}: doppelt im Build`);
  builtById.set(e.id, e);
}
for (const e of data) {
  if (!e || !e.id) continue;
  const b = builtById.get(e.id);
  if (!b) {
    errors.push(`${e.id}: fehlt im Build-Output`);
    continue;
  }
  for (const p of nameProblems(b)) errors.push(`${e.id}: Build ${p}`);
  for (const p of fieldProblems(b)) errors.push(`${e.id}: Build ${p}`);
}

if (errors.length) {
  console.error(`✗ Schutztest: ${errors.length} Verlust${errors.length === 1 ? '' : 'e'}`);
  for (const x of errors.slice(0, 40)) console.error('  ' + x);
  if (errors.length > 40) console.error(`  … und ${errors.length - 40} weitere`);
  process.exit(1);
}
console.log(`✓ Schutztest: ${data.length} Einträge (Minimum ${minEntries}), Build ${built.length}, keine Verluste bei IDs, names.de/tr/en oder Pflichtfeldern`);
