# food-database

Eigene Lebensmittel-Datenbank für einen Kalorientracker: **4245 Gerichte** aus **49 Küchen** — 926 türkisch (`tr`), 668 deutsch (`de`) und 2651 weitere aus Europa und dem Kaukasus — plus **631 Grundzutaten** (Basis-Lebensmittel roh und in üblichen Zubereitungen wie gekocht, gegrillt, getrocknet, tiefgekühlt oder aus der Dose, mit USDA-Referenzwerten; 27 Zubereitungen ohne USDA-Datensatz daraus geschätzt), mit Kalorien, Protein, Kohlenhydraten, Fett und Ballaststoffen (bei Grundzutaten meist auch Zucker), dazu eine kostenlose Such-API für das Suchfeld der App.

> **Die Werte der Gerichte sind berechnete Schätzungen, keine Labor- oder Herstellerangaben.**
> Jedes Gericht hat `"quality": "estimate"` und `"source": "calculated from typical recipe and approximate reference values"`. Die Nährwerte entstehen aus einem typischen Hausrezept und einer Zutaten-Referenztabelle (ungefähre Werte in der Größenordnung von USDA/BLS), nicht aus einer Analyse des fertigen Gerichts. Abweichungen von etwa ±10–25 % gegenüber einem konkreten Rezept sind normal (Fettmenge, Garzeit, Portionsgröße). Bitte die Zahlen nicht als medizinische oder kennzeichnungsrechtliche Nährwertangabe verwenden. Geprüfte Werte können später **denselben Eintrag überschreiben** (siehe unten).

Die Rohdaten (Stand `main`):

```
https://raw.githubusercontent.com/HealthUp1123/food-database/main/data/foods.json
```

**Datenstand (29.10.2026, Welle 3 + Grundzutaten + Zubereitungsvarianten + geschätzte Zubereitungen):** 4876 Einträge. Davon sind 4245 Gerichte (`type: "dish"`, `quality: "estimate"`) aus 49 Küchen – tr 926, de 668, übrige Europa/Kaukasus 2651; davon 2114 mit `off_similar`-Hinweis, 0 Fertigprodukte entfernt. Dazu kommen 631 Grundzutaten (`type: "item"`, `prepared: "base_ingredient"`, Quelle USDA FoodData Central SR Legacy; 604 `quality: "reference"`, 27 `quality: "estimate"`): Gemüse 227, Obst 91, Getreide/Teigwaren/Brot 57, Fisch & Meeresfrüchte 50, Milchprodukte & Eier 47, Fleisch 40, Nüsse & Samen 36, Hülsenfrüchte 34, Geflügel 32, Fette & Öle 11, Zucker & Salz 6. Davon sind 309 Zubereitungs- und Haltbarkeitsvarianten mit eigenem USDA-Datensatz (z. B. `tomate-getrocknet`, `tomatenmark`, `haehnchenbrust-gegrillt`, `erbsen-gruen-tiefgekuehlt`, `mandeln-geroestet`) und 27 geschätzte Gemüse-Zubereitungen ohne USDA-Datensatz (z. B. `tomate-gegrillt`, `zucchini-in-oel-gebraten`, `brokkoli-gedaempft`, aus der rohen Grundzutat mit Ausbeute-, Retentions- und Fettaufnahmefaktoren aus CoFID 2021, Bognár 2002 und Bergström 1994 berechnet); nach Zustand: cooked 118, processed 75, dry 46, dried 42, canned 41, grilled 31, frozen 27, fried 24, baked 21, roasted 16, smoked 4, raw 186.

**Grundzutaten** sind rohe oder kaum verarbeitete Basis-Lebensmittel (z. B. `tomate-roh`, `haferflocken`, `haehnchenbrust-roh`) und ihre üblichen Zubereitungen (z. B. `tomate-getrocknet`, `haehnchenbrust-gegrillt`), keine Fertig- oder Markenprodukte. Sie tragen `note: "Grundzutat, kein Fertigprodukt"` (Varianten z. B. `"Grundzutat (zubereitet), kein Fertigprodukt"`), `category: "Grundzutat: …"`, `cuisine: "int"`, `unit: "g"`, den Zustand in `state` und den USDA-Datensatz in `fdc_id` und `source`. Die Werte sind 1:1 aus USDA übernommen und nur gerundet; Ausnahme sind die geschätzten Zubereitungen (`quality: "estimate"`, `note: "Grundzutat (zubereitet, geschätzt), kein Fertigprodukt"`, `derived_from` = ID der rohen Grundzutat, Faktoren und Quellen in `source`). Details: [`tools/base_ingredients/README.md`](tools/base_ingredients/README.md).

**Gerichte und Fertigprodukte sind getrennt.** Ein Gericht (zuhause oder Restaurant, aus einem Rezept berechnet) bleibt in der Datenbank, auch wenn Open Food Facts ein gleichnamiges Fertigprodukt führt. Es bekommt `prepared` (`homemade` oder `restaurant`), `is_packaged_product: false` und bei einem Namenstreffer `off_similar` (höchstens drei Barcodes, nur als Hinweis). Marken- und Supermarktprodukte werden nicht aufgenommen. Nichts wurde entfernt: `removed_in_off.json` ist leer. **2114** der 4245 Gerichte tragen `off_similar`. Der Abgleich lief gegen einen Open-Food-Facts-Dump vom **29.10.2026**.

Aufbau der Schätzung, Garfaktor, Küchen und der OFF-Abgleich stehen in [`tools/dishes/BUILD_NOTES.md`](tools/dishes/BUILD_NOTES.md).

## Inhalt

```
data/foods.json                 Die Datenbank (JSON-Array, 4245 Gerichte aus 49 Küchen + 631 Grundzutaten)
src/search.mjs                  Gemeinsames Such-Modul (API + lokale CLI)
api/worker.js                   Cloudflare Worker (Such-API)
api/wrangler.toml               Worker-Konfiguration
scripts/validate.mjs            Datenprüfung (ohne Abhängigkeiten)
scripts/search-local.mjs        Lokale Suche per Kommandozeile
scripts/test-worker.mjs         Schnelltest des API-Handlers
tools/dishes/                   Generator, Batches (eu3_*.py), wave3/, Rezepte, Kandidaten
tools/base_ingredients/         Grundzutaten-, Varianten- und Schätzliste und Generator (USDA SR Legacy)
tools/dishes/tools/off_check.py Abgleich mit Open Food Facts (Dump nicht im Repo)
.github/workflows/validate.yml  Prüfung bei jedem Push und Pull Request
```

## Datenformat

`data/foods.json` ist ein Array. Ein Eintrag:

```json
{
  "id": "karniyarik",
  "name": "Karnıyarık",
  "type": "dish",
  "barcode": null,
  "synonyms": ["Karniyarik", "Gespaltener Bauch", "Gefüllte Aubergine mit Hack"],
  "cuisine": "tr",
  "category": "Gemüse mit Fleisch",
  "prepared": "homemade",
  "is_packaged_product": false,
  "per100g": { "kcal": 104, "protein": 3.9, "carbs": 5.0, "fat": 7.8, "fiber": 2.2 },
  "portion": { "label": "1 Portion (2 Hälften)", "grams": 445 },
  "ingredients": [
    { "name": "Aubergine", "grams": 250 },
    { "name": "Rinderhackfleisch", "grams": 80 }
  ],
  "quality": "estimate",
  "source": "calculated from typical recipe and approximate reference values"
}
```

| Feld | Pflicht | Beschreibung |
| --- | --- | --- |
| `id` | ja | Eindeutig, klein, mit Bindestrichen (`karniyarik`). Nicht mehr ändern, wenn die App sie speichert. |
| `name` | ja | Anzeigename, deutsch oder in der Originalschreibung (z. B. `Karnıyarık`). |
| `type` | ja | `"dish"` (Gericht) oder `"item"` (Artikel/Zutat/Produkt). Gerichte sind `dish`, Grundzutaten sind `item`. |
| `barcode` | ja | EAN-8/EAN-13 als **String** (führende Nullen) oder `null`. `null` ist gültig und bei allen jetzigen Gerichten gesetzt (kein Verpackungs-Barcode). Ist ein String gesetzt, muss die Prüfziffer stimmen und der Code eindeutig sein. |
| `synonyms` | ja | Alternative Namen und Schreibweisen (darf leer sein: `[]`). |
| `cuisine` | ja | Ländercode aus der festen Liste, u. a. `tr`, `de`, `it`, `fr`, `es`, `gr`, `pl` und seit Welle 3 auch `ge`, `am`, `az`, `md`, `by`, `me`, `xk`, `ad`, `li`, `mc`, `sm`. `int` steht für länderübergreifende Grundzutaten. |
| `category` | ja | Deutsche Kategorie, z. B. `Suppe`, `Kebap`, `Hauptgericht Fleisch`, `Kuchen`, `Getränk`. |
| `prepared` | nein | Bei Gerichten `"homemade"` (zuhause) oder `"restaurant"` (Restaurant/Imbiss). Bei Grundzutaten `"base_ingredient"`; dann sind `type: "item"`, `is_packaged_product: false` und `barcode: null` Pflicht. |
| `state` | nein | Zustand der Grundzutat: `raw` (roh), `cooked` (gekocht, gedünstet, geschmort), `grilled` (gegrillt), `fried` (in der Pfanne gebraten), `baked` (im Ofen gebacken/gebraten), `roasted` (geröstet, z. B. Nüsse), `dry` (trocken, z. B. Reis, Nudeln, Hülsenfrüchte), `dried` (getrocknet, z. B. Rosinen, getrocknete Tomaten), `frozen` (tiefgekühlt, unzubereitet), `canned` (Dose/Glas), `smoked` (geräuchert), `processed` (einfach verarbeitet, z. B. Mehl, Öl, Milch, Saft, Tomatenmark). |
| `unit` | nein | Bezugseinheit, immer `"g"` (Nährwerte pro 100 g). |
| `note` | nein | Bei Grundzutaten `"Grundzutat, kein Fertigprodukt"`; bei Varianten je nach Zustand z. B. `"Grundzutat (zubereitet), kein Fertigprodukt"`, `"Grundzutat (getrocknet), kein Fertigprodukt"`, `"Grundzutat (tiefgekühlt, unzubereitet), kein Fertigprodukt"`, `"Grundzutat (Konserve, generisch), kein Markenprodukt"` oder `"Grundzutat (verarbeitet, generisch), kein Markenprodukt"`; bei geschätzten Zubereitungen `"Grundzutat (zubereitet, geschätzt), kein Fertigprodukt"`. |
| `fdc_id` | nein | USDA-FoodData-Central-ID des Quelldatensatzes (positive Ganzzahl). |
| `derived_from` | nein | Nur bei geschätzten Grundzutat-Zubereitungen: ID der rohen Grundzutat, aus der die Werte berechnet wurden (z. B. `tomate-roh`). |
| `source_missing` | nein | Nährwerte, die in der Quelle fehlen (`"fiber"`, `"sugar"`). |
| `is_packaged_product` | nein | `false` bei Gerichten. `true` wäre nur für `type: "item"` mit Barcode sinnvoll; bei `type: "dish"` ist `true` ungültig. |
| `off_similar` | nein | Bis zu 3 Open-Food-Facts-Barcodes (6–14 Ziffern) ähnlich benannter Fertigprodukte. Nur ein Hinweis; das Gericht bleibt ein eigener Eintrag. |
| `per100g` | ja | `kcal` (0–950), `protein`, `carbs`, `fat`, `fiber` (je 0–100 g pro 100 g), optional `sugar` (0–100 g). Protein + Kohlenhydrate + Fett ≤ 100 g (0,15 g Rundungstoleranz). |
| `portion` | nein | Typische Portion: `label` (Text) und `grams` (> 0, max. 5000). Die App rechnet damit von 100 g auf die Portion um. |
| `ingredients` | ja | Zutaten der zugrunde gelegten Portion: `{ "name", "grams" }`, `grams` > 0. Das sind Rezeptmengen, keine zweite Nährwertquelle. |
| `quality` | ja | `"estimate"` (berechnet, wie jetzt bei allen 4245 Gerichten), `"reference"` (aus einer amtlichen Nährwertdatenbank übernommen, wie bei 604 der 631 Grundzutaten) oder `"verified"` (später mit geprüften Werten überschrieben). Die 27 geschätzten Grundzutat-Zubereitungen sind `"estimate"`. |
| `source` | ja | Herkunft der Nährwerte. Bei Schätzwerten der feste Hinweis auf Rezept plus Referenzwerte; bei geprüften Einträgen die konkrete Quelle. |

Gerichte sind pro 100 g angegeben. `portion.grams` ist das übliche Tellergewicht nach dem Garen. `ingredients[].grams` sind die Rohmengen dieser Portion (aufgenommenes Wasser und Bratfett stehen mit in der Liste).

Kategorien sind Küchengruppen, keine Ernährungslabels. Dieselbe Speise kann regional anders heißen; hier steht jeweils ein verbreitetes Standardrezept.

`off_similar` steht nur, wenn der Dump ein gleichnamiges Fertigprodukt kannte (Beispiel: `wiener-schnitzel`). Fehlt das Feld, gab es keinen solchen Treffer. Die Barcodes gehören zum Fertigprodukt, nicht zum Gericht.

## Geprüfte Werte nachtragen

Die `id` bleibt. So finden gespeicherte Mahlzeiten in der App denselben Eintrag, auch wenn die Zahlen später genauer werden.

1. Den Eintrag in `data/foods.json` über die `id` suchen (nicht neu anlegen und die alte `id` nicht umbenennen).
2. `per100g` durch geprüfte Zahlen ersetzen. Quelle kann die Verpackung, der Hersteller, eine amtliche Nährwertdatenbank (z. B. BLS) oder eine Laboranalyse sein. `portion` und `ingredients` nur anpassen, wenn die geprüfte Menge von der Schätzung abweicht. Die Zutatenliste muss ein nicht-leeres Array bleiben.
3. `"quality": "verified"` setzen.
4. `"source"` auf die konkrete Herkunft ändern, inklusive Stand, z. B. `"BLS, Code …, Stand 2026-11-01"` oder `"Herstellerangabe, Produkt …"`.
5. Liegt eine echte EAN vor, `barcode` als String eintragen (gültige Prüfziffer). Ohne Verpackungscode `null` lassen.
6. `node scripts/validate.mjs` ausführen, dann committen und pushen.

Solange `quality` auf `"estimate"` steht, gelten die berechneten Rezeptwerte. Die App kann Einträge mit `"verified"` gegenüber Schätzungen bevorzugen.

## Validierung

```bash
node scripts/validate.mjs
```

Prüft Pflichtfelder (einschließlich `cuisine`, `category`, `ingredients`, `quality`, `source`), die optionalen Felder `prepared`, `is_packaged_product`, `off_similar`, `state`, `unit`, `note`, `fdc_id`, `source_missing` und `per100g.sugar`, die Regeln für Grundzutaten (`type: "item"`, kein Barcode, kein Fertigprodukt), Wertebereiche (kcal 0–950, Makros 0–100 g, Protein + Kohlenhydrate + Fett ≤ 100 g + 0,15 g Rundung), eindeutige `id`s, eindeutige Barcodes und die EAN-Prüfziffer. **`barcode: null` ist erlaubt** und erzeugt keinen Fehler. Ein Gericht mit `is_packaged_product: true` ist ein Fehler.

Weicht `kcal` stark von `4·Protein + 4·Kohlenhydrate + 9·Fett` ab, gibt es eine **Warnung**, keinen Fehler. 29 Gerichte (Wein und Spirituosen) liegen darüber, weil Ethanol etwa 7 kcal/g liefert und in den Makros nicht vorkommt. Diese 29 Warnungen sind erwartet.

Bei echten Fehlern ist der Exit-Code `1`. Es braucht nur Node ≥ 20, keine Installation. Die GitHub Action `.github/workflows/validate.yml` läuft bei jedem Push und Pull Request.

## Lokale Suche (zum Testen)

```bash
node scripts/search-local.mjs karniyarik
node scripts/search-local.mjs "Karnıyarık"   # ı = i
node scripts/search-local.mjs karniyark       # ein Zeichen daneben
node scripts/search-local.mjs koelsch         # oe = ö
node scripts/search-local.mjs "Karnıyarık" --limit 3 --json
node scripts/test-worker.mjs                  # testet den API-Handler
```

### So funktioniert die Suche

- Groß-/Kleinschreibung, Umlaute und türkische Buchstaben sind egal: `Karnıyarık`, `karniyarik` und `Karniyarik` finden dasselbe (`ı`/`İ` → `i`, `ş` → `s`, `ğ` → `g`, `ç` → `c`, `ä`/`ae` → `a`, `ö`/`oe` → `o`, `ü`/`ue` → `u`, `ß` → `ss`).
- Reihenfolge der Treffer: exakt → Wortanfang (Präfix) → Teilstring → Tippfehler (Levenshtein-Distanz 1 bei 3–5 Zeichen, 2 ab 6 Zeichen; unter 3 Zeichen keine Fehlertoleranz). `karniyark` trifft deshalb `Karnıyarık`.
- Gesucht wird in `name` und `synonyms`. Treffer im Namen stehen vor Treffern über Synonyme.
- Mehrere Wörter: Alle Wörter müssen passen.

## API

Die API ist ein Cloudflare Worker (kostenloser Plan reicht), liefert JSON und erlaubt CORS (`Access-Control-Allow-Origin: *`). `BASE` ist die URL nach dem Deploy.

```bash
BASE="https://food-database-api.<dein-account>.workers.dev"
```

| Endpunkt | Beschreibung |
| --- | --- |
| `GET /search?q=<text>&limit=<n>` | Suche in Name und Synonymen. `limit` 1–50, Standard 10. Treffer **ohne** `ingredients` (die Liste wäre in jeder Suche Ballast). Nährwerte, Portion, Küche und Kategorie sind dabei. |
| `GET /item/{id}` | Voller Eintrag inklusive `ingredients`. 404, wenn die `id` fehlt. |
| `GET /barcode/{ean}` | Voller Eintrag zu einer EAN-8/EAN-13. 400 bei ungültiger Prüfziffer, 404 wenn unbekannt. Aktuell hat kein Gericht einen Barcode (`null`), der Endpunkt ist für spätere geprüfte Produkte da. |
| `GET /health` | Status und Anzahl der Einträge. |

```bash
curl "$BASE/health"
# {"status":"ok","count":4876}

curl "$BASE/search?q=karniyarik&limit=5"
# {"query":"karniyarik","count":1,"results":[{"id":"karniyarik","name":"Karnıyarık","barcode":null, ...}]}

curl "$BASE/search?q=Karn%C4%B1yar%C4%B1k"
curl "$BASE/search?q=karniyark"

curl "$BASE/item/karniyarik"
# voller Eintrag, inkl. ingredients

curl "$BASE/barcode/4006381333931"
# 404 – gültige EAN, aber keinem Eintrag zugeordnet
```

## Deployment (Cloudflare Workers)

1. Kostenloses Konto auf [cloudflare.com](https://dash.cloudflare.com/sign-up) anlegen.
2. Repo klonen und Node ≥ 20 installieren.
3. Optional lokal ausprobieren: `cd api && npx wrangler dev` (läuft dann auf `http://localhost:8787`).
4. Einloggen: `cd api && npx wrangler login`
5. Deployen: `cd api && npx wrangler deploy`
6. Wrangler zeigt die URL an (`https://food-database-api.<account>.workers.dev`). Mit `curl .../health` prüfen.
7. Nach jeder Datenänderung erneut `npx wrangler deploy` ausführen – die Daten werden beim Deploy in den Worker eingebunden.

Hinweis: Der kostenlose Plan hat ein Tageslimit an Anfragen. Cache Treffer deshalb in der App. Die API sendet bereits `Cache-Control: public, max-age=300`.

### Optional: statisches Fallback über GitHub

Wenn du keine API betreiben willst, lädst du die Rohdatei einmal und suchst lokal mit `src/search.mjs`:

```
https://raw.githubusercontent.com/HealthUp1123/food-database/main/data/foods.json
```

Das ist bei diesem Datenumfang (4876 Einträge) praktikabel. Für die Zutatenliste brauchst du keinen zweiten Endpunkt, die Datei enthält sie bereits. In der Such-API fehlt `ingredients` in der Trefferliste absichtlich; `GET /item/{id}` liefert sie nach.

## Einbau in die App: Suchfeld mit Live-Suche (Debounce)

```ts
const API = "https://food-database-api.<dein-account>.workers.dev";

type Nutrients = { kcal: number; protein: number; carbs: number; fat: number; fiber: number; sugar?: number };
type Food = {
  id: string;
  name: string;
  type: "item" | "dish";
  barcode: string | null;
  synonyms: string[];
  cuisine: string;
  category: string;
  prepared?: "homemade" | "restaurant" | "base_ingredient";
  state?: "raw" | "cooked" | "grilled" | "fried" | "baked" | "roasted" | "dry" | "dried" | "frozen" | "canned" | "smoked" | "processed"; // nur Grundzutaten
  unit?: "g";
  note?: string; // "Grundzutat, kein Fertigprodukt" bzw. "Grundzutat (zubereitet), kein Fertigprodukt" usw.
  fdc_id?: number; // USDA FoodData Central
  source_missing?: ("fiber" | "sugar")[];
  is_packaged_product?: boolean;
  off_similar?: string[];
  per100g: Nutrients;
  portion?: { label: string; grams: number };
  ingredients?: { name: string; grams: number }[]; // nur /item und /barcode
  quality: "estimate" | "reference" | "verified";
  source: string;
};

let timer: ReturnType<typeof setTimeout> | undefined;
let controller: AbortController | undefined;

export function onSearchInput(text: string, render: (foods: Food[]) => void) {
  clearTimeout(timer);
  controller?.abort();
  const q = text.trim();
  if (q.length < 2) return render([]);
  timer = setTimeout(async () => {
    controller = new AbortController();
    try {
      const res = await fetch(`${API}/search?q=${encodeURIComponent(q)}&limit=10`, { signal: controller.signal });
      if (!res.ok) throw new Error(`HTTP ${res.status}`);
      const data = await res.json();
      render(data.results as Food[]);
    } catch (e) {
      if ((e as Error).name !== "AbortError") console.error("Suche fehlgeschlagen", e);
    }
  }, 250);
}

export async function lookupItem(id: string): Promise<Food | null> {
  const res = await fetch(`${API}/item/${encodeURIComponent(id)}`);
  return res.ok ? ((await res.json()) as Food) : null;
}

export async function lookupBarcode(ean: string): Promise<Food | null> {
  const res = await fetch(`${API}/barcode/${ean}`);
  return res.ok ? ((await res.json()) as Food) : null;
}

export const nutrientsFor = (f: Food, grams: number) =>
  Object.fromEntries(Object.entries(f.per100g).map(([k, v]) => [k, +(v * grams / 100).toFixed(1)]));
```

`onSearchInput(inputEl.value, renderList)` im `input`-Event des Suchfelds aufrufen. Die Trefferliste hat Nährwerte pro 100 g, aber keine Zutaten; die holst du bei Bedarf mit `lookupItem(id)`. Werte mit `quality: "estimate"` in der Oberfläche als Schätzung kennzeichnen.

## Daten neu erzeugen

Rezepttexte und die Zutaten-Referenz liegen unter `tools/dishes/` (`build.py`, `batches/*.py` inklusive `eu3_*.py`, `wave3/`, `recipes/`, `candidates/`, `ingredients_src.txt`, `ingredients_add_*.txt`, `ingredients.json`). Die Batches erzeugen `tools/dishes/tools/compose_eu.py`, `compose_eu2.py` und `compose_eu3.py`. Im Verzeichnis `tools/dishes`:

```bash
python3 build.py
```

Das schreibt dort `foods.json`, eine aktualisierte `ingredients.json` und `build_report.txt`. Danach den OFF-Abgleich (`tools/off_check.py`, siehe BUILD_NOTES) und die neue `foods.json` nach `data/foods.json` kopieren. `node scripts/validate.mjs` laufen lassen. Nicht committen: `build_report.txt`, `__pycache__/`, `*.log`, `off_dump/`, `off_check_cache.sqlite`, `off_check_status*.json`, `*.duckdb`.

## Roadmap

- [x] Datenformat festlegen
- [x] Validierung (Skript + GitHub Action)
- [x] Such-API (Cloudflare Worker) mit Umlaut- und Tippfehler-toleranter Suche
- [x] Platzhalter durch 4245 berechnete Gerichte ersetzen (49 Küchen, davon 926 türkisch und 668 deutsch, `quality: "estimate"`)
- [x] Gerichte und Fertigprodukte trennen; 2114 Gerichte mit `off_similar` aus dem OFF-Dump vom 29.10.2026 markiert, keines entfernt
- [x] 295 Grundzutaten mit USDA-Referenzwerten (`quality: "reference"`, inkl. Zucker)
- [x] 309 Zubereitungsvarianten der Grundzutaten (gekocht, gegrillt, gebraten, getrocknet, tiefgekühlt, Dose, Saft, geröstet, geräuchert), ebenfalls 1:1 aus USDA
- [ ] Einzelne Einträge mit geprüften Werten überschreiben (`quality: "verified"`, Quelle im Feld `source`)
- [ ] Echte Barcodes ergänzen, wo ein verpacktes Produkt dahintersteht
- [ ] API deployen und in die App einbinden
- [ ] Automatisches Deployment per GitHub Action (`wrangler deploy` bei Änderungen an `data/`)
- [ ] Optional: weitere Nährwerte (Zucker, Salz, gesättigte Fette, Alkohol gramm), mehrere Portionen
- [ ] Optional: Datenbank aufteilen, wenn sie deutlich über diesen Umfang wächst

## Hinweis

Die Rezepte stammen aus allgemeinem Küchenwissen, die Referenzwerte sind Näherungen. Die Werte der Grundzutaten stammen aus USDA FoodData Central (SR Legacy, Public Domain/CC0). Übernimm keine fremden Nährwerttabellen, ohne deren Lizenz zu prüfen. Wer einen Eintrag überschreibt, trägt die geprüfte Quelle in `source` ein.
