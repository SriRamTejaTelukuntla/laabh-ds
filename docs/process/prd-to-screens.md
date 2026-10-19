# Playbook: PRD → Figma screens

The `/prd-to-screens` skill follows this. Designers can read it to know what to expect.
Quality bar: the build rules in `.claude/rules/` (including `trading-ux.md` and `accessibility.md`) while building,
and the review rulebooks in `docs/ux/` at the checkpoints.

## 0 · Setup
- Run `/get-latest`. Confirm the product Figma file key in `docs/figma-map.md` and that the Figma plugin is signed in.
- Create `prds/<feature>/` with `prd.md` (the PRD as given) and `plan.md` from [plan-template.md](plan-template.md). Check it with `scripts/plan-check.py`.

## 1 · Understand (no Figma yet)
- Read the PRD. List flows, screens, states, data and edge cases. List **questions** where the PRD is unclear.
- Fill in the **review context** (`docs/ux/ux-governance.md` §2): platform (iOS + Android), user segment, surfaces, the main task per screen, market states.
- List the **states** each screen needs: loading, empty, error, offline, market closed, success (`TR-STATE-02`). Missing in the PRD → a question, not a guess.
- Read `docs/ux/decisions.md` so nothing already decided is re-asked.
- Map every screen element to DS components (`docs/index.md`, `docs/patterns/`). List **gaps** (needs a new component or token).
- Pick the closest reference screen for each screen type (`docs/references/selected-screens.md`).
- If the PRD asks for something that breaks a build rule (`trading-ux.md`, `accessibility.md`), add it to the questions.

## 2 · Plan → checkpoint ✋
Write `plan.md` and show it:

| ID | Screen | Type (flow step / result / tab / detail / sheet state) | Surface | Components | States | Rules that apply | Reference | Status |
|---|---|---|---|---|---|---|---|---|

- **Surface** is the `ux-governance.md` §6 area (order, portfolio, funds, onboarding…).
- **Rules that apply** lists the `TR-*` sections and the accessibility criteria the screen triggers (`docs/ux/accessibility.md` §5.0),
  e.g. `TR-ORD`, `TR-NUM` · `A11Y-AUT-01`, `A11Y-TIM-01`. The build must cover them.
- Plus: review context, open questions, gaps and the proposed handling, the Figma page/section names, and an empty **Decisions & waivers** table.

**Wait for approval.**

## 3 · Build one screen → checkpoint ✋
- In the product file, create (after asking) the page `<Feature>` and a Section per flow step.
- Build the first screen in Light: frame 390×844 → Screen Atmosphere instance → Status Bar → header → body → footer → Home Indicator.
  Instances only, tokens only, auto layout, one section per `use_figma` call, screenshot after each.
- Run `/ds-audit` on the frame (fix its S2s), then a **quick design review** at stage *in review* (`S1`–`S2` only, `ux-governance.md` §2):
  walk the screen's task against its "Rules that apply". Fix what you find before showing it; mention anything you couldn't fix.
- Show the screenshot. **Wait for OK or changes.** Record decisions in `plan.md`.

## 4 · Build the rest
- Build remaining screens in plan order, then extra state frames (errors, empty, loading, sheets, market closed).
- Update `plan.md` after each screen (status, node link).

## 5 · Dark
- Duplicate every Light frame, set Color Tokens mode **Dark**, place to the right, screenshot all Dark frames.

## 5½ · Handoff annotations
- Add the annotations each screen triggers (`docs/ux/accessibility.md` §8, `AN-01…AN-15`) as Figma annotations, ID first in the label:
  accessible names for icon-only buttons, reading and focus order, live regions for confirmations and errors, hit areas (48 dp on Android primary actions),
  gesture alternatives, input purpose, timeouts, and the 200% text / landscape note on core screens.
- Annotate on the Light frames; Dark frames share them.

## 6 · Audit & review
- Run `/ds-audit` on the page, saved to `prds/<feature>/audit.md`: raw values, detached instances, unstyled text, screen chrome, Light/Dark pairs,
  contrast (measured in both modes), hit targets. Findings inside DS components go to a DS owner, not the screen.
- Run `/design-review` at stage *final*: one report for UX + accessibility (`ux-governance.md` §9), saved to `prds/<feature>/review.md`.
- **Gate:** any `S1` is fixed before handoff. Each `S2` is fixed, or waived with a reason in `plan.md` (Decisions & waivers). `S3`/`S4` go to the report.
- Fix what you can (after the person's OK); list the rest. Report: screens built (links), decisions made, open questions, gaps, audit result, review verdict.
- Final `plan.md` update. Suggest `/share-changes` if `plan.md` or docs changed.

## Rules for the agent
- Never improvise a component; gaps go to the report and `/new-component`.
- Never touch the DS file in this flow.
- If the person asks for changes, apply them to Light first, then mirror in Dark.
- Reviews are read-only: report first, change the design only when the person agrees.
- Never remove or shrink a mandatory disclosure or consent to fix a finding (`GOV-08`).
