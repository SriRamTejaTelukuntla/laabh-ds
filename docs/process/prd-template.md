# PRD template (for design-ready PRDs)

Copy into `prds/<feature>/prd.md`. Any format works (a pasted Google Doc or PDF is fine), but PRDs with these sections
produce better screens on the first try. Sections marked * are the most important for design.

```markdown
# <Feature name>

## Problem & goal *
Who is this for, what problem it solves, how we'll know it worked.

## Users & entry points *
Who uses it; where they come from (tab, deep link, notification, flow step).

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

## Rules & compliance
Regulatory requirements, consents, disclosures, things that must never happen.

## Out of scope
What not to design.

## Open questions
```
