# Erweiterung Welle 4 (`build_extension.py`)

Erzeugt die 331 Einträge von Welle 4 (Zubereitungen, deutsche und türkische Grundprodukte, Imbiss, asiatische Küche, Getränke) aus freien amtlichen Nährwertdatenbanken und hängt sie an `data/foods.json` an.

```bash
python3 tools/extension/build_extension.py --src <all.pkl> [--write] [--report build_report.json]
```

* `--src`: Pickle mit den normalisierten Quelltabellen (BLS 4.0, Ciqual 2025, CoFID 2021, USDA FNDDS 2021–2023). Die Rohdateien sind frei herunterladbar (BLS: DOI 10.25826/Data20251217-134202-0; Ciqual: Zenodo 17550133; CoFID: gov.uk; FNDDS: fdc.nal.usda.gov). Sie liegen nicht im Repo.
* Portionsgewichte kommen aus der FNDDS-Datei `food_portion.csv` (Pfad per Umgebungsvariable `FNDDS_PORTIONS`).
* Ohne `--write` gibt es nur einen Probelauf mit der Zählung je Bereich. `--report` schreibt die neuen IDs, die übersprungenen Datensätze (mit Grund) und die entfernten Aliase als JSON.

## Regeln

* **Spezifikation statt Raten:** Jeder Eintrag ist in `spec_veg.py`, `spec_de.py`, `spec_dishes.py` oder `spec_drinks.py` mit Quellcode, 8 Namen (de en tr fr es pt it zh), Kategorie, Zustand und Aliasen festgelegt.
* **Umrechnung:** Kohlenhydrate = verfügbare KH + Ballaststoffe, damit sie wie bei USDA Gesamt-KH sind. kcal werden wie veröffentlicht als Ganzzahl übernommen, alles andere wird auf 0,1 g gerundet. Alkohol ab 0,05 g kommt in `per100g.alcohol`. Fehlt ein Wert in der Quelle, wird er nur bei eindeutigen Fällen als 0 eingetragen (Ballaststoffe bei ≤ 3 g KH, Protein/Fett bei Getränken) und in `source_missing` vermerkt. Fehlender Zucker wird weggelassen. Andere Lücken führen zum Ausschluss.
* **Schätzungen:** Nur 5 türkische Grundzutaten (`kasar-peyniri`, `pastirma`, `sucuk`, `kaymak`, `yufka-teig`). Sie haben `quality: "estimate"`, `method: "similar_food"`, `derived_from` = Kennung des vergleichbaren Quelldatensatzes und die Begründung in `source`.
* **Keine Duplikate:** Ein Eintrag wird übersprungen, wenn der Quelldatensatz, die `id` oder ein neuer Anzeigename schon im Bestand vorkommt (normalisierter Vergleich mit Namen, `names.*`, Synonymen und Aliasen). `MANUAL_SKIP` deckt inhaltliche Duplikate ab. Ein neuer Alias, der dem Anzeigenamen eines bestehenden Eintrags entspricht, wird entfernt.
* **Keine Marken- oder Fertigprodukte.** Gerichte sind generische Rezeptdatensätze. Bei Imbissgerichten steht die Portionsgröße in `portion` und in `note`.
