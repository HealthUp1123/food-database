#!/usr/bin/env python3
"""Generator für die Gerichte-Datenbank (tr + de).

Aufruf:  python3 build.py
Liest:   ingredients_src.txt (Referenztabelle), batches/*.py (Gerichtsdefinitionen)
Schreibt: foods.json, ingredients.json, build_report.txt

Zeilenformat in den Batch-Dateien (eine Zeile pro Gericht):
  Name{optional-id} | Synonym1, Synonym2 | Kategorie-Code | Garfaktor | Portionslabel | zutat gramm, zutat gramm, ...
- Zutatenmengen = rohe Mengen für EINE typische Portion (Wasser wird explizit gelistet, wenn es mitgekocht wird).
- Garfaktor = Gewicht nach dem Garen / Summe der Zutaten (Verdunstung, Fettverlust; < 1.0).
- Portionsgramm = Summe * Garfaktor (auf 5 g gerundet); Nährwerte pro 100 g = Summe(Zutat g * Zutat-pro-100g) / Portionsgramm * 100.
Alle Werte sind SCHÄTZWERTE aus typischen Rezepten und ungefähren Referenzwerten, keine Laborwerte.
"""
import importlib.util, json, glob, os, re, sys, unicodedata, collections

HERE = os.path.dirname(os.path.abspath(__file__))
CATS = {
 'S':'Suppe','E':'Eintopf','HF':'Hauptgericht Fleisch','HG':'Hauptgericht Geflügel','HFi':'Hauptgericht Fisch',
 'HV':'Hauptgericht vegetarisch','GZ':'Gemüse/Zeytinyağlı','GM':'Gemüse mit Fleisch','KB':'Kebap','KF':'Köfte',
 'DO':'Dolma/Sarma','T':'Teigwaren','V':'Vorspeise/Meze','D':'Dessert','G':'Gebäck','FR':'Frühstück','GT':'Getränk',
 'B':'Beilage','SA':'Salat','BR':'Brot','K':'Kuchen','RP':'Reisgericht','HH':'Hülsenfrüchte','SN':'Snack',
 'SD':'Sauce/Dip','WU':'Wurstgericht','BO':'Börek/Hamurişi','PI':'Pide/Lahmacun/Gözleme','MA':'Mantı/Teigtaschen',
 'KN':'Knödel/Kartoffelgericht','NA':'Nudelgericht','FL':'Fleischgericht (Braten)','EI':'Eiergericht','PF':'Pfannengericht',
 'KO':'Konserve/Eingelegtes','KR':'Kleingebäck/Gebäck herzhaft','SW':'Süßspeise/Sirupgebäck','PU':'Pudding/Milchdessert',
}
def translit(s, cuisine):
    m = {'ı':'i','İ':'I','ş':'s','Ş':'S','ğ':'g','Ğ':'G','ç':'c','Ç':'C','â':'a','î':'i','û':'u','ê':'e','é':'e','è':'e'}
    if cuisine == 'de':
        m.update({'ä':'ae','ö':'oe','ü':'ue','Ä':'Ae','Ö':'Oe','Ü':'Ue','ß':'ss'})
    else:
        m.update({'ä':'a','ö':'o','ü':'u','Ä':'A','Ö':'O','Ü':'U','ß':'ss'})
    s = ''.join(m.get(c, c) for c in s)
    s = unicodedata.normalize('NFKD', s)
    return ''.join(c for c in s if not unicodedata.combining(c))
def slug(s, cuisine):
    s = translit(s, cuisine).lower()
    s = re.sub(r'[^a-z0-9]+', '-', s).strip('-')
    return s

def load_ingredients():
    ing = {}
    for l in open(os.path.join(HERE,'ingredients_src.txt'), encoding='utf8'):
        l = l.strip()
        if not l or l.startswith('#'): continue
        k,n,kc,p,c,f,fi = l.split('|')
        ing[k] = dict(name=n, kcal=float(kc), protein=float(p), carbs=float(c), fat=float(f), fiber=float(fi))
    return ing

def load_batches():
    out = []
    for path in sorted(glob.glob(os.path.join(HERE,'batches','*.py'))):
        spec = importlib.util.spec_from_file_location(os.path.basename(path)[:-3], path)
        mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
        out.append((os.path.basename(path), mod.CUISINE, mod.TEXT))
    return out

def main():
    ing = load_ingredients()
    errors, warnings, dishes = [], [], []
    ids = {}; names = {}
    for fname, cuisine, text in load_batches():
        for ln, line in enumerate(text.splitlines(), 1):
            line = line.strip()
            if not line or line.startswith('#'): continue
            ctx = f'{fname}:{ln}'
            parts = [p.strip() for p in line.split('|')]
            if len(parts) != 6: errors.append(f'{ctx}: erwarte 6 Felder, habe {len(parts)}: {line[:60]}'); continue
            name, syns, cat, yld, label, ings = parts
            m = re.match(r'^(.*?)\{([a-z0-9-]+)\}$', name)
            did = None
            if m: name, did = m.group(1).strip(), m.group(2)
            if not did: did = slug(name, cuisine)
            if cat not in CATS: errors.append(f'{ctx} {name}: unbekannte Kategorie {cat}'); continue
            try: yld = float(yld)
            except: errors.append(f'{ctx} {name}: Garfaktor ungültig'); continue
            if not (0.5 <= yld <= 1.05): errors.append(f'{ctx} {name}: Garfaktor {yld} unplausibel')
            lst = []; tot = dict(kcal=0,protein=0,carbs=0,fat=0,fiber=0); raw = 0
            for tok in [t.strip() for t in ings.split(',') if t.strip()]:
                try: k, g = tok.rsplit(' ',1); g = float(g)
                except: errors.append(f'{ctx} {name}: Zutat ungültig "{tok}"'); continue
                if k not in ing: errors.append(f'{ctx} {name}: unbekannte Zutat "{k}"'); continue
                lst.append((k,g)); raw += g
                for f in tot: tot[f] += g * ing[k][f] / 100
            if not lst: errors.append(f'{ctx} {name}: keine Zutaten'); continue
            pg = max(5, int(round(raw * yld / 5.0)) * 5)
            per = {'kcal': int(round(tot['kcal']/pg*100))}
            for f in ('protein','carbs','fat','fiber'): per[f] = round(tot[f]/pg*100, 1)
            sy = []
            for s in [x.strip() for x in syns.split(',') if x.strip()]:
                if s != name and s not in sy: sy.append(s)
            a = translit(name, cuisine)
            if a != name and a not in sy: sy.insert(0, a)
            e = collections.OrderedDict()
            e['id']=did; e['name']=name; e['type']='dish'; e['barcode']=None; e['synonyms']=sy
            e['cuisine']=cuisine; e['category']=CATS[cat]; e['per100g']=per
            e['portion']={'label':label,'grams':pg}
            merged = collections.OrderedDict()
            for k,g in lst: merged[k] = merged.get(k,0)+g
            e['ingredients']=[{'name':ing[k]['name'],'grams':(int(g) if float(g).is_integer() else g)} for k,g in merged.items()]
            e['quality']='estimate'
            e['source']='calculated from typical recipe and approximate reference values'
            if did in ids: errors.append(f'{ctx} {name}: doppelte id {did} (auch {ids[did]})')
            ids[did] = ctx
            nk = (cuisine, slug(name,cuisine))
            if nk in names: errors.append(f'{ctx} {name}: doppelter Name')
            names[nk] = ctx
            dishes.append((e, cat, yld))
    # Plausibilität
    ALK_NAMES = {'Rotwein','Weißwein','Bier'}
    flags = []
    for e, cat, yld in dishes:
        p = e['per100g']; est = 4*p['protein']+4*p['carbs']+9*p['fat']
        c = f"{e['id']}"
        if p['protein']+p['carbs']+p['fat'] > 100.0001: errors.append(f'{c}: P+C+F > 100')
        if not 0 <= p['kcal'] <= 950: errors.append(f'{c}: kcal außerhalb 0-950')
        alk = any(i['name'] in ALK_NAMES for i in e['ingredients'])
        if alk:
            if p['kcal'] < est*0.85-1: errors.append(f'{c}: kcal < Makro (Alkohol)')
        elif abs(est-p['kcal']) > max(0.15*max(est,p['kcal']), 12): errors.append(f'{c}: kcal {p["kcal"]} vs Makro {est:.0f} >15%')
        if p['fiber'] > p['carbs']+0.05: errors.append(f'{c}: Ballaststoffe > Kohlenhydrate')
        g = e['portion']['grams']
        reasons = []
        if g < 25 or g > 900: reasons.append(f'Portion {g} g')
        if p['kcal'] < 12 and cat not in ('GT',): reasons.append(f'kcal/100g {p["kcal"]} sehr niedrig')
        if p['kcal'] > 560: reasons.append(f'kcal/100g {p["kcal"]} sehr hoch')
        pk = p['kcal']*g/100
        if pk > 1300: reasons.append(f'Portion {pk:.0f} kcal')
        if pk < 15 and cat != 'GT': reasons.append(f'Portion nur {pk:.0f} kcal')
        if reasons: flags.append(f'{e["id"]}: ' + '; '.join(reasons))
    out = [d[0] for d in dishes]
    json.dump(out, open(os.path.join(HERE,'foods.json'),'w',encoding='utf8'), ensure_ascii=False, indent=2)
    json.dump([dict(key=k, name=v['name'], per100g={f:v[f] for f in ('kcal','protein','carbs','fat','fiber')}) for k,v in ing.items()],
              open(os.path.join(HERE,'ingredients.json'),'w',encoding='utf8'), ensure_ascii=False, indent=2)
    cnt = collections.Counter(d['cuisine'] for d in out)
    cc = collections.Counter((d['cuisine'],d['category']) for d in out)
    with open(os.path.join(HERE,'build_report.txt'),'w',encoding='utf8') as f:
        f.write(f'Gerichte: {len(out)}  tr={cnt["tr"]} de={cnt["de"]}\nIngredients: {len(ing)}\nFehler: {len(errors)}\n')
        for x in errors: f.write('ERR '+x+'\n')
        f.write('\nZu prüfen (Flags):\n'+'\n'.join(flags)+'\n\nKategorien:\n')
        for (c,k),n in sorted(cc.items()): f.write(f'{c} {k}: {n}\n')
    print(f'Gerichte {len(out)} tr={cnt["tr"]} de={cnt["de"]} Fehler={len(errors)} Flags={len(flags)}')
    for x in errors[:40]: print('ERR', x)
    for x in flags[:25]: print('FLAG', x)
    return 1 if errors else 0
if __name__ == '__main__': sys.exit(main())
