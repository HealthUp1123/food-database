#!/usr/bin/env python3
"""Erweiterung 2026-10: hängt neue Einträge aus freien Nährwertdatenbanken an data/foods.json an.

Aufruf:  python3 tools/extension/build_extension.py --src <all.pkl> [--write]
all.pkl = zusammengeführte Quelltabellen (BLS 4.0, Ciqual 2025, CoFID 2021, CH 7.1, USDA FNDDS/SR),
Spalten: db, code, name, origin, kcal, prot, fat, cho (verfügbare KH), fib, sug, alc.
Ohne --write wird nur geprüft und berichtet.
"""
import argparse, json, math, re, sys, unicodedata, os
from pathlib import Path
import pandas as pd

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from spec_veg import BASE, PREP, VEG, VEG_EXTRA
from spec_de import DE
from spec_dishes import TR, TR_EST, TR_DRINKS, IMBISS, ASIA
from spec_drinks import DRINKS, SKIP_EXISTING

REPO = HERE.parent.parent
# Kürzere/klarere IDs, wo der automatisch erzeugte Slug zu lang oder unschön ist
ID_OVERRIDE = {
 'rum-37-540-prozent-vol': 'rum',
 'kaisergemuese-brokkoli-blumenkohl-karotten-im-ofen-gebacken': 'kaisergemuese-im-ofen-gebacken',
 'kaisergemuese-brokkoli-blumenkohl-karotten-gebraten-ohne-fett': 'kaisergemuese-gebraten-ohne-fett',
 'peperoni-gruen-pfefferschote-gebraten-ohne-fett': 'peperoni-gruen-gebraten-ohne-fett',
 'peperoni-rot-pfefferschote-gebraten-ohne-fett': 'peperoni-rot-gebraten-ohne-fett',
 'tavuk-doener-haehnchen-doenerfleisch-gegrillt': 'tavuk-doener-fleisch-gegrillt',
 'doener-vegetarisch-fladenbrot-mit-rohkost-schafskaese-und-sauce': 'doener-vegetarisch',
 'lahmacun-mit-haehnchen-grillfleisch-salat-und-sauce': 'lahmacun-mit-haehnchen-und-salat',
 'pho-mit-rindfleisch-vietnamesische-nudelsuppe': 'pho-mit-rindfleisch',
 'pho-ohne-fleisch-vietnamesische-nudelsuppe': 'pho-ohne-fleisch',
 'egg-roll-vegetarisch-us-fruehlingsrolle-frittiert': 'egg-roll-vegetarisch-frittiert',
}
# Inhaltliche Duplikate, die der Namensvergleich nicht erkennt (bestehender Eintrag beschreibt dasselbe Gericht)
MANUAL_SKIP = {
 'BLS:Y9A1090': 'inhaltlich gleich wie bestehendes "lahmacun-durum" (Schätzwert) - Upgrade-Kandidat',
 'BLS:Y599112': 'inhaltlich gleich wie bestehendes "tavuk-wrap" (Schätzwert) - Upgrade-Kandidat',
}
LANGS = ['de', 'en', 'tr', 'fr', 'es', 'pt', 'it', 'zh']
FNDDS_PORTIONS = os.environ.get('FNDDS_PORTIONS', '/workspace/base_ingredients/src/fndds/FoodData_Central_survey_food_csv_2024-10-31/food_portion.csv')

CITE = {
 'BLS': ('BLS 4.0', 'Max Rubner-Institut (2025): Bundeslebensmittelschlüssel (BLS), Version 4.0 - Deutsche Nährstoffdatenbank, Karlsruhe, DOI 10.25826/Data20251217-134202-0, Lizenz CC BY 4.0'),
 'CIQ': ('Ciqual 2025', 'Anses (2025): Ciqual French food composition table, Version 2025, Zenodo-Record 17550133, Lizenz CC BY 4.0'),
 'COFID': ('CoFID 2021', 'Public Health England (2021): McCance and Widdowson\'s The Composition of Foods Integrated Dataset (CoFID) 2021, Open Government Licence v3.0'),
 'CH': ('CH 7.1', 'Schweizer Nährwertdatenbank V7.1, Bundesamt für Lebensmittelsicherheit und Veterinärwesen (BLV), naehrwertdaten.ch (frei verwendbar mit Quellenangabe)'),
 'FNDDS': (None, 'USDA FoodData Central, FNDDS 2021-2023 (Survey Foods, Release 2024-10-31), gemeinfrei (CC0 1.0)'),
 'SR': (None, 'USDA FoodData Central, SR Legacy (April 2018)'),
}

def slug(s):
    s = s.lower()
    for a, b in (('ä', 'ae'), ('ö', 'oe'), ('ü', 'ue'), ('ß', 'ss'), ('ı', 'i'), ('ş', 's'), ('ğ', 'g'), ('ç', 'c'), ('%', '-prozent')):
        s = s.replace(a, b)
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode()
    s = re.sub(r'[^a-z0-9]+', '-', s).strip('-')
    return re.sub(r'-+', '-', s)

def norm(s):
    s = unicodedata.normalize('NFKD', str(s).casefold())
    s = ''.join(c for c in s if not unicodedata.combining(c)).replace('ı', 'i').replace('ß', 'ss')
    return re.sub(r'\s+', ' ', re.sub(r'[^\w]+', ' ', s)).strip()

def r1(x):
    v = round(float(x) + 1e-9, 1)
    return 0.0 if v == 0 else v

def isnan(x):
    return x is None or (isinstance(x, float) and math.isnan(x))

def names8(s):
    parts = [p.strip() for p in s.split('|')]
    assert len(parts) == 8 and all(parts), s
    return dict(zip(LANGS, parts))

class Builder:
    def __init__(self, src):
        df = pd.read_pickle(src)
        df['k'] = df.db + ':' + df.code.astype(str)
        self.df = df.drop_duplicates('k').set_index('k')
        self.foods = json.load(open(REPO / 'data/foods.json', encoding='utf-8'))
        self.ids = {e['id'] for e in self.foods}
        self.keys = {}
        self.display = {}
        self.dropped_aliases = []
        for e in self.foods:
            for s in [e['name'], *e.get('names', {}).values()]:
                self.display.setdefault(norm(s), e['id'])
        self.src_ids = set()
        for e in self.foods:
            for s in self.strings(e):
                self.keys.setdefault(norm(s), e['id'])
            if e.get('source_id'): self.src_ids.add(e['source_id'])
            if e.get('fdc_id'): self.src_ids.add(f"FDC:{e['fdc_id']}")
        p = pd.read_csv(FNDDS_PORTIONS, usecols=['fdc_id', 'portion_description', 'gram_weight'])
        self.portions = {(int(a), b): float(c) for a, b, c in zip(p.fdc_id, p.portion_description, p.gram_weight)}
        self.new, self.skipped, self.missing = [], [], []

    @staticmethod
    def strings(e):
        yield e['name']
        yield from e.get('synonyms', [])
        yield from e.get('names', {}).values()
        for v in e.get('aliases', {}).values(): yield from v

    def row(self, src):
        if src not in self.df.index:
            self.missing.append(src); return None
        return self.df.loc[src]

    def values(self, src, r, allow_fill=False):
        """per100g + source_missing + Text zur KH-Herleitung. None = nicht verwendbar."""
        if isnan(r.kcal):
            return None, 'kcal fehlt in der Quelle'
        miss, fills = [], []
        def get(col, key):
            v = r[col]
            if isnan(v):
                if allow_fill or key in ('fiber', 'sugar'):
                    miss.append(key); return 0.0
                return None
            return float(v)
        prot, fat, cho = get('prot', 'protein'), get('fat', 'fat'), get('cho', 'carbs_available')
        if None in (prot, fat, cho):
            return None, 'Protein/Fett/KH fehlt in der Quelle'
        fib = r.fib
        if isnan(fib):
            if cho <= 3 or allow_fill:
                fib = 0.0; miss.append('fiber')
            else:
                return None, f'Ballaststoffe fehlen in der Quelle bei {cho:g} g KH'
        fib = float(fib)
        p = {'kcal': int(round(float(r.kcal) + 1e-9)), 'protein': r1(prot), 'carbs': r1(cho + fib), 'fat': r1(fat), 'fiber': r1(fib)}
        if isnan(r.sug):
            miss.append('sugar')
        else:
            p['sugar'] = r1(min(float(r.sug), cho + fib))
        alc = r.get('alc')
        if not isnan(alc) and float(alc) >= 0.05:
            p['alcohol'] = r1(alc)
        miss = [m for m in ('protein', 'fat', 'fiber', 'sugar') if m in miss]
        ktxt = f'Kohlenhydrate = verfügbare KH {cho:g} g + Ballaststoffe {fib:g} g (an USDA-Gesamt-KH angeglichen), kcal wie veröffentlicht.'
        if miss:
            ktxt += ' In der Quelle nicht angegeben: ' + ', '.join({'protein': 'Protein', 'fat': 'Fett', 'fiber': 'Ballaststoffe', 'sugar': 'Zucker'}[m] for m in miss) + (' (als 0 g gesetzt, außer Zucker).' if any(m != 'sugar' for m in miss) else '.')
        return (p, miss, ktxt), None

    def cite(self, src, r, ktxt):
        db, code = src.split(':', 1)
        label, base = CITE[db]
        nm = re.sub(r'\s+', ' ', str(r['name'])).strip()
        origin = '' if isnan(r.get('origin')) else re.sub(r'\s+', ' ', str(r.get('origin'))).strip()
        if db in ('FNDDS', 'SR'):
            return f'{base}, FDC ID {code}: {nm}. {ktxt}', {'fdc_id': int(code)}
        kind = 'rezeptberechnet' if re.search(r'rezept|recipe|zutaten|ingredients|calculated', origin, re.I) else 'Tabellenwert'
        o = f'; Datenherkunft laut Quelle: {origin}' if origin else ''
        return f'{base}; Code {code} "{nm}". Datensatz der Datenbank ({kind}{o}). {ktxt}', {'source_id': f'{label}:{code}'}

    def dup(self, e, src_key):
        if e.get('_src') in MANUAL_SKIP:
            return MANUAL_SKIP[e['_src']]
        if src_key in self.src_ids:
            return f'Quelldatensatz {src_key} bereits verwendet'
        if e['id'] in self.ids:
            return f'id {e["id"]} existiert'
        for s in [e['name'], *e['names'].values()]:
            k = norm(s)
            if k in self.keys:
                return f'Name "{s}" existiert bereits ({self.keys[k]})'
        return None

    def add(self, e, src, area, src_key):
        if 'aliases' in e:
            al = {}
            for l, vs in e['aliases'].items():
                keep = []
                for v in vs:
                    hit = self.display.get(norm(v))
                    if hit: self.dropped_aliases.append((e['id'], v, hit))
                    else: keep.append(v)
                if keep: al[l] = keep
            if al: e['aliases'] = al
            else: e.pop('aliases')
        e['_src'] = src
        if e['id'] in ID_OVERRIDE:
            e = {'id': ID_OVERRIDE[e['id']], **{k: v for k, v in e.items() if k != 'id'}}
        reason = self.dup(e, src_key)
        e.pop('_src')
        if reason:
            self.skipped.append((area, src, e['id'], reason)); return
        self.ids.add(e['id']); self.src_ids.add(src_key)
        for s in self.strings(e): self.keys.setdefault(norm(s), e['id'])
        e['_area'] = area
        self.new.append(e)

    def portion(self, spec, src=''):
        if not spec: return None, ''
        if isinstance(spec[1], (int, float)) and len(spec) == 2:
            return {'label': spec[0], 'grams': spec[1]}, ''
        label, fdc, desc = spec[:3]
        mult = spec[3] if len(spec) > 3 else 1
        g = self.portions.get((fdc, desc))
        assert g, (fdc, desc)
        grams = round(g * mult, 1)
        grams = int(grams) if grams == int(grams) else grams
        how = f'{mult} x ' if mult != 1 else ''
        other = '' if src == f'FNDDS:{fdc}' else ' (Portionsgröße eines vergleichbaren FNDDS-Gerichts übernommen)'
        return {'label': label, 'grams': grams}, f'Portionsgröße aus USDA FNDDS 2021-2023 food_portion, FDC ID {fdc} "{desc}" = {how}{g:g} g{other}.'

    def base_entry(self, src, names, cat, state, aliases, area, note='Grundzutat (zubereitet), kein Fertigprodukt', syn=None, cuisine='int'):
        r = self.row(src)
        if r is None: return
        v, why = self.values(src, r)
        if v is None:
            self.skipped.append((area, src, slug(names['de']), why)); return
        p, miss, ktxt = v
        source, ref = self.cite(src, r, ktxt)
        e = {'id': slug(names['de']), 'name': names['de'], 'names': names}
        al = {k: v for k, v in (aliases or {}).items() if v}
        if al: e['aliases'] = al
        e.update({'type': 'item', 'barcode': None, 'synonyms': syn or [], 'cuisine': cuisine, 'category': cat,
                  'prepared': 'base_ingredient', 'is_packaged_product': False})
        if state: e['state'] = state
        e.update({'unit': 'g', 'note': note, 'per100g': p, 'ingredients': [{'name': names['de'], 'grams': 100}],
                  'quality': 'reference', 'source': source})
        e.update(ref)
        if miss: e['source_missing'] = miss
        self.add(e, src, area, ref.get('source_id') or f"FDC:{ref['fdc_id']}")

    def run(self):
        # 1 Zubereitungen
        for src, b, prep in VEG:
            bn, al = BASE[b]; pn, state = PREP[prep]
            bn, pn = names8(bn), names8(pn)
            n = {l: (f'{bn[l]}（{pn[l]}）' if l == 'zh' else f'{bn[l]}, {pn[l]}') for l in LANGS}
            cat = 'Grundzutat: Getreide, Teigwaren & Brot' if src.startswith('BLS:K27') else 'Grundzutat: Gemüse'  # Pilze/Kartoffeln stehen im Bestand unter Gemüse
            self.base_entry(src, n, cat, state, al, '1 Zubereitungen')
        for src, nm, state, al in VEG_EXTRA:
            self.base_entry(src, names8(nm), 'Grundzutat: Gemüse', state, al, '1 Zubereitungen')
        # 2 Deutsche Grundprodukte
        for src, nm, cat, state, al in DE:
            note = 'Grundzutat (verarbeitet, generisch), kein Markenprodukt' if state in ('processed', 'smoked', 'baked', 'roasted') else 'Grundzutat, kein Fertigprodukt'
            if state == 'cooked': note = 'Grundzutat (zubereitet), kein Fertigprodukt'
            if state == 'raw': note = 'Grundzutat, kein Fertigprodukt'
            self.base_entry(src, names8(nm), cat, state, al, '2 Deutsche Grundprodukte', note=note)
        # 3 Türkische Grundzutaten
        for d in TR:
            note = {'processed': 'Grundzutat (verarbeitet, generisch), kein Markenprodukt', 'grilled': 'Grundzutat (zubereitet), kein Fertigprodukt',
                    'cooked': 'Grundzutat (zubereitet), kein Fertigprodukt'}.get(d['state'], 'Grundzutat, kein Fertigprodukt')
            self.base_entry(d['src'], names8(d['names']), d['cat'], d['state'], d['aliases'], '3 Türkische Grundzutaten', note=note)
        for d in TR_EST:
            self.estimate(d)
        for src, nm, cu, por, al in TR_DRINKS:
            self.drink(src, names8(nm), cu, por, al, '3 Türkische Grundzutaten')
        # 4 Imbiss / 5 Asiatisch
        for d in IMBISS: self.dish(d, '4 Imbiss/Streetfood')
        for d in ASIA:
            if d['type'] == 'item':
                self.base_entry(d['src'], names8(d['names']), d['cat'], d['state'], d['aliases'], '5 Asiatische Küche',
                                note='Grundzutat (zubereitet), kein Fertigprodukt' if d['state'] == 'cooked' else 'Grundzutat, kein Fertigprodukt')
            else:
                self.dish(d, '5 Asiatische Küche')
        # 6 Getränke
        for src, nm, cu, por, al in DRINKS:
            self.drink(src, names8(nm), cu, por, al, '6 Getränke')
        for src, ex in SKIP_EXISTING.items():
            self.skipped.append(('6 Getränke', src, ex, f'existiert bereits als "{ex}" (Schätzwert) - Upgrade-Kandidat, nicht doppelt angelegt'))

    def estimate(self, d):
        r = self.row(d['src'])
        if r is None: return
        v, why = self.values(d['src'], r)
        p, miss, ktxt = v
        names = names8(d['names'])
        db, code = d['src'].split(':', 1)
        nm = re.sub(r'\s+', ' ', str(r['name'])).strip()
        base = CITE[db][1]
        derived = f'{CITE[db][0] or "FDC"}:{code}'
        e = {'id': d['id'], 'name': names['de'], 'names': names}
        if d['aliases']: e['aliases'] = d['aliases']
        e.update({'type': 'item', 'barcode': None, 'synonyms': [], 'cuisine': 'int', 'category': d['cat'], 'prepared': 'base_ingredient',
                  'is_packaged_product': False, 'state': d['state'], 'unit': 'g',
                  'note': 'Grundzutat (verarbeitet, generisch, geschätzt), kein Markenprodukt - Werte eines ähnlichen Lebensmittels',
                  'per100g': p, 'ingredients': [{'name': names['de'], 'grams': 100}], 'quality': 'estimate',
                  'source': f'Geschätzt (Methode similar_food): {d["why"]} Referenz: {base}; Code {code} "{nm}". {ktxt}',
                  'derived_from': derived, 'method': 'similar_food'})
        if miss: e['source_missing'] = miss
        self.add(e, d['src'], '3 Türkische Grundzutaten', f'EST:{d["id"]}')

    def dish(self, d, area):
        src = d['src']; r = self.row(src)
        if r is None: return
        v, why = self.values(src, r)
        names = names8(d['names'])
        if v is None:
            self.skipped.append((area, src, slug(names['de']), why)); return
        p, miss, ktxt = v
        source, ref = self.cite(src, r, ktxt)
        por, ptxt = self.portion(d['portion'], src)
        e = {'id': slug(names['de']), 'name': names['de'], 'names': names}
        if d['aliases']: e['aliases'] = d['aliases']
        e.update({'type': 'dish', 'barcode': None, 'synonyms': d['syn'], 'cuisine': d['cuisine'], 'category': d['cat'],
                  'prepared': d['prepared'], 'is_packaged_product': False})
        notes = ['Generisches Gericht (Nährwerte für das ganze Gericht aus amtlicher Datenbank), kein Markenprodukt.']
        if por:
            notes.append(ptxt + (' Imbiss-Portionen können deutlich größer sein.' if area.startswith('4') else ''))
        else:
            notes.append('Keine Portionsgröße angegeben, weil die Quelle keine nennt.')
        e['note'] = ' '.join(notes)
        e['per100g'] = p
        if por: e['portion'] = por
        e.update({'ingredients': [{'name': names['de'], 'grams': por['grams'] if por else 100}], 'quality': 'reference', 'source': source})
        e.update(ref)
        if miss: e['source_missing'] = miss
        self.add(e, src, area, ref.get('source_id') or f"FDC:{ref['fdc_id']}")

    def drink(self, src, names, cuisine, por, aliases, area):
        r = self.row(src)
        if r is None: return
        v, why = self.values(src, r, allow_fill=True)
        if v is None:
            self.skipped.append((area, src, slug(names['de']), why)); return
        p, miss, ktxt = v
        source, ref = self.cite(src, r, ktxt)
        e = {'id': slug(names['de']), 'name': names['de'], 'names': names}
        if aliases: e['aliases'] = aliases
        e.update({'type': 'item', 'barcode': None, 'synonyms': [], 'cuisine': cuisine, 'category': 'Getränk',
                  'is_packaged_product': False,
                  'note': 'Generisches Getränk, kein Markenprodukt. Portion = übliche Ausschank-/Füllmenge, Dichte ca. 1 g/ml angenommen.'
                          + (' Alkohol (Ethanol) in per100g.alcohol in g/100 g; liefert ca. 7 kcal/g, deshalb liegt kcal über 4/4/9.' if 'alcohol' in p else ''),
                  'per100g': p, 'portion': {'label': por[0], 'grams': por[1]},
                  'ingredients': [{'name': names['de'], 'grams': por[1]}], 'quality': 'reference', 'source': source})
        e.update(ref)
        if miss: e['source_missing'] = miss
        self.add(e, src, area, ref.get('source_id') or f"FDC:{ref['fdc_id']}")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--src', required=True)
    ap.add_argument('--write', action='store_true')
    ap.add_argument('--report', default=None)
    a = ap.parse_args()
    b = Builder(a.src)
    b.run()
    from collections import Counter
    print('Neu:', len(b.new))
    for (ar, q), n in sorted(Counter((e['_area'], e['quality']) for e in b.new).items()): print(f'  {ar:28} {q:9} {n}')
    print('Fehlende Codes:', b.missing)
    print('Entfernte Aliase (= Anzeigename eines anderen Eintrags):')
    for x in b.dropped_aliases: print('  ', *x, sep=' | ')
    print('Übersprungen:', len(b.skipped))
    for s in b.skipped: print('  ', *s, sep=' | ')
    if a.report:
        json.dump({'new': [{'id': e['id'], 'area': e['_area'], 'quality': e['quality'], 'kcal': e['per100g']['kcal']} for e in b.new],
                   'skipped': b.skipped, 'dropped_aliases': b.dropped_aliases, 'missing': b.missing}, open(a.report, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    if a.write:
        for e in b.new: e.pop('_area')
        foods = b.foods + b.new
        txt = json.dumps(foods, ensure_ascii=False, indent=2) + '\n'
        (REPO / 'data/foods.json').write_text(txt, encoding='utf-8')
        print('geschrieben:', len(foods))

if __name__ == '__main__':
    main()
