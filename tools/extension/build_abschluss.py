#!/usr/bin/env python3
"""Hängt die Grundzutaten der Abschlussliste an data/foods.json.

Aufruf:
  python3 tools/extension/build_abschluss.py --write
  python3 tools/dishes/build.py
  python3 tools/extension/build_abschluss.py --enrich

--write ergänzt fehlende IDs und Synonyme und schreibt data/foods.json.
--enrich liest tools/dishes/foods.json, setzt Namen und prepared der neuen
Rezepte aus tr_11_abschluss.META und schreibt data/foods.json.
Beides nutzt json.dumps(indent=2, ensure_ascii=False) plus Zeilenumbruch.
"""
import importlib.util, json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, HERE)
from spec_abschluss import RECORDS, BLS, CIQ, USDA

def r1(x):
    v = round(float(x) + 1e-9, 1)
    return 0.0 if v == 0 else v

def kcal_i(x):
    return int(round(float(x) + 1e-9))

def load(path):
    with open(path, encoding='utf-8') as f:
        return json.load(f)

def dump(path, data):
    text = json.dumps(data, ensure_ascii=False, indent=2) + '\n'
    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)

def cite(rec):
    db = rec['db']
    code = str(rec['code'])
    orig = rec['orig']
    if db == 'BLS':
        return f'{BLS}; Code {code} "{orig}". Datensatz der Datenbank (Tabellenwert; Datenherkunft laut Quelle: {rec.get("herk", "Formelberechnung")}).'
    if db == 'CIQ':
        return f'{CIQ}; Code {code} "{orig}". Datensatz der Datenbank (Tabellenwert). Eiweiß ist N × 6,25. kcal ist die Energie nach Verordnung (EU) Nr. 1169/2011.'
    if db == 'USDA':
        return f'{USDA}, FDC ID {code}: {orig}.'
    return ''

def kh_sentence(rec, cho, fib):
    if rec.get('carbs_total'):
        return (f'Kohlenhydrate sind der Gesamtwert {cho:g} g inkl. Ballaststoffe {fib:g} g. '
                f'Ballaststoffe sind die klassischen AOAC-Ballaststoffe der Quelle, ohne separat gezählte Fructane.')
    return (f'Kohlenhydrate = verfügbare KH {cho:g} g + Ballaststoffe {fib:g} g (an USDA-Gesamt-KH angeglichen), kcal wie veröffentlicht. '
            f'Ballaststoffe ohne separat gezählte Fructane.')

def build_entry(rec, foods_by_id):
    if rec.get('copy_from'):
        src = foods_by_id[rec['copy_from']]
        p = dict(src['per100g'])
        cho, fib = p['carbs'], p['fiber']
    else:
        fib = 0.0 if rec['fib'] is None else float(rec['fib'])
        cho_raw = float(rec['cho'])
        if rec.get('carbs_total'):
            carbs = r1(cho_raw)
        else:
            carbs = r1(cho_raw + fib)
        p = {
            'kcal': kcal_i(rec['kcal']),
            'protein': r1(rec['p']),
            'carbs': carbs,
            'fat': r1(rec['f']),
            'fiber': r1(fib),
        }
        if rec['sug'] is not None:
            p['sugar'] = r1(min(float(rec['sug']), p['carbs']))
        cho, fib = cho_raw, fib
    miss = list(rec.get('missing') or [])
    if rec['sug'] is None and 'sugar' not in miss and not rec.get('copy_from'):
        miss.append('sugar')
    names = rec['names']
    e = {'id': rec['id'], 'name': names['de'], 'names': names, 'type': 'item', 'barcode': None,
         'synonyms': list(rec['syn']), 'cuisine': 'int', 'category': rec['cat']}
    if rec['kind'] != 'drink':
        e['prepared'] = 'base_ingredient'
    e['is_packaged_product'] = False
    if rec['state']:
        e['state'] = rec['state']
        e['unit'] = 'g'
    bits = []
    if rec['kind'] == 'near':
        bits.append('Nahe Entsprechung: ' + rec['why'])
    if rec.get('extra'):
        bits.append(rec['extra'])
    if rec.get('fib_note'):
        bits.append(rec['fib_note'])
    if rec['kind'] != 'drink':
        note = ' '.join(bits) if bits else ('Grundzutat, kein Fertigprodukt' if rec['state'] in ('raw', 'dry', None) else 'Grundzutat (verarbeitet, generisch), kein Markenprodukt')
        if rec['kind'] == 'ref' and rec['state'] == 'dried':
            note = (note + ' ' if bits else '') + 'Grundzutat (getrocknet), kein Fertigprodukt'
        elif rec['kind'] == 'ref' and not bits:
            note = 'Grundzutat, kein Fertigprodukt' if rec['state'] in ('raw', 'dry') else 'Grundzutat (verarbeitet, generisch), kein Markenprodukt'
        e['note'] = note.strip()
    else:
        e['note'] = 'Generisches Getränk, kein Markenprodukt. Portion = übliche Tasse, Dichte ca. 1 g/ml angenommen. ' + ' '.join(bits)
    e['per100g'] = p
    if rec['kind'] == 'drink':
        label, grams = rec['portion']
        e['portion'] = {'label': label, 'grams': grams}
        e['ingredients'] = [{'name': names['de'], 'grams': grams}]
    else:
        e['ingredients'] = [{'name': names['de'], 'grams': 100}]
    if rec['kind'] == 'near':
        e['quality'] = 'estimate'
        if rec.get('copy_from'):
            src = foods_by_id[rec['copy_from']]
            e['source'] = (f'Geschätzt (Methode similar_food): {rec["why"]} '
                           f'Werte unverändert vom Eintrag {rec["copy_from"]} übernommen. '
                           f'Referenz dort: {src["source"]}')
        else:
            e['source'] = (f'Geschätzt (Methode similar_food): {rec["why"]} Referenz: {cite(rec)} {kh_sentence(rec, cho, fib)}')
        e['derived_from'] = rec['derived']
        e['method'] = 'similar_food'
    else:
        e['quality'] = 'reference'
        e['source'] = f'{cite(rec)} {kh_sentence(rec, cho, fib)}'
        if rec.get('extra'):
            e['source'] += ' ' + rec['extra']
        if rec.get('fib_note'):
            e['source'] += ' ' + rec['fib_note']
        if rec['db'] == 'USDA':
            e['fdc_id'] = int(rec['code'])
        elif rec['db'] == 'BLS':
            e['source_id'] = f'BLS 4.0:{rec["code"]}'
        elif rec['db'] == 'CIQ':
            e['source_id'] = f'Ciqual 2025:{rec["code"]}'
    if miss:
        e['source_missing'] = miss
    # Plausibilität 4*(KH-BST)+4P+9F+2BST
    est = 4 * (p['carbs'] - p['fiber']) + 4 * p['protein'] + 9 * p['fat'] + 2 * p['fiber']
    if p['protein'] + p['carbs'] + p['fat'] > 100.15:
        raise SystemExit(f'{rec["id"]}: P+KH+F > 100')
    if p['fiber'] > p['carbs'] + 0.001:
        raise SystemExit(f'{rec["id"]}: Ballaststoffe {p["fiber"]} > Kohlenhydrate {p["carbs"]}')
    gap = abs(est - p['kcal'])
    explained = {'zitronensaeure', 'weinessig', 'apfelessig'}
    if gap > 30 and rec['id'] not in explained:
        hint = (f'Die Formel 4·(KH−BST)+4·Eiweiß+9·Fett+2·BST ergibt {est:.0f} kcal, veröffentlicht sind {p["kcal"]} kcal. '
                f'Das ist der Energiefaktor der Quelle, kein geschätzter kcal-Wert.')
        e['note'] = (e.get('note', '') + ' ' + hint).strip()
        e['source'] = e['source'] + ' ' + hint
        print(f'WARN {rec["id"]}: kcal {p["kcal"]} vs Formel {est:.1f} (Abstand {gap:.1f})')
    return e

def apply_synonyms(foods):
    path = os.path.join(ROOT, 'tools', 'base_ingredients', 'synonym_additions.py')
    spec = importlib.util.spec_from_file_location('synonym_additions', path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    by = {e['id']: e for e in foods}
    for iid, syns in mod.ADD.items():
        e = by.get(iid)
        if e is None:
            raise SystemExit(f'Synonym-Ziel fehlt: {iid}')
        have = list(e.get('synonyms') or [])
        for s in syns:
            if ',' in s:
                raise SystemExit(f'Komma im Synonym: {s}')
            if s not in have:
                have.append(s)
        e['synonyms'] = have

def write_new(path):
    foods = load(path)
    ids = {e['id'] for e in foods}
    by = {e['id']: e for e in foods}
    new = []
    for rec in RECORDS:
        if rec['id'] in ids:
            continue
        new.append(build_entry(rec, by))
        ids.add(rec['id'])
    foods.extend(new)
    apply_synonyms(foods)
    dump(path, foods)
    print(f'neu {len(new)}, gesamt {len(foods)}')

def enrich(src, dest):
    foods = load(src)
    spec = importlib.util.spec_from_file_location(
        'tr_11_abschluss', os.path.join(ROOT, 'tools', 'dishes', 'batches', 'tr_11_abschluss.py'))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    by = {e['id']: e for e in foods}
    n = 0
    for iid, meta in mod.META.items():
        e = by.get(iid)
        if e is None:
            raise SystemExit(f'Rezept fehlt im Build: {iid}')
        e['names'] = meta['names']
        e['prepared'] = meta['prepared']
        e['is_packaged_product'] = False
        n += 1
    # Feldreihenfolge der neuen Gerichte an den Bestand anpassen: names hinter name.
    for e in foods:
        if e['id'] not in mod.META:
            continue
        ordered = {}
        for key in ('id', 'name', 'names', 'type', 'barcode', 'synonyms', 'cuisine', 'category',
                    'prepared', 'is_packaged_product', 'per100g', 'portion', 'ingredients', 'quality', 'source'):
            if key in e:
                ordered[key] = e[key]
        for key, val in e.items():
            if key not in ordered:
                ordered[key] = val
        e.clear()
        e.update(ordered)
    dump(dest, foods)
    print(f'Gerichte ergänzt: {n}, geschrieben {dest}, Einträge {len(foods)}')

def main():
    data = os.path.join(ROOT, 'data', 'foods.json')
    built = os.path.join(ROOT, 'tools', 'dishes', 'foods.json')
    if '--enrich' in sys.argv:
        enrich(built, data)
    elif '--write' in sys.argv:
        write_new(data)
    else:
        foods = load(data)
        by = {e['id']: e for e in foods}
        for rec in RECORDS:
            if rec['id'] in by:
                print('vorhanden', rec['id'])
                continue
            e = build_entry(rec, by)
            print(rec['id'], e['per100g'])
        print('Trockenlauf, nichts geschrieben')

if __name__ == '__main__':
    main()
