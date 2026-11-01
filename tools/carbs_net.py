#!/usr/bin/env python3
"""Stellt per100g.carbs auf verfügbare Kohlenhydrate (ohne Ballaststoffe) um
und setzt in der Quelle unbekannte Werte auf null.

Die Eingabe ist die Gesamt-KH-Basis: carbs enthält die Ballaststoffe,
fehlende protein/fat/fiber stehen als 0 und sind in source_missing genannt.
fiber ist der Wert, der zum Laufzeitpunkt in der Datei steht (nach PR #12
die AOAC-Ballaststoffe).

Regeln:
- Die Quelle dokumentiert „verfügbare KH X g“ (alter Satz „an USDA-Gesamt-KH
  angeglichen“ oder „= … g (Gesamt-KH)“, auch mit Dezimalkomma): carbs wird X,
  auf 0,1 g gerundet. Der Wert hängt nicht von fiber ab.
- Alle anderen Einträge: carbs = max(0, carbs − fiber), auf 0,1 g.
- source_missing-Felder protein/fat/fiber: 0 wird null. Gemessene Nullen bleiben 0.
  Zucker bleibt weggelassen.

Gerichte aus tools/dishes/build.py sind schon netto (der Generator zieht die
Ballaststoffe der Zutat ab). Dieses Skript nicht auf diese Ausgabe und nicht
ein zweites Mal anwenden. Erkannt wird die Gesamt-KH-Basis an den beiden
Sätzen oben. Ausgabe: json.dumps(indent=2, ensure_ascii=False) plus Zeilenumbruch.

Aufruf:
  python3 tools/carbs_net.py            # Bericht, schreibt nicht
  python3 tools/carbs_net.py --write    # data/foods.json ersetzen
"""
import argparse, json, re, sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT = ROOT / 'data' / 'foods.json'

NUM = r'[0-9]+(?:[.,][0-9]+)?'
ALIGN_USDA = re.compile(
    rf'Kohlenhydrate = verfügbare KH ({NUM}) g \+ Ballaststoffe {NUM} g \(an USDA-Gesamt-KH angeglichen\)'
)
ALIGN_SUM = re.compile(
    rf'Kohlenhydrate = verfügbare KH ({NUM}) g \+ Ballaststoffe {NUM} g = {NUM} g \(Gesamt-KH\)'
)
ZERO_SET = re.compile(r'\(als 0 g gesetzt, außer Zucker\)')
NULL_FIELDS = ('protein', 'fat', 'fiber')


def r1(x):
    """Eine Dezimalstelle, Halbe aufwärts (wie tools/extension/build_extension.py)."""
    return round(float(x) + 1e-9, 1)


def parse_num(token):
    return float(token.replace(',', '.'))


def documented(src):
    """(Token, welches Muster) oder None. Token bleibt unverändert für den Quelltext."""
    m = ALIGN_USDA.search(src)
    if m:
        return m.group(1), 'usda'
    m = ALIGN_SUM.search(src)
    if m:
        return m.group(1), 'sum'
    return None


def rewrite_source(src, token, kind):
    repl = f'Kohlenhydrate = verfügbare KH {token} g (ohne Ballaststoffe)'
    pat = ALIGN_USDA if kind == 'usda' else ALIGN_SUM
    return pat.sub(repl, src, count=1)


def bucket(e):
    s = e.get('source') or ''
    if s.startswith('calculated from typical recipe'):
        return 'Rezept (Zutatentabelle)'
    if 'Geschätzt aus' in s or (e.get('quality') == 'estimate' and e.get('method') == 'similar_food'):
        return 'Schätzung (USDA-Rohwert bzw. similar_food)'
    if 'FNDDS' in s:
        return 'USDA FNDDS'
    if 'USDA FoodData Central, SR Legacy' in s:
        return 'USDA SR Legacy'
    if 'Ciqual' in s or 'Anses' in s:
        return 'Ciqual'
    if 'CoFID' in s or 'McCance' in s:
        return 'CoFID'
    if 'Schweizer Nährwert' in s:
        return 'CH'
    if 'Livsmedelsverket' in s:
        return 'SE'
    if 'Bundeslebensmittelschlüssel' in s:
        return 'BLS 4.0'
    return 'andere'


def convert(data):
    """Ändert data in place. Liefert den Bericht."""
    hits = sum(1 for e in data if documented(e.get('source') or ''))
    if hits == 0:
        raise SystemExit(
            'Keine Gesamt-KH-Basis erkannt (weder „an USDA-Gesamt-KH angeglichen“ '
            'noch „g (Gesamt-KH)“). Das Skript nicht auf eine schon umgestellte Datei '
            'und nicht auf die Netto-Ausgabe von tools/dishes/build.py anwenden.'
        )
    changed = Counter()
    unchanged = Counter()
    documented_n = Counter()
    subtracted = Counter()
    examples = {}
    nulls = []
    showcase = {
        'zucchini-gegrillt', 'paprika-rot-gegrillt', 'tomate-roh', 'wiener-schnitzel',
        'zucchini-in-oel-gebraten', 'chicken-nuggets-imbiss', 'rote-bete-gedaempft',
        'suesskartoffel-wedges-im-ofen-mit-oel', 'karniyarik', 'weizenkleie',
        'knoblauch-gebraten-ohne-fett', 'jasminreis-gekocht', 'spargel-weiss-roh',
    }
    for e in data:
        b = bucket(e)
        p = e['per100g']
        old = p['carbs']
        src = e.get('source') or ''
        doc = documented(src)
        if doc:
            token, kind = doc
            new = r1(parse_num(token))
            documented_n[b] += 1
            how = 'Quelle'
        else:
            kind = None
            token = None
            fib = p.get('fiber')
            if not isinstance(fib, (int, float)):
                raise SystemExit(f'{e.get("id")}: fiber ist nicht numerisch, Subtraktion nicht möglich')
            new = r1(old - fib)
            if new < 0:
                new = 0.0
            subtracted[b] += 1
            how = 'carbs−fiber'
        if new == 0:
            new = 0.0
        p['carbs'] = new
        if new != old:
            changed[b] += 1
        else:
            unchanged[b] += 1
        if e['id'] in showcase or (how == 'Quelle' and b in ('Ciqual', 'CoFID') and b not in {x[1] for x in examples.values()}):
            examples[e['id']] = (e['id'], b, how, old, new, p.get('fiber'))
        if doc:
            src = rewrite_source(src, token, kind)
            e['source'] = src
        if ZERO_SET.search(e.get('source') or ''):
            e['source'] = ZERO_SET.sub('(als null gesetzt, außer Zucker)', e['source'], count=1)
        for k in NULL_FIELDS:
            if k in e.get('source_missing', []) and p.get(k) == 0:
                p[k] = None
                nulls.append((e['id'], k, b))
            elif k in e.get('source_missing', []) and p.get(k) not in (0, 0.0, None):
                raise SystemExit(f'{e.get("id")}: source_missing enthält {k}, der Wert ist aber {p.get(k)!r} (kein 0)')
    return {
        'changed': changed,
        'unchanged': unchanged,
        'documented': documented_n,
        'subtracted': subtracted,
        'examples': examples,
        'nulls': nulls,
        'text_hits': hits,
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
    print(f'Datei: {path}  Einträge: {len(data)}  Quelltexte mit dokumentierten verfügbaren KH: {rep["text_hits"]}')
    print(f'{"Quelle":<42} {"geändert":>8} {"unverändert":>12} {"davon Quelle":>12} {"davon Differenz":>16}')
    for b in buckets:
        print(f'{b:<42} {rep["changed"][b]:8d} {rep["unchanged"][b]:12d} {rep["documented"][b]:12d} {rep["subtracted"][b]:16d}')
    print(f'{"SUMME":<42} {sum(rep["changed"].values()):8d} {sum(rep["unchanged"].values()):12d} {sum(rep["documented"].values()):12d} {sum(rep["subtracted"].values()):16d}')
    print('\nBeispiele (alt → neu):')
    order = ['zucchini-gegrillt', 'paprika-rot-gegrillt', 'knoblauch-gebraten-ohne-fett', 'jasminreis-gekocht',
             'tomate-roh', 'karniyarik', 'spargel-weiss-roh', 'chicken-nuggets-imbiss',
             'rote-bete-gedaempft', 'suesskartoffel-wedges-im-ofen-mit-oel']
    shown = []
    for i in order:
        if i in rep['examples']:
            shown.append(rep['examples'][i])
    for row in rep['examples'].values():
        if row not in shown:
            shown.append(row)
    for i, b, how, old, new, fib in shown:
        print(f'  {i}: {old} → {new}  ({b}, {how}, fiber={fib})')
    print(f'\nnull-Felder: {len(rep["nulls"])}  Einträge: {len({i for i, _, _ in rep["nulls"]})}')
    by = Counter(k for _, k, _ in rep['nulls'])
    print('  je Feld:', dict(by))
    for i, k, b in rep['nulls']:
        print(f'  {i}.{k}  ({b})')
    if a.write:
        text = json.dumps(data, ensure_ascii=False, indent=2) + '\n'
        path.write_text(text, encoding='utf-8')
        again = json.dumps(json.loads(text), ensure_ascii=False, indent=2) + '\n'
        if again != text:
            raise SystemExit('json.dumps-Runde ist nicht stabil')
        print(f'\ngeschrieben: {path}')
    else:
        print('\nProbelauf, nichts geschrieben. Zum Schreiben: --write')
    return 0


if __name__ == '__main__':
    sys.exit(main())
