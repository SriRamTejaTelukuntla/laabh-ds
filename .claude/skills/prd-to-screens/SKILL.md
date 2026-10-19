---
name: prd-to-screens
description: Turn a PRD into Figma screens in the product file, built only from DS components and tokens, in Light and Dark, with checkpoints. Reads the PRD, writes prds/<feature>/plan.md (flows, screens, states, rules that apply, questions, gaps), builds one screen for approval, then the rest, the Dark copies and the handoff annotations, and finishes with /ds-audit and /design-review. Resumes from plan.md on any laptop. Use when someone pastes or attaches a PRD, says "build the screens for X", "design this feature", or "continue the <feature> screens".
argument-hint: "<PRD (paste, file or doc text)> | continue <feature>"
---

# /prd-to-screens

Follow `docs/process/prd-to-screens.md`: **0 Setup → 1 Understand → 2 Plan ✋ → 3 One screen ✋ → 4 The rest → 5 Dark → 5½ Annotations → 6 Audit & review.**
The person never needs to know git or the Plugin API. Explain each step in plain words and show screenshots.
Build to `.claude/rules/` (components, tokens, layout, typography, light-dark, naming, accessibility, trading-ux, figma-safety). Those rules aren't repeated here: follow them.

## Rules
- **Checkpoints:** stop for an OK after the plan (2), after the first screen (3), and at the end of each flow-step section (4). Never sprint through.
- **Product file only.** Never build in, or change, the DS file. Ask before creating a page or a section, and before moving or deleting anything you didn't create in this session.
- **Components first, tokens only.** Instances of DS components, set through their properties. Never detach. Never draw a lookalike.
  Missing component or token → **stop**: add it to the plan's Gaps and offer `/new-component`. Don't improvise a one-off.
- **Don't build a rule break quietly.** A PRD ask that breaks `trading-ux.md` or `accessibility.md` goes into Open questions; it isn't built, and it isn't dropped silently either.
- **Save progress in the repo.** Update `prds/<feature>/plan.md` (status, Figma links, Log) after every approved step, then `python3 scripts/plan-check.py prds/<feature>/plan.md`.
- **One step per `use_figma` call** (one section of one screen), screenshot after each. If a step fails halfway, remove the partial frames before retrying.
- Don't commit or push: that's `/share-changes` at the end.

## 0 · Setup
1. Run the `/get-latest` checks (or `/get-latest setup`): the repo is up to date, the Figma plugin is signed in (`whoami`).
2. **Product file key** in `docs/figma-map.md` ("Laabh — Product"). If it still says `_TBD_`, **stop**: ask a DS owner to create the product file, enable the DS library in it, and add the key. Steps 1–2 can still run.
3. Load `figma:figma-use` and `figma:figma-generate-design` before the first `use_figma` call.
4. **New feature:** pick a kebab-case name with the person. `git switch -c prd/<feature>` (from an up-to-date `main`), create `prds/<feature>/prd.md` (the PRD exactly as given)
   and `prds/<feature>/plan.md` from `docs/process/plan-template.md`.
5. **Continuing** ("continue the kyc screens"): `git switch prd/<feature>` (clean tree only), read `plan.md` and run `python3 scripts/plan-check.py prds/<feature>/plan.md`.
   It prints the next screen and the last Log line. Pick up there, and re-find Figma nodes by name or key (node IDs from another session may be stale).

## 1 · Understand (no Figma yet)
- Flows, screens, decision points, data and edge cases from the PRD. The PRD template (`docs/process/prd-template.md`) shows what a complete PRD covers: what's missing becomes a **question**.
- **Review context** (`docs/ux/ux-governance.md` §2): platform, surface, segment, main task per screen, market states.
- **States per screen:** loading, empty, error, offline, market closed, success (`TR-STATE-02`). Missing in the PRD → a question, not a guess.
- `docs/ux/decisions.md`: don't re-ask what's decided (`D-01` sheet close, `D-02` portrait, `D-03` review step, `D-04` platforms).
- **Components:** map every element with `docs/index.md`, `docs/components/<name>.md` and `docs/patterns/` (screen-anatomy, forms, lists-cards, navigation, overlays, onboarding-kyc).
- **References:** the closest screen in `docs/references/selected-screens.md` for each screen type (reference only: reuse structure, not text or data).
- **Rules that apply** per screen: the `TR-*` sections for its surface and the accessibility criteria it triggers (`docs/ux/accessibility.md` §5.0), e.g. `TR-ORD · A11Y-ERR-03`.
- Money: every order or money movement has a review step (`D-03`) and a status after submit (`TR-ORD-06`). Numbers follow `TR-NUM-*` (₹, Indian grouping, true minus, sign + colour).

## 2 · Plan → checkpoint ✋
1. Fill in `plan.md` (template: `docs/process/plan-template.md`): status, review context, flows, the **Screens** table (ID, screen, type, surface, components, states, rules that apply, reference, status `planned`),
   open questions, gaps with the proposed handling, an empty Decisions & waivers table, and a Log line. Screen IDs: one letter for the feature + 2 digits (`K01`); state frames add a letter (`K03b`).
2. `python3 scripts/plan-check.py prds/<feature>/plan.md`. Fix every `FAIL`.
3. Show it in plain words: the flows, the screen list (one line each), the questions that block building, and the gaps. Name the Figma page and section names you'll create. **Wait for approval.**

## 3 · Build one screen → checkpoint ✋
1. **Look first:** screenshot the product file's target page. Ask, then create the page `<Feature>` and a Section per flow step (`<n> · <Step name>`), in clear space.
2. **Build kit:** `python3 scripts/build-kit.py <component names…>` prints one `const KIT = {…};` line with the library keys (components, text and effect styles, variable collections).
   Paste it at the top of each `use_figma` script. Import by key, never by a node ID from another file:
   components `figma.importComponentSetByKeyAsync(key)` (`set: true`) or `importComponentByKeyAsync`; styles `figma.importStyleByKeyAsync`;
   variables `figma.teamLibrary.getVariablesInLibraryCollectionAsync(KIT.collections['Color Tokens'])` → find by name → `figma.variables.importVariableByKeyAsync`.
3. Build the first screen in **Light**, one section per call, following `docs/patterns/screen-anatomy.md`:
   frame `<ID> <Screen name> — Light`, 390×844, fill `surface/page` → `Screen Atmosphere` (first child, absolute at 0,0, constraints left-right + top) → `Status Bar` (Fill width) →
   header (`Top Bar` in flows, `App Header` in the app) → Body → Footer (primary CTA `Button Solid · Brand · lg`, Fill) → `Home Indicator` (Fill width).
   Auto layout everywhere; fills, strokes, radius, padding and gaps bound to tokens; every text a text style; text inside instances set with `setProperties` (the TEXT property keys end in `#…`).
4. Screenshot after each section. Fix clipping, overflow, hug-vs-fill and misalignment. Dense screens: also check at 375×667.
5. **Check before showing:** `/ds-audit` on the frame (fix its S2s), then a quick `/design-review` at stage *in review* (S1–S2 only) against the screen's "Rules that apply". Fix what you can.
6. Show the screenshot, say what you couldn't fix, and **wait for an OK or changes**. Record decisions in `plan.md` (Decisions & waivers, Log); set the screen to `approved` with its Figma link.

## 4 · Build the rest
- Remaining screens in plan order, then the extra state frames (errors, empty, loading, sheets, market closed). Reuse the approved screen's structure.
- After each screen: screenshot it, set its status to `built` with the Figma link, and run `plan-check.py`.
- At the end of each flow-step section: show its screenshots together and **wait for an OK** before the next section.
- Changes asked for later: Light first, then mirror in Dark.

## 5 · Dark
For every approved Light frame: duplicate it, rename `— Light` to `— Dark`, set the copy's `Color Tokens` mode to **Dark** (`setExplicitVariableModeForCollection` with the library collection and its Dark mode ID),
and place it to the right (same y, 80 px gap). Screenshot every Dark frame. If Dark needs a manual fix, the token is wrong: report it as a gap, don't patch it. Status → `dark`.

## 5½ · Handoff annotations
Add the annotations each screen triggers (`docs/ux/accessibility.md` §8, `AN-01…AN-15`) as Figma annotations on the Light frames, the ID first in each label (`AN-03 Accessible name: "Back"`).
At least: names for icon-only buttons, reading and focus order, live regions for confirmations and errors, hit areas (48 dp on Android primary actions), gesture alternatives,
input purpose (tel, email, one-time code), timeouts, and the 200% text and landscape note on core screens. Check them with `scripts/figma/review-context.js` (its `anIds`). Status → `annotated`.

## 6 · Audit & review
1. `/ds-audit` on the page, saved to `prds/<feature>/audit.md` (`audit-report.py --out`). Findings inside DS components go to a DS owner, not the screen.
2. `/design-review` at stage *final*, saved on top of `prds/<feature>/review.md`.
3. **Gate:** every `S1` is fixed before handoff. Each `S2` is fixed, or waived with a reason in `plan.md` (Decisions & waivers). `S3`/`S4` stay in the reports.
4. Fix what you can after an OK, re-run both, then set screens to `reviewed` and the plan status to `handed off`.

## Report
In plain words: screens built (with Figma links), decisions made, open questions, gaps (and the `/new-component` proposals), the audit result and the review verdict.
Final `plan.md` update and `plan-check.py`, then suggest `/share-changes` (feature work: no DS-owner review needed).

## Gotchas
- Library Status Bar and Home Indicator instances are 393 wide: set them to Fill on a 390 frame.
- The DS file's Selected Screens are 393×852. New screens are 390×844.
- `display-md/Semibold` and `display-xl/Semibold` render in Space Grotesk Bold by design (`.claude/rules/typography.md`).
- The file uses dynamic page loading: use the async APIs (`getNodeByIdAsync`, `getMainComponentAsync`) and `page.loadAsync()`.
