# Grundzutaten (USDA FoodData Central)

631 Grundzutaten mit Nährwerten pro 100 g (keine Fertig- oder Markenprodukte):

- 295 rohe bzw. unverarbeitete Basis-Lebensmittel (`base_list.py`, `quality: "reference"`)
- 309 Zubereitungs- und Haltbarkeitsvarianten davon (`variants_list.py`, `quality: "reference"`), z. B. `Tomate, getrocknet`, `Tomatenmark`, `Tomate, aus der Dose (geschält, im Saft)`, `Hähnchenbrust, gegrillt`, `Erbsen grün, tiefgekühlt`, `Mandeln, geröstet`, `Hühnerei, Spiegelei`, `Kartoffel, Pellkartoffel (gekocht, ohne Schale gegessen)`, `Linsen, gekocht`
- 27 geschätzte Zubereitungen ohne eigenen USDA-Datensatz (`estimates_list.py`, `quality: "estimate"`), z. B. `Tomate, gegrillt`, `Paprika rot, gegrillt`, `Zucchini, in Öl gebraten`, `Aubergine, im Ofen geröstet (mit Öl)`, `Brokkoli, gedämpft`; siehe [Geschätzte Zubereitungen](#geschätzte-zubereitungen)

## Quelle

USDA FoodData Central, **SR Legacy (April 2018)**, Public Domain (CC0 1.0).
Download: <https://fdc.nal.usda.gov/fdc-datasets/FoodData_Central_sr_legacy_food_csv_2018-04.zip>

Jeder Roh- und Varianteneintrag verweist auf genau einen USDA-Datensatz (`fdc_id` und der englische Originalname in `source`).
Die Werte werden nur übernommen und gerundet (kcal ganzzahlig, Makros auf 0,1 g), nichts wird geschätzt. Ausnahme sind die 27 als `estimate` markierten Zubereitungen (eigener Abschnitt unten).

| Feld | Nährstoff-ID (USDA) |
| --- | --- |
| `kcal` | 1008 Energy (KCAL) |
| `protein` | 1003 Protein |
| `carbs` | 1005 Carbohydrate, by difference |
| `fat` | 1004 Total lipid (fat) |
| `fiber` | 1079 Fiber, total dietary |
| `sugar` | 2000 Sugars, total (optional) |

Fehlt in USDA ein Wert, steht er in `source_missing`:
- `fiber` fehlt nur bei Lebensmitteln mit 0 g Kohlenhydraten (Fleisch, Fisch, Öl usw.). Dort wird `fiber: 0` gesetzt.
  Lebensmittel mit Kohlenhydraten und ohne USDA-Ballaststoffwert wurden nicht aufgenommen.
- `sugar` fehlt bei 74 Einträgen (23 Basis, 50 Varianten, 1 Schätzung, die das Fehlen von der rohen Grundzutat erbt) und wird dann weggelassen (kein Schätzwert).

## Neu bauen

```bash
cd tools/base_ingredients
curl -LO https://fdc.nal.usda.gov/fdc-datasets/FoodData_Central_sr_legacy_food_csv_2018-04.zip
unzip -q FoodData_Central_sr_legacy_food_csv_2018-04.zip -d usda
python3 build_base.py usda/FoodData_Central_sr_legacy_food_csv_2018-04 ../../data/foods.json          # Probelauf
python3 build_base.py usda/FoodData_Central_sr_legacy_food_csv_2018-04 ../../data/foods.json --write  # schreiben
cd ../.. && npm test
```

`build_base.py` ist idempotent: Es entfernt zuerst alle Einträge mit `prepared: "base_ingredient"` und hängt die Listen aus `base_list.py`, `variants_list.py` und `estimates_list.py` neu an.
Jede Liste enthält je Zeile den deutschen Namen, die Kategorie, den Zustand, deutsche Synonyme und die exakte USDA-Beschreibung.

## Hinweise zur Zuordnung

- `Vollmilch (ca. 3,5 %)` entspricht USDA „Milk, whole, 3.25% milkfat“. Milch 1,5 % hat kein USDA-Gegenstück, deshalb gibt es Milch 1 % und 2 %.
- `Weizenmehl (Auszugsmehl, ~Typ 405)` entspricht „Wheat flour, white, all-purpose“. Für Typ 1050 und für Quark gibt es keine passenden USDA-Datensätze.
- Schlagsahne 30 % entspricht „light whipping cream“, 36 % entspricht „heavy whipping cream“.
- Bei Milchprodukten liegt USDA-Zucker (gemessen) teils leicht über den Kohlenhydraten (Differenzrechnung). Das ist ein Rundungsartefakt der Quelle.
- Leinöl: 0,11 g Eiweiß + 99,98 g Fett ergeben 100,1 g. Der Validator erlaubt dafür 0,15 g Rundungstoleranz.
- Brot: Die üblichen Brotsorten (Weißbrot, Vollkornbrot, Roggenbrot, Baguette, Brötchen …) gibt es schon als Gerichte. Sie wurden nicht doppelt angelegt; aufgenommen ist nur Pitabrot.

## Zubereitungsvarianten

Jede Variante ist ein eigener USDA-Datensatz für genau diese Zubereitung (z. B. „Tomatoes, sun-dried“, „Chicken, broilers or fryers, breast, meat only, cooked, roasted“). Es wird nichts mit Ausbeute- oder Retentionsfaktoren hochgerechnet: Alle 309 Varianten sind `quality: "reference"`, 0 sind Schätzungen.

Zustände (`state`): `cooked` (gekocht, gedünstet, geschmort, gedämpft), `grilled` (USDA „broiled“/„grilled“ bzw. bei Fisch „cooked, dry heat“), `fried` (Pfanne: „pan-fried“, „sauteed“, „stir-fried“, Spiegelei), `baked` (Ofen: „roasted“/„baked“ bei Fleisch und Gemüse), `roasted` (geröstete Nüsse, Samen, Kerne), `dried`, `frozen` (tiefgekühlt, unzubereitet), `canned` (Dose/Glas, abgetropft wenn so angegeben), `smoked`, `processed` (Saft, Mark, Püree, Pulver, Milchvarianten).

`note` je Zustand: `Grundzutat (zubereitet), kein Fertigprodukt`, `Grundzutat (getrocknet), kein Fertigprodukt`, `Grundzutat (tiefgekühlt, unzubereitet), kein Fertigprodukt`, `Grundzutat (Konserve, generisch), kein Markenprodukt`, `Grundzutat (verarbeitet, generisch), kein Markenprodukt`; neue rohe Varianten (z. B. `Wachtelei, roh`, `Teff, roh`) tragen `Grundzutat, kein Fertigprodukt`.

Regeln beim Bauen:

- Doppelte Namen oder Synonyme gegen **alle** Einträge (auch Gerichte) brechen den Lauf ab; doppelte Variantensynonyme werden weggelassen und gemeldet. Doppelte `fdc_id`s brechen ab.
- Was es schon als Gericht gibt, wurde nicht als Variante angelegt: Bratkartoffeln/Rösti, Kartoffelpüree, Pommes frites, Rührei, Omelett, eingelegter Hering (Bismarckhering/Rollmops), gebratene Champignons, Enten-/Gänsebraten mit Haut, Brathähnchen, Orangensaft (Portakal Suyu), Sauerkraut, eingelegte Rote Bete (Pancar Turşusu), Sultaninen (= Rosinen).
- Varianten ohne USDA-Ballaststoffwert bei Kohlenhydraten > 0 wurden nicht aufgenommen (u. a. Kokosmilch aus der Dose, frische Pasta gekocht, Soba, Somen, Maronen gekocht/getrocknet, Rund-/Mittelkornreis gekocht).
- Gegrilltes, im Ofen geröstetes, gebratenes und gedämpftes Gemüse ohne USDA-Datensatz steht nicht hier, sondern als Schätzung in `estimates_list.py` (siehe unten).
- Bei Saft gibt es nur generische Säfte (keine Marken, kein „aus Konzentrat mit Zuckerzusatz“).
- Sehr ballaststoffreiche Trockenprodukte (getrocknete Kräuter, Kleie) zeigen im Validator die Warnung „kcal weicht von Makro-Schätzung ab“: USDA rechnet dort mit spezifischen Energiefaktoren, die Werte sind korrekt übernommen.

## Geschätzte Zubereitungen

`estimates_list.py` enthält übliche Zubereitungen, für die USDA keinen eigenen Datensatz hat. Sie werden aus der rohen USDA-Grundzutat (unrundete Werte) berechnet und tragen `quality: "estimate"`, `note: "Grundzutat (zubereitet, geschätzt), kein Fertigprodukt"`, `derived_from` (ID der rohen Grundzutat), keine `fdc_id` und in `source` die rohe USDA-Quelle sowie jeden verwendeten Faktor mit Quelle. `ingredients` nennt die Rohware (100 / Ausbeute g) und gegebenenfalls Rapsöl (Fettaufnahme / Ausbeute g).

Formel pro 100 g zubereitet: `(Rohwert × Retention + Fettaufnahme × Ölwert / 100) / Ausbeute`. Ausbeute = Gewicht zubereitet / Gewicht roh, Fettaufnahme in g Öl je 100 g Rohware, Ölwerte aus `Rapsöl` (USDA FDC 172336). Zucker folgt der Kohlenhydrat-Retention, kcal der Retention von Protein/Fett/KH (alle gleich).

Faktorquellen (nur dokumentierte Werte, nichts geraten):

| Quelle | verwendet für |
| --- | --- |
| McCance and Widdowson's Composition of Foods Integrated Dataset (CoFID) 2021, Public Health England, Open Government Licence v3, Blatt „1.3 Proximates“, <https://www.gov.uk/government/publications/composition-of-foods-integrated-dataset-cofid> | Ausbeute und Fettaufnahme per Massenbilanz aus Wasser und Fett roh vs. zubereitet: Tomate und grüner Spargel gegrillt (ohne Fett, Ausbeute = Trockenmasse roh / Trockenmasse zubereitet), Zucchini, Aubergine, grüner Spargel, Lauch und Pastinake im Ofen mit Öl geröstet, Zwiebel im Ofen gebacken (CoFID: 20 % Gewichtsverlust), Zucchini, Aubergine, Champignons und Tomate in Öl gebraten |
| Bognár, A. (2002): Tables on weight yield of food and retention factors of food constituents for the calculation of nutrient composition of cooked foods (dishes). Berichte der Bundesforschungsanstalt für Ernährung BFE-R-02-03, <https://www.fao.org/uploads/media/bognar_bfe-r-02-03.pdf> | Ausbeute beim Dämpfen (Tab. 17–20) und Retention beim Dämpfen (Tab. 26, 28, 30: Protein/Fett/KH 0,95, Ballaststoffe 0,94); „Bake in oven“-Retention 1,00 als Beleg für Retention 1,0 bei trockener Hitze |
| Bergström, L. (1994): Nutrient losses and gains in the preparation of foods (NLG-Projekt, Livsmedelsverket), Ausbeutefaktoren veröffentlicht in Phenol-Explorer, <http://phenol-explorer.eu/publications/1269> | Ausbeute Aubergine gegrillt (0,40) und Paprika gegrillt (0,93; für rot, gelb, grün) |

Der Massenbilanz-Ansatz: Mit Fettzugabe bleibt die fettfreie Trockenmasse erhalten, also Ausbeute = (100 − Wasser_roh − Fett_roh) / (100 − Wasser_zub − Fett_zub) und Fettaufnahme = Ausbeute × Fett_zub − Fett_roh.

Nicht aufgenommen, weil kein dokumentierter Faktor gefunden wurde: Zucchini, Champignons, Zwiebel und Maiskolben gegrillt; Kürbis, Karotte (nur Ausbeute, keine Fettaufnahme belegt) und Rote Bete im Ofen geröstet; Rote Bete gedämpft (Bognár-Ausbeute bezieht sich auf ungeschälte Knollen); Paprika gelb gebraten (keine Fettaufnahme belegt); Süßkartoffel-Wedges (CoFID vergleicht mit Schale gegart vs. ohne Schale roh); Zuckerschoten gebraten (CoFID-Ausbeute > 1, widersprüchlich). Bereits als USDA-Variante vorhanden und nicht doppelt angelegt: Zwiebel gebraten, Paprika rot/grün gebraten, Butternut-Kürbis im Ofen gebacken, Süßkartoffel gebacken.

Gerichte mit gleichem Synonym (z. B. „Ofenzucchini“, „Ofenaubergine“, „gegrillte Aubergine“, „Pilze gebraten“) bleiben eigene Einträge; das Synonym wird bei der Schätzung weggelassen und beim Bauen gemeldet.
