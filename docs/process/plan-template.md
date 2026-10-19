# plan.md template

`/prd-to-screens` copies this into `prds/<feature>/plan.md` and keeps it current after every approved step.
It's how work survives switching laptops or people. Check it with `python3 scripts/plan-check.py prds/<feature>/plan.md`.

```markdown
# <Feature name>: screen plan

> **Status:** planning · **Updated:** <date> · **Branch:** `prd/<feature>` · **Figma:** <page link, once created>

## Review context
| Context | Value |
|---|---|
| Platform | iOS + Android |
| Surface | <order · watchlist · portfolio · funds · onboarding · …> (`docs/ux/ux-governance.md` §6) |
| User segment | <first-time investor · regular investor · active trader · derivatives/pro> |
| Market states | <open · pre-open · closed · holiday · halted, or "n/a"> |
| Entry points | <tab, deep link, notification, flow step> |

## Flows
1. <Flow name>: <step> → <step> → <step>

## Screens
| ID | Screen | Type | Surface | Components | States | Rules that apply | Reference | Status | Figma |
|---|---|---|---|---|---|---|---|---|---|
| K01 | <Screen name> | flow step | onboarding | Top Bar, TextField md, Button lg | default, error, loading | TR-ACC · A11Y-FRM-01, A11Y-ERR-02 | A02 `101:129199` | planned | |

## Open questions
| # | Question | Why it matters | Owner | Answer |
|---|---|---|---|---|
| Q1 | | | | |

## Gaps
| Need | Proposed handling | Status |
|---|---|---|
| — | | |

## Decisions & waivers
| Date | Decision or waived finding | Why | Decided by |
|---|---|---|---|
| — | | | |

## Log
- <date>: plan written. Next: approve the plan.
```

**Screen IDs:** one letter per feature + 2 digits (`K01`, `K02`). Extra state frames add a lower-case letter (`K03b Verify · wrong code`).
**Type:** flow step · result · tab · detail · sheet state (`docs/patterns/screen-anatomy.md`).
**Status**, in order: `planned` → `built` (Light) → `approved` → `dark` → `annotated` → `reviewed`. `blocked` (with the reason in the Log) can replace any of them.
**Figma:** the Light frame's node link, then the Dark one (`Light 12:34 · Dark 12:90`).
