# PRD template (for design-ready PRDs)

Copy into `prds/<feature>/prd.md`. Any format works (a pasted Google Doc or PDF is fine), but PRDs with these sections
produce better screens on the first try. Sections marked * are the most important for design.

```markdown
# <Feature name>

## Problem & goal *
Who is this for, what problem it solves, how we'll know it worked.

## Users & entry points *
Who uses it (first-time investor, regular investor, active trader); where they come from (tab, deep link, notification, flow step).

## User flow(s) *
Numbered steps per flow, including decision points:
1. User taps "Add money" on Funds
2. Enters amount (min ₹100, max ₹5,00,000/day via UPI)
3. If amount > balance limit → show error …

## Screens & content
Per screen: purpose, key information, actions, required copy (exact legal text in quotes).

## Data & formats *
Fields, examples of real values, units, ranges, formatting (₹, %, dates), what's prefilled.

## States & edge cases *
Empty, loading, errors (each with recovery), limits, offline, permissions, first-time vs returning.
Market states that change behaviour (pre-open, closed, holiday, fund cut-off time).

## Money & orders *
Every order or money movement in the flow: what's submitted, what the review step shows, charges and taxes, settle time,
status after submit (placed → executed / rejected), and how to modify or cancel.

## Login, OTP & timers
Authentication steps (OTP, MPIN, biometrics), session timeouts, OTP resend rules, anything time-limited.

## Live data & gestures
What updates live (prices, NAV), and any swipe, drag or long-press interactions.

## Rules & compliance
Regulatory requirements, consents, disclosures (exact text in quotes, from compliance), things that must never happen.

## Out of scope
What not to design.

## Open questions
```
