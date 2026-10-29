#!/usr/bin/env python3
"""Erzeugt Grundzutaten (rohe/unverarbeitete Basis-Lebensmittel) und ihre Zubereitungsvarianten
(gekocht, gegrillt, getrocknet, tiefgekühlt, Dose, Saft ...) aus USDA FoodData Central, SR Legacy (April 2018).
Alle Nährwerte kommen 1:1 aus den USDA-Datensätzen (pro 100 g essbarer Anteil), nur gerundet.
Listen: base_list.py (L, Rohwaren) und variants_list.py (V, Varianten).
Dazu estimates_list.py (E): zubereitete Grundzutaten ohne eigenen USDA-Datensatz, aus der rohen USDA-Grundzutat
mit dokumentierten Ausbeute-, Retentions- und Fettaufnahmefaktoren berechnet (quality "estimate").
Nutzung: python3 build_base.py <usda_sr_legacy_csv_dir> <foods.json> [--write]
CSV: https://fdc.nal.usda.gov/fdc-datasets/FoodData_Central_sr_legacy_food_csv_2018-04.zip
"""
import csv, json, re, sys, unicodedata, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_list import L
from variants_list import V
from estimates_list import E

NUT = {'1008': 'kcal', '1003': 'protein', '1005': 'carbs', '1004': 'fat', '1079': 'fiber', '2000': 'sugar'}

def slug(s):
    s = s.lower().replace('ä', 'ae').replace('ö', 'oe').replace('ü', 'ue').replace('ß', 'ss')
    s = unicodedata.normalize('NFD', s)
    s = ''.join(c for c in s if not unicodedata.combining(c))
    s = s.replace('%', '-prozent')
    return re.sub(r'[^a-z0-9]+', '-', s).strip('-')

SUFFIX = re.compile(r"\s*\(Includes foods for USDA's Food Distribution Program\)")

RAW_STATES = {'raw', 'dry'}
NOTE = {
    'frozen': 'Grundzutat (tiefgekühlt, unzubereitet), kein Fertigprodukt',
    'canned': 'Grundzutat (Konserve, generisch), kein Markenprodukt',
    'dried': 'Grundzutat (getrocknet), kein Fertigprodukt',
    'processed': 'Grundzutat (verarbeitet, generisch), kein Markenprodukt',
}
NOTE_ESTIMATE = 'Grundzutat (zubereitet, geschätzt), kein Fertigprodukt'
OIL = 'Rapsöl'  # Fettaufnahme beim Braten/Rösten, Werte aus der USDA-Grundzutat

def note_for(state):
    if state in RAW_STATES:
        return 'Grundzutat, kein Fertigprodukt'
    return NOTE.get(state, 'Grundzutat (zubereitet), kein Fertigprodukt')

def norm(t):
    """Wie normalize() in src/search.mjs."""
    t = str(t).replace('İ', 'i').replace('ı', 'i').lower().replace('ß', 'ss')
    t = t.replace('ä', 'ae').replace('ö', 'oe').replace('ü', 'ue')
    t = unicodedata.normalize('NFD', t)
    t = ''.join(c for c in t if not unicodedata.combining(c))
    t = t.replace('ae', 'a').replace('oe', 'o').replace('ue', 'u')
    return re.sub(r'[^a-z0-9]+', ' ', t).strip()

def main():
    d, foods_path = sys.argv[1], sys.argv[2]
    write = '--write' in sys.argv
    by_desc = {SUFFIX.sub('', r['description']): r['fdc_id'] for r in csv.DictReader(open(os.path.join(d, 'food.csv'), encoding='utf-8'))}
    ITEMS = L + V
    miss_desc = [x[-1] for x in ITEMS if SUFFIX.sub('', x[-1]) not in by_desc]
    if miss_desc:
        raise SystemExit('USDA-Beschreibung nicht gefunden: ' + ' | '.join(miss_desc))
    wanted = {by_desc[SUFFIX.sub('', x[-1])] for x in ITEMS}
    vals = {}
    for r in csv.DictReader(open(os.path.join(d, 'food_nutrient.csv'), encoding='utf-8')):
        if r['fdc_id'] in wanted and r['nutrient_id'] in NUT:
            vals.setdefault(r['fdc_id'], {})[NUT[r['nutrient_id']]] = float(r['amount'])
    data = json.load(open(foods_path, encoding='utf-8'))
    data = [e for e in data if e.get('prepared') != 'base_ingredient']  # idempotent
    ids = {e['id'] for e in data}
    names = {e['name'].lower() for e in data}
    # Dublettenprüfung gegen alle bestehenden Namen und Synonyme (auch Gerichte), normalisiert wie die Suche
    taken = {}
    for e in data:
        for t in [e['name']] + (e.get('synonyms') or []):
            taken.setdefault(norm(t), e['id'])
    seen_fdc = {}
    out, missing = [], []
    clashes, dropped_syn, nofiber = [], [], []
    for i, (name, cat, state, syn, desc) in enumerate(ITEMS):
        is_variant = i >= len(L)
        fid = by_desc[SUFFIX.sub('', desc)]
        if fid in seen_fdc:
            raise SystemExit(f'{name}: FDC {fid} schon verwendet von {seen_fdc[fid]}')
        seen_fdc[fid] = name
        if is_variant:
            if norm(name) in taken:
                clashes.append(f'{name} -> {taken[norm(name)]}')
                continue
            keep = [x for x in syn if norm(x) not in taken]
            dropped_syn += [f'{name}: "{x}" ({taken[norm(x)]})' for x in syn if x not in keep]
            syn = keep
        v = vals[fid]
        for k in ('kcal', 'protein', 'carbs', 'fat'):
            if k not in v:
                raise SystemExit(f'{name}: {k} fehlt in USDA {fid}')
        miss = [k for k in ('fiber', 'sugar') if k not in v]
        if 'fiber' in miss and v['carbs'] > 0:
            nofiber.append(f'{name} (FDC {fid})')
            continue
        if miss:
            missing.append((name, miss))
        p = {'kcal': round(v['kcal']), 'protein': round(v['protein'], 1), 'carbs': round(v['carbs'], 1),
             'fat': round(v['fat'], 1), 'fiber': round(v.get('fiber', 0.0), 1)}
        if 'sugar' in v:
            p['sugar'] = round(v['sugar'], 1)
        iid = slug(name)
        assert iid not in ids, iid
        assert name.lower() not in names, name
        ids.add(iid); names.add(name.lower())
        en = SUFFIX.sub('', desc)
        e = {
            'id': iid, 'name': name, 'type': 'item', 'barcode': None,
            'synonyms': list(dict.fromkeys(syn + [en])),
            'cuisine': 'int', 'category': 'Grundzutat: ' + cat,
            'prepared': 'base_ingredient', 'is_packaged_product': False,
            'state': state, 'unit': 'g', 'note': note_for(state) if is_variant else 'Grundzutat, kein Fertigprodukt',
            'per100g': p,
            'ingredients': [{'name': name, 'grams': 100}],
            'quality': 'reference',
            'source': f'USDA FoodData Central, SR Legacy (April 2018), FDC ID {fid}: {en}',
            'fdc_id': int(fid),
        }
        if miss:
            e['source_missing'] = miss
        e['_raw'] = v
        out.append(e)
        for t in [name] + e['synonyms']:
            taken.setdefault(norm(t), iid)
    est = estimates(E, out, ids, names, taken, dropped_syn, clashes)
    if nofiber:
        raise SystemExit('Ballaststoffe fehlen in USDA (KH > 0) - nicht erfinden, Eintrag entfernen:\n  ' + '\n  '.join(nofiber))
    if clashes:
        raise SystemExit('Variantenname kollidiert mit bestehendem Namen/Synonym (aus variants_list.py entfernen):\n  ' + '\n  '.join(clashes))
    if dropped_syn:
        print(f'{len(dropped_syn)} Varianten-Synonyme weggelassen (schon an anderem Eintrag vergeben):')
        for x in dropped_syn:
            print('  -', x)
    print(f'{len(out)} Grundzutaten aus USDA erzeugt ({len(L)} Rohwaren-Liste, {len(V)} Varianten-Liste), {len(est)} geschätzt (estimates_list.py); ohne USDA-Wert (fiber=0 nur bei 0 g KH, sugar sonst weggelassen): {len(missing)}')
    for n, m in missing:
        print('  -', n, m)
    if write:
        json.dump(data + out + est, open(foods_path, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
        open(foods_path, 'a').write('\n')
    return out + est

def estimates(items, out, ids, names, taken, dropped_syn, clashes):
    """Zubereitete Varianten ohne USDA-Datensatz aus der rohen Grundzutat (unrund. USDA-Werte) berechnen."""
    base = {e['name']: e for e in out}
    oil = base[OIL]['_raw']
    res = []
    for name, cat, state, syn, base_name, m in items:
        if norm(name) in taken:
            clashes.append(f'{name} -> {taken[norm(name)]}')
            continue
        keep = [x for x in syn if norm(x) not in taken]
        dropped_syn += [f'{name}: "{x}" ({taken[norm(x)]})' for x in syn if x not in keep]
        b = base[base_name]
        v, y, g, ret = b['_raw'], m['y'], m['oil'], m.get('ret', {})
        if not 0.2 <= y <= 1.5:
            raise SystemExit(f'{name}: Ausbeute {y} unplausibel')
        r = lambda k: ret.get(k, 1.0)
        # Energie: Protein/Fett/KH-Retention gemeinsam (bei Dampf 0,95), plus Öl
        q = {
            'kcal': (v['kcal'] * r('carbs') + g * oil['kcal'] / 100) / y,
            'protein': v['protein'] * r('protein') / y,
            'carbs': v['carbs'] * r('carbs') / y,
            'fat': (v['fat'] * r('fat') + g * oil['fat'] / 100) / y,
            'fiber': v.get('fiber', 0.0) * r('fiber') / y,
        }
        if 'sugar' in v:
            q['sugar'] = v['sugar'] * r('carbs') / y
        p = {k: (round(x) if k == 'kcal' else round(x, 1)) for k, x in q.items()}
        iid = slug(name)
        assert iid not in ids, iid
        assert name.lower() not in names, name
        ids.add(iid); names.add(name.lower())
        ing = [{'name': base_name, 'grams': round(100 / y, 1)}]
        if g:
            ing.append({'name': OIL, 'grams': round(g / y, 1)})
        e = {
            'id': iid, 'name': name, 'type': 'item', 'barcode': None,
            'synonyms': keep,
            'cuisine': 'int', 'category': 'Grundzutat: ' + cat,
            'prepared': 'base_ingredient', 'is_packaged_product': False,
            'state': state, 'unit': 'g', 'note': NOTE_ESTIMATE,
            'per100g': p,
            'ingredients': ing,
            'quality': 'estimate',
            'source': (f'Geschätzt aus {base_name} ({b["source"]}). {m["src"]}. '
                       f'Formel: pro 100 g zubereitet = (roh x Retention + Fettaufnahme) / Ausbeute.'),
            'derived_from': b['id'],
        }
        if 'source_missing' in b:
            e['source_missing'] = b['source_missing']
        res.append(e)
        for t in [name] + keep:
            taken.setdefault(norm(t), iid)
    for e in out:
        e.pop('_raw', None)
    return res

if __name__ == '__main__':
    main()
