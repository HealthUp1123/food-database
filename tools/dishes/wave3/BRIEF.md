# Welle 3: neue typische Gerichte (Ziel gesamt > 1000 neue, 3 Teams)

Projekt: /workspace/dishes2 (lies BUILD_NOTES.md). Bestand: 2884 Gerichte, Liste in /workspace/dishes2/existing_names.txt (Format `cuisine | Name | Synonyme`).

## Deine Aufgabe
1. **Suchen:** Sammle typische, real verbreitete Gerichte/Speisen/Getränke deines Bereichs, die noch NICHT im Bestand sind (Kochbücher, Wikipedia-Listen „List of X dishes", Speisekarten; WebSearch/WebFetch erlaubt, aber zügig – Küchenwissen ist ok). Nur echte Gerichte (zuhause/Restaurant/Imbiss/Bäcker), keine Markenprodukte, keine reinen Zutaten (z.B. „Mehl", „Ketchup"), keine Supermarkt-Fertigprodukte.
2. **Abgleich Bestand:** Normalisiert (klein, ohne Akzente, ä=ae, ı=i, ß=ss) gegen Name UND Synonyme in existing_names.txt prüfen (Python-Skript). Auch Varianten-Duplikate vermeiden (z.B. „Gulaschsuppe" vs. „Gulyásleves" – wenn gleiches Gericht, weglassen; echte regionale Varianten mit anderem Rezept sind ok).
3. **Abgleich Open Food Facts:** Regel des Users: Gerichte (zuhause/Restaurant) und Fertigprodukte sind getrennt. Ein Gericht wird NICHT verworfen, nur weil OFF ein gleichnamiges Fertigprodukt hat (es wird später automatisch per Dump markiert). Verwirf aber alles, was selbst ein abgepacktes Markenprodukt/Supermarktartikel ist. Optional schneller Check: `/workspace/venv/bin/python -c "import duckdb; c=duckdb.connect('/workspace/dishes2/off_dump/off_names.duckdb', read_only=True); print(c.execute('show tables').fetchall())"` (nur read_only!). Die offizielle OFF-Markierung macht der Zusammenbau.
4. **Entscheiden + Rezept:** Für jedes aufgenommene Gericht ein typisches Hausrezept für EINE Portion. Ausgabe: eine Zeile pro Gericht in deine Datei, exakt:
   `cc | Name | Synonym1, Synonym2 | KAT | Garfaktor | Portionslabel | zutat1 g, zutat2 g, ...`
   - cc: Ländercode wie im Bestand (tr, de, it, fr, es, pt, gr, gb, ie, nl, be, at, ch, se, no, dk, fi, is, pl, cz, sk, hu, rs, hr, ba, bg, al, mk, si, ro, ee, lv, lt, ua, ru, cy, mt, lu); weitere nur wenn nötig (ge, am, az, md, by, me, xk, ad, li, mc, sm).
   - Synonyme: 0–4, ggf. deutscher Name/Schreibweise ohne Sonderzeichen; leer erlaubt (dann `|  |`).
   - KAT: einer der Codes aus build.py CATS (S,E,HF,HG,HFi,HV,GZ,GM,KB,KF,DO,T,V,D,G,FR,GT,B,SA,BR,K,RP,HH,SN,SD,WU,BO,PI,MA,KN,NA,FL,EI,PF,PZ,AU,KO,KR …) – lies die vollständige Liste in build.py Zeile 18ff.
   - Garfaktor 0.5–1.05 (gegart/roh); beim Kochen aufgenommenes Wasser als `wasser`/`bruehe`.
   - Zutaten-Keys NUR aus /workspace/dishes2/ingredients.json oder deiner eigenen Datei ingredients_add (siehe unten).
   - Plausibel: kcal ≈ 4·P+4·KH+9·F (±15 %), Portion meist 80–1200 kcal, kcal/100 g ≤ 560 (Ausnahme reine Fettgerichte, begründen), Ballaststoffe ≤ KH. Alkoholika ausgenommen.
5. Neue Zutaten in deine Datei `key|Name (de)|kcal|protein|carbs|fat|fiber` (pro 100 g, Präfix deines Teams), nur wenn wirklich nötig. Vorher prüfen, ob die x1_–x4_-Zutaten (in ingredients_add_1..4.txt) schon passen – die darfst du mitbenutzen.
6. Sanity-Check per Python am Ende: Format (7 Felder), Keys existieren, keine Duplikate untereinander und gegen Bestand, Werte plausibel (Nährwerte aus Zutaten ausrechnen).

Arbeite zügig in Blöcken (je ~50 Zeilen schreiben). Ändere NICHTS außerhalb deiner eigenen Dateien in /workspace/dishes2/wave3/.
