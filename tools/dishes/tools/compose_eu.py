#!/usr/bin/env python3
"""Fügt recipes/rec_*.txt (Name | Garfaktor | Portionslabel | Zutaten) mit candidates/survivors.json
(Synonyme, Kategorie, Küche) zu batches/eu_<cc>.py zusammen. Nur Gerichte mit Rezept werden übernommen."""
import json, glob, os, collections
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sv = {d['name']: d for d in json.load(open(os.path.join(R, 'candidates', 'survivors.json'), encoding='utf8'))}
used = set(); out = collections.defaultdict(list)
for f in sorted(glob.glob(os.path.join(R, 'recipes', 'rec_*.txt'))):
    for l in open(f, encoding='utf8'):
        l = l.strip()
        if not l or l.startswith('#'): continue
        p = [x.strip() for x in l.split('|')]
        if len(p) != 4: print('BAD', l[:70]); continue
        n, y, lab, ing = p
        if n not in sv: print('KEIN KANDIDAT', n); continue
        d = sv[n]; used.add(n)
        out[d['cuisine']].append(f"{n} | {', '.join(d['synonyms'])} | {d['cat']} | {y} | {lab} | {ing}")
for cc, lines in out.items():
    open(os.path.join(R, 'batches', f'eu_{cc}.py'), 'w', encoding='utf8').write(f"CUISINE = '{cc}'\nTEXT = \"\"\"\n" + '\n'.join(lines) + '\n"""\n')
print('Rezepte:', len(used), 'Küchen:', len(out), '| Survivors ohne Rezept:', len(sv) - len(used))
