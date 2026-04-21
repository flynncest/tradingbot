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
