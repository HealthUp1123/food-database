# Grundzutaten (USDA FoodData Central)

604 Grundzutaten mit Referenz-Nährwerten pro 100 g (keine Fertig- oder Markenprodukte):

- 295 rohe bzw. unverarbeitete Basis-Lebensmittel (`base_list.py`)
- 309 Zubereitungs- und Haltbarkeitsvarianten davon (`variants_list.py`), z. B. `Tomate, getrocknet`, `Tomatenmark`, `Tomate, aus der Dose (geschält, im Saft)`, `Hähnchenbrust, gegrillt`, `Erbsen grün, tiefgekühlt`, `Mandeln, geröstet`, `Hühnerei, Spiegelei`, `Kartoffel, Pellkartoffel (gekocht, ohne Schale gegessen)`, `Linsen, gekocht`

## Quelle

USDA FoodData Central, **SR Legacy (April 2018)**, Public Domain (CC0 1.0).
Download: <https://fdc.nal.usda.gov/fdc-datasets/FoodData_Central_sr_legacy_food_csv_2018-04.zip>

Jeder Eintrag verweist auf genau einen USDA-Datensatz (`fdc_id` und der englische Originalname in `source`).
Die Werte werden nur übernommen und gerundet (kcal ganzzahlig, Makros auf 0,1 g), nichts wird geschätzt.

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
- `sugar` fehlt bei 73 Einträgen (23 Basis, 50 Varianten) und wird dann weggelassen (kein Schätzwert).

## Neu bauen

```bash
cd tools/base_ingredients
curl -LO https://fdc.nal.usda.gov/fdc-datasets/FoodData_Central_sr_legacy_food_csv_2018-04.zip
unzip -q FoodData_Central_sr_legacy_food_csv_2018-04.zip -d usda
python3 build_base.py usda/FoodData_Central_sr_legacy_food_csv_2018-04 ../../data/foods.json          # Probelauf
python3 build_base.py usda/FoodData_Central_sr_legacy_food_csv_2018-04 ../../data/foods.json --write  # schreiben
cd ../.. && npm test
```

`build_base.py` ist idempotent: Es entfernt zuerst alle Einträge mit `prepared: "base_ingredient"` und hängt die Listen aus `base_list.py` und `variants_list.py` neu an.
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
- Gegrilltes Gemüse (Tomate, Zucchini, Aubergine, Paprika gegrillt) fehlt, weil USDA dafür keinen Datensatz hat und nicht geschätzt wird.
- Bei Saft gibt es nur generische Säfte (keine Marken, kein „aus Konzentrat mit Zuckerzusatz“).
- Sehr ballaststoffreiche Trockenprodukte (getrocknete Kräuter, Kleie) zeigen im Validator die Warnung „kcal weicht von Makro-Schätzung ab“: USDA rechnet dort mit spezifischen Energiefaktoren, die Werte sind korrekt übernommen.
