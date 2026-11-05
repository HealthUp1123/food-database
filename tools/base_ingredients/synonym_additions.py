# Synonyme, die build.py nicht aus den Batches übernimmt.
# Nichts wird entfernt. Kommas kommen in den Suchbegriffen nicht vor.
# Der Abschluss-Builder trägt sie in data/foods.json nach.
# yaprak-sarma-etli steht in reference_overrides.json: assemble_bestand
# lässt die Batch-Synonyme dort liegen und behält die Liste aus foods.json.
ADD = {
    'doner-fleisch': ['Yaprak döner', 'Yaprak doner', 'Sliced-leaf döner'],
    'yaprak-sarma-etli': ['Tokat yaprağı sarma', 'Tokat yapragi sarma'],
}
