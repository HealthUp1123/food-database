#!/usr/bin/env python3
"""Erzeugt Grundzutaten (rohe/unverarbeitete Basis-Lebensmittel) aus USDA FoodData Central, SR Legacy (April 2018).
Alle Nährwerte kommen 1:1 aus den USDA-Datensätzen (pro 100 g essbarer Anteil), nur gerundet.
Nutzung: python3 build_base.py <usda_sr_legacy_csv_dir> <foods.json> [--write]
CSV: https://fdc.nal.usda.gov/fdc-datasets/FoodData_Central_sr_legacy_food_csv_2018-04.zip
"""
import csv, json, re, sys, unicodedata, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from base_list import L

NUT = {'1008': 'kcal', '1003': 'protein', '1005': 'carbs', '1004': 'fat', '1079': 'fiber', '2000': 'sugar'}

def slug(s):
    s = s.lower().replace('ä', 'ae').replace('ö', 'oe').replace('ü', 'ue').replace('ß', 'ss')
    s = unicodedata.normalize('NFD', s)
    s = ''.join(c for c in s if not unicodedata.combining(c))
    s = s.replace('%', '-prozent')
    return re.sub(r'[^a-z0-9]+', '-', s).strip('-')

def main():
    d, foods_path = sys.argv[1], sys.argv[2]
    write = '--write' in sys.argv
    by_desc = {r['description']: r['fdc_id'] for r in csv.DictReader(open(os.path.join(d, 'food.csv'), encoding='utf-8'))}
    wanted = {by_desc[x[-1]] for x in L}
    vals = {}
    for r in csv.DictReader(open(os.path.join(d, 'food_nutrient.csv'), encoding='utf-8')):
        if r['fdc_id'] in wanted and r['nutrient_id'] in NUT:
            vals.setdefault(r['fdc_id'], {})[NUT[r['nutrient_id']]] = float(r['amount'])
    data = json.load(open(foods_path, encoding='utf-8'))
    data = [e for e in data if e.get('prepared') != 'base_ingredient']  # idempotent
    ids = {e['id'] for e in data}
    names = {e['name'].lower() for e in data}
    out, missing = [], []
    for name, cat, state, syn, desc in L:
        fid = by_desc[desc]
        v = vals[fid]
        for k in ('kcal', 'protein', 'carbs', 'fat'):
            if k not in v:
                raise SystemExit(f'{name}: {k} fehlt in USDA {fid}')
        miss = [k for k in ('fiber', 'sugar') if k not in v]
        if 'fiber' in miss and v['carbs'] > 0:
            raise SystemExit(f'{name}: Ballaststoffe fehlen in USDA {fid} (KH > 0) - nicht erfinden, Eintrag entfernen')
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
        en = re.sub(r"\s*\(Includes foods for USDA's Food Distribution Program\)", '', desc)
        e = {
            'id': iid, 'name': name, 'type': 'item', 'barcode': None,
            'synonyms': list(dict.fromkeys(syn + [en])),
            'cuisine': 'int', 'category': 'Grundzutat: ' + cat,
            'prepared': 'base_ingredient', 'is_packaged_product': False,
            'state': state, 'unit': 'g', 'note': 'Grundzutat, kein Fertigprodukt',
            'per100g': p,
            'ingredients': [{'name': name, 'grams': 100}],
            'quality': 'reference',
            'source': f'USDA FoodData Central, SR Legacy (April 2018), FDC ID {fid}: {en}',
            'fdc_id': int(fid),
        }
        if miss:
            e['source_missing'] = miss
        out.append(e)
    print(f'{len(out)} Grundzutaten erzeugt; ohne USDA-Wert (fiber=0 nur bei 0 g KH, sugar sonst weggelassen): {len(missing)}')
    for n, m in missing:
        print('  -', n, m)
    if write:
        json.dump(data + out, open(foods_path, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
        open(foods_path, 'a').write('\n')
    return out

if __name__ == '__main__':
    main()
