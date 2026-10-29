# Build-Notizen: Gerichte-Datenbank (türkisch, deutsch, europäisch)

**Alle Werte sind Schätzungen (`quality: "estimate"`), keine Laborwerte.** Abweichungen von ±10–25 % gegenüber echten Gerichten sind normal (Rezept, Fettmenge, Portionsgröße).

## Methode
- Pro Gericht ein typisches Hausrezept für **eine Portion** (Zutaten in g, roh bzw. Zutatenzustand).
- Nährwerte werden **programmatisch** aus einer Zutaten-Referenztabelle (`ingredients.json`, ca. 275 Zutaten, pro 100 g, USDA/BLS-ähnliche Näherungswerte) berechnet – nicht von Hand geschätzt.
- **Garfaktor** (Gewicht gegart / roh, 0,5–1,05) bestimmt das Portionsgewicht (auf 5 g gerundet). `per100g` = Summe der Zutatenwerte / Portionsgewicht × 100.
- Beim Kochen aufgenommenes Wasser (Reis, Nudeln, Eintöpfe) steht explizit als Zutat (`wasser`, `bruehe`); bei Frittiertem nur das aufgenommene Öl.
- Kaffee/Tee sind vereinfacht über Wasser-/Teeeintrag (≈ 0 kcal) abgebildet.

## Plausibilitätsprüfungen (`build.py`, Exit 1 bei Fehlern)
- unbekannte Zutat, doppelte ID/Name, Garfaktor außerhalb 0,5–1,05 → Fehler
- kcal ≈ 4·Eiweiß + 4·KH + 9·Fett (±15 %, min. ±12 kcal), Eiweiß+KH+Fett ≤ 100 g, kcal 0–950, Ballaststoffe ≤ KH
- **Alkohol-Ausnahme:** Einträge mit Wein/Bier (Glühwein, Bier, Weinschorle, Bowle, Federweißer …) liegen bewusst über der Makro-Schätzung (Alkohol ≈ 7 kcal/g); geprüft wird nur, dass kcal nicht darunter liegen. Der Repo-Validator zeigt dafür 3 Warnungen (Weißwein, Rotwein, Glühwein) – erwartet.
- Zusätzlich: Repo-Validator `scripts/validate.mjs` → 2884 gültig (angepasste Kopie in `repo_patch/`, siehe unten).

## Felder
`id, name, type:"dish", barcode:null, synonyms, cuisine (tr|de|it|fr|es|pt|gr|gb|ie|nl|be|at|ch|se|no|dk|fi|is|pl|cz|sk|hu|rs|hr|ba|bg|al|mk|si|ro|ee|lv|lt|ua|ru|cy|mt|lu), prepared ("homemade"|"restaurant"), is_packaged_product:false, [off_similar], category, per100g{kcal,protein,carbs,fat,fiber}, portion{label,grams}, ingredients[{name,grams}], quality:"estimate", source:"calculated from typical recipe and approximate reference values"`

## Einschränkungen
- Regionale Varianten und Familienrezepte unterscheiden sich stark; hier jeweils ein verbreitetes Standardrezept.
- Unsichere/seltene Gerichte (Zutaten teils grob angenähert): Murtuğa, Kavut, Haşıl, Meftune, Sembusek, Irok, Herise, Kibbeh Mardin, Pehlivan/Saray Kebabı, Çibörek, Kömbe Köfte, Pestil, Cezerye, Keşkül, Pişmaniye, Menengiç-/Dibek-Kaffee, Malzbier, Federweißer.
- Teller-Kombinationen (z. B. „Schnitzel mit Pommes“, „Rouladen mit Rotkohl und Klößen“) sind ganze Mahlzeiten, keine Einzelkomponenten.
- Quelle der Rezepte: allgemeines Küchenwissen, keine Hersteller-/Labordaten; Stück-/Portionsgrößen sind Richtwerte.

## Neu erzeugen
`python3 build.py` → rohes `foods.json` (danach nach `foods_before_off.json` kopieren und `off_check.py apply` ausführen, siehe unten) →`foods.json`, `ingredients.json`, `build_report.txt` (Rezepte in `batches/*.py`, Zutaten in `ingredients_src.txt`).

## Europäische Gerichte (neu)
- **644 neue Gerichte** aus 36 Küchen (ohne Türkei/Deutschland), jeweils mit Rezept × Zutatentabelle, `quality: "estimate"`, Synonymen, Kategorie, Portion. Zutatentabelle um ca. 25 Zutaten erweitert (u. a. Ricotta, Pecorino, Rohschinken, Chorizo, Stockfisch, Hummer, Foie gras, Quittenbrot …).
- Rezepte stehen in `recipes/rec_*.txt` (Format `Name | Garfaktor | Portionslabel | Zutaten`), `tools/compose_eu.py` erzeugt daraus `batches/eu_<cc>.py`; Kandidatenlisten/Auswahl in `candidates/`.
- Anzahl je Küche: gr 72, it 55, es 47, pt 34, gb 33, fr 30, at 27, hu 27, pl 24, cz 21, ch 20, dk 19, hr 17, rs 17, ua 17, bg 14, ru 14, cy 13, nl 12, ro 12, ba 11, ie 11, be 10, mk 10, mt 10, no 10, al 8, fi 8, lt 8, se 8, lu 7, sk 6, si 5, ee 3, is 3, lv 1.
- Auswahl: Kandidaten (ca. 1700) wurden gegen die bestehenden Gerichte entdoppelt. Ca. 1000 wurden **nicht** neu geschrieben, weil sie beim damaligen Abgleich (nach der früheren Regel „nicht eintragen, wenn in OFF“) einen OFF-Namenstreffer hatten. Nach der neuen Regel dürften sie eingetragen werden – das ist **nicht** passiert; Liste in `candidates/cands_status.json`.
- Baltikum/Slowakei/Slowenien/Island sind dünn besetzt (wenige bekannte Gerichte ohne OFF-Treffer).

## Gerichte vs. Fertigprodukte & Open Food Facts (aktuelle Regel)
Gerichte (zuhause/Restaurant/Imbiss) und Fertigprodukte werden **getrennt** gesehen:
- Ein Gericht wird **nicht entfernt**, nur weil OFF ein gleichnamiges Fertigprodukt hat. Es bekommt `prepared` (`homemade`/`restaurant`), `is_packaged_product: false` und bei OFF-Treffern `off_similar` (bis zu 3 OFF-Barcodes, nur Hinweis).
- Entfernt werden nur Einträge, die selbst Fertig-/Supermarktprodukte sind (`type: "item"` mit Barcode, der in OFF vorliegt). Aktuell gibt es keine solchen Einträge → `removed_in_off.json` ist leer (`[]`).
- `prepared` ist eine Heuristik (`tools/off_check.py: prepared_of`): `restaurant` bei Kategorien Kebap, Pide/Lahmacun/Gözleme, Snack oder Schlüsselwörtern (Döner, Pizza, Burger, Currywurst …), sonst `homemade`. Ein vorhandenes Feld hat Vorrang.
- **Treffer-Definition** (konservativ): Namen werden normalisiert (klein, Diakritika weg, ß→ss, ä/ö/ü auch als ae/oe/ue, Satzzeichen→Leerzeichen, Tokens). Verglichen werden Gerichtsname + bis zu 4 Synonyme gegen `product_name`/`generic_name` von OFF. Treffer bei: `exact` (Token-Folge gleich), `off_in_dish` (OFF-Name als Ganzwort-Folge im Gerichtsnamen, ≥ 80 % der Tokens), `dish_in_off` (Gericht als Ganzwort-Folge im OFF-Namen, macht ≥ 80 % der OFF-Tokens aus). Mengenangaben im OFF-Namen und ein Marken-Präfix/-Suffix werden ignoriert. Reine Marken- oder Zutaten-Treffer zählen nicht; „near“ ist nur informativ.
- **Methode/Stand:** Hauptabgleich = lokaler OFF-**Dump** (`en.openfoodfacts.org.products.csv.gz`, abgerufen 29.10.2026, ca. 4,5 Mio. Produkte, DuckDB-Index) für **alle 1879 Gerichte**. API-Gegenprobe (Search-a-licious, `https://search.openfoodfacts.org/search`, 1 Anfrage/s, Backoff bei 429, SQLite-Cache) nur für **770 Gerichte** (der Lauf wurde auf Wunsch abgebrochen; die alte `cgi/search.pl` / `api/v2/search` lieferten am 29.10.2026 „Page temporarily unavailable“). Die API fand keinen Treffer, den der Dump nicht schon hatte.
- Ergebnis: **601 von 1879 Gerichten** haben mindestens einen OFF-Treffer (alle aus den ursprünglichen 1235: 354 de, 247 tr) und tragen `off_similar`; bei 305 davon matcht nur ein Synonym. Neue europäische Gerichte: 0 Treffer (sie waren vorab nach dem Dump ausgewählt). **0 Einträge entfernt.**
- Grenzen: Ein Namenstreffer heißt nur „OFF kennt ein Produkt gleichen Namens“ – meist ein Industrie-Fertigprodukt (Konserve, Tiefkühlware), nicht dasselbe wie das Rezeptgericht. Umgekehrt entstehen falsche Negative bei anderer Schreibweise/Sprache (OFF-Name nur in anderer Sprache). Der Dump ist ein Schnappschuss; OFF-Daten ändern sich laufend. Barcodes in `off_similar` können ungewöhnlich formatiert sein (führende Nullen, UPC-A); nur 6–14-stellige Ziffern werden übernommen.

### Prüfung für neue Einträge
```
python3 build.py && cp foods.json foods_before_off.json
/workspace/venv/bin/python tools/off_check.py check --backend dump --input foods_before_off.json      # Dump (benötigt duckdb + off_dump/)
python3 tools/off_check.py check --backend api  --input foods_before_off.json --only-ids a,b,c         # optionale API-Gegenprobe (1 Req/s)
/workspace/venv/bin/python tools/off_check.py apply --input foods_before_off.json --out foods.json --removed removed_in_off.json --backends api,dump
```
Dump neu aufbauen: `off_check.py dump-index --csv off_dump/en.openfoodfacts.org.products.csv.gz`. Status: `off_check_status.json` (API), `off_check_status_dump.json` (Dump), Cache `off_check_cache.sqlite`. Der Dump (1,5 GB) und der DuckDB-Index (540 MB) liegen unter `off_dump/` und sind **nicht** im Bundle-ZIP.

### Schema/Validator (lokale Kopie in `repo_patch/`, nichts nach GitHub gepusht)
`scripts/validate.mjs` prüft neue **optionale** Felder: `prepared` ∈ {homemade, restaurant}; `is_packaged_product` boolean (true bei `type: "dish"` verboten); `off_similar` = Array mit höchstens 3 Barcode-Strings (6–14 Ziffern). `src/search.mjs` und `api/worker.js` reichen die Einträge unverändert durch (keine Änderung nötig). README um die drei Felder und die Regel ergänzt. `node scripts/validate.mjs foods.json` → 2884 gültig; `scripts/test-worker.mjs` bestanden. Warnung (erwartet): Alkoholika (Tuică, Rakı, Rakija: kcal > Makro-Schätzung).

## Nachholrunde (29.10.2026): 1005 zuvor ausgelassene Gerichte
- Hintergrund: Unter der alten Regel („nichts eintragen, was in OFF vorliegt“) waren ca. 1000 europäische Kandidaten ausgelassen worden. Nach der Regeländerung (nur markieren) und Freigabe durch den Owner wurden sie nachgetragen.
- Eingabe: `candidates/rest_all.json` (1016 Kandidaten), `recipes/rec_extra_{1..4}.txt` (1009 Rezepte), 10 neue Zutaten `x2_*`–`x4_*` (aus `ingredients_add_*.txt` an `ingredients_src.txt` angehängt). Zusammensetzen: `python3 tools/compose_eu2.py` → `batches/eu2_<cc>.py` (35 Küchen); `build.py` lädt `eu2_*` zuletzt, die bisherigen 1879 Gerichte und ihre IDs sind unverändert (geprüft: alle Felder identisch).
- Entdoppelung (normalisiert: klein, ohne Diakritika, ß→ss) gegen die 1879 und untereinander: entfernt **Knödel di speck** und **Bündner Gerstensuppe** (existieren schon), **Bouchées à la reine** und **Pastéis de bacalhau** (doppelt in den Extra-Rezepten); 78 Synonyme, die bereits bei anderen Gerichten stehen, wurden gestrichen (Gericht bleibt). Details: `candidates/eu2_dedup_report.json`. 7 Kandidaten ohne Rezept/ohne Übernahme (1016 − 1005 − 4 Duplikate).
- Build: 0 Fehler, 0 Flags. Korrektur: Pain au chocolat (Rezept war zu fettig, 584 kcal/100 g). `FAT_OK` in `build.py`: Smalec ze skwarkami und Jumări (reine Fettgerichte, >560 kcal/100 g plausibel).
- OFF (Dump, alle 2884 geprüft; API-Gegenprobe weiterhin nur für die früheren 770): **1605 Gerichte** mit OFF-Treffer (601 alte + 1004 neue; 1602 tragen `off_similar`, 3 ohne gültigen 6–14-stelligen Barcode). Alle 2884 `prepared` + `is_packaged_product:false`. **0 entfernt** (`removed_in_off.json` = `[]`).
- Validierung: `repo_patch/scripts/validate.mjs foods.json` → 2884 Einträge gültig (14 erwartete Warnungen, Alkoholika); `scripts/test-worker.mjs` bestanden.
