# Build-Notizen: Gerichte-Datenbank (türkisch + deutsch)

**Alle Werte sind Schätzungen (`quality: "estimate"`), keine Laborwerte.** Abweichungen von ±10–25 % gegenüber echten Gerichten sind normal (Rezept, Fettmenge, Portionsgröße).

## Methode
- Pro Gericht ein typisches Hausrezept für **eine Portion** (Zutaten in g, roh bzw. Zutatenzustand).
- Nährwerte werden **programmatisch** aus einer Zutaten-Referenztabelle (`ingredients.json`, ca. 250 Zutaten, pro 100 g, USDA/BLS-ähnliche Näherungswerte) berechnet – nicht von Hand geschätzt.
- **Garfaktor** (Gewicht gegart / roh, 0,5–1,05) bestimmt das Portionsgewicht (auf 5 g gerundet). `per100g` = Summe der Zutatenwerte / Portionsgewicht × 100.
- Beim Kochen aufgenommenes Wasser (Reis, Nudeln, Eintöpfe) steht explizit als Zutat (`wasser`, `bruehe`); bei Frittiertem nur das aufgenommene Öl.
- Kaffee/Tee sind vereinfacht über Wasser-/Teeeintrag (≈ 0 kcal) abgebildet.

## Plausibilitätsprüfungen (`build.py`, Exit 1 bei Fehlern)
- unbekannte Zutat, doppelte ID/Name, Garfaktor außerhalb 0,5–1,05 → Fehler
- kcal ≈ 4·Eiweiß + 4·KH + 9·Fett (±15 %, min. ±12 kcal), Eiweiß+KH+Fett ≤ 100 g, kcal 0–950, Ballaststoffe ≤ KH
- **Alkohol-Ausnahme:** Einträge mit Wein/Bier (Glühwein, Bier, Weinschorle, Bowle, Federweißer …) liegen bewusst über der Makro-Schätzung (Alkohol ≈ 7 kcal/g); geprüft wird nur, dass kcal nicht darunter liegen. Der Repo-Validator (`scripts/validate.mjs`) behandelt kcal über der Makro-Schätzung bei diesen Zutaten (Bier, Weißwein, Rotwein) nicht als Fehler und gibt dafür keine Warnung aus.
- Zusätzlich: Repo-Validator `scripts/validate.mjs` → 1235 gültig.

## Ablage im Repo
- Fertige Datenbank: `data/foods.json` (diese Datei lädt die API).
- Generator und Quellen liegen in diesem Verzeichnis (`tools/dishes/`).
- `python3 build.py` schreibt `foods.json`, `ingredients.json` und `build_report.txt` hierher. Die neue `foods.json` danach nach `data/foods.json` kopieren. `build_report.txt` und `__pycache__/` nicht committen.

## Felder
`id, name, type:"dish", barcode:null, synonyms, cuisine (tr|de), category, per100g{kcal,protein,carbs,fat,fiber}, portion{label,grams}, ingredients[{name,grams}], quality:"estimate", source:"calculated from typical recipe and approximate reference values"`

## Einschränkungen
- Regionale Varianten und Familienrezepte unterscheiden sich stark; hier jeweils ein verbreitetes Standardrezept.
- Unsichere/seltene Gerichte (Zutaten teils grob angenähert): Murtuğa, Kavut, Haşıl, Meftune, Sembusek, Irok, Herise, Kibbeh Mardin, Pehlivan/Saray Kebabı, Çibörek, Kömbe Köfte, Pestil, Cezerye, Keşkül, Pişmaniye, Menengiç-/Dibek-Kaffee, Malzbier, Federweißer.
- Teller-Kombinationen (z. B. „Schnitzel mit Pommes“, „Rouladen mit Rotkohl und Klößen“) sind ganze Mahlzeiten, keine Einzelkomponenten.
- Quelle der Rezepte: allgemeines Küchenwissen, keine Hersteller-/Labordaten; Stück-/Portionsgrößen sind Richtwerte.

## Neu erzeugen
`python3 build.py` → `foods.json`, `ingredients.json`, `build_report.txt` (Rezepte in `batches/*.py`, Zutaten in `ingredients_src.txt`).
