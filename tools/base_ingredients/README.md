# Grundzutaten (USDA FoodData Central)

295 rohe bzw. unverarbeitete Basis-Lebensmittel (keine Fertig- oder Markenprodukte) mit Referenz-Nährwerten pro 100 g.

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
- `sugar` fehlt bei 23 Einträgen und wird dann weggelassen (kein Schätzwert).

## Neu bauen

```bash
cd tools/base_ingredients
curl -LO https://fdc.nal.usda.gov/fdc-datasets/FoodData_Central_sr_legacy_food_csv_2018-04.zip
unzip -q FoodData_Central_sr_legacy_food_csv_2018-04.zip -d usda
python3 build_base.py usda/FoodData_Central_sr_legacy_food_csv_2018-04 ../../data/foods.json          # Probelauf
python3 build_base.py usda/FoodData_Central_sr_legacy_food_csv_2018-04 ../../data/foods.json --write  # schreiben
cd ../.. && npm test
```

`build_base.py` ist idempotent: Es entfernt zuerst alle Einträge mit `prepared: "base_ingredient"` und hängt die Liste aus `base_list.py` neu an.
Die Liste enthält je Zeile den deutschen Namen, die Kategorie, den Zustand, deutsche Synonyme und die exakte USDA-Beschreibung.

## Hinweise zur Zuordnung

- `Vollmilch (ca. 3,5 %)` entspricht USDA „Milk, whole, 3.25% milkfat“. Milch 1,5 % hat kein USDA-Gegenstück, deshalb gibt es Milch 1 % und 2 %.
- `Weizenmehl (Auszugsmehl, ~Typ 405)` entspricht „Wheat flour, white, all-purpose“. Für Typ 1050 und für Quark gibt es keine passenden USDA-Datensätze.
- Griechischer Joghurt gibt es in USDA nur fettarm oder mager, nicht als Vollfett-Variante.
- Schlagsahne 30 % entspricht „light whipping cream“, 36 % entspricht „heavy whipping cream“.
- Bei Milchprodukten liegt USDA-Zucker (gemessen) teils leicht über den Kohlenhydraten (Differenzrechnung). Das ist ein Rundungsartefakt der Quelle.
- Leinöl: 0,11 g Eiweiß + 99,98 g Fett ergeben 100,1 g. Der Validator erlaubt dafür 0,15 g Rundungstoleranz.
- Brot: Die üblichen Brotsorten (Weißbrot, Vollkornbrot, Roggenbrot, Baguette, Brötchen …) gibt es schon als Gerichte. Sie wurden nicht doppelt angelegt; aufgenommen ist nur Pitabrot.
