// Liest data/foods.app.json (Format A4) und gibt normale Objekte zurück:
// {id, name, names{de,en,tr}, per100g{kcal,protein,carbs,fat,fiber}, type, cuisine, aliases, synonyms} (+ prepared/state für die Suche)
export function decode(rows) {
  if (!Array.isArray(rows)) rows = rows.d; // ganze Datei {v, f, d} oder nur d
  return rows.map(([id, de, en, tr, kcal, protein, carbs, fat, fiber, art, cuisine, x = {}]) => {
    const enN = en === 0 ? de : en, trN = tr === 0 ? de : tr === 1 ? enN : tr;
    const f = { id, name: x.o === 1 ? enN : x.o === 2 ? trN : x.o || de, names: { de, en: enN, tr: trN },
      per100g: { kcal, protein, carbs, fat, fiber }, type: art === 2 ? 'dish' : 'item', cuisine,
      aliases: x.a || {}, synonyms: x.s || [] };
    if (art <= 1) f.prepared = 'base_ingredient';
    if (art === 0) f.state = 'raw';
    return f;
  });
}
