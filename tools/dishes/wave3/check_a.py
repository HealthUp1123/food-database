import re, unicodedata, sys, difflib, collections, os
W='/workspace/dishes2/wave3'; D='/workspace/dishes2'
def norm(s):
    m={'ı':'i','İ':'i','ł':'l','đ':'d','ø':'o','æ':'ae','ß':'ss','œ':'oe','ð':'d','þ':'th','ə':'a','Ə':'a'}
    s=''.join(m.get(c,c) for c in s.lower())
    s=unicodedata.normalize('NFKD',s); s=''.join(c for c in s if not unicodedata.combining(c))
    s=s.replace('ae','a').replace('oe','o').replace('ue','u')
    return re.sub(r'[^a-z0-9]+','',s)
def slugx(s):
    m={'ł':'l','đ':'d','ø':'o','æ':'ae','ð':'d','þ':'th','œ':'oe','ı':'i','İ':'I','ş':'s','ğ':'g','ç':'c','ä':'a','ö':'o','ü':'u','ß':'ss','ə':'a','Ə':'A'}
    s=''.join(m.get(c,c) for c in s); s=unicodedata.normalize('NFKD',s); s=''.join(c for c in s if not unicodedata.combining(c))
    return re.sub(r'[^a-z0-9]+','-',s.lower()).strip('-')
ing={}
for f in [D+'/ingredients_src.txt']+[D+f'/ingredients_add_{i}.txt' for i in range(1,5)]+[W+'/ingredients_add_a.txt']:
    if not os.path.exists(f): continue
    for l in open(f,encoding='utf8'):
        l=l.strip()
        if not l or l.startswith('#'): continue
        k,n,*v=l.split('|'); ing[k]=list(map(float,v))
ex={}
for l in open(D+'/existing_names.txt',encoding='utf8'):
    p=[x.strip() for x in l.split('|')]
    names=[p[1]]+[s.strip() for s in p[2].split(',') if s.strip()] if len(p)>2 else [p[1]]
    for n in names: ex.setdefault(norm(n),f'{p[0]}|{p[1]}')
exslug={slugx(l.split('|')[1].strip()) for l in open(D+'/existing_names.txt',encoding='utf8')}
CATS=set('S E HF HG HFi HV GZ GM KB KF DO T V D G FR GT B SA BR K RP HH SN SD WU BO PI MA KN NA FL EI PF PZ AU KO KR SW PU'.split())
ALK={'wein_rot','wein_weiss','bier','spirituose','likoerwein','likoer','apfelwein','weinbrand'}
errs=[];flags=[];seen={};cnt=collections.Counter();n=0
fuzzy=[]
exkeys=list(ex.keys())
for ln,l in enumerate(open(W+'/team_a.txt',encoding='utf8'),1):
    l=l.strip()
    if not l or l.startswith('#'): continue
    p=[x.strip() for x in l.split('|')]
    if len(p)!=7: errs.append(f'{ln}: {len(p)} Felder: {l[:50]}'); continue
    cc,name,syn,cat,y,lab,ings=p; n+=1; cnt[cc]+=1
    if cat not in CATS: errs.append(f'{ln} {name}: KAT {cat}')
    y=float(y)
    if not .5<=y<=1.05: errs.append(f'{ln} {name}: Garfaktor {y}')
    tot=[0]*5; raw=0; alk=False
    for t in [t.strip() for t in ings.split(',') if t.strip()]:
        try: k,g=t.rsplit(' ',1); g=float(g)
        except: errs.append(f'{ln} {name}: Zutat "{t}"'); continue
        if k not in ing: errs.append(f'{ln} {name}: unbekannt {k}'); continue
        if k in ALK: alk=True
        raw+=g; tot=[a+g*b/100 for a,b in zip(tot,ing[k])]
    if raw==0: continue
    pg=max(5,int(round(raw*y/5))*5); per=[x/pg*100 for x in tot]
    est=4*per[1]+4*per[2]+9*per[3]
    if not alk and abs(est-per[0])>max(.15*max(est,per[0]),12): errs.append(f'{ln} {name}: kcal {per[0]:.0f} vs makro {est:.0f}')
    if per[4]>per[2]+.05: errs.append(f'{ln} {name}: fiber>carbs')
    pk=per[0]*pg/100
    if per[0]>560: flags.append(f'{ln} {name}: {per[0]:.0f} kcal/100g')
    if (pk<80 and cat!='GT') or pk>1200: flags.append(f'{ln} {name}: Portion {pk:.0f} kcal ({pg} g)')
    if pg<25 or pg>900: flags.append(f'{ln} {name}: Portion {pg} g')
    allnames=[name]+[s.strip() for s in syn.split(',') if s.strip()]
    for nm in allnames:
        k=norm(nm)
        if k in ex: errs.append(f'{ln} {name}: Bestand-Duplikat "{nm}" ~ {ex[k]}')
        if k in seen and seen[k]!=ln: errs.append(f'{ln} {name}: intern doppelt "{nm}" (Zeile {seen[k]})')
        seen.setdefault(k,ln)
    if slugx(name) in exslug: errs.append(f'{ln} {name}: slug existiert')
    if '--fuzzy' in sys.argv:
        m=difflib.get_close_matches(norm(name),exkeys,1,0.85)
        if m: fuzzy.append(f'{ln} {name} ~ {ex[m[0]]}')
print('Zeilen',n,dict(cnt)); print('Fehler',len(errs)); print('\n'.join(errs)); print('Flags',len(flags)); print('\n'.join(flags))
if fuzzy: print('FUZZY'); print('\n'.join(fuzzy))
