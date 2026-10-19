---
name: new-component
description: Add a component to the DS, or change one, with checkpoints. Checks it doesn't exist already, writes the proposal (why, anatomy, props, states, tokens), maps every value to tokens, drafts the component set in the DS Figma file, re-checks bindings while the designer refines it, walks the review checklist, and writes the component doc, index row and audit lists. Agent drafts, designer refines, DS owner approves. Use when someone says "new component", "we need a component for X", "the DS is missing X", "promote this to a component", when /prd-to-screens or /ds-audit finds a gap, or when /ds-sync lists a component NOT IN DOCS.
argument-hint: "<what you need, e.g. bottom navigation bar>"
---

# /new-component

Add or change a component the way `docs/process/new-component.md` says: **1 Propose → 2 Spec → 3 Tokens → 4 Draft → 5 Refine → 6 Review → 7 Document → 8 Publish.**
The person never needs to know git or the Plugin API. Explain each step in plain words and show the result before moving on.

## Rules
- **Checkpoints.** Stop for an OK after the proposal (steps 1–3), after the first draft screenshot (step 4), and after the review (step 6).
- **Who:** anyone can propose (steps 1–3). Only a **DS owner** (`.github/CODEOWNERS`) can approve new tokens or let the draft go into the DS file.
  If the person isn't one, finish the proposal, share it with `/share-changes`, and stop: a DS owner picks it up from there.
- **DS file only, and safely.** This is the one skill that edits the DS file ("Laabh — Design System", `mmAhXn4vJKlmuThcAMgGss`). Before the first change, save a named version
  (`figma.saveVersionHistoryAsync("Before <Name>")`). Ask before creating a page, and before touching any node, variable or master you didn't create in this session.
- **Never** publish the library, delete or rename existing variables, or change another component's master as a side effect. Publishing is the DS owner's step 8.
- **Build from what exists:** nested DS instances (Button, Icon Button, Badge, `icon/*`), never detached copies. Tokens only (`.claude/rules/tokens.md`). Corner smoothing 0.6.
- Load `figma:figma-use` before any `use_figma` call (DS owners can use figma-console: `figma_navigate` with `lock: true`, then `figma_execute` with `fileKey` and `timeout: 30000`).
- Don't commit or push here: that's `/share-changes`. Ask before adding a `CHANGELOG.md` entry (entries may be paused).

## 0 · Preflight
1. `git status` and `git branch --show-current`. On `main`: create `feat/<kebab-name>` (e.g. `feat/navigation-bar`). Changing an existing component: `feat/<kebab-name>-<change>` (a breaking change is marked in the commit, not the branch).
2. **Does it exist already?** Check, in this order, and stop if one fits:
   - `docs/index.md`: the component table and "Known gaps" (the gap may already have a plan).
   - `docs/proposals/`: an open proposal for the same thing.
   - The DS file: `search_design_system` (or `figma.root.findAll` on component pages) for the name and close synonyms.
   - A variant or property of an existing component (`docs/components/<name>.md`) that would do the job. Prefer adding a variant over a new component.
   - Name clashes: a name that's taken means something else (`Tab Bar` is the in-page tabs, so a bottom bar is `Navigation Bar`).
3. **Is it worth a component?** It appears on 2+ screens, or it's a clear system gap (`.claude/rules/components.md` rule 4). A one-off composition stays a composition.
4. **DS or product?** Generic UI (works in any app) → COMPONENTS. Laabh-specific compositions (stock row, holdings card, App Header) → PRODUCT COMPONENTS.
5. Ask whether they're a DS owner (see Rules).

## 1–3 · Proposal → checkpoint ✋
Write `docs/proposals/<kebab-name>.md`. Same shape as `docs/proposals/screen-atmosphere.md`:

| Section | What goes in it |
|---|---|
| Status line | `**Status:** proposed` · Proposed: date · Section: COMPONENTS or PRODUCT COMPONENTS · Source design (node link, if any) |
| Why | Where it appears (screens, node IDs), what people do today, why existing components can't do it |
| Anatomy | Each layer: size, auto layout, fill/stroke/text token, nested instances |
| Properties | Variant props (`Style`, `Tone`, `Size` `xs–xl`, `State`, `Selection`), booleans `Show …`, text props (`Label`, `Title`, …), instance swap for icons and content. Names per `.claude/rules/naming.md`. Most common variant = default |
| States | Default, Hover/Pressed, Focus (`focus/ring`), Disabled; Error/Success where it holds a value |
| Sizes | Heights from `.claude/rules/layout.md` (Button-like: 28/32/40/52/56; fields 40/52/56). Tap area ≥ 44 |
| Content | Label length, casing, truncation, numbers in `num-*` with sign (`.claude/rules/trading-ux.md`) |
| Accessibility | Role, accessible name (icon-only parts), states announced, live region if it shows status, gesture alternatives (`docs/ux/accessibility.md` §8, `AN-*`) |
| Light / Dark | What changes between modes. It must come from tokens alone |
| Tokens | Every value → token, marked `exists` or **`new`** (step 3) |
| Figma plan | Version name, page, frames, the order of work |
| Open points | Questions for the designer or DS owner |

**Step 3 · Tokens.** Map every value with `docs/foundations/*.md` (readable) and `tokens/*.json` (exact). Pick by role, not by look.
A value with no fitting token is usually off-pattern: check `docs/patterns/` first. If a new token is really needed, propose its name (`<group>/<kebab-leaf>`, primitives like `alpha/frost600-50`),
its Light and Dark values and the primitive each points to.
Check the contrast of **every** text, icon and border pair, new or existing, in both modes:
`python3 scripts/token-contrast.py <fg> <bg> [<bg below> …]` (add `--ui` for borders, meaningful icons and large text: 3:1). Backgrounds go top-down; it ends on `surface/page`.
A failing pair gets a different semantic token (tinted surfaces need `text/<tone>-strong`, `docs/foundations/colors.md`), never a new value.

Show the proposal in a few lines (what, why, props, new tokens) and **wait for an OK**. Not a DS owner? Share it with `/share-changes` and stop here.

## 4 · Draft in Figma → checkpoint ✋
One step per `use_figma` call. Screenshot after each.
1. Save the version: `"Before <Name>"`. Note its name for the commit's `Figma-Version:` footer.
2. New tokens (if approved): create the primitive(s) and the semantic variable with both modes set. Never edit an existing variable's value.
3. Ask, then create the page `↳ <Name>` in the right section (after the last page there; record it in `docs/figma-map.md` later).
4. Build the frames, Light first: `<Name> — Variants` (the component set), `<Name> — Reference` (the component in a sample 390-wide screen, with short usage notes).
   Add `— Components` / `— Patterns` only if they help. Dark copies (`— Dark`) to the right, 80 px gap, `Color Tokens` mode set to Dark.
5. Inside the set: auto layout everywhere, Fill/Hug set deliberately, every fill/stroke/radius/gap/padding bound, text styles, `elevation/*` only on the outermost surface,
   component properties wired to the layers (text props, `Show …` booleans, instance swaps). In the set's description: `Status: draft`.
6. Check it: run `scripts/figma/inspect-components.js` (verbatim, `GROUPS` line from step 7.2) on the new set. `raw` must be 0, or explained.
   Screenshot the Variants and Reference frames in Light and Dark; fix clipping, overflow, hug-vs-fill and misalignment before showing them.

Show both screenshots, the property list and the `raw` count. **Wait for an OK.**

## 5 · Designer refines
The designer polishes in Figma. After each round they tell you, and you re-run step 4.6 (`raw` = 0, screenshots in both modes) and say what changed or broke (an unbound fill, a detached nested instance, a missing state).

## 6 · Review → checkpoint ✋
Walk the review checklist in `docs/process/new-component.md`, one line each: ✅, ❌ (what's wrong) or n/a. Measure contrast on the Reference frames with `/ds-audit`
(Light and Dark). Fix every ❌ you can (after an OK), then ask the DS owner to approve. Their approval goes in the proposal's status line.

## 7 · Document
1. `cp docs/components/_template.md docs/components/<kebab-name>.md`. Fill the hand-written sections from the proposal: one-line summary, Use it for / Don't use it for (name the alternative),
   Rules, Content, Accessibility, Figma doc drift (`none`, or each known exception). Status `beta` (`stable` only after use in 2 features), Since, Figma page, Owner.
2. AUTO block: `python3 scripts/write-component-docs.py --groups <kebab-name>=<set id>[,<sub-component id>]` prints the `GROUPS` line. Run `scripts/figma/inspect-components.js` with that line,
   save it with `python3 scripts/figma-result.py <exportedAt> scratch/new-component/<kebab-name>.json`, then `python3 scripts/write-component-docs.py scratch/new-component/<kebab-name>.json`.
3. `docs/index.md`: add the component to the link list at the top and a row to the table (Use for, Status, Page, Set ID, Set key, Key props: from the AUTO block). Remove it from "Known gaps".
4. `docs/figma-map.md`: add the page row.
5. `scripts/figma/audit.js`: add the name to `DS_NAMES`; to `TAPPABLE` if people tap it, `CONTAINER_TAPS` if the whole thing is one tap target, `CONTROLS` if its border identifies it.
6. New behaviour or usage → update the rule or pattern that covers it (`.claude/rules/*.md`, `docs/patterns/*.md`). Was it a gap in a feature's `plan.md`? Mark it resolved there.
7. New tokens → `/ds-sync` (step 3, tokens) so `tokens/*.json` and the foundations docs include them. Never hand-edit the JSON.
8. Proposal status line → `approved and built; documented in docs/components/<kebab-name>.md`.
9. Check: `python3 scripts/check-counts.py` prints `Counts match.` Then `/ds-sync` step 1 (fingerprint) shows no `NOT IN DOCS` for it.

Then suggest `/share-changes` (DS-owner review). Typical commits: `feat(tokens): …` (if any), `feat(components): add <Name>`, `docs(<area>): …` for rule or pattern updates.

## 8 · Publish (DS owner)
After the PR is merged: publish the Figma library with the same version note, run `/ds-sync`, and tell designers (`/get-latest` will show it).

## Changing an existing component
Same steps, with the proposal titled `Change: <Name>` and only the parts that change. Also:
- List where it's used (instances in the product file, `search_design_system`) and what each change does to them.
- **Breaking** (a renamed or removed prop, variant or layer that overrides depend on): commit as `feat!` with a `BREAKING CHANGE:` footer. Keep the old variant or component one release,
  mark it `deprecated` in its doc with the replacement, then remove it.
- After the change: re-run step 7.2 for its doc (`--groups <kebab-name>` finds the IDs) and suggest `/ds-audit` on product pages that use it.

## Report
In plain words: what was added or changed (component, props, tokens), the Figma page and the saved version name, the screenshots, the review result,
the repo files written, and what's left (DS-owner approval, `/ds-sync`, publishing, open points).
