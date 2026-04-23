# Trade Log

| Date | Symbol | Side | Qty | Entry | Exit | P&L | Notes |
|------|--------|------|-----|-------|------|-----|-------|

## Open Positions
- **Unknown** — Alpaca API has returned `unauthorized` all day (open, midday, EOD). Cannot confirm whether positions exist. Assume unverified until auth restored.

## Performance Summary
- Total trades: 0
- Win rate: —
- Avg win: —
- Avg loss: —
- Total P&L: $0
- Days traded: 0
- Days blocked by ops issues: 1 (2026-04-20)

---

## 2026-04-20 (Mon) — Market Open Routine: STAND DOWN
- **Action:** No trades placed.
- **Reason:** Alpaca API returned `unauthorized` on get_account, get_positions, and get_open_orders. Cannot verify equity, buying power, existing exposure, or daily P&L — therefore cannot validate guardrails (10% max position size, max 5 positions, -2% daily loss halt).
- **Plan carried forward:** NVDA breakout >$202.25 on 2x volume (primary); IGV reclaim $85.15 on pullback (secondary); IWM >$276.50 (tertiary). No pre-earnings holds for ISRG/TSLA.

## 2026-04-20 — Midday Review: HALTED (API Unauthorized)
- `get_account()` and `get_positions()` both returned `{"message": "unauthorized."}` on retry.
- **No actions taken.**

## 2026-04-20 — EOD Review: STILL UNAUTHORIZED
- Third consecutive failure of account/positions/orders endpoints.
- SPY closed $708.70, -0.31% on the day (prev close $710.92). Mild risk-off tape — consistent with the Iran headline overlay noted at open.
- **Portfolio return today: UNKNOWN** (cannot read equity). **Benchmark (SPY): -0.31%**.
- **Trades closed today: 0** (no trades opened today either).
- **Open positions going into Tue 2026-04-21: UNKNOWN — requires auth restoration before any new action.**
- **Opportunity cost:** NVDA/IGV/IWM setups could not be acted on. Need to check Tue whether they triggered and what we missed.


## 2026-04-21 (Tue) — Market Open Routine: STAND DOWN (Day 2 of ops incident)
- **Action:** No trades placed.
- **Reason:** Alpaca API `get_account()` and `get_positions()` both returned `{"message": "unauthorized."}` again at the open. This is Day 2 / session 4 consecutive of auth failure.
- **Guardrail logic:** Cannot verify equity → cannot size 10% max position; cannot verify open positions → cannot check 5-max or layer risk; cannot verify today's P&L → cannot enforce -2% daily halt. Per strategy.md operational guardrails, never layer new trades on an unknown book. Per research_log.md rules of engagement for today, auth health check is mandatory before any order.
- **Forfeited setups:**
  - NVDA pivot $202.25 breakout (primary, pre 202.06) — Day 2 missed if it triggers
  - IWM pullback to $276.50-277.00 retest (secondary, pre 277.35)
  - IGV already extended — was WATCH only anyway
- **Escalation:** P0 incident. If auth is not restored by EOD, escalate further — 2 trading days of forfeited opportunity and an unknown position book is a material risk.
- **Next action:** Retry auth at midday. If restored, FIRST step is reconciliation (read positions + equity + open orders) before any new entry. Only then, re-evaluate NVDA/IWM setups against updated intraday prices.


## 2026-04-21 — Midday Review: FAILED (API Unauthorized)
- Attempted midday position review routine.
- `get_account`, `get_positions`, and `get_open_orders` all returned `{"message": "unauthorized."}`.
- No actions taken: could not verify daily P&L, could not evaluate losers, could not tighten stops on winners.
- Guardrails NOT enforced this cycle:
  - 8% loss-cut threshold
  - 3% trailing stop on +5% winners
  - 2% account-wide daily drawdown halt
- ACTION REQUIRED: restore Alpaca API credentials before next review cycle. Manually verify positions via broker UI in the interim.


## 2026-04-21 — EOD Review: STILL UNAUTHORIZED (Day 2, session 3)
- `get_account()` and `get_positions()` both returned `{"message": "unauthorized."}` again at EOD.
- `get_market_snapshot("SPY")` succeeded — **public market data endpoints work; only authenticated endpoints fail.** This isolates the fault to credentials/permissions, not general API outage.
- **SPY closed $704.15, -0.75%** (prev close $709.49). Today was a larger risk-off day than Monday (-0.31%). Two-day SPY drawdown ≈ -1.06%.
- **Portfolio return today: UNKNOWN** (cannot read equity).
- **Trades closed today: 0.** Trades opened today: 0.
- **Open positions going into Wed 2026-04-22: UNKNOWN.** Reconciliation remains mandatory as the first action once auth is restored.
- **Forfeited setups (Day 2):** NVDA $202.25 breakout, IWM $276.50 retest, IGV $85.15 reclaim — now stale; must re-evaluate against fresh prices once auth is restored.
- **Ops status:** Credentials issue is confirmed (market-data-only endpoint works). This is **48 trading hours of unusable account access**. Escalation is beyond "retry later" — it now needs a credential rotation / support ticket outside this loop.

### Performance Summary (as of 2026-04-21 EOD)
- Total trades: 0
- Win rate: —
- Avg win: —
- Avg loss: —
- Total P&L: $0 (cannot verify, but no orders placed)
- Days traded: 0
- Days blocked by ops issues: **2** (2026-04-20, 2026-04-21)
- Benchmark over blocked window: SPY -1.06% cumulative — we neither participated in downside nor had any hedge on (exposure unknown).


## 2026-04-22 (Wed) — Market Open Routine: STAND DOWN (Day 3 of ops incident)
- **Action:** No trades placed. No orders attempted.
- **Reason:** Alpaca authenticated endpoints still returning `{"message": "unauthorized."}` at the open:
  - `get_account()` → unauthorized
  - `get_positions()` → unauthorized
  - `get_open_orders()` → unauthorized
- **Hard gate triggered:** Per strategy.md (2026-04-21 update) and today's research_log.md rules of engagement, >1 consecutive blocked trading day requires credential rotation out-of-loop BEFORE any further retry or order placement. This is Day 3 / session 7 of the outage. The gate is active.
- **Guardrails that cannot be enforced without auth:**
  - 10% max position size (no equity reading)
  - 5-max concurrent positions (no position reading)
  - -2% daily loss halt (no P&L reading)
  - -8% hard cut per position (no entry/current price tracking for held names)
  - 5% trailing stop placement (requires a filled entry)
- **Regime context (market data still works):** SPY 704.08 pre, broke the 705 stand-down line from yesterday's plan. Per research_log today: "If SPY stays below 705 all session → STAND DOWN on all longs." Even if auth were restored, the regime rule would still demand extreme selectivity — only ISRG >$455 reclaim would have been live.
- **Forfeited setups (Day 3):** ISRG reclaim $455 (post-earnings reversal, MEDIUM-HIGH conviction); SPY 705 reclaim scalp (LOW-MED). Both now untrackable without order capability.
- **Escalation required (out-of-loop):**
  1. Rotate Alpaca API keys
  2. Verify account status and positions via broker UI directly
  3. Confirm no stranded open orders or uncovered positions
  4. Only then resume trading routine
- **No ClickUp notification sent** (per instructions: notify only when trades are actually placed).
- **Days blocked by ops issues: 3** (2026-04-20, 2026-04-21, 2026-04-22).


## 2026-04-22 — Midday Review SKIPPED (API Auth Failure)
- Attempted routine midday position review at user's request.
- All Alpaca endpoints returned `unauthorized` (get_account, get_positions, get_open_orders).
- No actions taken: could not verify daily loss limit, could not cut losers, could not tighten stops on winners.
- **Action required from operator:** rotate/refresh Alpaca API keys and re-run the midday routine ASAP. Open positions are currently unmanaged with respect to the -8% cut rule and the +5% trailing-stop tightening rule.


## 2026-04-22 — EOD Review: STILL UNAUTHORIZED (Day 3, session 9 of outage)
- EOD auth retry (the only retry allowed this session per incident-mode rule): `get_account()` → `unauthorized`, `get_positions()` → `unauthorized`. Public endpoint `get_market_snapshot("SPY")` succeeded.
- **SPY closed $711.18, +0.59%** (prev close $706.98). Today was a relief-rally / risk-on bounce after Tuesday's -0.75%. 3-day SPY path: Mon -0.31%, Tue -0.75%, Wed +0.59% — net ~-0.48% cumulative.
- **Portfolio return today: UNKNOWN** (cannot read equity). **Benchmark (SPY): +0.59%.**
- **Trades closed today: 0.** Trades opened today: 0. No post-mortem material at the trade level for the 3rd consecutive day.
- **Open positions going into Thu 2026-04-23: UNKNOWN.** Reconciliation is still the mandatory first action once auth is restored.
- **Forfeited setups (Day 3):** ISRG $455 reclaim (post-earnings), SPY 705 reclaim scalp. Both now reference-only — can't be acted on.
- **Ops status:** Day 3 confirmed. Credentials remain broken. Per strategy.md "resolution path" rule, >1 blocked day mandates credential rotation out-of-loop before continuing. That has not happened yet — this is now the primary blocker to all trading activity, not any market condition.

### Performance Summary (as of 2026-04-22 EOD)
- Total trades: 0
- Win rate: —
- Avg win: —
- Avg loss: —
- Total P&L: $0 (cannot verify, but no orders placed — no way to open or close)
- Days traded: 0
- Days blocked by ops issues: **3** (2026-04-20, 2026-04-21, 2026-04-22)
- Benchmark over blocked window: SPY cumulative ~-0.48% (Mon -0.31%, Tue -0.75%, Wed +0.59%). Missed: one real risk-off day (Tue) and one reversal bounce (Wed). Net result for a blind account: unknown but operationally the right choice was zero-action.


## 2026-04-23 (Thu) — Market Open Routine: STAND DOWN (Day 4 of ops incident)
- **Action:** No trades placed. No orders attempted.
- **Reason:** Alpaca authenticated endpoints still returning `{"message": "unauthorized."}` at the open:
  - `get_account()` → unauthorized
  - `get_positions()` → unauthorized
  - `get_open_orders()` → unauthorized
- **Hard gate active:** Per strategy.md and research_log.md rules of engagement for today, the credential-rotation gate requires operator confirmation out-of-loop BEFORE any retry or order placement. No such confirmation has been logged. This is Day 4 / session 10 of the outage.
- **Guardrails that cannot be enforced without auth:** 10% max size, 5-max concurrent, -2% daily loss halt, -8% hard cut, 5% trailing stop placement. Trading without these is an explicit guardrail violation — would rather not trade than break risk rules.
- **Regime context (market data still works):** Tape is RISK-ON REPAIR. SPY 711.21 reclaimed the 705 line. NVDA $202.50 has re-triggered its original $202.25 breakout pivot — this was the A+ setup of the plan. IWM at $276.48 offers a spring reclaim setup >$277. ISRG and IGV are already extended; no chase. In a tradeable world, today's plan would have been: NVDA 50% starter on hold of $202.25–$203.25 + IWM half-size on reclaim >$277.
- **Forfeited setups today (Day 4):**
  - NVDA $202.25 breakout RE-TRIGGER (MEDIUM-HIGH conviction) — the originally-planned Monday setup has come back around; missed again
  - IWM spring reclaim >$277 (MEDIUM) — B+ setup, failed-breakdown pattern
  - SPY 709.50 pullback trend-follow (LOW-MED, tactical)
- **Escalation (out-of-loop, unchanged):**
  1. Rotate Alpaca API keys — not yet done after 4 sessions
  2. Verify account status and positions via broker UI directly
  3. Confirm no stranded open orders or uncovered positions
  4. Log rotation in trade_log.md, then resume routine
- **No ClickUp notification sent** (per instructions: notify only when trades are actually placed).
- **Days blocked by ops issues: 4** (2026-04-20, 2026-04-21, 2026-04-22, 2026-04-23).
- **Cumulative opportunity cost (estimated):** ISRG $455→$484 (+6.4%) setup fully played out without participation; NVDA re-trigger is live today; IWM spring today. 4th straight session of missed A-tier setups. The operational issue has now clearly dominated any market-based P&L for the week.


## 2026-04-23 — Midday Review: BLOCKED (API Unauthorized)

**Status:** Unable to execute midday position review routine.

**Issue:** All Alpaca API calls returned `{"message": "unauthorized."}`:
- get_account() → unauthorized
- get_positions() → unauthorized
- get_open_orders() → unauthorized

**Actions taken:** None. Cannot verify account equity, positions, P&L, or existing orders.

**Risk implications:**
- Cannot confirm whether 2% daily loss halt has triggered
- Cannot cut losers breaching -8% threshold
- Cannot tighten trailing stops on +5% winners
- Positions are effectively unmanaged this session

**Next steps required (human):**
1. Verify Alpaca API key / secret / permissions are valid and not expired
2. Confirm account is not flagged/restricted
3. Re-run midday review once credentials restored
