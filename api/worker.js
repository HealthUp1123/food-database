// Cloudflare Worker: JSON-Such-API für die Lebensmittel-Datenbank.
// Endpunkte: GET /search?q=&limit=&lang=  |  GET /item/{id}?lang=  |  GET /item/{id}  |  GET /barcode/{ean}  |  GET /health
import foods from '../data/foods.json' with { type: 'json' };
import { buildIndex, search, findByBarcode, isValidEan, displayName, LANGS, resolveLang } from '../src/search.mjs';

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

/** Listenantworten ohne Zutatenliste; das volle Objekt liegt unter GET /item/{id}. */
export function toListItem(food) {
  if (!food || typeof food !== 'object') return food;
  const { ingredients, ...rest } = food;
  return rest;
}

/** Optional ?lang=xx: ergänzt `display_name` (Name in dieser Sprache, Fallback `name`). */
function withLang(food, lang) {
  return lang ? { ...food, display_name: displayName(food, lang) } : food;
}

/** Erzeugt einen fetch-Handler für beliebige Daten (so testbar ohne Cloudflare). */
export function createHandler(data) {
  const index = buildIndex(data);
  const byId = new Map(data.map((food) => [food.id, food]));
  return async function handle(request) {
    if (request.method === 'OPTIONS') return new Response(null, { status: 204, headers: CORS });
    if (request.method !== 'GET') return json({ error: 'Methode nicht erlaubt' }, 405);

    const url = new URL(request.url);
    const path = url.pathname.replace(/\/+$/, '') || '/';
    const cache = { 'Cache-Control': 'public, max-age=300' };

    if (path === '/health') return json({ status: 'ok', count: data.length, languages: LANGS });

    const langParam = (url.searchParams.get('lang') || '').trim().toLowerCase();
    // Nur de/en/tr; jede andere Sprache (z. B. zh, es, it, "pt-BR") fällt auf Englisch zurück, kein Fehler.
    const lang = resolveLang(langParam);
    const langInfo = lang ? { lang, ...(langParam.split(/[-_]/)[0] !== lang ? { lang_requested: langParam } : {}) } : {};

    if (path === '/search') {
      const q = (url.searchParams.get('q') || '').trim();
      if (!q) return json({ error: 'Parameter q fehlt' }, 400);
      if (q.length > 100) return json({ error: 'q ist zu lang (max. 100 Zeichen)' }, 400);
      const limit = Math.max(1, Math.min(parseInt(url.searchParams.get('limit') || '10', 10) || 10, 50));
      const results = search(index, q, limit, lang).map((f) => withLang(toListItem(f), lang));
      return json({ query: q, ...langInfo, count: results.length, results }, 200, cache);
    }

    const item = path.match(/^\/item\/([a-z0-9]+(?:-[a-z0-9]+)*)$/);
    if (item) {
      const hit = byId.get(item[1]);
      return hit ? json(withLang(hit, lang), 200, cache) : json({ error: 'Eintrag nicht gefunden' }, 404);
    }

    const m = path.match(/^\/barcode\/(\d+)$/);
    if (m) {
      const ean = m[1];
      if (!isValidEan(ean)) return json({ error: 'Ungültiger Barcode (EAN-8/EAN-13 mit korrekter Prüfziffer erwartet)' }, 400);
      const hit = findByBarcode(data, ean);
      return hit ? json(withLang(hit, lang), 200, cache) : json({ error: 'Barcode nicht gefunden' }, 404);
    }

    return json({ error: 'Nicht gefunden', endpoints: ['/search?q=&limit=&lang=', '/item/{id}', '/barcode/{ean}', '/health'] }, 404);
  };
}

const handle = createHandler(foods);

export default {
  fetch(request) {
    return handle(request);
  },
};
