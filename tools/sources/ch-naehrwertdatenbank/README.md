# Schweizer Nährwertdatenbank V7.1

Kopie der offiziellen Downloaddatei und der Nutzungsbedingungen. Abruf am **2026-11-01**. Nichts davon wurde per Mail angefragt; beides stammt von den öffentlichen Seiten des BLV.

## Daten

| | |
| --- | --- |
| Datei | `Schweizer_Nahrwertdatenbank_V7.1_Download_2026-11-01.xlsx` |
| URL | https://naehrwertdaten.ch/wp-content/uploads/2026/07/Schweizer_Nahrwertdatenbank.xlsx |
| Verlinkt von | https://naehrwertdaten.ch/de/downloads/ |
| Version | Schweizer Nährwertdatenbank, generische Lebensmittel **V 7.1 (01.07.2026)** (Titelzeile der Datei) |
| Blatt | `Generische Lebensmittel` |

## Nutzungsbedingungen

| Datei | URL |
| --- | --- |
| `Nutzungsbedingungen_Downloads_2026-11-01.html` | https://naehrwertdaten.ch/de/downloads/ |
| `Nutzungsbedingungen_Informationen_2026-11-01.html` | https://naehrwertdaten.ch/de/informationen/ |
| `Nutzungsbedingungen_Rechtliches_2026-11-01.html` | https://naehrwertdaten.ch/de/rechtliches/ |

Die Download- und die Informationsseite (Stand des Abrufs 2026-11-01) sagen: Das Herunterladen ist kostenlos. Die Daten dürfen unter Angabe eines Quellenvermerks auch kommerziell genutzt werden, zum Beispiel in einer Ernährungstagebuch-App, und für wissenschaftliche Zwecke. Herausgeber ist das Bundesamt für Lebensmittelsicherheit und Veterinärwesen (BLV).

Die Seite „Rechtliches“ ist der allgemeine Haftungs- und Urheberhinweis der Website (letzte Änderung laut Seite: 27.02.2019). Sie verlangt für die Reproduktion von Website-Elementen die vorherige Zustimmung der Rechtsinhaber. Die Regel für die Nährwertdaten selbst steht auf der Download-Seite: Nutzung mit Quellenvermerk, auch kommerziell.

## Abgleich am 2026-11-01

Die fünf Einträge in `data/foods.json` mit `source_id` `CH 7.1:{Code}` wurden gegen diese Datei geprüft. In der Datenbank ist `carbs` = verfügbare Kohlenhydrate + Nahrungsfasern, auf 0,1 g gerundet; `kcal` ist der veröffentlichte ganzzahlige Wert. Protein, Fett, Ballaststoffe und Zucker sind auf 0,1 g gerundet.

| ID | Code | Name in der Quelle | kcal | Protein | Fett | KH verfügbar | Nahrungsfasern | KH gesamt | Zucker | Ergebnis |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `rote-bete-gedaempft` | 1019 | Rande, gedämpft (ohne Zugabe von Salz) | 56 | 2 | 0,4 | 10 | 2,7 | 12,7 | 10 | stimmt |
| `zuckerschoten-gedaempft` | 1012 | Kefe, gedämpft (ohne Zugabe von Salz) | 52 | 4,1 | 0,3 | 6,9 | 2,5 | 9,4 | 2,9 | stimmt |
| `kuerbis-gedaempft` | 1020 | Kürbis, gedämpft (ohne Zugabe von Salz) | 29 | 1,1 | 0,1 | 4,7 | 2,2 | 6,9 | 4 | stimmt |
| `fenchel-gedaempft` | 1008 | Fenchel, gedämpft (ohne Zugabe von Salz) | 22 | 1 | 0,4 | 2,5 | 2,4 | 4,9 | 2,1 | stimmt |
| `zucchini-gedaempft` | 1654 | Zucchetti, gedämpft (ohne Zugabe von Salz) | 18 | 1,3 | 0,3 | 1,9 | 1,1 | 3,0 | 1,9 | stimmt |

Alle fünf Werte in `per100g` stimmen mit der heruntergeladenen Datei überein. Der `source`-Text dieser Einträge lautet jetzt: `Quelle: Schweizer Nährwertdatenbank V7.1, BLV (naehrwertdaten.ch), ID {Code}; KH umgerechnet (inkl. Nahrungsfasern), gerundet`.
