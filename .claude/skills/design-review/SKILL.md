---
name: design-review
description: Review Figma screens or a flow for UX and accessibility in one pass, read-only. Gathers the review context, walks the user's task (not a checklist of laws), checks the trading rules for the surfaces present and the WCAG 2.2 criteria the design triggers, rates findings S1–S4 with confidence, sends contrast and token checks to /ds-audit, and writes one report with a verdict to prds/<feature>/review.md. Use when someone says "review this", "design review", "UX review", "accessibility review", "is this ready for handoff", "check this flow", before handoff, and at the /prd-to-screens checkpoints.
argument-hint: "<Figma link(s)> [exploration|in review|final] [feature]"
---

# /design-review

Run `docs/ux/ux-governance.md` and `docs/ux/accessibility.md` together and write **one** report (governance §9).
**Read-only:** it never changes the design. Fixes are offered, and made only after the person says yes.
It's the judgement half of review. Measured things (contrast, token binding, tap sizes) belong to `/ds-audit`, which this skill runs for its hand-offs.

> **Rule zero** (governance): a finding is a real problem in this design with a consequence for a user. Laws explain findings; they never create them.
> Zero findings is a valid result. Never pad the report.

## Rules
- **Walk the task, not the catalogue** (`GOV-04`). Never go law by law or criterion by criterion. Let the problems pick the IDs.
- **Applicability test** (`GOV-02`) on every candidate: ① the trigger is visible, ② you can name the element, ③ a realistic user here is slowed, misled or put at risk, ④ fixing it changes the design. Any "no" → drop it.
- **One primary ID + at most one supporting** per finding (`GOV-03`). Never cite a `MYTH-*`. Never raise web-only rules (`W-*`, web-only criteria: `D-04`).
- **Don't re-raise** what `docs/ux/decisions.md` or the feature's "Decisions & waivers" already ruled (`GOV-07`).
- **Never** recommend removing, hiding or shrinking a disclosure, risk warning or consent (`GOV-08`). Make it visible at the decision point instead.
- **Unknown ≠ fail.** What the design can't show becomes an *annotation missing* note or a *Question for the team*. Never estimate a contrast ratio from a screenshot: measure it (`/ds-audit`).
- Anything that can cause a wrong order or a misread of money is `S1`.

## 0 · Preflight
1. **Target.** From each link: `fileKey` (after `/design/`) and the node (`node-id=101-129198` → `101:129198`). Review **Light and Dark**: if the Dark copies sit in another section, include it.
   Product screens are in each feature's own Figma file (link in `prds/<feature>/plan.md`); the DS file's Selected Screens are reference only.
   **Library up to date:** Scripts can't see pending library updates, so ask: does the file show **Library updates available** (Assets panel)? If yes, have it accepted (Review → Update all) first: a review on an old library version judges outdated components.
2. **Connect.** Official Figma plugin: load `figma:figma-use`, then `use_figma`. DS owners with figma-console: `figma_navigate` with `lock: true`, then `figma_execute` with `fileKey` and `timeout: 30000`.
3. **Feature.** If there's one, read `prds/<feature>/plan.md` (review context, "Rules that apply" per screen, Decisions & waivers) and the older reviews in `prds/<feature>/review.md`.

## 1 · Load context (governance §8.1, §2)
1. Read `docs/ux/ux-governance.md`, `docs/ux/accessibility.md` §4–§5.0 and §8, `docs/ux/decisions.md`, and `docs/content/voice.md` (vocabulary).
   `docs/ux/ux-laws.md` is the lookup for step 4: read an entry's *Apply when* and *Don't cite when* before citing it.
2. Fill in the review context: platform, surface (§6), user segment, task per screen, **stage**, states supplied, market state. Use `plan.md` first, then the defaults in §2.
   Ask only what would change the verdict (max 3 questions). Put everything inferred under *Assumptions*.
3. **Stage filter:** *exploration* → `S1`–`S2` and flow problems only · *in review* (the first-screen checkpoint) → `S1`–`S2` · *final* (pre-handoff) → everything, `S4` included.

## 2 · Look at everything (§8.2)
1. Run `scripts/figma/review-context.js` **verbatim**, changing only the `TARGET` line. It returns, per screen: mode, text in reading order with its style, the DS instances and their props,
   the annotations (and which `AN-xx` IDs are present), and flags (a hyphen used as a minus, K/M/B, placeholder text). Save it: `python3 scripts/figma-result.py <exportedAt> scratch/design-review/context.json`.
   If `more` isn't empty, run again with those IDs.
2. Screenshot every screen, Light and Dark (`get_screenshot`, or `figma_take_screenshot` with `nodeId`). Look at layout, hierarchy, what's tappable, what's in the thumb zone.
3. List the **missing states** (`TR-STATE-02`): loading, empty, error, offline, market closed, success. Don't review states you haven't seen.
4. **Content realism:** do the numbers add up (P&L = current − invested)? Picture the worst case: the longest name, the biggest value in Indian format, negatives, zero, empty.

## 3 · Walk the task (§8.3–8.4)
For the main task on each screen: *What does the user need to see? What do they do? What could go wrong? How do they know it worked?*
Then check only what the design contains:
- the `TR-*` sections (governance §6) for the **surfaces present**, and the mobile rules `M-01…M-10` (§5);
- the accessibility criteria **triggered** (`accessibility.md` §5.0). Read each one's *Skip when* and exceptions before raising it, and name the exception when you clear it;
- the annotations the screens trigger (`accessibility.md` §8, `AN-01…AN-15`). Missing ones go under *Notes for the team → Annotations missing*, not findings (unless the gap is itself a failure).

## 4 · Write the findings (§7, §3)
Each finding, in plain words (the report labels, governance §9): **Where** (screen + element + node ID), **What's wrong** (fact), **Why it matters** (who, what goes wrong),
**Fix** (smallest fix with DS components and tokens; name the trade-off, governance §4), **Rule** (one primary ID · optional supporting `TR-*`/`M-*`/`X-*`), **How sure** (High, Medium, Needs research), **Status** (Open, or Fixed with the date).
Write for a designer or PM who hasn't read the rule book: the problem and the harm first, the IDs last.
- **Severity** from governance §3 (accessibility §9 uses the same scale). Escalate one level for the order, confirmation or funds flow, a first-run flow, an irreversible step, or 3+ screens;
  de-escalate for a rarely used pro surface with an alternative, a recovery on the same screen, or a strong convention missing only an extra cue.
- **Merge** duplicates. A problem on 3+ screens is reported once, with every screen listed in *Where*.
- A component-level problem (inside a DS component) is reported once and handed to a DS owner (`/new-component` to change it). No component for a need → *Design-system gaps* (under *Notes for the team*).

## 5 · Hand-offs: measure, don't guess
1. Run `/ds-audit` on the same frames (its `scripts/figma/audit.js`, saved under `scratch/ds-audit/`). Use its measured contrast pairs, hit targets and raw values:
   a measured failure on the task becomes a finding with the ratio and "measured by /ds-audit"; everything else stays in the audit report.
2. For a fix that swaps a colour token, check the new pair first: `python3 scripts/token-contrast.py <fg> <bg> [<bg below> …]` (`--ui` for borders and icons).
3. Anything still unmeasured goes under *Notes for the team* as "to measure", never as a finding.

## 6 · Report (§9) and self-check (§8.7)
1. Write the report in the governance §9 template, so anyone can read it in ten seconds: **Result** in plain words, what was checked, the open-problem counts,
   **At a glance** (one table row per finding: problem, where, how serious, fix, who, status), **What to do next**, then **Details** (`### DR-01 · <problem> · 🔴 Must fix (S1)`
   with the bullet fields), Questions for the team, Missing screens or states, Good things (max 3), Checked and fine, and Notes for the team (annotations missing, what /ds-audit measured,
   design-system gaps, needs research, about this review). No "laws checked" list.
2. **Result** (verdict, §3): any open `S1` or systemic `S2` → ❌ *Not ready for handoff* · an open `S2` with a clear fix → ⚠️ *Ready after fixes* · otherwise ✅ *Ready for handoff*.
   Fixed findings stay in the report with *Status: Fixed* and don't count.
3. Save it **on top** of `prds/<feature>/review.md` (newest first). No feature → `scratch/design-review/review.md`, and say it isn't saved in the repo.
4. `python3 scripts/review-check.py <that file>`. Fix every `FAIL` (unknown or misused IDs, missing fields, too many IDs, counts or result that don't add up, a colour word that doesn't match the S-level). Read each `WARN` and fix it or say why it stays.
5. Then walk the rest of the §8.7 self-check yourself: each finding names an element and an impact, nothing contradicts a decision, no recommendation hides mandatory content,
   recommendations use DS parts, anything that risks a wrong order or a misread of money is `S1`.

## 7 · Tell the person
In plain words, short (the report's *At a glance* is a good outline): the result and counts; the must-fix and should-fix problems in one line each (where, what, fix, who); questions that need a decision (and who decides);
what was handed to `/ds-audit` and what it measured; the report's path. Then **offer** fixes as a short list and ask before changing anything.
- `S1`s must be fixed before handoff. An `S2` the team keeps is a **waiver**: record it (date, finding, why, decided by) in `plan.md` "Decisions & waivers", or in `docs/ux/decisions.md` if it's product-wide.
- A finding seen in 3+ reviews: suggest promoting it to a `TR-*` rule (governance §10).
- When fixing (after an OK): the feature's file only, one screen per call, Light first then Dark, screenshot both, then re-review just that screen.
