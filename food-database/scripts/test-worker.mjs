#!/usr/bin/env node
// Schneller Test des Worker-Handlers ohne Cloudflare (Node >= 20.10).
import assert from 'node:assert/strict';
import worker from '../api/worker.js';

const get = async (path, init) => {
  const res = await worker.fetch(new Request('https://example.test' + path, init));
  return { res, body: res.status === 204 ? null : await res.json() };
};

let t = await get('/health');
assert.equal(t.res.status, 200); assert.equal(t.body.status, 'ok'); assert.ok(t.body.count >= 18);

t = await get('/search?q=apfel&limit=3');
assert.equal(t.res.status, 200); assert.equal(t.body.results[0].id, 'apfel');
assert.ok(t.body.results.length <= 3);
assert.equal(t.res.headers.get('access-control-allow-origin'), '*');

t = await get('/search?q=aepfel'); assert.equal(t.body.results[0].id, 'apfel');
t = await get('/search?q=apfl'); assert.equal(t.body.results[0].id, 'apfel');
t = await get('/search?q=%C3%84PFEL'); assert.equal(t.body.results[0].id, 'apfel');
t = await get('/search'); assert.equal(t.res.status, 400);

t = await get('/barcode/2000000000015'); assert.equal(t.res.status, 200); assert.equal(t.body.id, 'apfel');
t = await get('/barcode/2000000000014'); assert.equal(t.res.status, 400);
t = await get('/barcode/4006381333931'); assert.equal(t.res.status, 404);

t = await get('/search?q=x', { method: 'OPTIONS' }); assert.equal(t.res.status, 204);
t = await get('/nix'); assert.equal(t.res.status, 404);
t = await get('/search?q=x', { method: 'POST' }); assert.equal(t.res.status, 405);

console.log('✓ Worker-Tests bestanden');
