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
