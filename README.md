# food-database

Eigene Lebensmittel-Datenbank für einen Kalorientracker. Die Daten liegen als JSON im Repo und werden später über eine Such-API in das Suchfeld der App eingebunden.

## Datenformat

Jeder Eintrag in `data/foods.json`:

```json
{
  "id": "apfel-roh",
  "name": "Apfel, roh",
  "type": "item",
  "barcode": null,
  "synonyms": ["Äpfel"],
  "per100g": {
    "kcal": 0,
    "protein": 0,
    "carbs": 0,
    "fat": 0,
    "fiber": 0
  },
  "portion": { "label": "1 Stück", "grams": 0 }
}
```

- `type`: `item` (Artikel) oder `dish` (Gericht)
- `barcode`: optional, EAN/GTIN mit gültiger Prüfziffer
- Nährwerte in Gramm (Kalorien in kcal), jeweils pro 100 g
- `portion`: optional, vor allem für Gerichte

## Geplante API

- `GET /search?q=apf&limit=20` Textsuche (Groß-/Kleinschreibung, Umlaute, Präfix)
- `GET /barcode/{ean}` Abruf per Barcode

## ToDo

1. Datenformat festlegen (dieses Dokument)
2. `data/foods.json` mit ersten echten, geprüften Einträgen füllen
3. Validierungsskript (Pflichtfelder, eindeutige IDs und Barcodes, Prüfziffer)
4. Such-API bauen und kostenlos hosten
5. API im Suchfeld der App einbinden
6. Datenbank laufend erweitern
