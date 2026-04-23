# Lessons Database

This file grows automatically. Every closed trade adds a lesson. Weekly review synthesizes patterns into strategy rule updates.

## Pattern Library — What Works
(Populated automatically by EOD routine)

## Mistake Log — What to Avoid
(Populated automatically by EOD routine)

## Strategy Rule Updates
(Populated automatically by weekly review)

## Win/Loss Stats by Pattern
(Populated automatically by weekly review)

---

## 2026-04-20 (Mon) — EOD Post-Mortem

### Trade-level post-mortems
**None.** Zero trades opened, zero trades closed. Broker API (`get_account`, `get_positions`, `get_open_orders`) returned `unauthorized` at open, midday, and EOD. The open routine correctly stood down rather than trade blind.

### Meta-level post-mortem (the real lesson of the day)

**[OPERATIONS] NO-TRADE DAY — Forced stand-down from broker auth failure**
- **Entry thesis:** N/A — routine called for NVDA >$202.25 breakout + IGV $85.15 reclaim + IWM >$276.50.
- **What happened:** Alpaca returned `unauthorized` on every account/position/order call across three routines. Setups could not be sized, placed, or monitored. SPY closed -0.31% — a mild risk-off day that was arguably a decent tactical environment but we had no way to verify guardrails (exposure, daily loss cap, position count), so standing down was the only defensible decision.
- **Root cause of outcome:** Not a trading error. An **operational/infrastructure failure** — almost certainly expired or revoked API credentials, or an account-level permission change. This has now cost a full trading day.
- **Lesson:** **When broker auth fails on the open routine, immediately escalate to a credentials check — do NOT just "retry at midday."** Three identical failures in one day is a process bug. Treat auth errors as a P0 incident, not a transient glitch.
- **Strategy impact:** Add an explicit Operational Guardrails section to strategy.md covering (a) what to do on auth failure, (b) required pre-market health check, and (c) the "stand-down is correct" rule so it isn't second-guessed later.

### Pattern Library — What Works
- Confirmed: **Standing down when guardrails cannot be verified is the correct default.** Trading blind is worse than missing a setup. A missed breakout costs opportunity; an unbounded position can cost the account.

### Mistake Log — What to Avoid
- **Retry loops without escalation.** Running the same failing API call at open → midday → EOD without attempting to fix the underlying credentials is wasted observation. The second failure, not the third, should have triggered an "ops incident" flag in the log.
- **Incomplete state going into next session.** Because we can't read positions, we literally do not know what we own heading into Tuesday. This is the worst possible starting state and must be resolved *before* Tuesday's open routine runs.


---

## 2026-04-21 (Tue) — EOD Post-Mortem

### Trade-level post-mortems
**None.** Zero trades closed today (and zero opened). Auth-failure incident continues — Day 2 of forced stand-down.

### Meta-level post-mortem (Day 2 of ops incident)

**[OPERATIONS] AUTH FAULT ISOLATED — Public data works, authenticated endpoints do not**
- **Entry thesis:** N/A — routines called for reconciling positions and re-evaluating NVDA/IWM/IGV setups.
- **What happened:** `get_account` and `get_positions` returned `unauthorized` on every attempt across open, midday, and EOD on Tuesday. However, `get_market_snapshot("SPY")` succeeded cleanly. This definitively isolates the fault to **authentication/permissions on the account-level API**, not a general outage or network issue. SPY closed -0.75% — a real trend day we had no ability to act on.
- **Root cause of outcome:** Credentials are broken (expired, revoked, or account permission changed). The Monday "escalate after second failure" rule was followed at Tuesday open, but we still burned two more API cycles (midday + EOD) that we already knew would fail. Observing the same failure three more times added zero information after the auth fault was confirmed.
- **Lesson:** **Once a failure mode is diagnostically confirmed (e.g., auth fails while public market data succeeds), STOP re-running the failing call. Switch the day's routine from "trade" to "incident mode": log the diagnosis, halt further API probing, and explicitly defer all setup evaluation until auth is restored.** Repeated identical probes do not constitute escalation.
- **Strategy impact:** Refine the Operational Guardrails in strategy.md — specifically the "auth-failure escalation rule" — to add a diagnostic step (test a public endpoint to isolate the fault) and an "incident mode" state that suppresses further redundant API retries within the same incident window.

### Pattern Library — What Works
- Re-confirmed (Day 2): **Standing down is still the correct default.** Had we guessed at positions and traded, today's -0.75% SPY move would have hit unknown exposure in unknown direction. The cost of missing NVDA/IWM setups is bounded; the cost of an unbounded position is not.
- New: **Public-endpoint probe as a diagnostic.** `get_market_snapshot` succeeded while `get_account` failed — that single data point isolates the fault to credentials. This should be a standard first-response diagnostic, not a Day-2 realization.

### Mistake Log — What to Avoid
- **Redundant probing within a confirmed incident.** After the open-routine auth failure was confirmed a credentials issue, running the same `get_account` / `get_positions` at midday and again at EOD produced no new information. Process bug: the "escalation rule" added yesterday addressed *detection* but not *suppression* of further identical probes once the incident is active.
- **Two-day forfeit without a path to resolution.** The escalation rule tells us to flag P0; it does not define what happens when flagging it doesn't fix it. We need a defined out-of-loop action (credential rotation, support ticket) — not just more logging.


---

## 2026-04-22 (Wed) — EOD Post-Mortem

### Trade-level post-mortems
**None.** Zero trades closed today. Zero trades opened today. This is Day 3 of a single ongoing ops incident. There is nothing to learn at the *trade* level because no trades exist to post-mortem.

### Meta-level post-mortem (Day 3 of ops incident — the pattern is now the lesson)

**[OPERATIONS] 3 CONSECUTIVE BLOCKED DAYS — Strategy rule was followed, but the rule itself is insufficient**
- **Entry thesis:** N/A — routines called for ISRG $455 reclaim and SPY 705 reclaim scalp.
- **What happened:** Auth endpoints still return `unauthorized` at open and at EOD. Public market data works. The open routine correctly stood down and entered incident mode per the 2026-04-21 strategy update. The midday routine (triggered by user) failed as expected and logged accordingly. SPY bounced +0.59% today — a setup we couldn't participate in because we have no verified book.
- **Root cause of outcome:** The *trading* decisions have been correct every day. The *operational* decision — who rotates the API key and when — has **not** been executed. Strategy.md says "more than 1 consecutive blocked trading day = mandatory credential rotation before continuing," but the agent cannot rotate keys; only the human operator can. The rule exists, but the *handoff* to the operator is not forcing action.
- **Lesson (specific and actionable):** **On Day 2+ of any auth outage, the pre-market routine must emit a single, explicit, high-urgency notification whose ONLY content is the out-of-loop action required ("ROTATE ALPACA API KEYS") — not a status report, not a market summary. A status update buried among market-data logs is easy to ignore; a single-purpose escalation alert is not.** Every additional log line we write about SPY prices while the account is dead dilutes the signal that the operator needs to act.
- **Strategy impact:** YES — add a rule to Operational Guardrails: "Day 2+ of ops incident = single-line urgent notification at open, repeated at EOD, whose only message is the required out-of-loop action. No other content. Suppress routine EOD performance notifications until auth is restored (because there is no performance to report)."

### Pattern Library — What Works
- Re-confirmed (Day 3): **Incident-mode suppression worked as designed.** The open routine did not re-probe auth repeatedly today — it ran one check and stopped, per yesterday's rule. That rule is now validated across two independent sessions. Keep it.
- Re-confirmed: **Standing down is still correct.** SPY +0.59% today would have been a good day to hold longs, but with no visibility into the book, "guess and hold" is indistinguishable from gambling. Zero action beats negative expectancy.

### Mistake Log — What to Avoid
- **Writing the same "still unauthorized" log entry three days in a row without changing the operator-facing signal.** Each day's trade log entry is longer and more detailed — but the *call to action* for the human (rotate the keys) has not been elevated in visibility. That is the mistake. Logging is not escalation.
- **Treating each daily EOD as if it's a fresh review.** It is not. 2026-04-20, 2026-04-21, and 2026-04-22 are the *same incident*. Continuing to run full EOD routines (performance calc, benchmark comparison, notification) when no trades exist is process theater. The EOD review on Day 2+ of an outage should be reduced to: "incident still active, days blocked = N, required action = rotate keys, notify operator."


---

## 2026-04-23 (Thu) — EOD Post-Mortem (Day 4 of same incident — kept short per reduced-EOD rule)

### Trade-level post-mortems
**None.** Zero trades opened, zero closed. Day 4 of the same ongoing ops incident. No new trade-level lessons possible — nothing was traded.

### Meta-level post-mortem (the ONE new thing Day 4 teaches)

**[OPERATIONS] Day 4 — Urgent notifications are also being ignored, not just status logs**
- **What happened:** Yesterday's strategy update added a Day-2+ single-purpose urgent notification ("ROTATE ALPACA API KEYS") at open and EOD. We followed it. Day 4 still arrived with the keys unrotated. The rule was correctly designed to cut through status-update noise — but apparently even urgent notifications are not producing operator action within 24h.
- **Root cause:** The agent-operator handoff has no acknowledgement loop. We fire an alert; we have no signal whether it was read, let alone acted on. We keep assuming tomorrow will be different — it hasn't been for 4 sessions.
- **Lesson (specific and actionable):** **On Day 3+ of the same outage (i.e., the urgent-notification rule has already fired twice without resolution), the agent must stop assuming the notification channel works. The EOD log must explicitly state: "Prior urgent notifications on Day 2 and Day 3 did not produce action — escalate via a different channel or assume the alerting path itself is broken." This reframes the problem from "operator hasn't acted yet" to "our escalation mechanism is failing" — which points at a fixable thing (check the notification channel) rather than waiting.**
- **Strategy impact:** YES — add a small refinement to Operational Guardrails: a Day-3+ rule that explicitly questions whether the notification channel itself is working, rather than continuing to fire the same alert.

### Pattern Library — What Works
- Re-confirmed (Day 4): **Reduced-EOD rule is correct.** Today's trade_log entry is 5 lines instead of a page. Nothing was lost. This is the right cadence during an active incident.
- Re-confirmed: **Standing down is still correct.** SPY -0.30% today — tame tape, but with no book visibility, still uninvestable.

### Mistake Log — What to Avoid
- **Assuming the alerting channel works just because we sent the alert.** 4 sessions of urgent alerts with no resolution suggests the channel itself might be the problem, not operator willingness. After 2 urgent alerts without resolution, suspect the messenger before blaming the recipient.
