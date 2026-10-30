# -*- coding: utf-8 -*-
"""Welle 5 – Funktionsfelder: yield/raw_id/cooked_id, salt/sat_fat/sugar, aliases.
Außerdem: entfernt die verworfenen Felder `portions`, `allergens`/`allergens_basis` und `popularity`, kürzt `names`/`aliases` auf de/en/tr und schreibt data/foods.json minifiziert.
Nur freie Quellen (USDA FDC SR Legacy/FNDDS, BLS 4.0, Ciqual 2025, CoFID 2021, Schweizer NWDB, Livsmedelsverket).
Alle Schätzungen werden im Datensatz gekennzeichnet (estimate:true bzw. *_basis / method).
Aufruf: python3 tools/functions/build_functions.py   (liest/schreibt data/foods.json idempotent)"""
import csv, json, math, os, re, statistics, sys
from collections import Counter, defaultdict
import pandas as pd
sys.path.insert(0, os.path.dirname(__file__))
from anchors import A as ANCH

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
SR = '/workspace/ext1/src/sr/FoodData_Central_sr_legacy_food_csv_2018-04/'
FN = '/workspace/base_ingredients/src/fndds/FoodData_Central_survey_food_csv_2024-10-31/'
ALL = '/workspace/ext1/src/all.pkl'
COFID = '/workspace/base_ingredients/cofid.xlsx'
SE = {'2614': '/workspace/base_ingredients/src/se2614.json', '3771': '/workspace/base_ingredients/src/se3771.json'}

foods = json.load(open(os.path.join(ROOT, 'data', 'foods.json')))
byid = {e['id']: e for e in foods}
FIELDS = ('portions', 'yield', 'raw_id', 'cooked_id', 'allergens', 'allergens_basis', 'popularity', 'nutrient_basis')
for e in foods:  # idempotent: Felder dieser Welle zuerst entfernen
    if (e.get('nutrient_basis') or {}).get('sugar') == 'source': e['per100g'].pop('sugar', None)
    for f in FIELDS: e.pop(f, None)
    for k in ('salt', 'sat_fat'): e['per100g'].pop(k, None)

# ---------------------------------------------------------------- Quellen laden
df = pd.read_pickle(ALL)
rows = {(r.db, str(r.code)): r for r in df.itertuples()}
srname = {r.name: str(r.code) for r in df[df.db == 'SR'].itertuples()}
need_fdc = {str(e['fdc_id']) for e in foods if 'fdc_id' in e} | {srname[v[0][4:]] for v in ANCH.values() if v and v[0].startswith('SRN:')}
def load_nut(path, ids, want):
    out = defaultdict(dict)
    with open(path + 'food_nutrient.csv') as f:
        for r in csv.DictReader(f):
            if r['fdc_id'] in ids and r['nutrient_id'] in want:
                out[r['fdc_id']][want[r['nutrient_id']]] = float(r['amount'])
    return out
SRN = load_nut(SR, need_fdc, {'1093': 'na', '1258': 'sfa', '2000': 'sug', '1051': 'water', '1008': 'kcal'})
FNN = load_nut(FN, need_fdc, {'307': 'na', '606': 'sfa', '269': 'sug', '255': 'water', '208': 'kcal'})
cof = pd.read_excel(COFID, sheet_name='1.4 Inorganics', header=0)
cof = cof.iloc[2:]
COFNA = {str(r[' ']).strip(): r['Sodium (mg)'] for _, r in cof.iterrows()}
def se_val(code):
    js = json.load(open(SE[code]))
    m = {x['euroFIRkod']: x['varde'] for x in js}
    return {'salt': m.get('NACL'), 'sfa': m.get('FASAT'), 'sug': m.get('SUGAR'), 'na': m.get('NA')}

def num(x):
    try:
        x = float(x)
        return None if math.isnan(x) else x
    except (TypeError, ValueError):
        return None

def source_values(e):
    """-> dict(kcal, salt, sfa, sug, water, label) aus der Primärquelle des Eintrags oder None."""
    if 'fdc_id' in e:
        c = str(e['fdc_id'])
        if c in SRN and ('SR', c) in rows:
            r, n = rows[('SR', c)], SRN[c]; lab = f'USDA SR Legacy FDC {c}'
        elif c in FNN:
            r, n = rows.get(('FNDDS', c)), FNN[c]; lab = f'USDA FNDDS 2021-2023 FDC {c}'
        else: return None
        return dict(kcal=n.get('kcal', num(getattr(r, 'kcal', None))), salt=(n['na'] * 2.5 / 1000 if 'na' in n else None),
                    sfa=n.get('sfa'), sug=n.get('sug'), water=n.get('water'), label=lab)
    sid = e.get('source_id')
    if not sid: return None
    db, code = sid.split(':', 1)
    key = {'BLS 4.0': 'BLS', 'Ciqual 2025': 'CIQ', 'CH 7.1': 'CH', 'CoFID 2021': 'COFID'}.get(db)
    if db == 'Livsmedelsverket':
        v = se_val(code)
        return dict(kcal=None, salt=num(v['salt']) if v['salt'] is not None else (num(v['na']) * 2.5 / 1000 if v['na'] is not None else None),
                    sfa=num(v['sfa']), sug=num(v['sug']), water=None, label=f'Livsmedelsverket {code}')
    r = rows.get((key, code))
    if r is None: return None
    salt = num(r.salt)
    if key == 'COFID':
        na = num(COFNA.get(code))
        salt = na * 2.5 / 1000 if na is not None else None
    return dict(kcal=num(r.kcal), salt=salt, sfa=num(r.sfa), sug=num(r.sug), water=num(r.water), label=sid)

rep = Counter(); examples = defaultdict(list)

# ---------------------------------------------------------------- 4) Nährstoffe aus Quellen
for e in foods:
    sv = source_values(e)
    if not sv: continue
    p = e['per100g']
    if sv['kcal'] is not None and abs(sv['kcal'] - p['kcal']) > max(3, 0.03 * p['kcal']):
        rep['nutr_kcal_mismatch_skip'] += 1; continue   # Eintrag weicht von der Quelle ab (z. B. umgerechnet) -> nichts übernehmen
    basis = {}
    if sv['salt'] is not None and 0 <= sv['salt'] <= 100:
        p['salt'] = round(sv['salt'], 2); basis['salt'] = 'source'
    if sv['sfa'] is not None and sv['sfa'] <= p['fat'] + 0.05:
        p['sat_fat'] = round(min(sv['sfa'], p['fat']), 1); basis['sat_fat'] = 'source'
    if 'sugar' not in p and sv['sug'] is not None and sv['sug'] <= p['carbs'] + 0.5:
        p['sugar'] = round(min(sv['sug'], max(p['carbs'], 0)), 1); basis['sugar'] = 'source'; rep['sugar_added_source'] += 1
    if basis: e['nutrient_basis'] = basis

# ---------------------------------------------------------------- 4b) Gerichte: Schätzung aus Rezept + Quell-Ankern
def anchor_vals(spec):
    """-> (fat, sfa, salt) eines Ankers."""
    if spec.startswith('AVG:'):
        vs = [anchor_vals(s) for s in spec[4:].split('|')]
        return tuple(None if any(v[i] is None for v in vs) else sum(v[i] for v in vs) / len(vs) for i in range(3))
    if spec == 'ZERO': return (0.0, 0.0, 0.0)
    if spec in ('VEG', 'FRUIT'): return CLASS[spec]
    db, code = spec.split(':', 1)
    if db == 'SRN':
        c = srname[code]; n = SRN[c]; r = rows[('SR', c)]
        return (num(r.fat) or 0.0, n.get('sfa', num(r.sfa)), n['na'] * 2.5 / 1000 if 'na' in n else None)
    r = rows[(db, code)]
    return (num(r.fat) or 0.0, num(r.sfa), num(r.salt))
def class_median(prefix):
    sub = df[(df.db == 'BLS') & df.code.astype(str).str.startswith(prefix) & df.name.str.contains(r'\broh\b')]
    shares = [s / f for f, s in zip(sub.fat, sub.sfa) if num(f) and f > 0.1 and num(s) is not None]
    salts = [x for x in sub.salt if num(x) is not None]
    return (1.0, statistics.median(shares), statistics.median(salts)), len(sub)
CLASS = {}
(CLASS['VEG'], nveg), (CLASS['FRUIT'], nfr) = class_median('G'), class_median('F')
rep['class_veg_n'], rep['class_fruit_n'] = nveg, nfr
ING = {i['name']: i['per100g'] for i in json.load(open(os.path.join(ROOT, 'tools', 'dishes', 'ingredients.json')))}
AV = {}
for n, v in ANCH.items():
    if v is None: AV[n] = None; continue
    fat, sfa, salt = anchor_vals(v[0])
    share = (sfa / fat) if (fat and sfa is not None and fat > 0) else (0.0 if fat == 0 else None)
    if v[0] in ('VEG', 'FRUIT'): share = sfa
    AV[n] = (share, salt if v[1] else None)

def dish_estimates(e):
    ings = e.get('ingredients') or []
    if not ings or any(i['name'] not in ING for i in ings): return None, None
    p = e['per100g']; tot_g = sum(i['grams'] for i in ings)
    if tot_g <= 0: return None, None
    fat_i = [(i, ING[i['name']]['fat'] * i['grams'] / 100) for i in ings]
    fsum = sum(f for _, f in fat_i)
    sat = None
    if p['fat'] == 0: sat = 0.0
    elif fsum > 0:
        unknown = sum(f for i, f in fat_i if AV.get(i['name']) is None or AV[i['name']][0] is None)
        if unknown <= 0.02 * fsum:   # max. 2 % des Fetts ohne Anker
            known = [(i, f) for i, f in fat_i if AV.get(i['name']) and AV[i['name']][0] is not None]
            kf = sum(f for _, f in known)
            share = sum(f * AV[i['name']][0] for i, f in known) / kf if kf else 0
            sat = round(min(p['fat'], p['fat'] * share), 1)
    salt = None
    names = {i['name'] for i in ings}
    if ('Salz' in names or e.get('category') == 'Getränk') and all(AV.get(n) and AV[n][1] is not None for n in names):
        rec_kcal = sum(ING[i['name']]['kcal'] * i['grams'] / 100 for i in ings) / tot_g * 100
        conc = p['kcal'] / rec_kcal if rec_kcal > 5 else 1.0
        conc = min(max(conc, 0.5), 2.5)
        s = sum(AV[i['name']][1] * i['grams'] for i in ings) / tot_g * conc
        salt = round(s, 2)
    return sat, salt

for e in foods:
    if e['type'] != 'dish' or e.get('nutrient_basis'): continue
    if e.get('quality') == 'reference': continue
    sat, salt = dish_estimates(e)
    basis = {}
    if sat is not None: e['per100g']['sat_fat'] = sat; basis['sat_fat'] = 'recipe_estimate'
    if salt is not None: e['per100g']['salt'] = salt; basis['salt'] = 'recipe_estimate'
    if basis: e['nutrient_basis'] = basis

# ---------------------------------------------------------------- 2) Ausbeute roh -> gekocht
PAIRS = []
for e in foods:
    if e['type'] == 'item' and e['category'] in ('Grundzutat: Getreide, Teigwaren & Brot', 'Grundzutat: Hülsenfrüchte') and e['id'].endswith('-roh'):
        c = e['id'][:-4] + '-gekocht'
        if c in byid: PAIRS.append((e['id'], c))
PAIRS += [('buchweizen-geroestet-roh', 'buchweizen-geroestet-gekocht'), ('dicke-bohnen-roh-getrocknet', 'dicke-bohnen-gekocht'),
          ('dinkel-korn', 'dinkel-gekocht'), ('haferflocken', 'haferflocken-mit-wasser-gekocht'), ('maisgriess', 'maisgriess-mit-wasser-gekocht')]
for r, c in sorted(set(PAIRS)):
    R, C_ = byid[r], byid[c]
    sr, sc = source_values(R), source_values(C_)
    if not sr or not sc or sr['water'] is None or sc['water'] is None: rep['yield_no_water'] += 1; continue
    fac = (100 - sr['water']) / (100 - sc['water'])
    if not (1.0 < fac < 12): rep['yield_implausible'] += 1; continue
    note = (f'Schätzung über Trockenmassebilanz: (100 − Wasser roh {sr["water"]:.1f} g) / (100 − Wasser gekocht {sc["water"]:.1f} g); '
            f'Wasserwerte aus {sr["label"]} und {sc["label"]}; Auslaugverluste nicht berücksichtigt')
    R['yield'] = {'factor': round(fac, 2), 'from': 'raw', 'to': 'cooked', 'method': 'dry_matter_balance', 'estimate': True, 'source': note}
    R['cooked_id'] = c; C_['raw_id'] = r
    rep['yield'] += 1; examples['yield'].append((r, c, round(fac, 2)))

# ---------------------------------------------------------------- 5) Umgangssprache
ALIAS = {  # zusätzliche umgangssprachliche/regionale deutsche Namen
 'pommes-frites': ['Fritten', 'Fritte'],
 'reibekuchen': ['Reibeplätzchen', 'Reiberdatschi', 'Grumbeerpannekuche'],
 'frikadellen': ['Bulette', 'Buletten', 'Fleischpflanzerl', 'Fleischküchle'],
 'magerquark': ['Topfen'],
 'kartoffel-roh': ['Erdapfel', 'Grumbeere'],
 'karotte-roh': ['Möhre', 'Rüebli', 'Mohrrübe', 'Gelbe Rübe'],
 'broetchen': ['Schrippe', 'Weckle', 'Weck', 'Semmel'],
 'laugenbrezel': ['Breze', 'Brezn'],
 'champignons-roh': ['Schwammerl'],
 'schlagsahne-ca-30-prozent': ['Obers', 'Schlagobers', 'Rahm'],
}
seen_names = defaultdict(set)
for e in foods:
    for n in [e['name']] + list(e.get('names', {}).values()) + e.get('synonyms', []) + [a for v in (e.get('aliases') or {}).values() for a in v]:
        seen_names[n.lower()].add(e['id'])
for i, al in ALIAS.items():
    e = byid.get(i)
    if not e: rep['alias_missing_id'] += 1; continue
    de = e.setdefault('aliases', {}).setdefault('de', [])
    for a in al:
        if a.lower() in seen_names and i not in seen_names[a.lower()]: rep['alias_collision_skip'] += 1; continue
        if a not in de: de.append(a); rep['alias_added'] += 1

for e in foods:
    if not e.get('aliases', {}).get('de', True): e['aliases'].pop('de')

# ---------------------------------------------------------------- Sprachen auf de/en/tr kürzen
KEEP_LANGS = ('de', 'en', 'tr')
for e in foods:
    e['names'] = {l: v for l, v in e['names'].items() if l in KEEP_LANGS}
    if 'aliases' in e:
        e['aliases'] = {l: v for l, v in e['aliases'].items() if l in KEEP_LANGS and v}
        if not e['aliases']: e.pop('aliases')

# ---------------------------------------------------------------- schreiben (minifiziert)
out = json.dumps(foods, ensure_ascii=False, separators=(',', ':')) + '\n'
open(os.path.join(ROOT, 'data', 'foods.json'), 'w').write(out)
cov = Counter()
for e in foods:
    t = e['type']
    for f in ('yield', 'raw_id', 'cooked_id'):
        if f in e: cov[f'{f}:{t}'] += 1
    for f in ('salt', 'sat_fat'):
        if f in e['per100g'] and f in e.get('nutrient_basis', {}): cov[f'{f}:{t}:{e["nutrient_basis"][f]}'] += 1
    if 'sugar' in e['per100g']: cov[f'sugar:{t}'] += 1
    if (e.get('nutrient_basis') or {}).get('sugar'): cov['sugar_new_from_source'] += 1
json.dump({'coverage': dict(sorted(cov.items())), 'report': dict(rep), 'class': {k: list(v) for k, v in CLASS.items()},
           'yield': examples['yield']}, open(os.path.join(os.path.dirname(__file__), 'build_report.json'), 'w'), ensure_ascii=False, indent=1)
print(json.dumps(dict(sorted(cov.items())), ensure_ascii=False, indent=0)); print(dict(rep))
