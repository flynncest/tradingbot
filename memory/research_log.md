# Research Log

## Date: 2026-04-21 (Tuesday) — Pre-market plan

## ⚠️ CRITICAL OPS STATE — UNRESOLVED FROM MONDAY
- **Position book is STILL UNKNOWN** going into today's open. Per strategy.md Operational Guardrails: "The FIRST action next session is to reconcile holdings before any new entries or exits. Never layer new trades on top of an unknown book."
- **MANDATORY before any order today:** run `get_account()` health check. If auth still fails, this is a P0 incident — do NOT trade. Mark Day 2 of ops incident.
- Assume zero positions only if reconciliation confirms it. Until then, everything below is a PLAN, not an order list.

## Market Regime — RISK-ON holding, geopolitical overlay persists
Pre-market snapshots (vs Mon 4/20 close):
- **SPY 708.72 (-0.11%)** — holding the 708 shelf / above 705 stand-down line. Record-zone digestion, not breakdown.
- **QQQ 646.79 (-0.18%)** — mild soft pre, Nasdaq still near records
- **IWM 277.35 (-0.13%)** — held Mon breakout above $276.50; RS still intact
- **VIX** — data error again (3rd session). Infer elevated from Iran headlines but cannot confirm. If VIX >18 rule triggers, we'd be blind to it — be conservative on sizing.
- **NVDA 202.06 (+0.17%)** — sitting right on the $202.25 pivot
- **IGV 86.30 (-0.33%)** — already cleared $85.15 reclaim (ran Mon), now extended; chase risk
- **ISRG 465.60 (-0.40%)** — reports tonight AMC; sell-side cutting PTs into print

**Headline tape:** "Oil pops, stocks slide on fading peace hopes" (Mon), Strait of Hormuz risk still live. Offset: "Tech rally may only be starting" (Yahoo). AI trade still leadership.

**Regime verdict:** Risk-on intact but NOT confirmed — SPY flat-to-down 2 days in a row at highs. Require volume + price confirmation on every entry. If SPY breaks 705 → STAND DOWN.

## Today's Watchlist

### 1. ⭐ NVDA — PRIMARY, still the cleanest setup
- **Pre:** 202.06 (+0.17%) — sitting on the pivot
- **Catalyst:** AI leadership theme intact; "tech rally may only be starting" narrative. Cerebras competitive noise is a known risk but not a thesis-killer.
- **Setup:** Breakout continuation. Pivot $202.25 unchanged from yesterday.
- **Entry:** Break & hold above $202.25 on 2x avg volume (avg 176M). 50% starter.
- **Stop:** Hard -8% (~$186); trail -5% from high once green. Initial stop $198.50 on intraday failure.
- **Target:** +10% partial (~$222), trail remainder
- **Conviction:** HIGH if volume confirms; LOW if it drifts through without volume (false breakout risk on day-2 of consolidation)

### 2. IWM — SECONDARY, breadth continuation already triggered
- **Pre:** 277.35 — already above Mon pivot $276.50
- **Catalyst:** Small-cap RS confirmed risk-on breadth despite Iran tape
- **Setup:** Pullback-to-pivot entry preferred now that breakout already printed
- **Entry:** $276.50-277.00 retest hold (not a chase above $278). 50% starter.
- **Stop:** -8% hard (~$255); intraday stop below $275
- **Target:** +10% partial (~$303)
- **Conviction:** MEDIUM — small caps most sensitive to any Iran/rate shock

### 3. IGV — DOWNGRADE to WATCH only
- **Pre:** 86.30 — ran past the $85.15 reclaim; no longer a pullback entry
- **Action:** Do NOT chase. Re-add to watch only if it pulls back to $85.00-85.25 on light volume. Historic-best-week extension risk is real.

### 4. ISRG — DO NOT TRADE PRE-EARNINGS
- Reports tonight AMC. Sell-side cutting PTs (Mizuho, BTIG, Evercore) into print — setup is asymmetric to the downside on guidance.
- **Plan:** Wed 4/22 — only enter if gap +5% on volume, then pulls back and reclaims gap level. No pre-print holds (strategy rule).

### 5. XLE — WATCH
- Oil popped Mon on Iran. Still no basing structure. Wait.

## High-Conviction Focus (1-2 best)
1. **NVDA >$202.25 with volume** — the one to act on if regime confirms
2. **IWM pullback to $276.50-277.00** — secondary, patient entry

## Key Risks / Events This Week
- **Iran / Strait of Hormuz escalation** — primary tape risk; SPY 705 is the line
- **ISRG earnings** tonight AMC (not a trade, but sentiment marker for medtech)
- **TSLA earnings** this week — megacap tech sentiment read
- **Q1 earnings peak** — single-stock gap risk high
- **VIX data broken** — flying without that instrument; reduce size if in doubt
- **Ops risk: Day 2 of potential auth failure** — reconcile FIRST

## Today's Rules of Engagement
- **Auth health check before ANY order** (strategy guardrail)
- **Reconcile positions BEFORE any new entry** (strategy guardrail)
- Max 2 concurrent entries
- 50% starter size on all entries; add on confirmation only
- If SPY breaks 705 → STAND DOWN
- No pre-earnings holds (ISRG tonight, TSLA later this week)
- Given VIX unknown, default to conservative sizing (treat as if VIX >18: half sizing)

## Process Notes
- Two consecutive flat-to-soft sessions at highs = coiled, not broken. Breakout today would be on day-3 base — typically higher-quality than day-1.
- NVDA pivot unchanged means yesterday's missed opportunity is still actionable today. Good.
- IGV opportunity was forfeited by the auth outage — lesson logged, move on.


## 2026-04-21 — Midday Observation
- Unable to observe market regime via positions today: Alpaca API returned unauthorized on all read endpoints.
- No live data captured. Resume observations once credentials are restored.
