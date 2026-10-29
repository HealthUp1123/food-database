#!/usr/bin/env python3
"""Open-Food-Facts-Abgleich (OFF) für die Gerichte-Datenbank.

REGEL (aktuell, Änderung vom User): Gerichte (zuhause/Restaurant/Imbiss) und Fertigprodukte werden GETRENNT gesehen.
  * Ein Gericht wird NICHT entfernt, nur weil OFF ein gleichnamiges Fertigprodukt hat. Es behält seinen Eintrag und bekommt
      "prepared": "homemade" | "restaurant", "is_packaged_product": false und bei OFF-Treffern "off_similar": [bis zu 3 OFF-Barcodes] (nur Hinweis).
  * Entfernt werden nur Einträge, die selbst Fertig-/Supermarktprodukte sind: type "item" mit Barcode, der in OFF vorliegt (Barcode-Abgleich gegen den Dump).
  (Frühere Regel "Gerichte, die in OFF vorliegen, nicht eintragen" ist damit abgelöst; die Treffer-Prüfung selbst bleibt als Hinweisgeber erhalten.)

Definition "OFF-Treffer" (konservativ, siehe BUILD_NOTES.md):
  Normalisierung (beide Seiten): Kleinbuchstaben, Diakritika entfernt (ä→a, ı→i, ç→c ...), ß→ss,
  zusätzlich die deutsche Umschreibung (ä→ae, ö→oe, ü→ue), Satzzeichen → Leerzeichen, in Wörter (Tokens) zerlegt.
  Verglichen werden Gerichtsname und die wichtigsten Synonyme (max. --max-terms) gegen product_name und
  generic_name jedes OFF-Produkts (ein Markenname am Anfang/Ende des OFF-Namens wird zusätzlich abgezogen).
  Treffer ("found"), wenn mindestens eine dieser Bedingungen gilt:
    exact        : Token-Folge von OFF-Name == Token-Folge des Gerichts/Synonyms
    off_in_dish  : OFF-Name steht als zusammenhängende Ganzwort-Folge im Gerichtsnamen und deckt >= 80 % der Gericht-Tokens ab
    dish_in_off  : Gericht steht als zusammenhängende Ganzwort-Folge im OFF-Namen und macht >= 80 % der OFF-Tokens aus
  Mengenangaben im OFF-Namen (400g, 0,5 l) werden vor dem Vergleich ignoriert.
  NICHT als Treffer zählen: reine Marken-Treffer, Zutaten-/Teilwort-Treffer, Treffer mit < 80 % Abdeckung ("near", nur informativ).

Backends:
  api  : OFF Search-a-licious (https://search.openfoodfacts.org/search), 1 Anfrage/s, Backoff bei 429/5xx, SQLite-Cache.
         (Die alte cgi/search.pl und api/v2/search lieferten am 29.10.2026 "Page temporarily unavailable".)
         Status-Datei: off_check_status.json
  dump : lokaler Abgleich gegen den OFF-CSV-Dump (en.openfoodfacts.org.products.csv.gz) -> DuckDB-Index (off_names.duckdb).
         Status-Datei: off_check_status_dump.json   (getrennt, damit parallele Läufe sich nicht überschreiben)

Aufrufe (im Ordner dishes2; für den dump-Backend /workspace/venv/bin/python verwenden, dort ist duckdb installiert):
  python3 tools/off_check.py check  --input foods_before_off.json --backend api            # nur noch nicht geprüfte Gerichte
  python3 tools/off_check.py check  --input foods_before_off.json --backend api --only-ids a,b,c
  python3 tools/off_check.py dump-index --csv off_dump/en.openfoodfacts.org.products.csv.gz
  python3 tools/off_check.py check  --input foods_before_off.json --backend dump
  python3 tools/off_check.py apply  --input foods_before_off.json --out foods.json --removed removed_in_off.json
  python3 tools/off_check.py status --input foods_before_off.json                          # Zusammenfassung
Status je Gericht: checked / found / matches / near / terms / Zeitpunkt.
"""
import argparse, json, os, re, sqlite3, sys, time, unicodedata, urllib.parse, urllib.request, urllib.error, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UA = "OwnDataBank/1.0 (healthplus.support.feedback@gmail.com)"
SAL = "https://search.openfoodfacts.org/search"
FIELDS = "code,product_name,generic_name,brands"
COVER = 0.8
STATUS_FILES = {'api': os.path.join(ROOT, 'off_check_status.json'), 'dump': os.path.join(ROOT, 'off_check_status_dump.json')}

# ---------------------------------------------------------------- Normalisierung
def _base(s, de):
    s = (s or '').lower()
    s = s.replace('ß', 'ss').replace('ı', 'i').replace('İ', 'i').replace('æ', 'ae').replace('œ', 'oe').replace('ø', 'o').replace('ł', 'l')
    if de:
        s = s.replace('ä', 'ae').replace('ö', 'oe').replace('ü', 'ue')
    s = unicodedata.normalize('NFKD', s)
    s = ''.join(c for c in s if not unicodedata.combining(c))
    s = re.sub(r'[^a-z0-9]+', ' ', s)
    return ' '.join(s.split())

QTY = re.compile(r'\b\d+(?:[.,]\d+)?\s?(?:g|gr|kg|mg|ml|cl|dl|l|oz|stk|st|x)\b', re.I)
def forms(s, strip_qty=False):
    """Normalisierte Varianten (Diakritika entfernt / deutsche Umschreibung) als Token-Tupel.
    strip_qty (nur OFF-Seite): Mengenangaben wie '400g', '0,5 l' werden vor dem Vergleich entfernt."""
    if strip_qty and s: s = QTY.sub(' ', s)
    out = []
    for de in (False, True):
        t = tuple(_base(s, de).split())
        if t and t not in out: out.append(t)
    return out

def norm(s): return _base(s, False)

def _contig(small, big):
    n, m = len(small), len(big)
    if n == 0 or n > m: return False
    return any(big[i:i+n] == small for i in range(m - n + 1))

def _brand_variants(tokens, brands):
    """OFF-Name ggf. ohne führende/nachgestellte Marke."""
    outs = [tokens]
    if isinstance(brands, str): brands = brands.split(',')
    for b in (brands or [])[:3]:
        for bt in forms(b):
            if len(tokens) > len(bt) and tokens[:len(bt)] == bt: outs.append(tokens[len(bt):])
            if len(tokens) > len(bt) and tokens[-len(bt):] == bt: outs.append(tokens[:-len(bt)])
    return outs

def match_kind(dish_term, off_name, brands=None):
    """Gibt 'exact' | 'off_in_dish' | 'dish_in_off' | 'near' | None zurück."""
    if not off_name: return None
    best = None
    rank = {'exact': 3, 'off_in_dish': 2, 'dish_in_off': 2, 'near': 1}
    for D in forms(dish_term):
        for T0 in forms(off_name, True):
            for T in _brand_variants(T0, brands):
                if not T: continue
                k = None
                if T == D: k = 'exact'
                elif _contig(T, D) and len(T) / len(D) >= COVER: k = 'off_in_dish'
                elif _contig(D, T) and len(D) / len(T) >= COVER: k = 'dish_in_off'
                elif (len(D) >= 2 and _contig(D, T)) or (len(T) >= 2 and _contig(T, D)): k = 'near'
                if k and (best is None or rank[k] > rank[best]): best = k
    return best

def dish_terms(d, max_terms=4):
    """Name + wichtigste Synonyme, dedupliziert über die normalisierten Formen."""
    seen, out = set(), []
    for s in [d['name']] + list(d.get('synonyms') or []):
        fs = set(forms(s))
        if not fs or fs & seen: continue
        seen |= fs; out.append(s)
        if len(out) >= max_terms: break
    return out

# ---------------------------------------------------------------- Cache + API
class Cache:
    def __init__(self, path):
        self.db = sqlite3.connect(path)
        self.db.execute('create table if not exists api_cache(endpoint text, term text, page_size int, body text, ts text, primary key(endpoint, term, page_size))')
        self.db.commit()
    def get(self, ep, term, ps):
        r = self.db.execute('select body from api_cache where endpoint=? and term=? and page_size=?', (ep, term, ps)).fetchone()
        return json.loads(r[0]) if r else None
    def put(self, ep, term, ps, body):
        self.db.execute('insert or replace into api_cache values(?,?,?,?,?)', (ep, term, ps, json.dumps(body, ensure_ascii=False), datetime.datetime.now(datetime.timezone.utc).isoformat() + 'Z'))
        self.db.commit()

class Api:
    def __init__(self, cache, min_interval=1.0, page_size=25, log=print, max_retries=6):
        self.cache, self.min_interval, self.ps, self.log, self.max_retries = cache, min_interval, page_size, log, max_retries
        self.last = 0.0; self.requests = 0; self.cached = 0; self.failed = 0
    def search(self, term):
        hit = self.cache.get('sal', term, self.ps)
        if hit is not None: self.cached += 1; return hit['hits'], True
        url = SAL + '?' + urllib.parse.urlencode({'q': term, 'page_size': self.ps, 'fields': FIELDS})
        wait = 30
        for attempt in range(self.max_retries):
            dt = time.time() - self.last
            if dt < self.min_interval: time.sleep(self.min_interval - dt)
            self.last = time.time(); self.requests += 1
            try:
                req = urllib.request.Request(url, headers={'User-Agent': UA, 'Accept': 'application/json'})
                with urllib.request.urlopen(req, timeout=60) as r:
                    body = r.read().decode('utf8')
                j = json.loads(body)
                res = {'hits': [{k: h.get(k) for k in ('code', 'product_name', 'generic_name', 'brands')} for h in j.get('hits', [])], 'count': j.get('count')}
                self.cache.put('sal', term, self.ps, res)
                return res['hits'], False
            except urllib.error.HTTPError as e:
                ra = e.headers.get('Retry-After')
                w = int(ra) if ra and ra.isdigit() else wait
                self.log(f'  HTTP {e.code} bei "{term}" -> warte {w}s (Versuch {attempt+1})')
            except Exception as e:
                w = wait; self.log(f'  Fehler {type(e).__name__} bei "{term}" -> warte {w}s (Versuch {attempt+1})')
            time.sleep(w); wait = min(wait * 2, 600)
        self.failed += 1
        return None, False

# ---------------------------------------------------------------- Status
def now(): return datetime.datetime.now().astimezone().isoformat(timespec='seconds')
def load_json(p, default):
    return json.load(open(p, encoding='utf8')) if os.path.exists(p) else default
def save_json(p, o):
    tmp = p + '.tmp'
    json.dump(o, open(tmp, 'w', encoding='utf8'), ensure_ascii=False, indent=1); os.replace(tmp, p)

def check_api(dishes, a, status, log):
    api = Api(Cache(a.cache), a.min_interval, a.page_size, log)
    t0 = time.time(); done = 0
    for i, d in enumerate(dishes, 1):
        st = status.setdefault(d['id'], {'name': d['name'], 'cuisine': d.get('cuisine')})
        if not a.recheck and st.get('api', {}).get('checked'): continue
        terms = dish_terms(d, a.max_terms); matches, near, ok = [], [], True
        for t in terms:
            hits, _ = api.search(t)
            if hits is None: ok = False; continue
            for h in hits:
                for fld in ('product_name', 'generic_name'):
                    k = match_kind(t, h.get(fld), h.get('brands'))
                    if k in ('exact', 'off_in_dish', 'dish_in_off'):
                        matches.append({'term': t, 'kind': k, 'code': h.get('code'), 'field': fld, 'off_name': h.get(fld), 'brands': h.get('brands')})
                    elif k == 'near':
                        near.append({'term': t, 'code': h.get('code'), 'field': fld, 'off_name': h.get(fld)})
        order = {'exact': 0, 'off_in_dish': 1, 'dish_in_off': 1}
        matches.sort(key=lambda m: order[m['kind']])
        # Treffer-Liste kurz halten
        uniq, seen = [], set()
        for m in matches:
            if m['code'] in seen: continue
            seen.add(m['code']); uniq.append(m)
        st['api'] = {'checked': ok, 'found': bool(uniq) if ok or uniq else None, 'terms': terms, 'matches': uniq[:5], 'n_matches': len(uniq),
                     'near': near[:3], 'checked_at': now()}
        if not ok and not uniq: st['api']['found'] = None
        done += 1
        if done % 10 == 0:
            save_json(a.status, status)
            el = time.time() - t0
            log(f'[api] {i}/{len(dishes)} geprüft (neu: {done}) | Requests {api.requests}, Cache {api.cached}, Fehler {api.failed} | {el/60:.1f} min')
    save_json(a.status, status)
    log(f'[api] fertig. neu geprüft {done}, Requests {api.requests}, aus Cache {api.cached}, endgültig fehlgeschlagen {api.failed}')

# ---------------------------------------------------------------- Dump
def dump_index(a, log):
    import duckdb
    if os.path.exists(a.dumpdb): os.remove(a.dumpdb)
    con = duckdb.connect(a.dumpdb)
    con.execute("pragma memory_limit='3GB'"); con.execute("pragma temp_directory='%s'" % os.path.join(os.path.dirname(a.dumpdb), 'duck_tmp'))
    log('Lese CSV (nur code, product_name, generic_name, brands) ...')
    con.execute(f"""create table raw as select code, product_name, generic_name, brands from read_csv('{a.csv}',
        delim='\\t', header=true, quote='', escape='', strict_mode=false, ignore_errors=true, sample_size=20000, max_line_size=20000000,
        columns={{'code':'VARCHAR','product_name':'VARCHAR','generic_name':'VARCHAR','brands':'VARCHAR'}}, all_varchar=true, auto_detect=false,
        null_padding=true) """ if False else f"""create table raw as select code, product_name, generic_name, brands from read_csv('{a.csv}',
        delim='\\t', header=true, quote='', escape='', ignore_errors=true, sample_size=20000, max_line_size=20000000, all_varchar=true, null_padding=true)
        where product_name is not null or generic_name is not null""")
    n = con.execute('select count(*) from raw').fetchone()[0]
    log(f'{n} Produkte mit Namen')
    con.execute("create table names as select code, product_name, generic_name, brands from raw"); con.execute('drop table raw')
    # Normalisierte Formen: fold (ä→a) und de (ä→ae)
    def sqlnorm(col, de):
        e = f"lower(coalesce({col},''))"
        e = f"replace(replace(replace(replace({e},'ß','ss'),'ı','i'),'æ','ae'),'ø','o')"
        if de: e = f"replace(replace(replace({e},'ä','ae'),'ö','oe'),'ü','ue')"
        return f"trim(regexp_replace(regexp_replace(strip_accents({e}),'[^a-z0-9]+',' ','g'),' +',' ','g'))"
    con.execute("create table forms(form varchar, code varchar, fld varchar)")
    for fld in ('product_name', 'generic_name'):
        for de in (False, True):
            con.execute(f"insert into forms select distinct {sqlnorm(fld, de)} f, code, '{fld}' from names where {fld} is not null")
            # ohne Marke (erste Marke als Präfix/Suffix)
            b = sqlnorm("split_part(brands,',',1)", de); nn = sqlnorm(fld, de)
            con.execute(f"""insert into forms select distinct substr({nn}, length({b})+2), code, '{fld}' from names
                            where brands is not null and {fld} is not null and length({b})>0 and starts_with({nn}, {b}||' ') and length({nn})>length({b})+1""")
            con.execute(f"""insert into forms select distinct substr({nn}, 1, length({nn})-length({b})-1), code, '{fld}' from names
                            where brands is not null and {fld} is not null and length({b})>0 and ends_with({nn}, ' '||{b}) and length({nn})>length({b})+1""")
    con.execute("delete from forms where form is null or form=''")
    con.execute("create table meta as select ? as built_at, ? as src, ? as n", [now(), os.path.basename(a.csv), n])
    log('Index fertig: ' + str(con.execute('select count(*) from forms').fetchone()[0]) + ' Namensformen')
    con.close()

def check_dump(dishes, a, status, log):
    import duckdb
    con = duckdb.connect(a.dumpdb, read_only=True)
    meta = con.execute('select * from meta').fetchone()
    log(f'[dump] Index vom {meta[0]} aus {meta[1]} ({meta[2]} Produkte)')
    # 1) Kandidatenphrasen je Gericht (exact + off_in_dish: alle zusammenhängenden Teilfolgen mit >= 80 % Abdeckung)
    rows, per = [], {}
    for d in dishes:
        terms = dish_terms(d, a.max_terms)
        per[d['id']] = terms
        for t in terms:
            for D in forms(t):
                n = len(D); mn = max(1, -(-int(COVER * n * 100) // 100))
                import math
                mn = max(1, math.ceil(COVER * n - 1e-9))
                for L in range(mn, n + 1):
                    for i in range(n - L + 1):
                        rows.append((d['id'], t, ' '.join(D), ' '.join(D[i:i+L])))
    con.execute('create temp table q(id varchar, term varchar, dish varchar, phrase varchar)')
    con.executemany('insert into q values(?,?,?,?)', rows)
    log(f'[dump] {len(rows)} Phrasen; Join (exact / off_in_dish) ...')
    cand = con.execute("""select distinct q.id, q.term, q.dish, f.form, f.code, f.fld from q join forms f on f.form=q.phrase""").fetchall()
    # 2) dish_in_off mit Zusatzwörtern (nur möglich bei >= 4 Tokens): LIKE-Scan
    long_terms = sorted({(r[0], r[1], r[2]) for r in rows if len(r[2].split()) >= 4})
    log(f'[dump] {len(cand)} Kandidaten; LIKE-Scan für {len(long_terms)} lange Terms ...')
    for j, (did, t, dish) in enumerate(long_terms):
        n = len(dish.split())
        for form, code, fld in con.execute("select form, code, fld from forms where form like ? and length(form)<=?", ('%' + dish + '%', int(len(dish) * 1.6) + 8)).fetchall():
            cand.append((did, t, dish, form, code, fld))
        if j % 200 == 0: log(f'  LIKE {j}/{len(long_terms)}')
    # 3) Rohnamen holen und mit match_kind verifizieren
    codes = sorted({c[4] for c in cand})
    raw = {}
    for i in range(0, len(codes), 5000):
        chunk = codes[i:i+5000]
        for code, pn, gn, br in con.execute(f"select code, product_name, generic_name, brands from names where code in ({','.join('?'*len(chunk))})", chunk).fetchall():
            raw[code] = (pn, gn, br)
    res = {d['id']: [] for d in dishes}
    for did, t, dish, form, code, fld in cand:
        pn, gn, br = raw.get(code, (None, None, None))
        name = pn if fld == 'product_name' else gn
        k = match_kind(t, name, br)
        if k in ('exact', 'off_in_dish', 'dish_in_off'):
            res[did].append({'term': t, 'kind': k, 'code': code, 'field': fld, 'off_name': name, 'brands': br})
    order = {'exact': 0, 'off_in_dish': 1, 'dish_in_off': 1}
    for d in dishes:
        ms = sorted(res[d['id']], key=lambda m: order[m['kind']]); uniq, seen = [], set()
        for m in ms:
            if m['code'] in seen: continue
            seen.add(m['code']); uniq.append(m)
        st = status.setdefault(d['id'], {'name': d['name'], 'cuisine': d.get('cuisine')})
        st['dump'] = {'checked': True, 'found': bool(uniq), 'terms': per[d['id']], 'matches': uniq[:5], 'n_matches': len(uniq), 'index': meta[0], 'checked_at': now()}
    save_json(a.status, status)
    log(f'[dump] fertig: {sum(1 for d in dishes if status[d["id"]]["dump"]["found"])} von {len(dishes)} in OFF gefunden')

# ---------------------------------------------------------------- apply / status
def load_status(a):
    """Vereinigt die Status-Dateien beider Backends (oder die mit --status angegebene Datei)."""
    if a.status: return load_json(a.status, {})
    out = {}
    for b, p in STATUS_FILES.items():
        for k, v in load_json(p, {}).items():
            out.setdefault(k, {'name': v.get('name'), 'cuisine': v.get('cuisine')})
            if b in v: out[k][b] = v[b]
    return out

def st_ok(st, b): return bool(st.get(b, {}).get('checked'))

RESTAURANT_CATS = {'Kebap', 'Pide/Lahmacun/Gözleme', 'Snack'}
RESTAURANT_WORDS = ('döner', 'doner', 'dürüm', 'durum', 'dürüm', 'lahmacun', 'kebab', 'kebap', 'iskender', 'adana', 'urfa', 'şiş', 'sis kebab', 'pide', 'pizza', 'burger',
                    'fish and chips', 'kumpir', 'midye', 'kokoreç', 'kokorec', 'lángos', 'langos', 'currywurst', 'pommes', 'smørrebrød', 'smorrebrod', 'tost', 'simit', 'çiğ köfte')
def prepared_of(d):
    """Heuristik für "prepared": restaurant (Imbiss/Restaurant-typisch) sonst homemade. Ein vorhandenes Feld hat Vorrang."""
    if d.get('prepared') in ('homemade', 'restaurant'): return d['prepared']
    n = (d.get('name') or '').lower()
    if d.get('category') in RESTAURANT_CATS or any(w in n for w in RESTAURANT_WORDS): return 'restaurant'
    return 'homemade'

def off_similar(st, backends, n=3):
    codes, seen = [], set()
    ms = [m for b in backends for m in st.get(b, {}).get('matches', [])]
    ms.sort(key=lambda m: 0 if m['kind'] == 'exact' else 1)
    for m in ms:
        if m['code'] and re.fullmatch(r'\d{6,14}', m['code']) and m['code'] not in seen: seen.add(m['code']); codes.append(m['code'])
    return codes[:n]

def packaged_item_in_off(d, a):
    """Nur für type "item" mit Barcode: liegt der Barcode im OFF-Dump?"""
    try:
        import duckdb
        con = duckdb.connect(a.dumpdb, read_only=True)
        r = con.execute('select count(*) from names where code = ?', (d['barcode'],)).fetchone()[0]; con.close(); return r > 0
    except Exception as e:
        print('Warnung: Barcode-Abgleich nicht möglich (' + str(e)[:80] + ')'); return False

def cmd_apply(a, log):
    dishes = json.load(open(a.input, encoding='utf8')); status = load_status(a)
    backends = a.backends.split(',')
    keep, removed, n_hit, n_unchecked = [], [], 0, 0
    for d in dishes:
        st = status.get(d['id'], {})
        if d.get('type') == 'item' and d.get('barcode'):
            if packaged_item_in_off(d, a):
                removed.append({'id': d['id'], 'name': d['name'], 'barcode': d['barcode'], 'reason': 'Fertig-/Supermarktprodukt (Barcode liegt in OFF vor)'}); continue
            keep.append(d); continue
        e = {}
        for k, v in d.items():
            if k in ('prepared', 'is_packaged_product', 'off_similar'): continue
            e[k] = v
            if k == 'category':
                e['prepared'] = prepared_of(d); e['is_packaged_product'] = False
        e.setdefault('prepared', prepared_of(d)); e.setdefault('is_packaged_product', False)
        if in_off(st, backends):
            sim = off_similar(st, backends); n_hit += 1
            e['off_similar'] = sim
        if not all(st_ok(st, b) for b in backends): n_unchecked += 1
        keep.append(e)
    json.dump(keep, open(a.out, 'w', encoding='utf8'), ensure_ascii=False, indent=2)
    json.dump(removed, open(a.removed, 'w', encoding='utf8'), ensure_ascii=False, indent=2)
    log(f'apply: {len(dishes)} -> behalten {len(keep)}, entfernt (nur Fertigprodukte) {len(removed)}, Gerichte mit OFF-Hinweis (off_similar) {n_hit}, nicht in allen Backends geprüft {n_unchecked}')

def in_off(st, backends):
    return any(st.get(b, {}).get('found') for b in backends)

def cmd_status(a, log):
    dishes = json.load(open(a.input, encoding='utf8')); status = load_status(a)
    for b in ('api', 'dump'):
        ch = sum(1 for d in dishes if st_ok(status.get(d['id'], {}), b)); f = sum(1 for d in dishes if status.get(d['id'], {}).get(b, {}).get('found'))
        log(f'{b}: geprüft {ch}/{len(dishes)}, mit OFF-Treffer {f}')

def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument('cmd', choices=['check', 'dump-index', 'apply', 'status', 'match'])
    p.add_argument('--input', default=os.path.join(ROOT, 'foods.json'))
    p.add_argument('--out', default=os.path.join(ROOT, 'foods.json'))
    p.add_argument('--removed', default=os.path.join(ROOT, 'removed_in_off.json'))
    p.add_argument('--append-removed', action='store_true')
    p.add_argument('--status', default=None, help='Default: off_check_status.json (api) bzw. off_check_status_dump.json (dump)')
    p.add_argument('--cache', default=os.path.join(ROOT, 'off_check_cache.sqlite'))
    p.add_argument('--dumpdb', default=os.path.join(ROOT, 'off_dump', 'off_names.duckdb'))
    p.add_argument('--csv', default=os.path.join(ROOT, 'off_dump', 'en.openfoodfacts.org.products.csv.gz'))
    p.add_argument('--backend', default='api', choices=['api', 'dump'])
    p.add_argument('--backends', default='api,dump', help='für apply: welche Backends zählen (Vereinigung)')
    p.add_argument('--only-ids'); p.add_argument('--only-cuisine'); p.add_argument('--limit', type=int)
    p.add_argument('--max-terms', type=int, default=4); p.add_argument('--page-size', type=int, default=25)
    p.add_argument('--min-interval', type=float, default=1.0, help='Sekunden zwischen API-Anfragen')
    p.add_argument('--recheck', action='store_true'); p.add_argument('--log', default=os.path.join(ROOT, 'tools', 'off_check.log'))
    p.add_argument('--terms', nargs='*'); a = p.parse_args()
    lf = open(a.log, 'a', encoding='utf8')
    def log(s):
        line = f'{datetime.datetime.now():%Y-%m-%d %H:%M:%S} {s}'; print(line, flush=True); lf.write(line + '\n'); lf.flush()
    if a.cmd == 'match':   # Schnelltest: off_check.py match "Wiener Schnitzel" "Wiener Schnitzel Knorr"
        print(match_kind(a.terms[0], a.terms[1])); return
    if a.cmd == 'dump-index': return dump_index(a, log)
    if a.cmd == 'apply': return cmd_apply(a, log)
    if a.cmd == 'status': return cmd_status(a, log)
    dishes = json.load(open(a.input, encoding='utf8'))
    if a.only_ids: s = set(a.only_ids.split(',')); dishes = [d for d in dishes if d['id'] in s]
    if a.only_cuisine: s = set(a.only_cuisine.split(',')); dishes = [d for d in dishes if d.get('cuisine') in s]
    if a.limit: dishes = dishes[:a.limit]
    if not a.status: a.status = STATUS_FILES[a.backend]
    status = load_json(a.status, {})
    log(f'check backend={a.backend} Gerichte={len(dishes)}')
    (check_api if a.backend == 'api' else check_dump)(dishes, a, status, log)

if __name__ == '__main__': main()
