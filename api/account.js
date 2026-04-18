export default async function handler(req, res) {
  res.setHeader('Access-Control-Allow-Origin', '*');
  try {
    const base = process.env.ALPACA_PAPER === 'false'
      ? 'https://api.alpaca.markets'
      : 'https://paper-api.alpaca.markets';
    const r = await fetch(`${base}/v2/account`, {
      headers: {
        'APCA-API-KEY-ID': process.env.ALPACA_API_KEY || '',
        'APCA-API-SECRET-KEY': process.env.ALPACA_SECRET_KEY || '',
      },
    });
    const d = await r.json();
    if (!r.ok) return res.json({ ok: false, error: d.message || 'Alpaca error' });
    res.json({
      ok: true,
      portfolio_value: d.portfolio_value,
      equity: d.equity,
      cash: d.cash,
      buying_power: d.buying_power,
      daytrade_count: d.daytrade_count,
    });
  } catch (e) {
    res.json({ ok: false, error: e.message });
  }
}
