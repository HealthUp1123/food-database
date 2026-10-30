# food-database

Eigene Lebensmittel-Datenbank für einen Kalorientracker: **4346 Gerichte** aus **57 Küchen** — 929 türkisch (`tr`), 668 deutsch (`de`), 2651 weitere aus Europa und dem Kaukasus, 86 aus Asien (`cn`, `jp`, `in`, `th`, `vn`, `kr`, `id`) und 9 internationale Imbissgerichte (`int`) — plus **838 Grundzutaten** und **73 Getränke** (Basis-Lebensmittel roh und in üblichen Zubereitungen wie gekocht, gegrillt, getrocknet, tiefgekühlt oder aus der Dose, mit Referenzwerten aus USDA sowie direkten Datensätzen aus dem Bundeslebensmittelschlüssel BLS 4.0, Ciqual, der Schweizer und der schwedischen Nährwertdatenbank; nur 21 Zubereitungen ohne direkten Datensatz geschätzt), mit Kalorien, Protein, Kohlenhydraten, Fett und Ballaststoffen (bei Grundzutaten meist auch Zucker), dazu eine kostenlose Such-API für das Suchfeld der App.

> **Die Werte der Gerichte sind berechnete Schätzungen, keine Labor- oder Herstellerangaben.**
> Jedes Gericht hat `"quality": "estimate"` und `"source": "calculated from typical recipe and approximate reference values"`. Die Nährwerte entstehen aus einem typischen Hausrezept und einer Zutaten-Referenztabelle (ungefähre Werte in der Größenordnung von USDA/BLS), nicht aus einer Analyse des fertigen Gerichts. Abweichungen von etwa ±10–25 % gegenüber einem konkreten Rezept sind normal (Fettmenge, Garzeit, Portionsgröße). Bitte die Zahlen nicht als medizinische oder kennzeichnungsrechtliche Nährwertangabe verwenden. Geprüfte Werte können später **denselben Eintrag überschreiben** (siehe unten).

Die Rohdaten (Stand `main`):

```
https://raw.githubusercontent.com/HealthUp1123/food-database/main/data/foods.json
```

**Erweiterung Welle 4 (30.10.2026):** +331 Einträge auf jetzt **5257**. Details siehe [Erweiterung Welle 4](#erweiterung-welle-4-30102026). Der folgende Absatz beschreibt den Stand davor.

**Datenstand (29.10.2026, Welle 3 + Grundzutaten + Zubereitungsvarianten + BLS/Ciqual/CH/SE-Zubereitungen + geschätzte Zubereitungen):** 4926 Einträge. Davon sind 4245 Gerichte (`type: "dish"`, `quality: "estimate"`) aus 49 Küchen – tr 926, de 668, übrige Europa/Kaukasus 2651; davon 2114 mit `off_similar`-Hinweis, 0 Fertigprodukte entfernt. Dazu kommen 681 Grundzutaten (`type: "item"`, `prepared: "base_ingredient"`; 604 aus USDA FoodData Central SR Legacy, 56 direkt aus BLS 4.0 (47), Schweizer Nährwertdatenbank (5), Ciqual 2025 (2) und Livsmedelsverket (2); 660 `quality: "reference"`, 21 `quality: "estimate"`): Gemüse 277, Obst 91, Getreide/Teigwaren/Brot 57, Fisch & Meeresfrüchte 50, Milchprodukte & Eier 47, Fleisch 40, Nüsse & Samen 36, Hülsenfrüchte 34, Geflügel 32, Fette & Öle 11, Zucker & Salz 6. Davon sind 309 Zubereitungs- und Haltbarkeitsvarianten mit eigenem USDA-Datensatz (z. B. `tomate-getrocknet`, `tomatenmark`, `haehnchenbrust-gegrillt`, `erbsen-gruen-tiefgekuehlt`, `mandeln-geroestet`) sowie 56 Gemüse-Zubereitungen mit direktem Datensatz aus einer nationalen Nährwertdatenbank (`source_id`, z. B. `zucchini-gegrillt` = BLS 4.0 G582172, `kuerbis-im-ofen-gebacken`, `paprika-gelb-gebraten-ohne-fett`, `rote-bete-gedaempft` = CH 1019, `suesskartoffel-wedges-im-ofen-mit-oel` = Livsmedelsverket 3771, `spargel-weiss-roh` = Ciqual 20282) und 21 geschätzte Gemüse-Zubereitungen ohne direkten Datensatz (z. B. `zucchini-in-oel-gebraten`, `brokkoli-gedaempft`, aus der rohen Grundzutat mit Ausbeute-, Retentions- und Fettaufnahmefaktoren aus CoFID 2021 und Bognár 2002 berechnet); nach Zustand: cooked 129, processed 75, dry 46, dried 42, canned 41, fried 40, baked 39, grilled 35, frozen 27, roasted 16, smoked 4, raw 187.

**Grundzutaten** sind rohe oder kaum verarbeitete Basis-Lebensmittel (z. B. `tomate-roh`, `haferflocken`, `haehnchenbrust-roh`) und ihre üblichen Zubereitungen (z. B. `tomate-getrocknet`, `haehnchenbrust-gegrillt`), keine Fertig- oder Markenprodukte. Sie tragen `note: "Grundzutat, kein Fertigprodukt"` (Varianten z. B. `"Grundzutat (zubereitet), kein Fertigprodukt"`), `category: "Grundzutat: …"`, `cuisine: "int"`, `unit: "g"`, den Zustand in `state` und den Quelldatensatz in `fdc_id` (USDA) bzw. `source_id` (andere Datenbanken, z. B. `BLS 4.0:G582172`) und `source`. Die Werte sind 1:1 aus der Quelle übernommen und nur gerundet (bei BLS, Ciqual, CH und SE: Kohlenhydrate = verfügbare KH + Ballaststoffe, damit sie wie bei USDA Gesamt-KH sind); Ausnahme sind die geschätzten Zubereitungen (`quality: "estimate"`, `note: "Grundzutat (zubereitet, geschätzt), kein Fertigprodukt"`, `derived_from` = ID der rohen Grundzutat, Faktoren und Quellen in `source`). Details: [`tools/base_ingredients/README.md`](tools/base_ingredients/README.md).

### Erweiterung Welle 4 (30.10.2026)

331 neue Einträge, fast alle direkt aus einem amtlichen Quelldatensatz übernommen (`quality: "reference"`). Nur 5 sind transparent geschätzt (`quality: "estimate"`, mit `derived_from`, `method` und Rechenweg in `source`). Erzeugt mit [`tools/extension/build_extension.py`](tools/extension/README.md).

| Bereich | reference | estimate | Beispiele |
| --- | --- | --- | --- |
| Fehlende Zubereitungen (Gemüse, Pilze, Kartoffeln, im Ofen / in der Pfanne ohne Fett) | 67 | – | `rotkohl-im-ofen-gebacken`, `pfifferlinge-gebraten-ohne-fett` |
| Deutsche Grundprodukte (Quark, Käse, Wurst & Schinken, Brot, Mehltypen, Senf …) | 75 | – | `magerquark`, `weizenmehl-type-1050`, `kochschinken` |
| Türkische Grundzutaten | 8 | 5 | `beyaz-peynir-kuhmilch-salzlakenkaese`, `sucuk` (geschätzt) |
| Imbiss & Streetfood (Portionsgramm in `portion` und `note`) | 14 | – | `doener-kebab-mit-haehnchen-im-fladenbrot`, `falafel-im-fladenbrot` |
| Asiatische Küche | 91 | – | `pad-thai-mit-haehnchen`, `chicken-korma`, `miso-suppe` |
| Getränke inkl. alkoholischer Getränke | 71 | – | `pils-alkoholfrei`, `rotwein-halbtrocken`, `gin-tonic` |

Quellen: BLS 4.0 (235), USDA FNDDS 2021–2023 (62, `fdc_id`), CoFID 2021 (25), Ciqual 2025 (4). Neu sind das optionale Feld `per100g.alcohol` (Ethanol in g/100 g, bei 52 Einträgen), die Felder `method` und `derived_from` auch für geschätzte Nicht-Gemüse-Einträge, `source_missing` auch für `protein`/`fat` (fehlen bei Getränken in der Quelle, dann als 0 eingetragen), die Küchen `cn`, `jp`, `kr`, `th`, `vn`, `in`, `id` sowie die Kategorien `Grundzutat: Wurst & Schinken` und `Grundzutat: Würzmittel & Aufstriche`. Getränke sind `type: "item"` ohne `prepared`; Gerichte aus FNDDS/BLS/CoFID sind `type: "dish"` mit `quality: "reference"` (generische Rezeptdatensätze, keine Markenprodukte). Werte pro 100 g; bei Getränken entsprechen 100 g näherungsweise 100 ml (Dichte ≈ 1; bei Spirituosen etwas weniger).

Nicht doppelt angelegt wurden 41 Quelldatensätze, deren Lebensmittel bereits existiert, meist als Schätzwert (z. B. `pils`, `rotwein-trocken`, `cappuccino`, `lahmacun-durum`, `tavuk-wrap`). Sie sind Kandidaten für ein späteres Upgrade auf `reference`; die Liste gibt `build_extension.py --report` aus.

**Gerichte und Fertigprodukte sind getrennt.** Ein Gericht (zuhause oder Restaurant, aus einem Rezept berechnet) bleibt in der Datenbank, auch wenn Open Food Facts ein gleichnamiges Fertigprodukt führt. Es bekommt `prepared` (`homemade` oder `restaurant`), `is_packaged_product: false` und bei einem Namenstreffer `off_similar` (höchstens drei Barcodes, nur als Hinweis). Marken- und Supermarktprodukte werden nicht aufgenommen. Nichts wurde entfernt: `removed_in_off.json` ist leer. **2114** der 4245 Gerichte tragen `off_similar`. Der Abgleich lief gegen einen Open-Food-Facts-Dump vom **29.10.2026**.

Aufbau der Schätzung, Garfaktor, Küchen und der OFF-Abgleich stehen in [`tools/dishes/BUILD_NOTES.md`](tools/dishes/BUILD_NOTES.md).

## Inhalt

```
data/foods.json                 Die Datenbank (JSON-Array, 4346 Gerichte aus 57 Küchen + 838 Grundzutaten + 73 Getränke)
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
  "names": { "de": "Karnıyarık", "en": "Karnıyarık", "tr": "Karnıyarık", "fr": "Karnıyarık", "es": "Karnıyarık", "pt": "Karnıyarık", "it": "Karnıyarık", "zh": "Karnıyarık" },
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
| `names` | ja | Name je Sprache: `de`, `en`, `tr`, `fr`, `es`, `pt` sind Pflicht (nicht leer), `it` und `zh` sind zusätzlich gesetzt. Siehe [Mehrsprachige Namen](#mehrsprachige-namen). |
| `aliases` | nein | Weitere landesübliche Namen je Sprache, z. B. `{ "de": ["Paradeiser"], "es": ["Jitomate"], "pt": ["Curgete"] }`. Werden durchsucht, aber nicht angezeigt. |
| `type` | ja | `"dish"` (Gericht) oder `"item"` (Artikel/Zutat/Produkt). Gerichte sind `dish`, Grundzutaten sind `item`. |
| `barcode` | ja | EAN-8/EAN-13 als **String** (führende Nullen) oder `null`. `null` ist gültig und bei allen jetzigen Gerichten gesetzt (kein Verpackungs-Barcode). Ist ein String gesetzt, muss die Prüfziffer stimmen und der Code eindeutig sein. |
| `synonyms` | ja | Alternative Namen und Schreibweisen (darf leer sein: `[]`). |
| `cuisine` | ja | Ländercode aus der festen Liste, u. a. `tr`, `de`, `it`, `fr`, `es`, `gr`, `pl` und seit Welle 3 auch `ge`, `am`, `az`, `md`, `by`, `me`, `xk`, `ad`, `li`, `mc`, `sm`, seit Welle 4 auch `cn`, `jp`, `kr`, `th`, `vn`, `in`, `id`. `int` steht für länderübergreifende Grundzutaten, Getränke und Imbissgerichte. |
| `category` | ja | Deutsche Kategorie, z. B. `Suppe`, `Kebap`, `Hauptgericht Fleisch`, `Kuchen`, `Getränk`. |
| `prepared` | nein | Bei Gerichten `"homemade"` (zuhause) oder `"restaurant"` (Restaurant/Imbiss). Bei Grundzutaten `"base_ingredient"`; dann sind `type: "item"`, `is_packaged_product: false` und `barcode: null` Pflicht. |
| `state` | nein | Zustand der Grundzutat: `raw` (roh), `cooked` (gekocht, gedünstet, geschmort), `grilled` (gegrillt), `fried` (in der Pfanne gebraten), `baked` (im Ofen gebacken/gebraten), `roasted` (geröstet, z. B. Nüsse), `dry` (trocken, z. B. Reis, Nudeln, Hülsenfrüchte), `dried` (getrocknet, z. B. Rosinen, getrocknete Tomaten), `frozen` (tiefgekühlt, unzubereitet), `canned` (Dose/Glas), `smoked` (geräuchert), `processed` (einfach verarbeitet, z. B. Mehl, Öl, Milch, Saft, Tomatenmark). |
| `unit` | nein | Bezugseinheit, immer `"g"` (Nährwerte pro 100 g). |
| `note` | nein | Bei Grundzutaten `"Grundzutat, kein Fertigprodukt"`; bei Varianten je nach Zustand z. B. `"Grundzutat (zubereitet), kein Fertigprodukt"`, `"Grundzutat (getrocknet), kein Fertigprodukt"`, `"Grundzutat (tiefgekühlt, unzubereitet), kein Fertigprodukt"`, `"Grundzutat (Konserve, generisch), kein Markenprodukt"` oder `"Grundzutat (verarbeitet, generisch), kein Markenprodukt"`; bei geschätzten Zubereitungen `"Grundzutat (zubereitet, geschätzt), kein Fertigprodukt"`. |
| `fdc_id` | nein | USDA-FoodData-Central-ID des Quelldatensatzes (positive Ganzzahl). |
| `source_id` | nein | Kennung des Quelldatensatzes außerhalb von USDA als `Datenbank:Code` (nicht-leerer String), z. B. `BLS 4.0:G582172`, `CH 7.1:1019`, `Ciqual 2025:20282`, `Livsmedelsverket:3771`, `CoFID 2021:13-642`. |
| `derived_from` | nein | Nur bei `quality: "estimate"`: ID der Grundzutat (z. B. `tomate-roh`) oder Quellkennung (z. B. `Ciqual 2025:12716`), aus der die Werte abgeleitet wurden; String oder Array von Strings. |
| `method` | nein | Schätzmethode: `"yield_factor"` (Ausbeute-/Retentionsfaktoren), `"similar_food"` (Werte eines vergleichbaren Lebensmittels) oder `"recipe"` (Rezeptberechnung). |
| `source_missing` | nein | Nährwerte, die in der Quelle fehlen (`"protein"`, `"fat"`, `"fiber"`, `"sugar"`). `protein`/`fat`/`fiber` stehen dann als 0 in `per100g`, `sugar` fehlt ganz. |
| `is_packaged_product` | nein | `false` bei Gerichten. `true` wäre nur für `type: "item"` mit Barcode sinnvoll; bei `type: "dish"` ist `true` ungültig. |
| `off_similar` | nein | Bis zu 3 Open-Food-Facts-Barcodes (6–14 Ziffern) ähnlich benannter Fertigprodukte. Nur ein Hinweis; das Gericht bleibt ein eigener Eintrag. |
| `per100g` | ja | `kcal` (0–950), `protein`, `carbs`, `fat`, `fiber` (je 0–100 g pro 100 g), optional `sugar` (0–100 g) und `alcohol` (Ethanol, 0–100 g). Protein + Kohlenhydrate + Fett ≤ 100 g (0,15 g Rundungstoleranz). |
| `portion` | nein | Typische Portion: `label` (Text) und `grams` (> 0, max. 5000). Die App rechnet damit von 100 g auf die Portion um. |
| `ingredients` | ja | Zutaten der zugrunde gelegten Portion: `{ "name", "grams" }`, `grams` > 0. Das sind Rezeptmengen, keine zweite Nährwertquelle. |
| `quality` | ja | `"estimate"` (berechnet, wie bei den 4245 Gerichten bis Welle 3), `"reference"` (aus einer amtlichen Nährwertdatenbank übernommen, wie bei 660 der 681 Grundzutaten) oder `"verified"` (später mit geprüften Werten überschrieben). Die 21 geschätzten Grundzutat-Zubereitungen und die 5 geschätzten türkischen Grundzutaten sind `"estimate"`; seit Welle 4 sind auch 101 Gerichte und 73 Getränke `"reference"` (direkter Quelldatensatz). |
| `source` | ja | Herkunft der Nährwerte. Bei Schätzwerten der feste Hinweis auf Rezept plus Referenzwerte; bei geprüften Einträgen die konkrete Quelle. |

Gerichte sind pro 100 g angegeben. `portion.grams` ist das übliche Tellergewicht nach dem Garen. `ingredients[].grams` sind die Rohmengen dieser Portion (aufgenommenes Wasser und Bratfett stehen mit in der Liste).

Kategorien sind Küchengruppen, keine Ernährungslabels. Dieselbe Speise kann regional anders heißen; hier steht jeweils ein verbreitetes Standardrezept.

`off_similar` steht nur, wenn der Dump ein gleichnamiges Fertigprodukt kannte (Beispiel: `wiener-schnitzel`). Fehlt das Feld, gab es keinen solchen Treffer. Die Barcodes gehören zum Fertigprodukt, nicht zum Gericht.

## Mehrsprachige Namen

Die App gibt es auf Deutsch, Englisch, Türkisch, Chinesisch, Spanisch und Italienisch. Deshalb hat jeder Eintrag ein Feld `names` mit dem Namen in jeder Sprache. `name` bleibt unverändert und ist weiterhin der Hauptname (Fallback).

```json
{
  "id": "tomate-roh",
  "name": "Tomate, roh",
  "names": { "de": "Tomate, roh", "en": "Tomato, raw", "tr": "Domates, çiğ", "fr": "Tomate, crue", "es": "Tomate, crudo", "pt": "Tomate, cru", "it": "Pomodoro, crudo", "zh": "番茄（生）" },
  "aliases": { "de": ["Paradeiser"], "es": ["Jitomate"], "zh": ["西红柿"] }
}
```

**Pflicht-Sprachen:** `de`, `en`, `tr`, `fr`, `es`, `pt`. Der Validator bricht ab, wenn eine davon fehlt oder leer ist. **Zusätzlich:** `it` und `zh`. Andere Sprachcodes sind nicht erlaubt.

**Regeln für die Namen:**

- **Grundzutaten** (Tomate, Gurke, Reis, Hähnchenbrust …) und ihre Zubereitungen (gekocht, gegrillt, getrocknet, Dose …) haben in jeder Sprache den dort üblichen Namen: `Gurke` → `Cucumber`, `Salatalık`, `Concombre`, `Pepino`, `Pepino`, `Cetriolo`, `黄瓜`.
- **Beschreibende Gerichte** werden übersetzt, z. B. `Gefüllte Paprika` → `Stuffed peppers`, `Biber dolması`, `Poivrons farcis` usw. Bei Landesgerichten steht oft der Originalname dabei, z. B. `Stifado (Rindfleisch-Zwiebel-Schmortopf)`.
- **Gerichte mit etabliertem Eigennamen** behalten in allen Sprachen den Originalnamen, z. B. `Karnıyarık`, `Lahmacun`, `Moussaka`, `Pastitsio`, `Francesinha`, `Kaiserschmarrn`. Für `zh` kann dann eine übliche chinesische Form stehen (z. B. `Pastel de nata` → `葡式蛋挞`); der Originalname ist dann Alias.
- Keine erfundenen Wort-für-Wort-Übersetzungen. Regionale Varianten stehen in `aliases`: Portugiesisch ist pt-PT zuerst, brasilianische Formen als Alias (z. B. `Curgete`/`Abobrinha`); Spanisch ist Spanien zuerst, lateinamerikanische Formen als Alias (`Patatas fritas`/`Papas fritas`).

**In der App anzeigen:** `names[appSprache] ?? name`. Bei der API geht das auch direkt mit `?lang=` (siehe unten): dann enthält jeder Treffer `display_name`. Für Sprachen der App ohne eigenes Feld (z. B. später weitere) einfach `en` oder `name` als Fallback nehmen.

**Suche:** Die Suche läuft immer über alle Sprachen gleichzeitig (`name`, `names.*`, `aliases.*`, `synonyms`). `domates`, `tomato`, `pomodoro`, `番茄` und `Tomate` finden also alle `tomate-roh`; `courgette`, `abobrinha` und `calabacín` finden `zucchini-roh`.

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

Prüft Pflichtfelder (einschließlich `cuisine`, `category`, `ingredients`, `quality`, `source`), die optionalen Felder `prepared`, `is_packaged_product`, `off_similar`, `state`, `unit`, `note`, `fdc_id`, `source_id`, `source_missing`, `derived_from`, `method`, `per100g.sugar` und `per100g.alcohol`, die Regeln für Grundzutaten (`type: "item"`, kein Barcode, kein Fertigprodukt), Wertebereiche (kcal 0–950, Makros 0–100 g, Protein + Kohlenhydrate + Fett ≤ 100 g + 0,15 g Rundung), eindeutige `id`s, eindeutige Barcodes und die EAN-Prüfziffer. **`barcode: null` ist erlaubt** und erzeugt keinen Fehler. Ein Gericht mit `is_packaged_product: true` ist ein Fehler.

Weicht `kcal` stark von `4·Protein + 4·Kohlenhydrate + 9·Fett` (+ `7·alcohol`, falls gesetzt) ab, gibt es eine **Warnung**, keinen Fehler. Erwartet sind derzeit 35 Warnungen: ältere geschätzte Getränke mit Alkohol ohne `alcohol`-Feld (Ethanol liefert etwa 7 kcal/g), ballaststoffreiche Grundzutaten wie Kleie und getrocknete Kräuter sowie die BLS-Datensätze `knoblauch-im-ofen-gebacken`/`knoblauch-gebraten-ohne-fett` (BLS zählt Fructane als Ballaststoffe, kcal wie veröffentlicht).

Bei echten Fehlern ist der Exit-Code `1`. Es braucht nur Node ≥ 20, keine Installation. Die GitHub Action `.github/workflows/validate.yml` läuft bei jedem Push und Pull Request.

## Lokale Suche (zum Testen)

```bash
node scripts/search-local.mjs karniyarik
node scripts/search-local.mjs "Karnıyarık"   # ı = i
node scripts/search-local.mjs karniyark       # ein Zeichen daneben
node scripts/search-local.mjs koelsch         # oe = ö
node scripts/search-local.mjs "Karnıyarık" --limit 3 --json
node scripts/search-local.mjs domates --lang en  # sucht in allen Sprachen, zeigt englische Namen
node scripts/test-worker.mjs                  # testet den API-Handler
```

### So funktioniert die Suche

- Groß-/Kleinschreibung, Umlaute, Akzente und türkische Buchstaben sind egal: `Karnıyarık`, `karniyarik` und `Karniyarik` finden dasselbe (`ı`/`İ` → `i`, `ş` → `s`, `ğ` → `g`, `ç` → `c`, `ä`/`ae` → `a`, `ö`/`oe` → `o`, `ü`/`ue` → `u`, `ß` → `ss`, `é`/`è`/`ñ`/`ã` usw. → Grundbuchstabe, `ø` → `o`, `æ` → `ae`, `ł` → `l`). Chinesische Schriftzeichen bleiben erhalten (`番茄`).
- Reihenfolge der Treffer: exakt → Wortanfang (Präfix) → Teilstring → Tippfehler (Levenshtein-Distanz 1 bei 3–5 Zeichen, 2 ab 6 Zeichen; unter 3 Zeichen keine Fehlertoleranz). `karniyark` trifft deshalb `Karnıyarık`.
- Gesucht wird in `name`, allen `names.*` (alle Sprachen), allen `aliases.*` und `synonyms`. Treffer in einem Namen stehen vor Treffern über Aliase/Synonyme.
- Ist der ganze Suchbegriff gleich einem Namen oder dem Kopfwort eines Namens (`domates` ↔ `Domates, çiğ`), steht der Eintrag ganz oben. Bei Gleichstand kommt die rohe Grundzutat vor Zubereitungen und vor Gerichten.
- Mehrere Wörter: Alle Wörter müssen passen.

## API

Die API ist ein Cloudflare Worker (kostenloser Plan reicht), liefert JSON und erlaubt CORS (`Access-Control-Allow-Origin: *`). `BASE` ist die URL nach dem Deploy.

```bash
BASE="https://food-database-api.<dein-account>.workers.dev"
```

| Endpunkt | Beschreibung |
| --- | --- |
| `GET /search?q=<text>&limit=<n>&lang=<sprache>` | Suche in Name, allen Sprachnamen, Aliasen und Synonymen. Optional `lang` (`de`, `en`, `tr`, `fr`, `es`, `pt`, `it`, `zh`; `pt-BR` usw. wird auf `pt` gekürzt): dann hat jeder Treffer zusätzlich `display_name` in dieser Sprache, und Treffer im Namen dieser Sprache werden bevorzugt. Unbekannte Sprache → 400. `limit` 1–50, Standard 10. Treffer **ohne** `ingredients` (die Liste wäre in jeder Suche Ballast). Nährwerte, Portion, Küche und Kategorie sind dabei. |
| `GET /item/{id}?lang=<sprache>` | Voller Eintrag inklusive `ingredients` (mit `lang` zusätzlich `display_name`). 404, wenn die `id` fehlt. |
| `GET /barcode/{ean}` | Voller Eintrag zu einer EAN-8/EAN-13. 400 bei ungültiger Prüfziffer, 404 wenn unbekannt. Aktuell hat kein Gericht einen Barcode (`null`), der Endpunkt ist für spätere geprüfte Produkte da. |
| `GET /health` | Status, Anzahl der Einträge und unterstützte Sprachen. |

```bash
curl "$BASE/health"
# {"status":"ok","count":5257,"languages":["de","en","tr","fr","es","pt","it","zh"]}

curl "$BASE/search?q=karniyarik&limit=5"
# {"query":"karniyarik","count":1,"results":[{"id":"karniyarik","name":"Karnıyarık","barcode":null, ...}]}

curl "$BASE/search?q=Karn%C4%B1yar%C4%B1k"
curl "$BASE/search?q=karniyark"

curl "$BASE/search?q=domates&lang=en&limit=3"
# {"query":"domates","lang":"en","count":3,"results":[{"id":"tomate-roh","name":"Tomate, roh","display_name":"Tomato, raw", ...}]}

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

Das ist bei diesem Datenumfang (5257 Einträge) praktikabel. Für die Zutatenliste brauchst du keinen zweiten Endpunkt, die Datei enthält sie bereits. In der Such-API fehlt `ingredients` in der Trefferliste absichtlich; `GET /item/{id}` liefert sie nach.

## Einbau in die App: Suchfeld mit Live-Suche (Debounce)

```ts
const API = "https://food-database-api.<dein-account>.workers.dev";

type Nutrients = { kcal: number; protein: number; carbs: number; fat: number; fiber: number; sugar?: number; alcohol?: number };
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
  source_id?: string; // andere Datenbank, z. B. "BLS 4.0:G582172"
  source_missing?: ("protein" | "fat" | "fiber" | "sugar")[];
  derived_from?: string | string[]; // nur bei quality "estimate"
  method?: "yield_factor" | "similar_food" | "recipe";
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
- [x] Mehrsprachige Namen (`names` de/en/tr/fr/es/pt Pflicht, dazu it/zh; `aliases`) und Suche über alle Sprachen, `?lang=` in der API
- [ ] Einzelne Einträge mit geprüften Werten überschreiben (`quality: "verified"`, Quelle im Feld `source`)
- [ ] Echte Barcodes ergänzen, wo ein verpacktes Produkt dahintersteht
- [ ] API deployen und in die App einbinden
- [ ] Automatisches Deployment per GitHub Action (`wrangler deploy` bei Änderungen an `data/`)
- [ ] Optional: weitere Nährwerte (Zucker, Salz, gesättigte Fette, Alkohol gramm), mehrere Portionen
- [ ] Optional: Datenbank aufteilen, wenn sie deutlich über diesen Umfang wächst

## Hinweis

Die Rezepte stammen aus allgemeinem Küchenwissen, die Referenzwerte sind Näherungen. Die Werte der Grundzutaten stammen aus USDA FoodData Central (SR Legacy, Public Domain/CC0), dem Bundeslebensmittelschlüssel (Max Rubner-Institut (2025): Bundeslebensmittelschlüssel (BLS), Version 4.0 – Deutsche Nährstoffdatenbank. Karlsruhe. DOI: 10.25826/Data20251217-134202-0; CC BY 4.0), Ciqual 2025 (Anses, CC BY 4.0), der Schweizer Nährwertdatenbank V7.1 (BLV, naehrwertdaten.ch, frei mit Quellenangabe) und der Livsmedelsdatabasen von Livsmedelsverket (CC BY 4.0) und CoFID 2021 (Public Health England (2021): McCance and Widdowson's The Composition of Foods Integrated Dataset 2021, Open Government Licence v3.0; Werte und Faktoren für Schätzungen). Die Imbiss- und asiatischen Gerichte mit `fdc_id` stammen aus USDA FoodData Central, FNDDS 2021–2023 (Survey Foods, Release 2024-10-31; gemeinfrei, CC0 1.0), ebenso die dort übernommenen Portionsgewichte. Die Namensnennung steht je Eintrag in `source`. Übernimm keine fremden Nährwerttabellen, ohne deren Lizenz zu prüfen. Wer einen Eintrag überschreibt, trägt die geprüfte Quelle in `source` ein.
