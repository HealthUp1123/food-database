#!/usr/bin/env python3
"""Generator für die Gerichte-Datenbank (tr + de).

Aufruf:  python3 build.py
Liest:   ingredients_src.txt (Referenztabelle), batches/*.py (Gerichtsdefinitionen),
         ../../data/foods.json (Bestand: Grundzutaten, Referenzen, Zusatzfelder),
         reference_overrides.json (optional, Liste im Format aus PR #15)
Schreibt: tools/dishes/foods.json (gleich data/foods.json, solange die Rezeptkerne stimmen),
          ingredients.json, build_report.txt
data/foods.json wird gelesen und nicht überschrieben.

Zeilenformat in den Batch-Dateien (eine Zeile pro Gericht):
  Name{optional-id} | Synonym1, Synonym2 | Kategorie-Code | Garfaktor | Portionslabel | zutat gramm, zutat gramm, ...
- Zutatenmengen = rohe Mengen für EINE typische Portion (Wasser wird explizit gelistet, wenn es mitgekocht wird).
- Garfaktor = Gewicht nach dem Garen / Summe der Zutaten (Verdunstung, Fettverlust; < 1.0).
- Portionsgramm = Summe * Garfaktor (auf 5 g gerundet); Nährwerte pro 100 g = Summe(Zutat g * Zutat-pro-100g) / Portionsgramm * 100.
Alle Werte sind SCHÄTZWERTE aus typischen Rezepten und ungefähren Referenzwerten, keine Laborwerte.
"""
import importlib.util, json, glob, os, re, sys, unicodedata, collections

HERE = os.path.dirname(os.path.abspath(__file__))

def load_json(path):
    try:
        with open(path, encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        raise SystemExit(f'{path}: kein gültiges JSON ({e.lineno}:{e.colno}: {e.msg})')

def check_per100g(where, p):
    if not isinstance(p, dict):
        raise SystemExit(f'{where}: per100g muss ein Objekt sein')
    for k, v in p.items():
        if v is None or (isinstance(v, (int, float)) and not isinstance(v, bool)):
            continue
        raise SystemExit(f'{where}: per100g.{k} muss eine Zahl oder null sein, nicht {type(v).__name__}')
CATS = {
 'S':'Suppe','E':'Eintopf','HF':'Hauptgericht Fleisch','HG':'Hauptgericht Geflügel','HFi':'Hauptgericht Fisch',
 'HV':'Hauptgericht vegetarisch','GZ':'Gemüse/Zeytinyağlı','GM':'Gemüse mit Fleisch','KB':'Kebap','KF':'Köfte',
 'DO':'Dolma/Sarma','T':'Teigwaren','V':'Vorspeise/Meze','D':'Dessert','G':'Gebäck','FR':'Frühstück','GT':'Getränk',
 'B':'Beilage','SA':'Salat','BR':'Brot','K':'Kuchen','RP':'Reisgericht','HH':'Hülsenfrüchte','SN':'Snack',
 'SD':'Sauce/Dip','WU':'Wurstgericht','BO':'Börek/Hamurişi','PI':'Pide/Lahmacun/Gözleme','MA':'Mantı/Teigtaschen',
 'KN':'Knödel/Kartoffelgericht','NA':'Nudelgericht','FL':'Fleischgericht (Braten)','EI':'Eiergericht','PF':'Pfannengericht',
 'PZ':'Pizza/Flammkuchen/Herzhafter Kuchen','AU':'Auflauf/Gratin',
 'KO':'Konserve/Eingelegtes','KR':'Kleingebäck/Gebäck herzhaft','SW':'Süßspeise/Sirupgebäck','PU':'Pudding/Milchdessert',
}
# Erlaubte Küchen-/Ländercodes (Welle 3: ge, am, az, md, by, me, xk, ad, li, mc, sm ergänzt)
CUISINES = set('tr de it fr es pt gr gb ie nl be at ch se no dk fi is pl cz sk hu rs hr ba bg al mk si ro ee lv lt ua ru cy mt lu ge am az md by me xk ad li mc sm'.split())
# Reine Fett-/Schmalzgerichte: >560 kcal/100 g ist hier plausibel (Schmalz/Grieben ca. 700-800 kcal)
FAT_OK = {'smalec-ze-skwarkami', 'jumari'}
def translit(s, cuisine):
    m = {'ł':'l','Ł':'L','đ':'d','Đ':'D','ø':'o','Ø':'O','æ':'ae','Æ':'Ae','ð':'d','þ':'th','œ':'oe','Œ':'Oe','ı':'i','İ':'I','ş':'s','Ş':'S','ğ':'g','Ğ':'G','ç':'c','Ç':'C','â':'a','î':'i','û':'u','ê':'e','é':'e','è':'e'}
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
    for path in sorted(glob.glob(os.path.join(HERE,'batches','*.py')), key=lambda p: (3 if os.path.basename(p).startswith('eu3_') else 2 if os.path.basename(p).startswith('eu2_') else 1 if os.path.basename(p).startswith('eu_') else 0, os.path.basename(p))):
        spec = importlib.util.spec_from_file_location(os.path.basename(path)[:-3], path)
        mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
        out.append((os.path.basename(path), mod.CUISINE, mod.TEXT))
    return out

def main():
    ing = load_ingredients()
    errors, warnings, dishes = [], [], []
    ids = {}; names = {}; allnames = {}
    for fname, cuisine, text in load_batches():
        if cuisine not in CUISINES: errors.append(f'{fname}: unbekannte Küche {cuisine}')
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
            if cuisine not in ('tr','de'):
                gk = slug(name,'x')
                if gk in allnames and allnames[gk] != cuisine: errors.append(f'{ctx} {name}: Name existiert bereits in Küche {allnames[gk]}')
            allnames.setdefault(slug(name,'x'), cuisine)
            names[nk] = ctx
            dishes.append((e, cat, yld))
    # Plausibilität
    ALK_NAMES = {'Rotwein','Weißwein','Bier','Spirituose 40 %','Sherry/Portwein/Likörwein','Likör','Apfelwein/Cider','Weinbrand/Rum'}
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
        if p['kcal'] > 560 and e['id'] not in FAT_OK: reasons.append(f'kcal/100g {p["kcal"]} sehr hoch')
        pk = p['kcal']*g/100
        if pk > 1300: reasons.append(f'Portion {pk:.0f} kcal')
        if pk < 15 and cat != 'GT': reasons.append(f'Portion nur {pk:.0f} kcal')
        if reasons: flags.append(f'{e["id"]}: ' + '; '.join(reasons))
    recipes = [d[0] for d in dishes]
    overridden = apply_reference_overrides(recipes)
    out = assemble_bestand(recipes, overridden)
    text = json.dumps(out, ensure_ascii=False, indent=2) + '\n'
    open(os.path.join(HERE,'foods.json'),'w',encoding='utf8').write(text)
    json.dump([dict(key=k, name=v['name'], per100g={f:v[f] for f in ('kcal','protein','carbs','fat','fiber')}) for k,v in ing.items()],
              open(os.path.join(HERE,'ingredients.json'),'w',encoding='utf8'), ensure_ascii=False, indent=2)
    cnt = collections.Counter(d['cuisine'] for d in recipes)
    cc = collections.Counter((d['cuisine'],d['category']) for d in recipes)
    with open(os.path.join(HERE,'build_report.txt'),'w',encoding='utf8') as f:
        f.write(f'Gerichte: {len(recipes)}  ' + ' '.join(f'{k}={v}' for k,v in sorted(cnt.items())) + f'\nAusgabe: {len(out)}\nIngredients: {len(ing)}\nFehler: {len(errors)}\n')
        for x in errors: f.write('ERR '+x+'\n')
        f.write('\nZu prüfen (Flags):\n'+'\n'.join(flags)+'\n\nKategorien:\n')
        for (c,k),n in sorted(cc.items()): f.write(f'{c} {k}: {n}\n')
    print(f'Gerichte {len(recipes)} tr={cnt["tr"]} de={cnt["de"]} eu={len(recipes)-cnt["tr"]-cnt["de"]} Ausgabe {len(out)} Fehler={len(errors)} Flags={len(flags)}')
    for x in errors[:40]: print('ERR', x)
    for x in flags[:25]: print('FLAG', x)
    return 1 if errors else 0

# Felder, die ein Override in einen bestehenden Eintrag schreiben darf.
# ingredients gehört nicht dazu: die Liste ersetzt Nährwerte, nicht die Rezeptzeilen.
OVERRIDE_FIELDS = {'per100g', 'quality', 'source', 'source_id', 'source_missing', 'names', 'fdc_id', 'note'}
OVERRIDE_REQUIRED = ('per100g', 'quality', 'source', 'source_id')

def apply_reference_overrides(recipes):
    """Liste im Format aus PR #15. Fehlt die Datei, passiert nichts.

    Pflicht je Objekt: id, per100g, quality, source, source_id.
    Optional und mitgelesen: source_missing, names, fdc_id, note.
    Abbruch bei einem Objekt statt einer Liste, bei fehlender id,
    doppelter id, unbekannter id und fehlenden Pflichtfeldern.
    ingredients bleiben unangetastet.

    source_id wird immer gelesen. yaprak-sarma-etli trägt in der Liste
    source_id "FDC:2706621", weil das Format das Feld verlangt, und
    zusätzlich fdc_id 2706621. In data/foods.json steht dieselbe Nummer
    nur in fdc_id, wie bei den anderen USDA-Zeilen. assemble_bestand
    hängt source_id deshalb nicht an, wenn der Bestand das Feld nicht hat.
    """
    path = os.path.join(HERE, 'reference_overrides.json')
    if not os.path.exists(path):
        return set()
    overrides = load_json(path)
    if not isinstance(overrides, list):
        raise SystemExit('reference_overrides.json muss eine Liste sein (Format aus PR #15)')
    by_id = {e['id']: e for e in recipes}
    seen = set()
    for o in overrides:
        if not isinstance(o, dict) or not isinstance(o.get('id'), str) or not o['id']:
            raise SystemExit('reference_overrides.json: Eintrag ohne id')
        if o['id'] in seen:
            raise SystemExit(f'reference_overrides.json: doppelte id {o["id"]}')
        seen.add(o['id'])
        e = by_id.get(o['id'])
        if e is None:
            raise SystemExit(f'reference_overrides.json: id {o["id"]} kommt in den Batches nicht vor')
        missing = [k for k in OVERRIDE_REQUIRED if k not in o]
        if missing:
            raise SystemExit(f'reference_overrides.json: {o["id"]} ohne Feld {", ".join(missing)}')
        check_per100g(f'reference_overrides.json: {o["id"]}', o['per100g'])
        e['per100g'] = o['per100g']
        e['quality'] = o['quality']
        e['source'] = o['source']
        e['source_id'] = o['source_id']
        if o.get('source_missing'):
            e['source_missing'] = o['source_missing']
        if o.get('names'):
            e['names'] = o['names']
        if 'fdc_id' in o and o['fdc_id'] is not None:
            e['fdc_id'] = o['fdc_id']
        if o.get('note'):
            e['note'] = o['note']
    print(f'Referenz-Overrides angewendet: {len(seen)}')
    return seen

def assemble_bestand(recipes, overridden=()):
    """Rezeptkerne aus den Batches, alles andere aus data/foods.json.

    Die Datei ist die Bestandsquelle für Grundzutaten, Referenz- und
    Erweiterungseinträge und für die Felder, die der Rezeptbau nicht setzt
    (names, aliases, prepared, is_packaged_product, off_similar und weitere).
    Stimmt der berechnete Kern mit dem Bestand überein, bleibt der Eintrag
    unverändert, einschließlich der Feldreihenfolge. Weicht er ab, gelten die
    berechneten Werte, die übrigen Felder bleiben. Einträge ohne Rezept
    (auch spätere Ergänzungen) werden unverändert übernommen. Neue Rezept-IDs
    werden angehängt. Es wird kein Nährwert, kein Name und keine ID erfunden.

    Overrides schreiben nur OVERRIDE_FIELDS und nur, wenn der Bestand das
    Feld schon führt. ingredients bleiben die des Bestands, nicht die
    Batch-Rezeptur. source_id von yaprak-sarma-etli ("FDC:2706621") fällt
    damit weg: veröffentlicht ist dort fdc_id.
    """
    path = os.path.normpath(os.path.join(HERE, '..', '..', 'data', 'foods.json'))
    bestand = load_json(path)
    if not isinstance(bestand, list):
        raise SystemExit('data/foods.json muss ein Array sein')
    overridden = set(overridden or ())
    by_gen = {e['id']: e for e in recipes}
    out, used = [], set()
    for entry in bestand:
        gen = by_gen.get(entry['id'])
        if gen is None:
            out.append(entry)
            continue
        used.add(entry['id'])
        if entry['id'] not in overridden and all(gen[k] == entry.get(k) for k in gen):
            out.append(entry)
            continue
        merged = {}
        for k, v in entry.items():
            if entry['id'] in overridden and k == 'ingredients':
                merged[k] = v
            elif entry['id'] in overridden and k in OVERRIDE_FIELDS and k in gen and gen[k] != v:
                merged[k] = gen[k]
            elif entry['id'] not in overridden and k in gen:
                merged[k] = gen[k]
            else:
                merged[k] = v
        if entry['id'] not in overridden:
            for k, v in gen.items():
                if k not in merged:
                    merged[k] = v
        out.append(merged)
    for e in recipes:
        if e['id'] not in used:
            out.append(dict(e))
    return out

if __name__ == '__main__': sys.exit(main())
