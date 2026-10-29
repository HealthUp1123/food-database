#!/usr/bin/env python3
"""Welle 3: wave3/team_{a,b,c}.txt (cc | Name | Synonyme | KAT | Garfaktor | Label | Zutaten) -> batches/eu3_<cc>.py
Entdoppelt normalisiert (Name+Synonyme) gegen den Bestand (foods_before_off.json vor Welle 3 = foods_2884 Basis) und zwischen Teams.
Kollidierende Synonyme werden gestrichen. Report: wave3/eu3_dedup_report.json"""
import json, glob, os, re, unicodedata, collections, sys
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = sys.argv[1] if len(sys.argv) > 1 else os.path.join(R, 'wave3', 'base_2884.json')
def keys(s):
    out = set()
    for v in (s, s.replace('ä','ae').replace('ö','oe').replace('ü','ue').replace('Ä','Ae').replace('Ö','Oe').replace('Ü','Ue')):
        v = v.replace('ß','ss').replace('ł','l').replace('Ł','L').replace('ø','o').replace('æ','ae').replace('đ','d').replace('ı','i').replace('İ','I')
        v = unicodedata.normalize('NFKD', v.lower()); v = ''.join(c for c in v if not unicodedata.combining(c))
        v = re.sub(r'[^a-z0-9а-яёіїєґ]+', ' ', v).strip()
        if v: out.add(v)
    return out
base = json.load(open(BASE, encoding='utf8'))
ex_names = set().union(*(keys(d['name']) for d in base)); ex_syn = set().union(*(keys(s) for d in base for s in d.get('synonyms', [])))
rep = {'dup_existing': [], 'dup_among_new': [], 'bad_line': [], 'syn_dropped': []}
# Namen aller neuen Gerichte vorab: ein Synonym, das Name eines anderen neuen Gerichts ist, wird gestrichen (Name hat Vorrang, z.B. Rumgrog/Grog)
allnew = collections.Counter()
for team in 'abc':
    for l in open(os.path.join(R, 'wave3', f'team_{team}.txt'), encoding='utf8'):
        p = [x.strip() for x in l.split('|')]
        if len(p) == 7 and not l.startswith('#'): allnew.update(keys(p[1]))
nn, ns = set(), set(); out = collections.defaultdict(list); used = collections.Counter()
for team in 'abc':
    for ln, l in enumerate(open(os.path.join(R, 'wave3', f'team_{team}.txt'), encoding='utf8'), 1):
        l = l.strip()
        if not l or l.startswith('#'): continue
        p = [x.strip() for x in l.split('|')]
        if len(p) != 7: rep['bad_line'].append(f'{team}:{ln} {l[:70]}'); continue
        cc, n, syn, cat, y, lab, ing = p
        k = keys(n)
        syns = []
        for s in (x.strip() for x in syn.split(',')):
            if not s: continue
            if (keys(s) - k) and any(allnew[x] for x in keys(s) - k) and not (keys(s) & k): rep['syn_dropped'].append(f'{n}: {s} (Name eines anderen neuen Gerichts)'); continue
            syns.append(s)
        if k & (ex_names | ex_syn) or any(keys(s) & ex_names for s in syns):
            rep['dup_existing'].append(f'{team}/{cc}: {n}'); continue
        if k & (nn | ns) or any(keys(s) & nn for s in syns):
            rep['dup_among_new'].append(f'{team}/{cc}: {n}'); continue
        keep = []
        for s in syns:
            ks = keys(s)
            if (ks & k) and not (ks & (ex_names | ex_syn | ns)): keep.append(s); continue
            if ks & (ex_syn | ns) or any(ks & keys(x) for x in keep): rep['syn_dropped'].append(f'{n}: {s}'); continue
            keep.append(s)
        nn |= k; [ns.update(keys(s)) for s in keep]; used[cc] += 1
        out[cc].append(f"{n} | {', '.join(keep)} | {cat} | {y} | {lab} | {ing}")
for fn in glob.glob(os.path.join(R, 'batches', 'eu3_*.py')): os.remove(fn)
for cc, lines in out.items():
    open(os.path.join(R, 'batches', f'eu3_{cc}.py'), 'w', encoding='utf8').write(f"CUISINE = '{cc}'\nTEXT = \"\"\"\n" + '\n'.join(lines) + '\n"""\n')
json.dump(rep, open(os.path.join(R, 'wave3', 'eu3_dedup_report.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=1)
print('übernommen', sum(used.values()), dict(used.most_common()), '\nDuplikat Bestand', len(rep['dup_existing']), '| untereinander', len(rep['dup_among_new']), '| Zeilenfehler', len(rep['bad_line']), '| Synonyme gestrichen', len(rep['syn_dropped']))
