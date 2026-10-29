#!/usr/bin/env python3
"""Nachholrunde: recipes/rec_extra_*.txt + candidates/rest_all.json -> batches/eu2_<cc>.py
Entdoppelt gegen die bestehenden Gerichte (foods_before_off.json, Namen+Synonyme, normalisiert) und untereinander.
Bestehende Gerichte/IDs werden nicht verändert. Schreibt candidates/eu2_dedup_report.json."""
import json, glob, os, re, unicodedata, collections
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def nk(s):
    s = s.replace('ß', 'ss').replace('ł', 'l').replace('ø', 'o').replace('æ', 'ae').replace('đ', 'd').replace('ı', 'i')
    s = unicodedata.normalize('NFKD', s.lower()); s = ''.join(c for c in s if not unicodedata.combining(c))
    return re.sub(r'[^a-z0-9]+', ' ', s).strip()
base = json.load(open(os.path.join(R, 'foods_before_off.json'), encoding='utf8'))
ex_names = {nk(d['name']) for d in base}; ex_syn = {nk(s) for d in base for s in d.get('synonyms', [])}
cands = {}
for d in json.load(open(os.path.join(R, 'candidates', 'rest_all.json'), encoding='utf8')): cands.setdefault(d['name'], d)
rep = {'no_candidate': [], 'dup_existing': [], 'dup_among_new': [], 'bad_line': [], 'syn_dropped': 0}
new_names, new_syn = set(), set(); out = collections.defaultdict(list); used = 0
for f in sorted(glob.glob(os.path.join(R, 'recipes', 'rec_extra_*.txt'))):
    for l in open(f, encoding='utf8'):
        l = l.strip()
        if not l or l.startswith('#'): continue
        p = [x.strip() for x in l.split('|')]
        if len(p) != 4: rep['bad_line'].append(l[:70]); continue
        n, y, lab, ing = p
        c = cands.get(n)
        if not c: rep['no_candidate'].append(n); continue
        k = nk(n)
        if k in ex_names or k in ex_syn or any(nk(s) in ex_names for s in c['synonyms']):
            rep['dup_existing'].append(n); continue
        if k in new_names or k in new_syn or any(nk(s) in new_names for s in c['synonyms']):
            rep['dup_among_new'].append(n); continue
        syns = []
        for s in c['synonyms']:
            if nk(s) in ex_syn or nk(s) in new_syn or nk(s) == k: rep['syn_dropped'] += 1; continue
            syns.append(s)
        new_names.add(k); new_syn.update(nk(s) for s in syns); used += 1
        out[c['cuisine']].append(f"{n} | {', '.join(syns)} | {c['cat']} | {y} | {lab} | {ing}")
for fn in glob.glob(os.path.join(R, 'batches', 'eu2_*.py')): os.remove(fn)
for cc, lines in out.items():
    open(os.path.join(R, 'batches', f'eu2_{cc}.py'), 'w', encoding='utf8').write(f"CUISINE = '{cc}'\nTEXT = \"\"\"\n" + '\n'.join(lines) + '\n"""\n')
json.dump(rep, open(os.path.join(R, 'candidates', 'eu2_dedup_report.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=1)
print('übernommen', used, '| ohne Kandidat', len(rep['no_candidate']), '| Duplikat zu bestehend', len(rep['dup_existing']), '| Duplikat untereinander', len(rep['dup_among_new']), '| Zeilenfehler', len(rep['bad_line']), '| Synonyme entfernt', rep['syn_dropped'])
