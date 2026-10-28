# food-database

Eigene Lebensmittel-Datenbank für einen Kalorientracker: Artikel und Gerichte mit Kalorien, Protein, Kohlenhydraten, Fett und Ballaststoffen, Name und (falls vorhanden) Barcode – plus eine kostenlose Such-API, die du als Quelle in das Suchfeld deiner App einbauen kannst.

> ⚠️ **BEISPIELDATEN (EXAMPLE DATA)**
> Alle Einträge in `data/foods.json` sind aktuell **Platzhalter** mit plausiblen, aber **nicht verifizierten** Werten und tragen das Flag `"_example": true`. Die Barcodes beginnen mit `2` (Bereich für interne Nutzung) und gehören **nicht** zu echten Produkten. Bitte nicht als Nährwertangaben verwenden. Im nächsten Schritt ersetzen wir sie nach und nach durch echte, geprüfte Einträge (siehe [Roadmap](#roadmap)).

## Inhalt

```
data/foods.json          Die Datenbank (JSON-Array)
src/search.mjs           Gemeinsames Such-Modul (API + lokale CLI)
api/worker.js            Cloudflare Worker (Such-API)
api/wrangler.toml        Worker-Konfiguration
scripts/validate.mjs     Datenprüfung (ohne Abhängigkeiten)
scripts/search-local.mjs Lokale Suche per Kommandozeile
scripts/test-worker.mjs  Schnelltest des API-Handlers
.github/workflows/validate.yml  Prüfung bei jedem Push und Pull Request
```

## Datenformat

`data/foods.json` ist ein Array. Ein Eintrag:

```json
{
  "id": "apfel",
  "name": "Apfel",
  "type": "item",
  "barcode": "2000000000015",
  "synonyms": ["Äpfel", "Apfel roh", "Tafelapfel"],
  "per100g": { "kcal": 52, "protein": 0.3, "carbs": 14, "fat": 0.2, "fiber": 2.4 },
  "portion": { "label": "1 mittelgroßer Apfel", "grams": 180 },
  "_example": true
}
```

| Feld | Pflicht | Beschreibung |
| --- | --- | --- |
| `id` | ja | Eindeutig, klein, mit Bindestrichen (`reis-gekocht`). Nicht mehr ändern, wenn die App sie speichert. |
| `name` | ja | Deutscher Anzeigename. |
| `type` | ja | `"item"` (Artikel/Zutat/Produkt) oder `"dish"` (Gericht). |
| `barcode` | ja | EAN-8/EAN-13 als **String** (führende Nullen!) oder `null`. Prüfziffer muss stimmen, eindeutig. |
| `synonyms` | ja | Alternative Namen/Schreibweisen (darf leer sein: `[]`). |
| `per100g` | ja | `kcal` (0–950), `protein`, `carbs`, `fat`, `fiber` (je 0–100 g pro 100 g). Protein + Kohlenhydrate + Fett ≤ 100 g. |
| `portion` | nein | Typische Portion: `label` (Text) und `grams` (> 0). Die App rechnet damit von 100 g auf die Portion um. |
| `_example` | nein | `true` = Platzhalter. Bei echten, geprüften Einträgen weglassen. |

Gerichte (`dish`) werden ebenfalls pro 100 g angegeben; die `portion` gibt die übliche Tellergröße an.

## Neue Einträge hinzufügen

1. Eintrag in `data/foods.json` ergänzen (am besten einen bestehenden kopieren).
2. Werte aus einer verlässlichen Quelle nehmen (Verpackung/Hersteller oder eine offizielle Nährwertdatenbank) und die Quelle im Commit vermerken. Dann `_example` entfernen.
3. Lokal prüfen: `node scripts/validate.mjs`
4. Committen und pushen. Die GitHub Action prüft automatisch ebenfalls.

## Validierung

```bash
node scripts/validate.mjs
```

Prüft Pflichtfelder, Typen, Wertebereiche (kcal 0–950, Makros 0–100 g, Protein + KH + Fett ≤ 100 g), eindeutige `id`s, eindeutige Barcodes und die EAN-Prüfziffer. Bei Fehlern gibt es Exit-Code `1`. Zusätzlich gibt es **Warnungen** (z. B. wenn die kcal stark von den Makros abweichen). Dafür braucht es nur Node ≥ 20, keine Installation. Die GitHub Action `.github/workflows/validate.yml` läuft bei jedem Push und Pull Request.

## Lokale Suche (zum Testen)

```bash
node scripts/search-local.mjs apfel
node scripts/search-local.mjs aepfel          # ae = ä
node scripts/search-local.mjs apfl            # Tippfehler
node scripts/search-local.mjs hafer --limit 3 --json
node scripts/search-local.mjs --barcode 2000000000015
node scripts/test-worker.mjs                  # testet den API-Handler
```

### So funktioniert die Suche

- Groß/Kleinschreibung und Umlaute sind egal: `Äpfel`, `aepfel`, `apfel` finden dasselbe (`ä`/`ae` → `a`, `ö`/`oe` → `o`, `ü`/`ue` → `u`, `ß` → `ss`).
- Reihenfolge der Treffer: exakt → Wortanfang (Präfix) → Teilstring → Tippfehler (Levenshtein-Distanz 1 bei 3–5 Zeichen, 2 ab 6 Zeichen; unter 3 Zeichen keine Fehlertoleranz).
- Gesucht wird in `name` und `synonyms`. Treffer im Namen stehen vor Treffern über Synonyme.
- Mehrere Wörter: Alle Wörter müssen passen.

## API

Die API ist ein Cloudflare Worker (kostenloser Plan reicht), liefert JSON und erlaubt CORS (`Access-Control-Allow-Origin: *`), kann also direkt aus Web-Apps aufgerufen werden. `BASE` ist die URL nach dem Deploy.

```bash
BASE="https://food-database-api.<dein-account>.workers.dev"
```

| Endpunkt | Beschreibung |
| --- | --- |
| `GET /search?q=<text>&limit=<n>` | Suche. `limit` 1–50, Standard 10. |
| `GET /barcode/{ean}` | Eintrag zu einem EAN-8/EAN-13. 400 bei ungültiger Prüfziffer, 404 wenn unbekannt. |
| `GET /health` | Status und Anzahl der Einträge. |

```bash
curl "$BASE/health"
# {"status":"ok","count":18}

curl "$BASE/search?q=aepfel&limit=5"
# {"query":"aepfel","count":1,"results":[{"id":"apfel","name":"Apfel", ... }]}

curl "$BASE/barcode/2000000000015"
# {"id":"apfel","name":"Apfel","type":"item","barcode":"2000000000015", ...}
```

## Deployment (Cloudflare Workers)

1. Kostenloses Konto auf [cloudflare.com](https://dash.cloudflare.com/sign-up) anlegen.
2. Repo klonen und Node ≥ 20 installieren.
3. Optional lokal ausprobieren: `cd api && npx wrangler dev` (läuft dann auf `http://localhost:8787`).
4. Einloggen: `cd api && npx wrangler login`
5. Deployen: `cd api && npx wrangler deploy`
6. Wrangler zeigt die URL an (`https://food-database-api.<account>.workers.dev`). Mit `curl .../health` prüfen.
7. Nach jeder Datenänderung erneut `npx wrangler deploy` ausführen – die Daten werden beim Deploy in den Worker eingebunden. (Automatisches Deployment per GitHub Action ist ein Punkt der Roadmap.)

Hinweis: Der kostenlose Plan hat ein Tageslimit an Anfragen. Cache Treffer deshalb in der App. Die API sendet bereits `Cache-Control: public, max-age=300`.

### Optional: statisches Fallback über GitHub Pages

Wenn du keine API betreiben willst, kannst du `data/foods.json` auch über GitHub Pages (Repo → Settings → Pages → Branch `main`) ausliefern, z. B. `https://<user>.github.io/food-database/data/foods.json`. Die App lädt die Datei dann einmal, cached sie und sucht lokal. Dann kannst du `src/search.mjs` direkt in der App wiederverwenden. Das ist bei wenigen tausend Einträgen sinnvoll; für sehr große Datenbanken ist die API besser.

## Einbau in die App: Suchfeld mit Live-Suche (Debounce)

```ts
const API = "https://food-database-api.<dein-account>.workers.dev";

type Food = {
  id: string; name: string; type: "item" | "dish"; barcode: string | null;
  synonyms: string[];
  per100g: { kcal: number; protein: number; carbs: number; fat: number; fiber: number };
  portion?: { label: string; grams: number };
};

let timer: ReturnType<typeof setTimeout> | undefined;
let controller: AbortController | undefined;

export function onSearchInput(text: string, render: (foods: Food[]) => void) {
  clearTimeout(timer);
  controller?.abort();                       // veraltete Anfrage abbrechen
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
  }, 250);                                   // 250 ms nach der letzten Eingabe
}

export async function lookupBarcode(ean: string): Promise<Food | null> {
  const res = await fetch(`${API}/barcode/${ean}`);
  return res.ok ? ((await res.json()) as Food) : null;
}

// Umrechnung auf eine Menge:
export const nutrientsFor = (f: Food, grams: number) =>
  Object.fromEntries(Object.entries(f.per100g).map(([k, v]) => [k, +(v * grams / 100).toFixed(1)]));
```

Beispiel: `onSearchInput(inputEl.value, renderList)` im `input`-Event des Suchfelds aufrufen.

## Roadmap

- [x] Datenformat festlegen
- [x] Validierung (Skript + GitHub Action)
- [x] Such-API (Cloudflare Worker) mit Umlaut- und Tippfehler-toleranter Suche
- [ ] **Beispieldaten durch echte, geprüfte Einträge ersetzen** (wir füllen die Datenbank zusammen, Quelle pro Eintrag dokumentieren)
- [ ] Echte Barcodes ergänzen (Verpackung scannen/abtippen)
- [ ] API deployen und in die App einbinden
- [ ] Automatisches Deployment per GitHub Action (`wrangler deploy` bei Änderungen an `data/`)
- [ ] Optional: Felder `source` (Quelle) und `updated` (Datum) pro Eintrag
- [ ] Optional: weitere Nährwerte (Zucker, Salz, gesättigte Fette), mehrere Portionen
- [ ] Optional: Datenbank in mehrere Dateien aufteilen, wenn sie groß wird

## Hinweis

Die Einträge sind Platzhalter. Übernimm keine Daten aus fremden Datenbanken, ohne deren Lizenz zu prüfen.
