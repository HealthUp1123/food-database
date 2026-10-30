# -*- coding: utf-8 -*-
"""Ballaststoff-Korrekturen (Welle 5 final) -> tools/fiber/fiber_final.json

Eingaben (alle im Repo):
  tools/fiber/ingredient_fiber.json   Zutatenwerte je Rezeptzutat mit allen freien Quellwerten (SR, BLS, Ciqual, CoFID)
  tools/fiber/review_decisions.json   Prüfentscheidungen zu den 158 Vorschlägen (übernehmen/anpassen/verwerfen)
  Basis-Ballaststoffwerte: data/foods.json im Stand VOR der Korrektur (Standard: `git show a39a477:data/foods.json`)

Regeln:
  a) Ballaststoffe = klassische AOAC-Methode (wie USDA SR, Ciqual, CoFID); Fructane/Inulin zählen NICHT.
     Knoblauch-Zutatenwert = Median der freien Quellen ohne den BLS-Wert (BLS 4.0 misst nach AOAC 2009.01 inkl. Fructane).
     Alle Gerichte mit Knoblauch werden mit diesem Wert neu gerechnet. BLS-Referenzeinträge für zubereiteten
     Knoblauch/Topinambur werden aus dem klassischen Rohwert abgeleitet (BLS-Zubereitungsfaktor × klassischer Rohwert).
  b) Maisgerichte aus Vollkornmais behalten ihren alten Wert (in den Prüfentscheidungen „verwerfen“).
Aufruf: python3 tools/fiber/derive_fiber.py [basis-foods.json]
Danach: python3 tools/fiber/apply_fiber.py (setzt die Werte idempotent in data/foods.json)."""
import json, os, statistics, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
ING = json.load(open(os.path.join(HERE, 'ingredient_fiber.json')))
DEC = {e['id']: e for e in json.load(open(os.path.join(HERE, 'review_decisions.json')))['entscheidungen']}
PROP = {e['id']: e for e in json.load(open(os.path.join(HERE, 'fiber_changes_proposal.json')))}
if len(sys.argv) > 1: base = json.load(open(sys.argv[1]))
else: base = json.loads(subprocess.check_output(['git', 'show', 'a39a477:data/foods.json'], cwd=ROOT))
B = {f['id']: f for f in base}

GARLIC = 'Knoblauch'
g = ING[GARLIC]
g_vals = [w for w in g['werte'] if not w['code'].startswith('BLS:')]
G_NEW = round(statistics.median(w['wert'] for w in g_vals), 2)       # 2.1 / 5.8 / 4.1 -> 4.1
G_OLD_SRC = g['alt']        # Wert in tools/dishes/ingredients_src.txt (Grundlage der alten Gerichtswerte)
G_OLD_MED = g['neu']        # Median inkl. BLS (Grundlage der 158 Vorschläge)
G_CODES = [w['code'] for w in g_vals]

def val(n, garlic):
    return garlic if n == GARLIC else ING[n]['neu']
def calc(f, garlic):
    return sum(i['grams'] * val(i['name'], garlic) / 100 for i in f['ingredients']) / f['portion']['grams'] * 100
def garlic_share(f, gv):
    gr = sum(i['grams'] for i in f['ingredients'] if i['name'] == GARLIC)
    return gr * gv / 100 / f['portion']['grams'] * 100
def r1(x): return round(x + 1e-9, 1)

AOAC = 'klassische AOAC-Methode ohne Fructane/Inulin'
out = []
for i, f in B.items():
    if not f['source'].startswith('calculated from typical recipe'): continue
    old = f['per100g']['fiber']
    has_g = any(x['name'] == GARLIC for x in f['ingredients'])
    d = DEC.get(i)
    rec = None
    if d:
        p = PROP[i]; codes = list(p['source_id'])
        if has_g and d['entscheidung'] == 'übernehmen':
            new = r1(calc(f, G_NEW)); why = 'Prüfung: übernehmen; Knoblauch ohne Fructane neu gerechnet'
        elif has_g and i in ('sarimsak-tursusu', 'makalo'):
            new = r1(calc(f, G_NEW)); why = f'Prüfung: anpassen (Knoblauch methodenabhängig); neu gerechnet mit Knoblauch {G_NEW} g/100 g ({AOAC})'
        elif has_g and d['entscheidung'] == 'anpassen':
            new = r1(d['wert'] + garlic_share(f, G_NEW) - garlic_share(f, G_OLD_MED)); why = 'Prüfung: anpassen (' + d['begruendung'] + '); Knoblauchanteil ohne Fructane'
        elif has_g:  # verwerfen: alter Wert bleibt, nur der Knoblauchanteil wird ersetzt
            new = r1(old + garlic_share(f, G_NEW) - garlic_share(f, G_OLD_SRC)); why = 'Prüfung: verwerfen (' + d['begruendung'] + '); nur Knoblauchanteil ohne Fructane neu gerechnet'
            codes = G_CODES
        elif d['entscheidung'] == 'übernehmen':
            new = d['vorschlag']; why = 'Prüfung: übernehmen'
        elif d['entscheidung'] == 'anpassen':
            new = d['wert']; why = 'Prüfung: anpassen – ' + d['begruendung']
        else:
            continue  # verwerfen ohne Knoblauch: alter Wert bleibt
        if has_g: codes = [c for c in codes if c != 'BLS:G490100'] + G_CODES  # BLS-Knoblauch (inkl. Fructane) nicht verwendet
        rec = dict(id=i, alt=old, neu=new, art='review_' + {'übernehmen': 'uebernehmen', 'anpassen': 'anpassen', 'verwerfen': 'verwerfen'}[d['entscheidung']],
                   method='recipe', source_codes=sorted(set(codes)), grund=why)
    elif has_g:
        new = r1(old + garlic_share(f, G_NEW) - garlic_share(f, G_OLD_SRC))
        if new == old: continue
        rec = dict(id=i, alt=old, neu=new, art='knoblauch', method='recipe', source_codes=G_CODES,
                   grund=f'Knoblauchanteil neu gerechnet: Knoblauch {G_OLD_SRC} → {G_NEW} g/100 g (Median USDA SR, Ciqual, CoFID; {AOAC})')
    if rec and rec['neu'] != old:
        if rec['neu'] > f['per100g']['carbs'] + 0.05: raise SystemExit(f'{i}: Ballaststoffe > Kohlenhydrate')
        out.append(rec)

# Referenzeinträge aus der Prüfung (z. B. Jasminreis gekocht: CoFID-NSP 0 g -> Median AOAC-Quellen)
for i, d in DEC.items():
    f = B[i]
    if f['source'].startswith('calculated from typical recipe') or d['entscheidung'] == 'verwerfen': continue
    p = PROP[i]
    out.append(dict(id=i, alt=f['per100g']['fiber'], neu=d['vorschlag'] if d['entscheidung'] == 'übernehmen' else d['wert'],
        art='review_uebernehmen' if d['entscheidung'] == 'übernehmen' else 'review_anpassen', method=p['method'],
        derived_from=[c.replace('SR:', 'USDA SR:').replace('CIQ:', 'Ciqual 2025:').replace('BLS:', 'BLS 4.0:').replace('COFID:', 'CoFID 2021:') for c in p['source_id']],
        source_codes=p['source_id'], grund='Prüfung: ' + d['entscheidung'] + ' – ' + p['begruendung']))

# BLS-Referenzeinträge (zubereitet) mit Fructan-Werten: klassischer Rohwert × BLS-Zubereitungsfaktor
TOPI_RAW = [('SR:169236', 1.6), ('CIQ:20196', 1.6)]          # Jerusalem artichoke, raw (USDA SR / Ciqual)
REF = {  # id: (BLS-Code zubereitet, BLS-Wert zubereitet, BLS-Rohcode, BLS-Rohwert, klassische Rohwerte, Vergleich)
 'knoblauch-im-ofen-gebacken': ('G490162', 33.291, 'G490100', 28.297, [(w['code'], w['wert']) for w in g_vals], 'Ciqual 11306 Garlic, roasted/baked 2,7 g'),
 'knoblauch-gebraten-ohne-fett': ('G490182', 44.916, 'G490100', 28.297, [(w['code'], w['wert']) for w in g_vals], 'Ciqual 11307 Garlic, pan-fried without fat 5,8 g'),
 'topinambur-im-ofen-gebacken': ('K430162', 15.474, 'K430100', 12.07, TOPI_RAW, 'CoFID 13-156 Jerusalem artichoke boiled 3,5 g (NSP), Ciqual 20050 cooked 2,2 g'),
 'topinambur-gebraten-ohne-fett': ('K430182', 13.716, 'K430100', 12.07, TOPI_RAW, 'Ciqual 20050 cooked 2,2 g'),
}
for i, (c, v, rc, rv, raw, cmp) in REF.items():
    f = B[i]; old = f['per100g']['fiber']
    raw_med = statistics.median(x for _, x in raw); fac = v / rv
    new = r1(raw_med * fac)
    raw_id = 'knoblauch-roh' if i.startswith('knoblauch') else 'topinambur-roh'
    out.append(dict(id=i, alt=old, neu=new, art='referenz_ohne_fructane', method='similar_food',
        derived_from=[raw_id, f'BLS 4.0:{c}'] + [k.replace('SR:', 'USDA SR:').replace('CIQ:', 'Ciqual 2025:').replace('COFID:', 'CoFID 2021:') for k, _ in raw],
        source_codes=[k for k, _ in raw] + [f'BLS:{rc}', f'BLS:{c}'],
        grund=(f'BLS 4.0 ({v:g} g) enthält Fructane/Inulin (AOAC 2009.01). Klassischer Rohwert = Median {", ".join(f"{k} {x:g}" for k, x in raw)} = {raw_med:g} g '
               f'× BLS-Zubereitungsfaktor {v:g}/{rv:g} (BLS {c}/{rc}) = {fac:.3f} → {new:g} g. Vergleich: {cmp}. '
               'Kohlenhydrate (gesamt) und kcal unverändert aus BLS; die Fructane zählen jetzt zu den Kohlenhydraten.')))

out.sort(key=lambda r: r['id'])
json.dump({'regel': 'Ballaststoffe nach klassischer AOAC-Methode (wie USDA SR, Ciqual, CoFID), ohne Fructane/Inulin; Maisgerichte aus Vollkornmais behalten den alten Wert',
           'knoblauch': {'alt_zutat': G_OLD_SRC, 'median_mit_bls': G_OLD_MED, 'neu': G_NEW, 'quellen': g_vals},
           'anzahl': len(out), 'aenderungen': out},
          open(os.path.join(HERE, 'fiber_final.json'), 'w'), ensure_ascii=False, indent=1)
from collections import Counter
print(len(out), Counter(r['art'] for r in out))
