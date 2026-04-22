# Research Log

## Date: 2026-04-22 (Wednesday) — Pre-market plan

## ⚠️ OPS STATE — Day 3 gate
- Mon 4/20 + Tue 4/21: Alpaca `unauthorized` on all account/position/order endpoints, both days. Public market-data endpoints work — fault is isolated to credentials.
- **Per strategy guardrail (2026-04-21 update):** >1 consecutive blocked trading day = **mandatory credential rotation before continuing.** Do NOT retry `get_account` today until out-of-loop action (rotate keys / support ticket / verify in broker UI) has occurred.
- **Trading posture today:** analysis only. No orders may be placed until (a) credentials rotated, (b) reconciliation of positions completed as FIRST action, (c) daily P&L and buying-power verifiable.
- Everything below is a PLAN — it becomes an order list only after the ops gate clears.

## Market Regime — RISK-OFF tilt, breakout thesis broken
Pre-market snapshots:
- **SPY 704.08 (-0.41%)** — **BROKE the 705 stand-down line from yesterday's plan.** Two-day drawdown deepening; SPY now at lowest print since the run. Momentum rolling from "digestion at highs" to "active pullback."
- **QQQ 644.33 (-0.49%)** — leading the downside; tech no longer leadership today.
- **IWM 274.51 (-0.64%)** — **breakout FAILED.** Below Mon pivot $276.50 and below yesterday's $275 intraday stop. Small-cap RS thesis invalidated for now.
- **VIXY 28.91 (+1.26%)** — vol bid, consistent with risk-off. (VIX direct still unreadable; using VIXY as proxy.)
- **NVDA 199.88 (-0.41%)** — **below the $202.25 breakout pivot** and sitting on the $200 round number. Breakout plan is off; this is now a test-of-support name.
- **IGV 86.68 (-1.07%)** — pulling back but not yet at the $85.00-85.25 re-entry zone.
- **ISRG 451.29 (-0.23%)** — reported Q1 beat, raised 2026 procedure growth outlook. Odd: positive print but stock flat-to-down pre. Need to watch open.

**Headline tape:** AI earnings setup dominates (NVDA/AMD/AVGO reports ahead). Iran talks "second round" — less escalation-driven than Monday. Main driver today is likely rotation/profit-taking at highs and pre-earnings positioning.

**Regime verdict:** RISK-OFF PULLBACK. SPY below the stand-down line is the decisive data point. Yesterday's breakout setups (NVDA, IWM) have all failed or unwound. Do not force longs into a broken tape. If SPY cannot reclaim 705 early, bias is bounce-fades, not breakout-buys.

## Today's Watchlist — reduced, defensive posture

### 1. ⭐ ISRG — POST-EARNINGS REVERSAL (highest conviction if it sets up)
- **Pre:** 451.29 (-0.23%). Q1 revenue +23%, procedure growth +17%, **raised full-year procedure growth guidance.**
- **Catalyst:** Clean fundamental beat + guidance raise into a tape that had gone negative pre-print (sell-side cut PTs Mon). Classic "positioned short, print is fine" reversal setup.
- **Setup:** Gap-and-go reclaim OR gap-fade-then-reclaim. The strategy rule says only enter if "gap +5% on volume, then pulls back and reclaims gap level." Currently no gap — so the classic rule doesn't trigger. Alternative: **reclaim of $455 on volume** (previous consolidation shelf) would signal institutional buying post-beat.
- **Entry:** Above $455 on 2x volume, after first 30 minutes. 50% starter.
- **Stop:** $444 (below pre-earnings low); ~-2.4% risk.
- **Target:** $475 (gap-fill to prior range high); +4.4% = ~1.8R. Take partial at +10% if it extends.
- **Conviction:** MEDIUM-HIGH on the thesis, but needs price confirmation — a positive print that CAN'T rally is a red flag, not a bargain.

### 2. SPY/QQQ reclaim — tape confirmation trade
- **Pre:** SPY 704.08, QQQ 644.33
- **Catalyst:** If SPY reclaims 705 early and holds, the pullback may be a 1-day flush.
- **Setup:** Long SPY above 705.50 with a tight stop at 703.50 (-0.3%). Tactical scalp only.
- **Entry:** SPY reclaim and hold of $705.50 in first hour, VIXY rolling over.
- **Stop:** $703.50.
- **Target:** $708.50 (retest Mon highs). ~1.5R scalp.
- **Conviction:** LOW-MEDIUM — only take if tape actually turns. Skip if SPY prints below 703 at open.

### 3. NVDA — DOWNGRADE to support-watch
- **Pre:** 199.88. Breakout thesis DEAD — no longer above $202.25.
- **New frame:** watch the $198-200 zone as support. Only interesting if it holds AND reclaims $202.25 with volume later this week. Not a Wednesday trade.
- **Action:** WATCH ONLY. No entry.

### 4. IWM — OFF the list
- Breakout failed. $276.50 pivot broken to the downside. Remove from watchlist until it reclaims 276.50 or builds a new base.

### 5. IGV — WATCH re-entry zone
- Wait for $85.00-85.25 pullback to light volume. Not there yet ($86.68). No action today unless it flushes.

### 6. TSLA — NO-TRADE (pre-earnings)
- Reports this week. Strategy rule: no pre-earnings holds. Skip.

## High-Conviction Focus (1-2 best)
1. **ISRG reclaim of $455** — post-earnings positive-surprise reversal is the cleanest asymmetric setup in a risk-off tape. Defined risk, clear trigger.
2. **SPY 705 reclaim scalp** — only as confirmation of regime repair. Small size, tactical.

## Key Risks / Events This Week
- **SPY below 705** — this is now the actual regime tell, not a hypothetical. If SPY stays sub-705, defer all longs.
- **TSLA earnings this week** — post-close single-stock gap risk.
- **NVDA/AMD/AVGO earnings ahead** — semis could gap either way; NVDA sitting on $200 support is precarious.
- **Iran "second round" talks** — headline risk remains bidirectional.
- **VIX data still broken (4th session)** — using VIXY as proxy; it's +1.26% pre, that's an alert.
- **Ops risk: credentials unresolved for 48h** — no trades until rotation completed.

## Today's Rules of Engagement
- **HARD GATE: no orders until credential rotation confirmed out-of-loop** (strategy guardrail).
- **Reconcile positions BEFORE any new entry** once auth restored.
- If SPY stays below 705 all session → **STAND DOWN on all longs.** This is the pre-written rule from yesterday and it has now triggered.
- Max 1 concurrent entry today (not 2) — regime is weaker than yesterday.
- 50% starter on any entry; no adds unless SPY reclaims and holds 706.
- VIXY > 29.50 intraday = size cut in half again (proxy for VIX spike).
- No pre-earnings holds (TSLA).

## Process Notes
- Yesterday's primary setup (NVDA >$202.25) never triggered and has now been invalidated by the pullback. No chase.
- Yesterday's secondary (IWM >$276.50) triggered intraday and failed — confirming the regime softened. Good that guardrails kept us out.
- The auth outage, in hindsight, protected capital from two things: an IWM failed-breakout long, and exposure into today's further weakness. Stand-down continues to be the right call while ops are broken.
- **New setup type logged:** Post-earnings positive-surprise into a risk-off tape (ISRG). Worth tracking as a repeatable pattern — beats during pullbacks tend to create better entries than beats at highs.
