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

function sameNames(a, b) {
  return JSON.stringify(a && a.names) === JSON.stringify(b && b.names);
}

export function compareToBaseline(baseline, working, allow) {
  const errors = [];
  const warnings = [];
  if (!Array.isArray(baseline) || !Array.isArray(working)) {
    return { errors: ['Basis oder data/foods.json ist kein Array'], warnings };
  }
  const used = new Set();
  const work = new Map(working.filter((e) => e && e.id).map((e) => [e.id, e]));
  const renames = allow.rename || [];
  const deletes = allow.delete || [];
  const drops = allow.dropSynonym || [];
  const prepared = allow.prepared || [];
  const packed = allow.isPackagedProduct || [];
  for (const base of baseline) {
    if (!base || !base.id) continue;
    const cur = work.get(base.id);
    if (!cur) {
      const renameAt = renames.findIndex((row) => row.from === base.id && work.has(row.to));
      if (renameAt >= 0) {
        used.add(`rename:${renameAt}`);
        continue;
      }
      const deleteAt = deletes.findIndex((row) => row.id === base.id);
      if (deleteAt >= 0) {
        used.add(`delete:${deleteAt}`);
        continue;
      }
      errors.push(`${base.id}: ID gegenüber der Git-Basis verschwunden`);
      continue;
    }
    if (!sameNames(base, cur)) warnings.push(`${base.id}: names gegenüber der Git-Basis geändert`);
    if (base.quality !== cur.quality) warnings.push(`${base.id}: quality gegenüber der Git-Basis geändert (${JSON.stringify(base.quality)} → ${JSON.stringify(cur.quality)})`);
    if (base.source !== cur.source) warnings.push(`${base.id}: source gegenüber der Git-Basis geändert`);
    for (const s of nonempty(base.synonyms)) {
      if (hasSyn(cur, s)) continue;
      const dropAt = drops.findIndex((row) => row.id === base.id && row.synonym === s);
      if (dropAt >= 0) {
        used.add(`dropSynonym:${dropAt}`);
        continue;
      }
      errors.push(`${base.id}: Synonym gegenüber der Git-Basis weggefallen (${JSON.stringify(s)})`);
    }
    if (base.prepared !== cur.prepared) {
      const at = prepared.findIndex((row) => row.id === base.id && row.from === base.prepared && row.to === cur.prepared);
      if (at >= 0) used.add(`prepared:${at}`);
      else errors.push(`${base.id}: prepared gegenüber der Git-Basis geändert (${JSON.stringify(base.prepared)} → ${JSON.stringify(cur.prepared)})`);
    }
    if (base.is_packaged_product !== cur.is_packaged_product) {
      const at = packed.findIndex((row) => row.id === base.id && row.from === base.is_packaged_product && row.to === cur.is_packaged_product);
      if (at >= 0) used.add(`isPackagedProduct:${at}`);
      else errors.push(`${base.id}: is_packaged_product gegenüber der Git-Basis geändert (${JSON.stringify(base.is_packaged_product)} → ${JSON.stringify(cur.is_packaged_product)})`);
    }
  }
  const lists = [
    ['delete', deletes, (row) => row.id],
    ['rename', renames, (row) => `${row.from} → ${row.to}`],
    ['dropSynonym', drops, (row) => `${row.id} / ${JSON.stringify(row.synonym)}`],
    ['prepared', prepared, (row) => `${row.id} ${JSON.stringify(row.from)} → ${JSON.stringify(row.to)}`],
    ['isPackagedProduct', packed, (row) => `${row.id} ${JSON.stringify(row.from)} → ${JSON.stringify(row.to)}`],
  ];
  for (const [kind, rows, label] of lists) {
    rows.forEach((row, i) => {
      if (!used.has(`${kind}:${i}`)) errors.push(`unbenutzte Freigabe (${kind}: ${label(row)})`);
    });
  }
  return { errors, warnings };
}

function git(args) {
  return spawnSync('git', args, { cwd: root, encoding: 'utf8', maxBuffer: 64 * 1024 * 1024 });
}

const ZERO_SHA = '0000000000000000000000000000000000000000';

function resolveBeforeOrParent(head) {
  const before = (process.env.GITHUB_EVENT_BEFORE || '').trim();
  if (before && before !== ZERO_SHA && before !== head) {
    const ok = git(['rev-parse', '--verify', '--quiet', `${before}^{commit}`]);
    if (ok.status !== 0 || !ok.stdout.trim()) {
      return { error: `github.event.before (${before}) ist hier kein Commit. Historie holen: git fetch origin main` };
    }
    return { ref: ok.stdout.trim() };
  }
  const parent = git(['rev-parse', '--verify', '--quiet', 'HEAD^1']);
  if (parent.status !== 0 || !parent.stdout.trim()) {
    return { error: 'merge-base ist HEAD, github.event.before fehlt und HEAD^1 gibt es nicht.' };
  }
  return { ref: parent.stdout.trim() };
}

export function baselineRef() {
  const headRun = git(['rev-parse', 'HEAD']);
  if (headRun.status !== 0 || !headRun.stdout.trim()) return { error: 'HEAD ist kein Commit' };
  const head = headRun.stdout.trim();
  const hasMain = git(['rev-parse', '--verify', '--quiet', 'origin/main']).status === 0;
  let warning = null;
  let ref;
  if (!hasMain) {
    if (process.env.GUARD_ALLOW_NO_MAIN !== '1') {
      return {
        error: 'origin/main fehlt. Holen mit: git fetch origin main\n'
          + 'Umgehung nur ausdrücklich mit GUARD_ALLOW_NO_MAIN=1. Das ist keine normale Prüfung und gibt eine Warnung aus.',
      };
    }
    warning = 'GUARD_ALLOW_NO_MAIN=1: origin/main fehlt. Die Basis ist nicht der Merge mit main. Normal: git fetch origin main';
    const picked = resolveBeforeOrParent(head);
    if (picked.error) return picked;
    ref = picked.ref;
  } else {
    const mb = git(['merge-base', 'HEAD', 'origin/main']);
    if (mb.status !== 0 || !mb.stdout.trim()) {
      return { error: 'merge-base HEAD origin/main ist fehlgeschlagen. git fetch origin main' };
    }
    ref = mb.stdout.trim();
    if (ref === head) {
      const picked = resolveBeforeOrParent(head);
      if (picked.error) return picked;
      ref = picked.ref;
    }
  }
  if (ref === head) return { error: 'Die Basis wäre HEAD selbst. Das ist keine Prüfung.' };
  return { ref, warning };
}

function loadBaseline(ref) {
  const shown = git(['show', `${ref}:data/foods.json`]);
  if (shown.status !== 0) {
    const detail = (shown.stderr || shown.error && shown.error.message || '').trim();
    throw new Error(`git show ${ref}:data/foods.json fehlgeschlagen${detail ? `: ${detail}` : ''}`);
  }
  return JSON.parse(shown.stdout);
}

function readJsonFile(rel) {
  const file = join(root, rel);
  let raw;
  try {
    raw = readFileSync(file, 'utf8');
  } catch (e) {
    if (e && e.code === 'ENOENT') throw new Error(`${rel} fehlt`);
    throw new Error(`${rel}: ${e.message}`);
  }
  try {
    return JSON.parse(raw);
  } catch (e) {
    throw new Error(`${rel}: kein gültiges JSON (${e.message})`);
  }
}

function loadAllow() {
  const rel = 'tools/guard/allowed-changes.json';
  const allow = readJsonFile(rel);
  const expect = {
    delete: ['id'],
    rename: ['from', 'to'],
    dropSynonym: ['id', 'synonym'],
    prepared: ['id', 'from', 'to'],
    isPackagedProduct: ['id', 'from', 'to'],
  };
  for (const [key, fields] of Object.entries(expect)) {
    if (!Array.isArray(allow[key])) throw new Error(`${rel}: ${key} muss eine Liste sein`);
    for (const row of allow[key]) {
      if (!row || typeof row !== 'object') throw new Error(`${rel}: Eintrag in ${key} ist kein Objekt`);
      if (typeof row.reason !== 'string' || !row.reason.trim()) throw new Error(`${rel}: Eintrag in ${key} ohne Begründung`);
      for (const field of fields) {
        if (!(field in row)) throw new Error(`${rel}: Eintrag in ${key} ohne ${field}`);
      }
      if (key === 'isPackagedProduct' && (typeof row.from !== 'boolean' || typeof row.to !== 'boolean')) {
        throw new Error(`${rel}: isPackagedProduct from und to müssen true oder false sein`);
      }
    }
  }
  return allow;
}

function loadMinEntries() {
  const parsed = readJsonFile('tools/guard/min-entries.json');
  if (!Number.isInteger(parsed.minEntries) || parsed.minEntries < 1) {
    throw new Error('tools/guard/min-entries.json: minEntries fehlt');
  }
  return parsed.minEntries;
}

function report(errors, warnings, data, built, minEntries, ref) {
  for (const w of warnings) console.warn(`! ${w}`);
  if (errors.length) {
    console.error(`✗ Schutztest: ${errors.length} Verlust${errors.length === 1 ? '' : 'e'}, Basis ${ref}`);
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
  let minEntries;
  let allow;
  try {
    minEntries = loadMinEntries();
    allow = loadAllow();
  } catch (e) {
    console.error(`✗ ${e.message}`);
    process.exit(1);
  }
  const picked = baselineRef();
  if (picked.error) {
    console.error(`✗ ${picked.error}`);
    process.exit(1);
  }
  if (picked.warning) console.warn(`⚠ ${picked.warning}`);
  let baseline;
  try {
    baseline = loadBaseline(picked.ref);
  } catch (e) {
    console.error(`✗ ${e.message}`);
    process.exit(1);
  }
  const baseDiff = compareToBaseline(baseline, data, allow);
  const errors = [...compareFoods(data, built, minEntries), ...baseDiff.errors];
  report(errors, baseDiff.warnings, data, built, minEntries, picked.ref);
}
