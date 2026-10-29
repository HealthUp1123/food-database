#!/usr/bin/env node
// Schneller Test des Worker-Handlers ohne Cloudflare (Node >= 20.10).
import assert from 'node:assert/strict';
import worker from '../api/worker.js';

const get = async (path, init) => {
  const res = await worker.fetch(new Request('https://example.test' + path, init));
  return { res, body: res.status === 204 ? null : await res.json() };
};

let t = await get('/health');
assert.equal(t.res.status, 200);
assert.equal(t.body.status, 'ok');
assert.equal(t.body.count, 4540);

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

console.log('✓ Worker-Tests bestanden');
