#!/usr/bin/env python3
"""Stellt per100g.carbs auf verfügbare Kohlenhydrate (ohne Ballaststoffe) um
und setzt in der Quelle unbekannte Werte auf null.

Die Eingabe ist die Gesamt-KH-Basis: carbs enthält die Ballaststoffe,
fehlende protein/fat/fiber stehen als 0 und sind in source_missing genannt.

Regeln (D1):
- Die Quelle dokumentiert „verfügbare KH X g“ (BLS, Ciqual, CoFID, CH, SE, FNDDS):
  carbs wird X, auf 0,1 g gerundet. Der Wert hängt nicht von fiber ab.
  Ändert D6 die Ballaststoffe, bleibt der Quellwert richtig (nicht doppelt,
  nicht gar nicht verrechnet).
- Alle anderen Einträge (USDA SR Legacy, geschätzte Zubereitungen, Gerichte
  aus der Zutatentabelle): carbs = max(0, carbs − fiber), auf 0,1 g.
  fiber ist der zum Laufzeitpunkt in der Datei stehende Wert. Nach dem Rebase
  auf D6 ist das die dann aktuelle Ballaststoffzahl.

Regeln (D2):
- Steht ein Feld in source_missing und ist protein, fat oder fiber, wird 0 zu null.
- Gemessene Nullen (nicht in source_missing) bleiben 0.
- sugar steht bei source_missing weiterhin nicht im Objekt (kein erfundener Wert).

Nicht zweimal auf eine schon umgestellte Datei anwenden. Erkannt wird die
Gesamt-KH-Basis am Satz „an USDA-Gesamt-KH angeglichen“. Nach dem Rebase auf D6
die foods.json von D6 behalten (Gesamt-KH, neue fiber) und dieses Skript
erneut mit --write ausführen. Konflikte in data/foods.json so auflösen,
nicht von Hand die Netto-Zahlen mergen.

Aufruf:
  python3 tools/convert_carbs_net.py            # Bericht, schreibt nicht
  python3 tools/convert_carbs_net.py --write    # data/foods.json ersetzen
"""
import argparse, json, re, sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT = ROOT / 'data' / 'foods.json'

# Satz der Gesamt-KH-Angleichung. Gruppe 1 ist der dokumentierte verfügbare Wert,
# unverändert (nicht gerundet), damit ein späterer Lauf denselben Quellwert liest.
ALIGN = re.compile(
    r'Kohlenhydrate = verfügbare KH ([0-9]+(?:\.[0-9]+)?) g \+ Ballaststoffe [0-9]+(?:\.[0-9]+)? g \(an USDA-Gesamt-KH angeglichen\)'
)
DOC = re.compile(r'verfügbare KH ([0-9]+(?:\.[0-9]+)?) g')
ZERO_SET = re.compile(r'\(als 0 g gesetzt, außer Zucker\)')
BASIS_MARK = 'an USDA-Gesamt-KH angeglichen'

NULL_FIELDS = ('protein', 'fat', 'fiber')


def r1(x):
    """Wie tools/extension/build_extension.py: eine Dezimalstelle, Halbe aufwärts."""
    return round(float(x) + 1e-9, 1)


def bucket(e):
    s = e.get('source') or ''
    if s.startswith('calculated from typical recipe'):
        return 'Rezept (Zutatentabelle)'
    if 'Geschätzt aus' in s or (e.get('quality') == 'estimate' and e.get('method') == 'similar_food'):
        return 'Schätzung (USDA-Rohwert bzw. similar_food)'
    if 'FNDDS' in s:
        return 'USDA FNDDS'
    if 'USDA FoodData Central, SR Legacy' in s or 'USDA FoodData Central, SR Legacy' in s:
        return 'USDA SR Legacy'
    if 'Bundeslebensmittelschlüssel' in s or 'BLS' in s:
        return 'BLS 4.0'
    if 'Ciqual' in s:
        return 'Ciqual'
    if 'CoFID' in s or 'McCance' in s:
        return 'CoFID'
    if 'Schweizer Nährwert' in s:
        return 'CH'
    if 'Livsmedelsverket' in s:
        return 'SE'
    return 'andere'


def convert(data):
    """Ändert data in place. Liefert den Bericht."""
    text_hits = sum(1 for e in data if BASIS_MARK in (e.get('source') or ''))
    if text_hits == 0:
        raise SystemExit(
            'Keine Gesamt-KH-Basis erkannt (Satz „an USDA-Gesamt-KH angeglichen“ fehlt). '
            'Das Skript nicht auf eine schon umgestellte Datei anwenden. '
            'Nach dem Rebase auf D6 die foods.json von D6 nehmen und erneut laufen lassen.'
        )
    changed = Counter()
    unchanged = Counter()
    documented = Counter()
    subtracted = Counter()
    examples = {}
    nulls = []
    showcase = {
        'zucchini-gegrillt', 'paprika-rot-gegrillt', 'tomate-roh', 'wiener-schnitzel',
        'zucchini-in-oel-gebraten', 'chicken-nuggets-imbiss', 'rote-bete-gedaempft',
        'suesskartoffel-wedges-im-ofen-mit-oel', 'karniyarik', 'weizenkleie',
    }
    for e in data:
        b = bucket(e)
        p = e['per100g']
        old = p['carbs']
        src = e.get('source') or ''
        m = ALIGN.search(src)
        if m:
            new = r1(m.group(1))
            documented[b] += 1
            how = 'Quelle'
        else:
            fib = p.get('fiber')
            if not isinstance(fib, (int, float)):
                raise SystemExit(f'{e.get("id")}: fiber ist nicht numerisch, Subtraktion nicht möglich')
            new = r1(old - fib)
            if new < 0:
                new = 0.0
            subtracted[b] += 1
            how = 'carbs−fiber'
        # 0.0 statt 0, damit json 0.0 schreibt wie der übrige Bestand.
        if new == 0:
            new = 0.0
        p['carbs'] = new
        if new != old:
            changed[b] += 1
        else:
            unchanged[b] += 1
        if e['id'] in showcase or (how == 'Quelle' and b in ('Ciqual', 'CoFID') and b not in {x[1] for x in examples.values()}):
            examples[e['id']] = (e['id'], b, how, old, new, p.get('fiber'))
        if m:
            e['source'] = ALIGN.sub(
                lambda mm, _m=m: f'Kohlenhydrate = verfügbare KH {_m.group(1)} g (ohne Ballaststoffe)',
                src,
                count=1,
            )
            src = e['source']
        if ZERO_SET.search(src):
            e['source'] = ZERO_SET.sub('(als null gesetzt, außer Zucker)', src, count=1)
        for k in NULL_FIELDS:
            if k in e.get('source_missing', []) and p.get(k) == 0:
                p[k] = None
                nulls.append((e['id'], k, b))
            elif k in e.get('source_missing', []) and p.get(k) not in (0, 0.0, None):
                raise SystemExit(f'{e.get("id")}: source_missing enthält {k}, der Wert ist aber {p.get(k)!r} (kein 0)')
    return {
        'changed': changed,
        'unchanged': unchanged,
        'documented': documented,
        'subtracted': subtracted,
        'examples': examples,
        'nulls': nulls,
        'text_hits': text_hits,
    }


def main():
    ap = argparse.ArgumentParser(description='Gesamt-KH auf verfügbare KH umstellen, unbekannte Werte auf null.')
    ap.add_argument('path', nargs='?', default=str(DEFAULT))
    ap.add_argument('--write', action='store_true', help='Datei ersetzen (sonst nur Bericht)')
    a = ap.parse_args()
    path = Path(a.path)
    data = json.loads(path.read_text(encoding='utf-8'))
    if not isinstance(data, list):
        raise SystemExit('foods.json muss ein Array sein')
    rep = convert(data)
    buckets = sorted(set(rep['changed']) | set(rep['unchanged']))
    print(f'Datei: {path}  Einträge: {len(data)}  Quelltexte mit Gesamt-KH-Angleichung: {rep["text_hits"]}')
    print(f'{"Quelle":<42} {"geändert":>8} {"unverändert":>12} {"davon Quelle":>12} {"davon Differenz":>16}')
    for b in buckets:
        print(f'{b:<42} {rep["changed"][b]:8d} {rep["unchanged"][b]:12d} {rep["documented"][b]:12d} {rep["subtracted"][b]:16d}')
    print(f'{"SUMME":<42} {sum(rep["changed"].values()):8d} {sum(rep["unchanged"].values()):12d} {sum(rep["documented"].values()):12d} {sum(rep["subtracted"].values()):16d}')
    print('\nBeispiele (alt → neu):')
    order = ['zucchini-gegrillt', 'paprika-rot-gegrillt', 'tomate-roh', 'karniyarik', 'wiener-schnitzel',
             'zucchini-in-oel-gebraten', 'chicken-nuggets-imbiss', 'rote-bete-gedaempft',
             'suesskartoffel-wedges-im-ofen-mit-oel', 'weizenkleie']
    shown = []
    for i in order:
        if i in rep['examples']:
            shown.append(rep['examples'][i])
    for row in rep['examples'].values():
        if row not in shown:
            shown.append(row)
    for i, b, how, old, new, fib in shown:
        print(f'  {i}: {old} → {new}  ({b}, {how}, fiber={fib})')
    print(f'\nnull-Felder: {len(rep["nulls"])}')
    by = Counter(k for _, k, _ in rep['nulls'])
    print('  je Feld:', dict(by))
    for i, k, b in rep['nulls']:
        print(f'  {i}.{k}  ({b})')
    if a.write:
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        print(f'\ngeschrieben: {path}')
    else:
        print('\nProbelauf, nichts geschrieben. Zum Schreiben: --write')
    return 0


if __name__ == '__main__':
    sys.exit(main())
