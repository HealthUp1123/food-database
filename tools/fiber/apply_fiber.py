# -*- coding: utf-8 -*-
"""Setzt die Ballaststoff-Korrekturen aus tools/fiber/fiber_final.json in data/foods.json (idempotent).
Muss NACH tools/functions/build_functions.py laufen (dieses schreibt foods.json neu, ändert aber keine Ballaststoffe).
Je geändertem Eintrag: per100g.fiber = neuer Wert, quality "estimate", method, ggf. derived_from und eine kurze Notiz.
Aufruf: python3 tools/fiber/apply_fiber.py   (danach: npm run build:app)"""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
PATH = os.path.join(ROOT, 'data', 'foods.json')
SEP = ' | Ballaststoffe: '
fx = {r['id']: r for r in json.load(open(os.path.join(HERE, 'fiber_final.json')))['aenderungen']}
foods = json.load(open(PATH))
done = 0
for e in foods:
    r = fx.get(e['id'])
    if not r: continue
    if e['per100g']['fiber'] not in (r['alt'], r['neu']): raise SystemExit(f"{e['id']}: Ballaststoffwert {e['per100g']['fiber']} weder alt ({r['alt']}) noch neu ({r['neu']})")
    e['per100g']['fiber'] = r['neu']
    e['quality'] = 'estimate'
    e['method'] = r['method']
    if r.get('derived_from'): e['derived_from'] = r['derived_from']
    if r['art'] == 'referenz_ohne_fructane': txt = f"{r['alt']:g} → {r['neu']:g} g, ohne Fructane/Inulin (klassische AOAC-Methode). {r['grund']}"
    elif r['art'] == 'knoblauch': txt = f"{r['alt']:g} → {r['neu']:g} g (Schätzung, {r['grund']}; Quellen {', '.join(r['source_codes'])})"
    else: txt = (f"{r['alt']:g} → {r['neu']:g} g (Schätzung, Rezeptrechnung mit Zutatenwerten = Median freier Quellen, klassische AOAC-Methode ohne Fructane/Inulin; "
                 f"Quellen {', '.join(r['source_codes'][:6])}{' …' if len(r['source_codes']) > 6 else ''}; Details tools/fiber/fiber_final.json)") if r['method'] == 'recipe' else \
               f"{r['alt']:g} → {r['neu']:g} g (Schätzung, {r['grund']})"
    base = (e.get('note') or '').split(SEP)[0].strip()
    if base.startswith('Ballaststoffe: '): base = ''
    e['note'] = (base + SEP + txt) if base else 'Ballaststoffe: ' + txt
    done += 1
if done != len(fx): raise SystemExit(f'nur {done} von {len(fx)} ids gefunden')
open(PATH, 'w').write(json.dumps(foods, ensure_ascii=False, separators=(',', ':')) + '\n')
print(f'{done} Ballaststoffwerte gesetzt')
