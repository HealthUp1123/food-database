// Schutztest: Build und Arbeitskopie dürfen gegenüber data/foods.json nichts verlieren.
// Zusätzlich gilt der Git-Stand der Basis (merge-base mit origin/main).
// Exit-Code 1 bei Verlust. Keine Abhängigkeiten. Node >= 20.10, python3, git.
import { spawnSync } from 'node:child_process';
import { readFileSync } from 'node:fs';
import { dirname, join, resolve } from 'node:path';
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
const MACRO_KEYS = ['kcal', 'protein', 'carbs', 'fat', 'fiber', 'sugar', 'alcohol'];

const nonempty = (list) => (Array.isArray(list) ? list.filter((s) => typeof s === 'string' && s.trim()) : []);

export function compareFoods(data, built, minEntries) {
  const errors = [];
  if (!Array.isArray(data) || !Array.isArray(built)) return ['foods.json muss ein Array sein'];
  if (!Number.isInteger(minEntries) || minEntries < 1) return ['tools/guard/min-entries.json: minEntries fehlt'];
  if (data.length < minEntries) errors.push(`data/foods.json hat ${data.length} Einträge, Mindestzahl ist ${minEntries}`);

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
  const synonymsShrink = (dataSyn, buildSyn) => {
    if (!Array.isArray(dataSyn)) return false;
    if (!Array.isArray(buildSyn)) return true;
    const left = nonempty(buildSyn);
    for (const s of nonempty(dataSyn)) {
      const i = left.indexOf(s);
      if (i < 0) return true;
      left.splice(i, 1);
    }
    return false;
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
    if (synonymsShrink(e.synonyms, b.synonyms)) errors.push(`${e.id}: synonyms im Build geschrumpft`);
    if (e.prepared !== b.prepared) errors.push(`${e.id}: prepared im Build weicht ab (${JSON.stringify(b.prepared)} statt ${JSON.stringify(e.prepared)})`);
    if (e.is_packaged_product !== b.is_packaged_product) errors.push(`${e.id}: is_packaged_product im Build weicht ab`);
    const dp = e.per100g || {};
    const bp = b.per100g || {};
    for (const key of MACRO_KEYS) {
      if (!(key in dp)) continue;
      if (dp[key] !== bp[key]) errors.push(`${e.id}: ${key} weicht ab (${JSON.stringify(bp[key])} statt ${JSON.stringify(dp[key])})`);
    }
  }
  return errors;
}

function hasSyn(entry, synonym) {
  return nonempty(entry && entry.synonyms).includes(synonym);
}

function recipeMatchesFile(working, built) {
  if (!working || !built) return false;
  if (working.quality !== 'estimate') return false;
  if (typeof working.source !== 'string' || !working.source.startsWith('calculated from typical recipe')) return false;
  const left = nonempty(built.synonyms);
  for (const s of nonempty(working.synonyms)) {
    const i = left.indexOf(s);
    if (i < 0) return false;
    left.splice(i, 1);
  }
  return left.length === 0;
}

export function compareToBaseline(baseline, working, built, allow) {
  const errors = [];
  if (!Array.isArray(baseline) || !Array.isArray(working)) return ['Basis oder data/foods.json ist kein Array'];
  const allowDelete = new Set((allow.delete || []).map((x) => x.id));
  const allowRename = new Map((allow.rename || []).map((x) => [x.from, x.to]));
  const allowSyn = new Set((allow.dropSynonym || []).map((x) => `${x.id}\0${x.synonym}`));
  const allowPrepared = new Set((allow.prepared || []).map((x) => x.id));
  const allowPack = new Set((allow.isPackagedProduct || []).map((x) => x.id));
  const work = new Map(working.filter((e) => e && e.id).map((e) => [e.id, e]));
  const builtById = new Map((built || []).filter((e) => e && e.id).map((e) => [e.id, e]));
  for (const base of baseline) {
    if (!base || !base.id) continue;
    const cur = work.get(base.id);
    if (!cur) {
      const to = allowRename.get(base.id);
      if (allowDelete.has(base.id) || (to && work.has(to))) continue;
      errors.push(`${base.id}: ID gegenüber der Git-Basis verschwunden`);
      continue;
    }
    for (const s of nonempty(base.synonyms)) {
      if (hasSyn(cur, s) || allowSyn.has(`${base.id}\0${s}`)) continue;
      const b = builtById.get(base.id);
      if (recipeMatchesFile(cur, b) && b && !hasSyn(b, s)) continue;
      errors.push(`${base.id}: Synonym gegenüber der Git-Basis weggefallen (${JSON.stringify(s)})`);
    }
    if (base.prepared !== cur.prepared && !allowPrepared.has(base.id)) {
      errors.push(`${base.id}: prepared gegenüber der Git-Basis geändert (${JSON.stringify(base.prepared)} → ${JSON.stringify(cur.prepared)})`);
    }
    if (base.is_packaged_product !== cur.is_packaged_product && !allowPack.has(base.id)) {
      errors.push(`${base.id}: is_packaged_product gegenüber der Git-Basis geändert (${JSON.stringify(base.is_packaged_product)} → ${JSON.stringify(cur.is_packaged_product)})`);
    }
  }
  return errors;
}

function git(args) {
  return spawnSync('git', args, { cwd: root, encoding: 'utf8', maxBuffer: 64 * 1024 * 1024 });
}

export function baselineRef() {
  const mb = git(['merge-base', 'HEAD', 'origin/main']);
  if (mb.status === 0 && mb.stdout.trim()) return mb.stdout.trim();
  if (git(['rev-parse', '--verify', '--quiet', 'origin/main']).status === 0) return 'origin/main';
  if (git(['rev-parse', '--verify', '--quiet', 'HEAD~']).status === 0) return 'HEAD~';
  return null;
}

function loadBaseline(ref) {
  const shown = git(['show', `${ref}:data/foods.json`]);
  if (shown.status !== 0) {
    const detail = (shown.stderr || shown.error && shown.error.message || '').trim();
    throw new Error(`git show ${ref}:data/foods.json fehlgeschlagen${detail ? `: ${detail}` : ''}`);
  }
  return JSON.parse(shown.stdout);
}

function loadAllow() {
  const file = join(root, 'tools', 'guard', 'allowed-changes.json');
  const allow = JSON.parse(readFileSync(file, 'utf8'));
  for (const key of ['delete', 'rename', 'dropSynonym', 'prepared', 'isPackagedProduct']) {
    if (!Array.isArray(allow[key])) throw new Error(`tools/guard/allowed-changes.json: ${key} muss eine Liste sein`);
    for (const row of allow[key]) {
      if (!row || typeof row.reason !== 'string' || !row.reason.trim()) {
        throw new Error(`tools/guard/allowed-changes.json: Eintrag in ${key} ohne Begründung`);
      }
    }
  }
  return allow;
}

function report(errors, data, built, minEntries, ref) {
  if (errors.length) {
    console.error(`✗ Schutztest: ${errors.length} Verlust${errors.length === 1 ? '' : 'e'}`);
    for (const x of errors.slice(0, 40)) console.error('  ' + x);
    if (errors.length > 40) console.error(`  … und ${errors.length - 40} weitere`);
    process.exit(1);
  }
  console.log(`✓ Schutztest: ${data.length} Einträge (Minimum ${minEntries}), Build ${built.length}, Basis ${ref}, keine verbotenen Verluste`);
}

const isDirect = process.argv[1] && resolve(process.argv[1]) === fileURLToPath(import.meta.url);
if (isDirect) {
  const run = spawnSync('python3', ['tools/dishes/build.py'], { cwd: root, encoding: 'utf8' });
  if (run.stdout) process.stdout.write(run.stdout);
  if (run.status !== 0) {
    if (run.stderr) process.stderr.write(run.stderr);
    console.error('✗ build.py ist fehlgeschlagen');
    process.exit(1);
  }
  const data = JSON.parse(readFileSync(join(root, 'data', 'foods.json'), 'utf8'));
  const built = JSON.parse(readFileSync(join(root, 'tools', 'dishes', 'foods.json'), 'utf8'));
  const minEntries = JSON.parse(readFileSync(join(root, 'tools', 'guard', 'min-entries.json'), 'utf8')).minEntries;
  const ref = baselineRef();
  if (!ref) {
    console.error('✗ Git-Basis nicht gefunden (merge-base origin/main, origin/main, HEAD~)');
    process.exit(1);
  }
  let baseline;
  try {
    baseline = loadBaseline(ref);
  } catch (e) {
    console.error(`✗ ${e.message}`);
    process.exit(1);
  }
  let allow;
  try {
    allow = loadAllow();
  } catch (e) {
    console.error(`✗ ${e.message}`);
    process.exit(1);
  }
  const errors = [
    ...compareFoods(data, built, minEntries),
    ...compareToBaseline(baseline, data, built, allow),
  ];
  report(errors, data, built, minEntries, ref);
}
