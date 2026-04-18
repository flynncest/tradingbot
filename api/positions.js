export default async function handler(req, res) {
  res.setHeader('Access-Control-Allow-Origin', '*');
  try {
    const base = process.env.ALPACA_PAPER === 'false'
      ? 'https://api.alpaca.markets'
      : 'https://paper-api.alpaca.markets';
    const r = await fetch(`${base}/v2/positions`, {
      headers: {
        'APCA-API-KEY-ID': process.env.ALPACA_API_KEY,
        'APCA-API-SECRET-KEY': process.env.ALPACA_SECRET_KEY,
      },
    });
    const data = await r.json();
    const positions = Array.isArray(data) ? data.map(p => ({
      symbol: p.symbol,
      qty: p.qty,
      avg_entry_price: p.avg_entry_price,
      current_price: p.current_price,
      market_value: p.market_value,
      unrealized_pl: p.unrealized_pl,
      unrealized_plpc: (parseFloat(p.unrealized_plpc) * 100).toFixed(2) + '%',
    })) : [];
    res.json({ ok: true, positions });
  } catch (e) {
    res.json({ ok: false, positions: [], error: e.message });
  }
}
