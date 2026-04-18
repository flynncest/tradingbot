const WORKFLOWS = {
  pre_market:    'pre_market.yml',
  market_open:   'market_open.yml',
  midday:        'midday.yml',
  end_of_day:    'end_of_day.yml',
  weekly_review: 'weekly_review.yml',
};

export default async function handler(req, res) {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
  if (req.method === 'OPTIONS') return res.status(200).end();
  if (req.method !== 'POST') return res.status(405).end();

  const { routine } = req.body || {};
  const wf = WORKFLOWS[routine];
  if (!wf) return res.json({ ok: false, error: 'Unknown routine' });

  try {
    const r = await fetch(
      `https://api.github.com/repos/flynncest/tradingbot/actions/workflows/${wf}/dispatches`,
      {
        method: 'POST',
        headers: {
          Authorization: `Bearer ${process.env.GITHUB_TOKEN}`,
          Accept: 'application/vnd.github+json',
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ ref: 'main' }),
      }
    );
    res.json({ ok: r.ok, status: r.status });
  } catch (e) {
    res.json({ ok: false, error: e.message });
  }
}
