---
name: ds-audit
description: Check Figma screens against the repo's rules, read-only. Finds raw values (colour, radius, spacing, text, effects not bound to tokens), detached or drawn copies of DS components, missing Status Bar / Home Indicator / Screen Atmosphere, missing or mismatched Light/Dark copies, measured contrast in both modes, and tap targets under 44 pt. Writes a plain-language report with node IDs and counts. Use when someone pastes a Figma link and asks to "audit", "check this follows the system", "check contrast" or "are these tokens", before handoff, and when /design-review or /prd-to-screens hands over contrast pairs or raw-value nodes.
argument-hint: "<Figma link or node ID> [more links]"
---

# /ds-audit

Check screens against `.claude/rules/` and report. **Read-only:** it never changes Figma. Fixes are offered, and made only after the person says yes.
It's the mechanical half of review. Judgement (flows, copy, states, annotations) is `/design-review`, which hands its contrast pairs and raw-value nodes here.

## What it checks

| Check | Rule | Base severity |
|---|---|---|
| Text contrast: 4.5:1, or 3:1 for large text (≥ 24 px, or ≥ 19 px bold), measured per mode | `accessibility.md` · WCAG 1.4.3 | S2 |
| Field, checkbox and radio borders, control glyphs, icon-only button icons, focus rings: 3:1 | `accessibility.md` · WCAG 1.4.11 | S2 |
| Tap targets: under 24 → S2 (WCAG 2.5.8); under 44 pt → S3 (house rule), S2 on a Solid (primary) Button; primary Button under 48 with no 48 dp annotation → S3 (`D-04`) | `accessibility.md` | S2–S3 |
| Frame named Light but renders Dark (or the reverse) · Light screen with no Dark copy | `light-dark.md` | S2 |
| Fill or stroke not bound to a `Color Tokens` variable, or bound to a primitive or another library | `tokens.md` | S3 |
| Radius not `radius/*`, padding or gap not `space/*`, shadow or blur without an `elevation/*` style | `tokens.md` | S3 |
| Text without a text style · `mono/*` in a screen · a style that isn't in `tokens/styles.*.json` | `typography.md` | S3 |
| Frame detached from a component · plain frame named like a DS component · instance of a missing or Sandbox component | `components.md` | S3 |
| No Screen Atmosphere as the first layer, no Status Bar, no Home Indicator | `components.md`, `layout.md` | S3 |
| Dark copy with no Light · Light and Dark with different layer counts · two screens with the same name | `light-dark.md`, `naming.md` | S3 |
| Frame not 390 wide or under 844 tall · frame fill not `surface/page` · name or section-name format · loose instance outside a screen | `layout.md`, `naming.md` | S4 |

Inside an instance, only what the screen overrides is checked. A component's own values are the library's business (`/ds-sync` reports them).
Findings that live inside a DS component (its tap size, its own border or text pairing) are listed once, under "Inside DS components".
`/design-review` may raise a severity: order or funds flow, first-run flow, or repeated on 3+ screens (`docs/ux/ux-governance.md` §3).

**Exemptions** (in the script's `EXEMPT` list, from each doc's "Figma doc drift" section): Status Bar `Time` is unstyled by design (`docs/components/system-components.md`).
Also not measured: disabled controls and `text/disabled`, text under a scrim or sheet, huge faint watermark glyphs (≥ 48 px, ≤ 20% opacity), and text over images (listed "to measure by hand").

## Rules
- **Read-only.** No edits to nodes, styles, variables or components while auditing. Fixing is a separate step that needs the person's OK.
- Run `scripts/figma/audit.js` **verbatim**: Read the file and pass its content to `figma_execute` / `use_figma`. Change only the `TARGET` and `FROM` lines.
- **Never hand-copy the result.** Save it with `scripts/figma-result.py` into `scratch/ds-audit/` (git-ignored). Big results are saved to a file by Claude Code; that's expected.
- **Verify before you report.** Look at the top S2 findings (screenshot the node, or read its fills) before calling them real. Say so plainly when one is a false positive, and fix the script if you can.
- Contrast failures are fixed by **choosing a different semantic token** (`docs/foundations/colors.md`), never by editing variable values.
- Never edit DS masters from a product task. A finding under "Inside DS components" goes to a DS owner (`/new-component` to change the component).

## 0 · Preflight
1. Get the target from the link. `fileKey` is the part after `/design/`; the node is `node-id=101-129022` → `101:129022`. No `node-id`? Ask which page or frame.
   One page, section or frame per run is best. Several are fine: `TARGET = ['1:2', '3:4']`.
2. Which file: the DS file is `mmAhXn4vJKlmuThcAMgGss`; each feature has its own file (link in `prds/<feature>/plan.md`, list in `docs/figma-map.md` § Feature files).
   For a feature file: Scripts can't see pending library updates, so ask: does the file show **Library updates available** (Assets panel)? If yes, have it accepted (Review → Update all) first, or the audit measures the old version. In a feature file, styles and variables come from the library, so the
   report checks their keys against `tokens/` (anything else is "from another library").
3. Connect:
   - **figma-console** (DS owners): `figma_navigate` with the file URL and `lock: true`. Call `figma_execute` with `fileKey` and `timeout: 30000`.
   - **Official Figma plugin**: load the `figma:figma-use` skill, then call `use_figma` with the same fileKey.

## 1 · Run
1. Read `scripts/figma/audit.js`. Set `const TARGET = [...]` to the node IDs and keep `FROM = 0`. Run it.
2. Save the result:
   - Shown inline: `python3 scripts/figma-result.py <exportedAt> scratch/ds-audit/run-0.json`.
   - Too large and saved to a file (the tool says where): `python3 scripts/figma-result.py exportedAt scratch/ds-audit/run-0.json --transcript <that file>`.
3. Check `file` is the file you meant. If `next` isn't `null`, the time budget ran out: run again with `FROM = <next>`, save as `run-1.json`, and repeat until `next` is `null`.
   (About 20 screens a second, so most pages finish in one run.)

## 2 · Report
1. `python3 scripts/audit-report.py scratch/ds-audit/run-*.json` writes `scratch/ds-audit/report.md` and prints a summary.
   For a feature, add `--out prds/<feature>/audit.md` so it's saved with the plan.
2. If it says **INCOMPLETE**, run the missing batch first.
3. Read the report. Verify the S2 findings (rules above) and note anything you think is wrong.

## 3 · Tell the person
In plain words, short:
- How many screens, and the counts by severity.
- The contrast failures (which text or border, on what, in which mode, the ratio), and the token that would fix each, if one clearly fits.
- Systemic issues (same problem on 3+ screens): one line each, they're the cheapest wins.
- What goes to a DS owner (the "Inside DS components" list).
- What wasn't checked (exemptions, "to measure by hand", hit areas larger than the component).
- Link the report file. Then **offer** fixes as a short list ("bind `Title` fill on A06 Dark to `text/primary`") and ask before changing anything.

When fixing (after an OK): the feature's file only, one screen per call, screenshot Light and Dark after, re-run the audit on that frame.

## Hand-offs from /design-review
`/design-review` lists pairs and nodes "to measure" under *Notes for the team* (`docs/ux/ux-governance.md` §9). Run the audit on the frames those come from, then answer
each pair from the report's "Contrast pairs measured" table (ratio, pass or fail, per mode) and each node from the findings. A pair not in the table wasn't rendered on those frames: say so.

## How it measures
- **Colours** are resolved per frame mode (`resolveForConsumer`) and composited over every layer painted behind the text: glass and alpha fills, scrims, sheets.
  Screen Atmosphere and background blur are left out; gradients are averaged and marked *approximate*.
- **Large text** is ≥ 24 px, or ≥ 19 px at weight 700+. Mixed text is measured per run of characters; gradient text uses its worst stop.
- **UI parts** are judged against what's outside them. A control whose own fill already stands out 3:1 passes even with a faint border.
- **Hit targets** are the component's bounds, or a wrapper frame holding only it. A bigger tappable parent, or spacing between small targets (WCAG's spacing exception), isn't seen.

## Gotchas
- Figma copies a bound colour's alpha into `paint.opacity`. Multiply both and an 8% hairline becomes 0.6%: the script uses the variable's alpha only.
- `strokeWeight` and `cornerRadius` can be `figma.mixed` (a symbol); compare them only after a type check.
- The file uses dynamic page loading: use the async APIs (`getNodeByIdAsync`, `getMainComponentAsync`) and `page.loadAsync()`.
- Keep `DS_NAMES`, `TAPPABLE` and `EXEMPT` in the script in step with `docs/index.md` and the components' "Figma doc drift" notes when components change.
