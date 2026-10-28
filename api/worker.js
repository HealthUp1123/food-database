// Cloudflare Worker: JSON-Such-API für die Lebensmittel-Datenbank.
// Endpunkte: GET /search?q=&limit=  |  GET /barcode/{ean}  |  GET /health
import foods from '../data/foods.json' with { type: 'json' };
import { buildIndex, search, findByBarcode, isValidEan } from '../src/search.mjs';

const CORS = {
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Methods': 'GET, OPTIONS',
  'Access-Control-Allow-Headers': 'Content-Type',
  'Access-Control-Max-Age': '86400',
};

function json(body, status = 200, extra = {}) {
  return new Response(JSON.stringify(body), {
    status,
    headers: { 'Content-Type': 'application/json; charset=utf-8', ...CORS, ...extra },
  });
}

/** Erzeugt einen fetch-Handler für beliebige Daten (so testbar ohne Cloudflare). */
export function createHandler(data) {
  const index = buildIndex(data);
  return async function handle(request) {
    if (request.method === 'OPTIONS') return new Response(null, { status: 204, headers: CORS });
    if (request.method !== 'GET') return json({ error: 'Methode nicht erlaubt' }, 405);

    const url = new URL(request.url);
    const path = url.pathname.replace(/\/+$/, '') || '/';
    const cache = { 'Cache-Control': 'public, max-age=300' };

    if (path === '/health') return json({ status: 'ok', count: data.length });

    if (path === '/search') {
      const q = (url.searchParams.get('q') || '').trim();
      if (!q) return json({ error: 'Parameter q fehlt' }, 400);
      if (q.length > 100) return json({ error: 'q ist zu lang (max. 100 Zeichen)' }, 400);
      const limit = Math.max(1, Math.min(parseInt(url.searchParams.get('limit') || '10', 10) || 10, 50));
      const results = search(index, q, limit);
      return json({ query: q, count: results.length, results }, 200, cache);
    }

    const m = path.match(/^\/barcode\/(\d+)$/);
    if (m) {
      const ean = m[1];
      if (!isValidEan(ean)) return json({ error: 'Ungültiger Barcode (EAN-8/EAN-13 mit korrekter Prüfziffer erwartet)' }, 400);
      const hit = findByBarcode(data, ean);
      return hit ? json(hit, 200, cache) : json({ error: 'Barcode nicht gefunden' }, 404);
    }

    return json({ error: 'Nicht gefunden', endpoints: ['/search?q=&limit=', '/barcode/{ean}', '/health'] }, 404);
  };
}

const handle = createHandler(foods);

export default {
  fetch(request) {
    return handle(request);
  },
};
