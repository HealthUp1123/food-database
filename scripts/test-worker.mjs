#!/usr/bin/env node
// Schneller Test des Worker-Handlers ohne Cloudflare (Node >= 20.10).
import assert from 'node:assert/strict';
import worker from '../api/worker.js';
import foods from '../data/foods.json' with { type: 'json' };

const get = async (path, init) => {
  const res = await worker.fetch(new Request('https://example.test' + path, init));
  return { res, body: res.status === 204 ? null : await res.json() };
};

let t = await get('/health');
assert.equal(t.res.status, 200);
assert.equal(t.body.status, 'ok');
assert.equal(t.body.count, 5257);

// Karnıyarık: ASCII, Originalschreibweise, ein fehlendes i.
t = await get('/search?q=karniyarik&limit=3');
assert.equal(t.res.status, 200);
assert.equal(t.body.results[0].id, 'karniyarik');
assert.equal(t.body.results[0].name, 'Karnıyarık');
assert.equal(t.body.results[0].cuisine, 'tr');
assert.equal(t.body.results[0].barcode, null);
assert.equal(t.body.results[0].quality, 'estimate');
assert.equal(t.body.results[0].prepared, 'homemade');
assert.equal(t.body.results[0].is_packaged_product, false);
assert.equal(t.body.results[0].per100g.kcal, 104);
assert.equal('ingredients' in t.body.results[0], false);
assert.ok(t.body.results.length <= 3);
assert.equal(t.res.headers.get('access-control-allow-origin'), '*');

t = await get('/search?q=' + encodeURIComponent('Karnıyarık'));
assert.equal(t.body.results[0].id, 'karniyarik');
assert.equal('ingredients' in t.body.results[0], false);

t = await get('/search?q=karniyark');
assert.equal(t.body.results[0].id, 'karniyarik');

// Umlaute weiter falten (ö/oe → o).
t = await get('/search?q=koelsch');
assert.equal(t.body.results[0].id, 'koelsch');
t = await get('/search?q=' + encodeURIComponent('Kölsch'));
assert.equal(t.body.results[0].id, 'koelsch');

t = await get('/search');
assert.equal(t.res.status, 400);

t = await get('/item/karniyarik');
assert.equal(t.res.status, 200);
assert.equal(t.body.id, 'karniyarik');
assert.equal(t.body.barcode, null);
assert.ok(Array.isArray(t.body.ingredients) && t.body.ingredients.length > 0);
assert.equal(t.body.ingredients[0].name, 'Aubergine');
assert.equal(t.body.prepared, 'homemade');
assert.equal(t.body.is_packaged_product, false);
assert.equal(t.res.headers.get('cache-control'), 'public, max-age=300');

t = await get('/item/wiener-schnitzel');
assert.equal(t.res.status, 200);
assert.equal(t.body.is_packaged_product, false);
assert.ok(Array.isArray(t.body.off_similar) && t.body.off_similar.length > 0 && t.body.off_similar.length <= 3);

// Grundzutaten (USDA-Referenzwerte, keine Fertigprodukte).
t = await get('/search?q=tomate&limit=3');
assert.equal(t.res.status, 200);
assert.equal(t.body.results[0].id, 'tomate-roh');
assert.equal(t.body.results[0].type, 'item');
assert.equal(t.body.results[0].prepared, 'base_ingredient');
assert.equal(t.body.results[0].quality, 'reference');
assert.equal('ingredients' in t.body.results[0], false);

t = await get('/search?q=haehnchenbrust%20roh&limit=3');
assert.equal(t.body.results[0].id, 'haehnchenbrust-roh');

t = await get('/item/tomate-roh');
assert.equal(t.res.status, 200);
assert.equal(t.body.name, 'Tomate, roh');
assert.equal(t.body.type, 'item');
assert.equal(t.body.barcode, null);
assert.equal(t.body.is_packaged_product, false);
assert.equal(t.body.note, 'Grundzutat, kein Fertigprodukt');
assert.equal(t.body.unit, 'g');
assert.equal(t.body.state, 'raw');
assert.equal(t.body.category, 'Grundzutat: Gemüse');
assert.equal(t.body.fdc_id, 170457);
assert.ok(t.body.source.startsWith('USDA FoodData Central'));
assert.equal(t.body.per100g.kcal, 18);
assert.equal(t.body.per100g.sugar, 2.6);

// Zubereitungsvarianten der Grundzutaten (gegrillt, getrocknet, Dose, ...).
t = await get('/search?q=tomate%20getrocknet&limit=3');
assert.equal(t.body.results[0].id, 'tomate-getrocknet');
assert.equal(t.body.results[0].prepared, 'base_ingredient');
assert.equal(t.body.results[0].state, 'dried');
t = await get('/item/tomate-getrocknet');
assert.equal(t.body.fdc_id, 168567);
assert.equal(t.body.quality, 'reference');
assert.equal(t.body.note, 'Grundzutat (getrocknet), kein Fertigprodukt');
t = await get('/search?q=haehnchenbrust%20gegrillt&limit=3');
assert.equal(t.body.results[0].id, 'haehnchenbrust-gegrillt');
assert.equal(t.body.results[0].state, 'grilled');
// Geschätzte Zubereitung ohne direkten Datensatz, abgeleitet aus der rohen Grundzutat
t = await get('/search?q=zucchini%20in%20%C3%B6l%20gebraten&limit=3');
assert.equal(t.body.results[0].id, 'zucchini-in-oel-gebraten');
t = await get('/item/zucchini-in-oel-gebraten');
assert.equal(t.body.quality, 'estimate');
assert.equal(t.body.note, 'Grundzutat (zubereitet, geschätzt), kein Fertigprodukt');
assert.equal(t.body.derived_from, 'zucchini-roh');
assert.equal(t.body.barcode, null);
assert.equal(t.body.is_packaged_product, false);
// Direkte Datensätze aus BLS 4.0 / Schweizer / schwedischer Nährwertdatenbank (source_id statt fdc_id)
t = await get('/search?q=zucchini%20gegrillt&limit=3');
assert.equal(t.body.results[0].id, 'zucchini-gegrillt');
assert.equal(t.body.results[0].state, 'grilled');
t = await get('/item/zucchini-gegrillt');
assert.equal(t.body.name, 'Zucchini, gegrillt');
assert.equal(t.body.quality, 'reference');
assert.equal(t.body.source_id, 'BLS 4.0:G582172');
assert.equal(t.body.fdc_id, undefined);
assert.ok(t.body.source.startsWith('Max Rubner-Institut (2025): Bundeslebensmittelschlüssel'));
assert.equal(t.body.per100g.kcal, 46);
assert.equal(t.body.per100g.carbs, 8.4); // 6,0 g verfügbare KH + 2,4 g Ballaststoffe
t = await get('/search?q=tomate%20gegrillt&limit=3');
assert.equal(t.body.results[0].id, 'tomate-gegrillt');
t = await get('/item/tomate-gegrillt');
assert.equal(t.body.quality, 'reference');
assert.equal(t.body.source_id, 'BLS 4.0:G561072');
t = await get('/search?q=rote%20bete%20ged%C3%A4mpft&limit=3');
assert.equal(t.body.results[0].id, 'rote-bete-gedaempft');
t = await get('/item/rote-bete-gedaempft');
assert.equal(t.body.source_id, 'CH 7.1:1019');
t = await get('/search?q=s%C3%BC%C3%9Fkartoffel%20wedges&limit=3');
assert.equal(t.body.results[0].id, 'suesskartoffel-wedges-im-ofen-mit-oel');
t = await get('/item/suesskartoffel-wedges-im-ofen-mit-oel');
assert.equal(t.body.source_id, 'Livsmedelsverket:3771');

// Mehrsprachige Namen (names/aliases, nur de/en/tr): Suche in allen drei Sprachen, akzent- und groß/klein-unabhängig.
t = await get('/item/tomate-roh');
for (const l of ['de', 'en', 'tr']) assert.ok(t.body.names[l], 'names.' + l);
assert.equal(t.body.names.tr, 'Domates, çiğ');
assert.equal(t.body.names.en, 'Tomato, raw');
for (const q of ['domates', 'Tomato', 'TOMATE']) {
  t = await get('/search?q=' + encodeURIComponent(q) + '&limit=3');
  assert.equal(t.body.results[0].id, 'tomate-roh', q);
}
for (const q of ['Zucchini', 'zucchini', 'kabak']) {
  t = await get('/search?q=' + encodeURIComponent(q) + '&limit=3');
  assert.equal(t.body.results[0].id, 'zucchini-roh', q);
}
for (const q of ['salatalık', 'salatalik', 'cucumber', 'Gurke']) {
  t = await get('/search?q=' + encodeURIComponent(q) + '&limit=3');
  assert.equal(t.body.results[0].id, 'gurke-roh', q);
}
for (const q of ['french fries', 'Pommes', 'patates kızartması']) {
  t = await get('/search?q=' + encodeURIComponent(q) + '&limit=3');
  assert.ok(t.body.results.slice(0, 2).some((r) => r.id === 'pommes-frites'), q);
}
t = await get('/search?q=chicken%20breast%20raw&limit=3');
assert.equal(t.body.results[0].id, 'haehnchenbrust-roh');
// Etablierter Gerichtsname bleibt in allen Sprachen gleich.
t = await get('/item/karniyarik');
assert.equal(t.body.names.en, 'Karnıyarık');
assert.equal(t.body.names.de, 'Karnıyarık');
// lang: display_name in der gewünschten Sprache, Fallback name; unbekannte Sprache → 400.
t = await get('/search?q=tomato&limit=3&lang=tr');
assert.equal(t.res.status, 200);
assert.equal(t.body.lang, 'tr');
assert.equal(t.body.results[0].display_name, 'Domates, çiğ');
// Nur de/en/tr: andere Sprachen (zh, es, it, pt-BR …) fallen auf Englisch zurück, kein Fehler.
t = await get('/search?q=domates&limit=3&lang=pt-BR');
assert.equal(t.res.status, 200);
assert.equal(t.body.lang, 'en');
assert.equal(t.body.lang_requested, 'pt-br');
assert.equal(t.body.results[0].display_name, 'Tomato, raw');
t = await get('/item/zucchini-roh?lang=zh');
assert.equal(t.body.display_name, t.body.names.en);
t = await get('/search?q=tomate&limit=1&lang=de-DE');
assert.equal(t.body.lang, 'de');
assert.equal('lang_requested' in t.body, false);
t = await get('/item/zucchini-roh');
assert.equal('display_name' in t.body, false);
t = await get('/search?q=tomate&lang=xx');
assert.equal(t.res.status, 200);
assert.equal(t.body.lang, 'en');
t = await get('/health');
assert.deepEqual(t.body.languages, ['de', 'en', 'tr']);
// Jeder Eintrag hat genau die Namen de/en/tr, keine Portionsliste, keine Allergene, keine Beliebtheit;
// die fünf Kernnährwerte sind immer Zahlen.
for (const f of foods) {
  assert.deepEqual(Object.keys(f.names).sort(), ['de', 'en', 'tr'], f.id);
  assert.ok(Object.keys(f.aliases || {}).every((l) => ['de', 'en', 'tr'].includes(l)), f.id);
  for (const k of ['portions', 'allergens', 'allergens_basis', 'popularity']) assert.equal(k in f, false, `${f.id}: ${k}`);
  for (const k of ['kcal', 'protein', 'carbs', 'fat', 'fiber']) assert.ok(Number.isFinite(f.per100g[k]), `${f.id}: ${k}`);
}

t = await get('/item/gibt-es-nicht');
assert.equal(t.res.status, 404);

// Keine echten Barcodes im Datensatz; null ist gültig. Prüfziffer und 404 bleiben.
t = await get('/barcode/2000000000014');
assert.equal(t.res.status, 400);
t = await get('/barcode/4006381333931');
assert.equal(t.res.status, 404);

t = await get('/search?q=x', { method: 'OPTIONS' });
assert.equal(t.res.status, 204);
t = await get('/nix');
assert.equal(t.res.status, 404);
assert.ok(t.body.endpoints.includes('/item/{id}'));
t = await get('/search?q=x', { method: 'POST' });
assert.equal(t.res.status, 405);

// ---- Welle 5: Suche (Umgangssprache, Tippfehler, Beliebtheit) und neue optionale Felder ----
const top = async (q, lang = 'de') => (await get(`/search?q=${encodeURIComponent(q)}&limit=5&lang=${lang}`)).body.results.map((r) => r.id);
assert.equal((await top('Fritten'))[0], 'pommes-frites');
assert.equal((await top('Kartoffelpuffer'))[0], 'reibekuchen'); // de: Heimatküche zuerst (ohne popularity)
assert.equal((await top('Kartoffelpuffer', 'tr'))[0], 'patates-mucveri');
assert.equal((await top('Patates mücveri', 'tr'))[0], 'patates-mucveri');
assert.ok((await top('Kartoffelpuffer')).includes('patates-mucveri'));
assert.equal((await top('Tomatte'))[0], 'tomate-roh');
assert.equal((await top('Tomaet'))[0], 'tomate-roh'); // Buchstabendreher (Damerau)
assert.equal((await top('domates'))[0], 'tomate-roh');
assert.equal((await top('domates', 'tr'))[0], 'tomate-roh');
assert.equal((await top('Semmel'))[0], 'broetchen');
assert.equal((await top('Topfen'))[0], 'magerquark');
assert.equal((await top('Bulette'))[0], 'frikadellen');
assert.equal((await top('Kartofel'))[0], 'kartoffel-roh');
const { levenshtein } = await import('../src/search.mjs');
assert.equal(levenshtein('tomaet', 'tomate'), 1);
assert.equal(levenshtein('reis', 'ries'), 1);

t = await get('/item/tomate-roh');
assert.equal(t.body.nutrient_basis.salt, 'source');
assert.ok(t.body.per100g.salt >= 0 && t.body.per100g.sat_fat <= t.body.per100g.fat);
t = await get('/item/reis-weiss-roh');
assert.equal(t.body.cooked_id, 'reis-weiss-gekocht');
assert.ok(t.body.yield.factor > 2 && t.body.yield.factor < 3.5 && t.body.yield.from === 'raw' && t.body.yield.to === 'cooked');
t = await get('/item/reis-weiss-gekocht');
assert.equal(t.body.raw_id, 'reis-weiss-roh');
t = await get('/item/reibekuchen');
assert.ok(t.body.portion.grams > 0); // altes Feld portion bleibt (abwärtskompatibel)
t = await get('/search?q=reibekuchen&limit=1');
assert.ok(['portions', 'allergens', 'popularity'].every((k) => !(k in t.body.results[0])));

console.log('✓ Worker-Tests bestanden');
