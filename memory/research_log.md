# Research Log

## Date: 2026-04-23 (Thursday) — Pre-market plan

## ⚠️ OPS STATE — Day 4 gate (assumed still active until operator confirms rotation)
- Mon 4/20 → Wed 4/22: Alpaca `unauthorized` on all authenticated endpoints for 3 consecutive sessions. Public market data endpoints work fine.
- **Per strategy guardrail:** credential rotation must be confirmed **out-of-loop** before any `get_account` retry or order placement. That confirmation has not been logged in trade_log.md as of yesterday's EOD.
- **Trading posture today:** analysis only until operator confirms keys have been rotated. If rotation has occurred, the FIRST action before any new entry is reconciliation (`get_account` + `get_positions` + `get_open_orders`) — because the position book is still `UNKNOWN` from before the outage.
- **If auth is restored this morning:** the plan below becomes tradeable, but only after reconciliation completes cleanly.

## Market Regime — RISK-ON REPAIR, breakout tape re-emerging
Pre-market snapshots (4/23):
- **SPY 711.21 (+0.10%)** — **reclaimed 705 stand-down line (now +6 pts above it)**, back above the Mon open-range high. Wed's +0.59% rally and this morning's stable print = regime is repaired. 3-day path: -0.31 / -0.75 / +0.59 / now flat-to-green = net positive reclaim.
- **QQQ 655.11 (-0.06%)** — holding yesterday's gains. Tech participating but not leading; broader tape carrying.
- **IWM 276.48 (+0.18%)** — **back AT the original Mon breakout pivot $276.50** after flushing below Tue/Wed. Small-caps reclaiming.
- **VIXY 28.54 (+0.31%)** — vol bid evaporated. News reports **VIX back to ~19** (prior peak was higher during Tue risk-off). Consistent with risk-on.
- **NVDA 202.50 (+0.12%)** — **back ABOVE the $202.25 breakout pivot** from Monday's original plan. The setup that was invalidated on Tue/Wed has re-triggered.
- **ISRG 483.62 (-0.12%)** — **gapped ~+7.6% yesterday** from ~$451 to $484 on Q1 beat + guidance raise. Our $455 reclaim entry would have triggered and hit the $475 target easily. Now EXTENDED — past target, no fresh entry here.
- **IGV 88.74 (+2.65%)** — software strong. Past prior $85-$85.25 re-entry zone; no pullback opportunity.

**Headline tape:** **Iran ceasefire extension is the macro unlock** — headline risk that weighed on Mon/Tue has been removed. AI earnings cycle ongoing (INTC reports tonight AMC; NVDA/AMD/AVGO still ahead next week). Software and semis catching a strong bid. VIX at multi-week lows.

**Regime verdict:** RISK-ON REPAIR. The pullback was a 2-day flush that has been reclaimed. Breakout-buys are back in play — but most of yesterday's move is already priced in (ISRG, IGV gone). Focus today is on names that have NOT yet extended and are re-triggering their original setups (NVDA), or pullbacks to newly-minted breakout levels.

## Today's Watchlist — breakout re-engagement

### 1. ⭐ NVDA — BREAKOUT RE-TRIGGER (highest conviction)
- **Pre:** 202.50 (+0.12%). Reclaimed the $202.25 pivot that was the original Monday trigger and was violated Tue/Wed.
- **Catalyst:** (a) regime repair + risk-on tape, (b) software/semi bid returning (IGV +2.65%), (c) NVDA reports earnings next week — pre-print drift upward is the classic setup, (d) Victory Giant (NVDA supplier) just priced largest HK IPO of year, +50% debut — supplier-strength read-through.
- **Setup:** Breakout confirmation above $202.25 that holds. Ideal entry is first pullback to $202.00-$202.50 that holds, with volume confirmation. Do NOT chase if it gaps straight up on open.
- **Entry:** $202.50-$203.25 zone on a hold with 1.5x+ relative volume (after first 15 min).
- **Stop:** $199.50 (below Wed's intraday low / $200 round number). Risk: ~-1.5% from $202.50.
- **Target 1 (partial):** $208 (+2.7%, ~1.8R). Target 2: $214 (+5.7%, ~3.8R).
- **Conviction:** MEDIUM-HIGH. Setup is the cleanest re-trigger on the board. Main risk: NVDA reports next week and the stock can gap either direction — **partial must come off before earnings date**, and no held position through the print (strategy rule).
- **Size:** 50% starter. Add only if SPY stays >709 and NVDA holds above entry with volume.

### 2. IWM — FAILED-BREAKOUT-RECLAIM / "Wyckoff spring" setup
- **Pre:** 276.48 (+0.18%). Back at the $276.50 pivot that failed mid-week.
- **Catalyst:** Risk-on regime + Iran ceasefire extension (small-caps are most sensitive to macro risk-off/risk-on). News headline yesterday explicitly tied IWM rally to ceasefire.
- **Setup:** Reclaim and HOLD above $277.00 after the Tue/Wed shakeout = classic failed-breakdown / spring pattern. Higher conviction than a first-time breakout because weak hands have already been flushed.
- **Entry:** Above $277.00 on volume, after first 30 min.
- **Stop:** $274.50 (below yesterday's reclaim base). Risk: ~-0.9%.
- **Target:** $281 (+1.4%, ~1.5R). Partial at $279.
- **Conviction:** MEDIUM. Small RS vs SPY; taking because the spring pattern is a strategy-approved setup and the regime supports it. Use half-size (2.5% rather than 5%).

### 3. SPY reclaim — regime-confirmation trend follow
- **Pre:** 711.21. Reclaimed stand-down line by +6 pts.
- **Catalyst:** Straightforward trend continuation in a risk-on tape.
- **Setup:** Pullback buy to 709.50-710.00 that holds. Do NOT buy breakouts to new highs; prefer reloading on dips within the reclaim.
- **Entry:** $709.50-$710.50 on volume hold.
- **Stop:** $707.75 (below Mon pivot). Risk: ~-0.3%.
- **Target:** $715 (+0.7%, ~2.3R).
- **Conviction:** LOW-MEDIUM. Tactical only. Smaller size (2.5%).

### 4. ISRG — NO NEW ENTRY (extended)
- **Pre:** 483.62. Already ran +7.6% yesterday on the Q1 beat. Our $455 entry / $475 target thesis played out in full. Do NOT chase a gap-and-go that already happened. Watch for a pullback to $470-475 over the next 1-3 sessions as a potential re-entry zone; not today.

### 5. IGV — NO NEW ENTRY (extended)
- **Pre:** 88.74 (+2.65%). Blew past the $85-85.25 re-entry zone. Wait for a pullback; no chase.

### 6. INTC — EARNINGS TONIGHT, NO-TRADE
- Reports Q1 after the bell. Strategy rule: no pre-earnings holds. Watch post-print reaction for Friday setups.

## High-Conviction Focus (top 1-2)
1. **NVDA >$202.25 breakout re-trigger** — the only A+ setup. Regime repaired, supplier read-through positive, software/semi bid back, original pivot reclaimed. **Hard exit before earnings next week regardless of P&L.**
2. **IWM spring reclaim >$277** — B+ setup, half-size. Failed-breakdown pattern is higher-probability than first-time breakouts in the same level.

## Key Risks / Events This Week
- **NVDA / AMD / AVGO earnings next week** — any NVDA position MUST be out before the print.
- **INTC reports tonight (AMC)** — could move semis AH/Friday open.
- **TSLA earnings already reported / MSFT/META/GOOGL next week** — mega-cap print cycle keeps beta high.
- **Iran headline risk** — ceasefire extension is the driver of today's risk-on; any reversal there is the single biggest reversal risk.
- **VIX at ~19** — low vol = less edge on breakouts (everything goes up), but also less tail risk today.
- **Ops risk: unresolved auth (Day 4)** — no trades until keys rotated. This remains the top operational blocker.

## Today's Rules of Engagement
- **HARD GATE (unchanged from Wed): no orders until credential rotation confirmed out-of-loop.** If auth is restored, reconciliation of positions is the FIRST action before any new entry.
- Max 2 concurrent entries today (regime supports it again; up from Wed's 1).
- 50% starter on any entry; add only on confirmation.
- **Pre-earnings rule:** NVDA position must be closed before NVDA reports. Check exact earnings date before entering.
- Trailing stops per strategy: 5% from entry high; tighten to 3% once +5%.
- If SPY loses 709 intraday, cut adds and tighten stops on all longs.
- VIXY spike above 29.50 = reduce size or exit.

## Process Notes
- **Yesterday's ISRG thesis played out textbook** — $455 reclaim hit, ran to $484. The setup ("post-earnings positive-surprise into a risk-off tape that was positioned short") is confirmed as a repeatable pattern. Log this for the lessons file once reconciliation is possible.
- **Yesterday's NVDA thesis invalidated → re-validated in 48 hours.** Monday plan: >$202.25 breakout. Tue/Wed: broken. Today: reclaimed. The original pivot was correct; the 2-day flush just shook out weak hands. Good reason NOT to abandon a level on the first break.
- **IWM is a spring setup now, not a first-break.** Higher probability, but smaller reward tape to tape — size accordingly.
- **Outage persisting into Day 4 without rotation** is the single biggest issue. Every additional session of forfeited setups (today's NVDA re-trigger would be the 4th clean setup missed) is real opportunity cost. Operator action to rotate keys remains the highest-leverage action available.


## 2026-04-23 — Midday Observation

Unable to observe market regime via positions/account data — Alpaca API returning unauthorized on all endpoints. No position or P&L data available this midday session. Operational/credential issue, not a market signal. Flag for credential rotation check.
