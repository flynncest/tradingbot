# Research Log

## Date: 2026-04-24 (Friday) — Pre-market plan

## ⚠️ OPS STATE — Day 5 gate (assumed still active until operator confirms rotation)
- Auth outage is now 4 completed sessions (Mon–Thu). No confirmation of credential rotation has been logged. This routine is **analysis only** — no orders, no `get_account` probes (incident-mode rule).
- If rotation occurs today: FIRST action is reconciliation (`get_account` + `get_positions` + `get_open_orders`) before any entry. Book is still `UNKNOWN` from pre-outage.
- Per strategy Day-3+ channel-integrity rule: prior urgent alerts (Day 2 & 3 & 4) did not produce action. The notification channel itself may be broken. This pre-market routine is *not* a trade routine and does NOT need to fire the urgent alert — that belongs to the open/EOD ops routines.

## Market Regime — RISK-OFF REVERSAL (yesterday's risk-on repair has un-repaired)
Pre-market snapshots (4/24, ~pre-open):
- **SPY 708.45 (-0.15%)** — **LOST the 709 intraday cut-line** from yesterday's plan. Below Wed close (711.18). Back into the Mon/Tue zone. Not catastrophic, but the reclaim tape from yesterday is no longer holding.
- **QQQ 651.42 (-0.58%)** — leading lower. Tech rolling over after Wed's +2% surge. News: "most overextended chip sector since 2000" is starting to cool.
- **IWM 275.52 (-0.01%)** — **BELOW the $276.50 pivot**. Yesterday's "spring reclaim" setup has failed; weak hands flushed and then re-flushed.
- **VIXY 28.51 (+0.21%)**, VIX ~19.7 per news, "edge of 20." Vol creeping up, not yet spiked.
- **NVDA 199.64 (+0.07%)** — **broke back below the $202.25 pivot AND below $200 round number**. The breakout re-trigger from yesterday has failed (2nd failure at this level in a week). Cannot buy the level; it's now resistance.
- **INTC 66.78 (-16.63%)** — massive pre-market drop. News last night said INTC beat Q1 / "soars AH" — but this morning it's -16% with a 20%+ reversal. Either the beat didn't hold into the call/guide, or a follow-up headline hit. This is a big tape event for semis and sentiment.
- **IGV 83.57 (-0.85%)** — giving back some of yesterday's +2.65%. Through prior re-entry zone.
- **ISRG 478.82 (flat)** — sat still overnight; minor pullback from yesterday's $484 extension. Not yet in $470–475 reload zone.

**Headline tape:**
- **Iran/Hormuz tensions BACK** — "stalled US-Iran talks," "fresh Mideast escalation." The ceasefire-extension tailwind that drove yesterday's risk-on has reversed. This is the primary macro driver today.
- **INTC earnings aftermath is the single biggest stock-specific event** — whatever happened on the call has taken a name that "soared" AH down -16% pre-market. Semiconductor read-through is negative.
- **"Chip stocks most overextended since 2000"** — narrative inflection; sets up profit-taking pressure.

**Regime verdict:** **RISK-OFF REVERSAL.** Three observations align: (1) breadth rolling over (SPY, QQQ, IWM all red or flat, QQQ leading down), (2) yesterday's A+ setup (NVDA re-trigger) has failed its pivot again, (3) two macro negatives simultaneously (Iran re-escalation + INTC blow-up + "overextended chips" article). Yesterday was a 1-day bounce in a messier tape, not a clean trend reclaim. **Default posture: defensive, very selective.**

## Today's Watchlist — mostly NO-CHASE; a couple of defensive / mean-reversion ideas

### 1. ⭐ NVDA — **SETUP INVALIDATED** — no long, watch for re-reclaim or short-setup
- **Pre:** 199.64. Broke back below $202.25 pivot AND lost $200 round number.
- **Status change:** The NVDA breakout thesis from yesterday is now **invalidated for the 2nd time** (1st was Tue/Wed). Two failed breakouts at the same level in one week = the level is resistance, not support. Do NOT buy a third attempt without a completely different setup structure (e.g., multi-day base reset).
- **What to watch, not trade:**
  - If NVDA reclaims AND holds >$202.25 intraday on volume, re-evaluate at that time (but the failure count makes this low-conviction).
  - If NVDA breaks <$197 on volume (Wed intraday low area), short/put setup may emerge — but NVDA reports next week so holding short risks the print.
- **Action today:** WATCH ONLY. No entries.

### 2. INTC — POST-EARNINGS CRUSHER, dead money near-term
- **Pre:** 66.78 (-16.63%) after "beat + soared AH" overnight flipped to a -16% morning.
- **Setup:** Classic post-earnings knife. Strategy rule: no post-earnings chases. First-day selloffs of this magnitude typically retest lower over 1–3 days before any bounce is buyable. Not a Day-1 trade.
- **Action today:** WATCH. Watch close. Note the low-of-day; if next week it forms a basing pattern with higher lows and volume dry-up, potential mean-reversion setup — **not today**.

### 3. SPY / QQQ — NO TREND TRADE TODAY
- **SPY 708.45** — below both the 709 cut-line and yesterday's 711 close. A first-15-min reclaim of 711 could reopen a tactical long but conviction is LOW given macro headlines. More likely scenario: sideways-to-down consolidation as Iran headlines dominate.
- **Action:** No index trade unless SPY reclaims 711 on volume AND VIX drops back <19 — then small tactical long to 713 with stop 709. Low-conviction; half-size (2.5%) if taken at all.

### 4. VIXY / hedge idea — **defensive tilt given headline risk**
- **Pre:** VIXY 28.51, VIX ~19.7. Iran re-escalation is a live tail. If ceasefire narrative breaks further, VIX 22-25 is not far.
- **Setup:** Small long VIXY as event hedge, NOT a directional trade. Entry above 28.75 on volume, or on any SPY break <707.
- **Entry:** VIXY $28.75 (breakout confirm) OR on SPY <707 trigger.
- **Stop:** $27.90 (below yesterday's base). Risk: ~-3%.
- **Target:** $30.50–$31 on any VIX spike toward 22+. Risk:reward ~2:1.
- **Conviction:** MEDIUM for hedge purpose, LOW for standalone speculation. **Size small (2–3%)** — contango drag makes this a day/2-day trade only, not a hold.
- **NOTE:** Only makes sense if we have directional longs to hedge. With book UNKNOWN due to auth outage, this is even more theoretical. If book is reconciled and long-heavy, VIXY hedge becomes the first action.

### 5. ISRG — pullback reload watch (NOT today)
- **Pre:** 478.82. Held yesterday's gap. Watching for pullback to $470–475 as potential re-entry for the original beat-and-raise momentum thesis. Not there yet.
- **Action:** Watchlist only. Alert: pullback to 472-475 on light volume = consider.

### 6. IGV — no re-entry
- **Pre:** 83.57. Through prior $85 reload zone; now rolling. Skip.

### 7. IWM — spring failed; no trade
- **Pre:** 275.52. Back below $276.50 pivot. Yesterday's spring thesis invalidated. Not a short here either (too mid-range). Skip.

## High-Conviction Focus (top 1-2 for today)
Honest assessment: **there is no A+ setup today.** Yesterday's A+ setup (NVDA re-trigger) has failed. The regime flipped overnight on Iran + INTC. Best trade today may be **no trade.**

1. **BEST IDEA — VIXY event hedge ONLY IF long exposure exists and can be verified.** Trigger: SPY breaks <707 OR VIXY >$28.75. Small size. Defensive, not speculative. **This is conditional on auth being restored and book being reconciled first.**
2. **SECOND — SPY tactical long reclaim >711** — very low conviction; only if VIX cools AND Iran headlines fade intraday. Skip if either condition fails.

Everything else today is **watchlist only, no entries.** Strong preference for zero trades over forcing a setup in a rolling-over tape with a headline overhang.

## Key Risks / Events to Watch Today
- **Iran/Hormuz headlines** — the macro driver. Any further escalation = SPY could leg down another 0.5–1%. Any de-escalation = sharp reversal up; don't short into headlines.
- **INTC follow-through** — if INTC stabilizes off the -16% open, semis may dig out. If it keeps bleeding into the $62s, SMH/QQQ get hit harder and NVDA gets pulled down with it.
- **Chip overextension narrative** — one mainstream article is now out about "most overextended since 2000." Self-fulfilling risk to semi sizing broadly.
- **VIX 20 line** — VIX ~19.7 is right at the threshold. A close >20 changes the tape character for next week.
- **Next week's earnings: NVDA / AMD / AVGO / MSFT / META / GOOGL.** Pre-print drift both directions — any new NVDA long MUST exit before the print.
- **Friday afternoon weekend risk** — Mideast headlines compound over weekends. Closing longs / adding hedges into Friday PM is the default in this tape.
- **OPS: Day 5 of auth outage** — no orders possible anyway. Every setup above is conditional on credential rotation occurring.

## Today's Rules of Engagement
- **HARD GATE (unchanged): no orders until credential rotation confirmed out-of-loop.**
- **Regime gate:** Default posture today is DEFENSIVE. Max 1 concurrent entry (down from Wed's 2, matching Mon's posture). 50% starter only. No adds in first 60 min.
- **No chase rule:** Do not buy NVDA here (failed level), do not buy INTC (post-earnings knife), do not buy IGV/IWM (failed levels).
- **Headline discipline:** If Iran escalation headline hits during session → cut any longs, do not short the hole. Wait for the first 15-min bar after the headline to stabilize.
- **VIX trip:** VIX >20 intraday = reduce any long size by half, tighten stops to 3%. VIX >22 = flat all longs.
- **Friday-into-weekend tilt:** Reduce or flatten any directional longs by 15:30 ET. Keep hedges (VIXY) over the weekend only if macro risk is still live.
- **Pre-earnings rule (reminder):** NVDA earnings next week — any NVDA touch (none planned today) must exit before the print.

## Process Notes — what today's tape teaches
- **The NVDA pivot has now failed twice in 5 sessions.** After a 2nd failure at the same level, the level is no longer a support/resistance to trade — it's a chop zone. Waiting for a fresh base (3+ days sideways) before the 3rd attempt is the textbook play. Log for lessons.
- **Yesterday's "risk-on repair" thesis had a 1-day lifespan.** The tell was that IGV and ISRG were already extended — when the leading names have already priced in the recovery, the recovery is probably close to done. Worth noting: on a reclaim day, if the best setups are already extended, the regime signal is weaker than it looks.
- **INTC post-earnings reversal** is a reminder: AH reactions are NOT confirmed until the next full session opens. "Stock soars AH on beat" is a headline, not a trade. The real move is Day-1 cash-session direction.
- **Ops outage continues to dominate.** Even if today's correct call is "no trade," we'd prefer to make that call from a verified book rather than a forced stand-down. Credential rotation remains the #1 leverage action for the desk.
