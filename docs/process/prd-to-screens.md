# Playbook: PRD → Figma screens

The `/prd-to-screens` skill follows this. Designers can read it to know what to expect.

## 0 · Setup
- Run `/get-latest`. Confirm the product Figma file key in `docs/figma-map.md` and that the Figma plugin is signed in.
- Create `prds/<feature>/` with `prd.md` (the PRD as given) and `plan.md`.

## 1 · Understand (no Figma yet)
- Read the PRD. List flows, screens, states, data and edge cases. List **questions** where the PRD is unclear.
- Map every screen element to DS components (`docs/index.md`, `docs/patterns/`). List **gaps** (needs a new component or token).
- Pick the closest reference screen for each screen type (`docs/references/selected-screens.md`).

## 2 · Plan → checkpoint ✋
Write `plan.md` and show it:

| ID | Screen | Type (flow step / result / tab / detail / sheet state) | Components | States | Reference | Status |
|---|---|---|---|---|---|---|

Plus: open questions, gaps and the proposed handling, the Figma page/section names. **Wait for approval.**

## 3 · Build one screen → checkpoint ✋
- In the product file, create (after asking) the page `<Feature>` and a Section per flow step.
- Build the first screen in Light: frame 390×844 → Screen Atmosphere instance → Status Bar → header → body → footer → Home Indicator.
  Instances only, tokens only, auto layout, one section per `use_figma` call, screenshot after each.
- Self-check against `/ds-audit` rules. Show the screenshot. **Wait for OK or changes.** Record decisions in `plan.md`.

## 4 · Build the rest
- Build remaining screens in plan order, then extra state frames (errors, empty, sheets).
- Update `plan.md` after each screen (status, node link).

## 5 · Dark
- Duplicate every Light frame, set Color Tokens mode **Dark**, place to the right, screenshot all Dark frames.

## 6 · Audit & report
- Run the `/ds-audit` checks on the page: raw values, detached instances, unstyled text, missing Dark, contrast, hit targets.
- Fix what you can; list the rest. Report: screens built (links), decisions made, open questions, gaps, audit result.
- Final `plan.md` update. Suggest `/share-changes` if `plan.md` or docs changed.

## Rules for the agent
- Never improvise a component; gaps go to the report and `/new-component`.
- Never touch the DS file in this flow.
- If the person asks for changes, apply them to Light first, then mirror in Dark.
