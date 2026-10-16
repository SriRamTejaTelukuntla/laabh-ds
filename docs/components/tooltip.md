# Tooltip

> **Status:** stable · **Since:** v1.0 · **Figma page:** `1:22`

A short explanation of a term or metric, opened by tapping an info icon.

## Use it for
- Jargon and metrics: XIRR, P/E, market cap, LTP, circuit limits.
- Place it with `Direction` so the arrow points at the trigger (usually an `icon/info` next to the term). Max width 240.

## Rules
- Under 2 lines of description; optional title phrased as a question ("What is XIRR?").
- Opens on tap, dismisses on tap outside (`Show Close` only for longer tips).
- Never put prices, P&L or anything essential in a tooltip. It must be visible on the page.
- In Figma, show it in a separate "state" frame of the screen, not on the default screen.

## Figma doc drift
- none (Reference frame corrected 16 Oct 2026)

<!-- AUTO:START (generated from Figma by scripts/figma/inspect-components.js; do not edit by hand) -->
### Tooltip

| | |
|---|---|
| Node ID | `33:134` (page `1:22`) |
| Key | `8e91a7da4b948434551a2b6bd1442dc6346899ae` |
| Variants | 12 · default: `Direction=top-center` |
| Default size | 240×92 |

| Property | Type | Values / default |
|---|---|---|
| Show Icon | boolean | true |
| Show Title | boolean | true |
| Show Close | boolean | false |
| Title | text | What is XIRR? |
| Description | text | Your annualised return, adjusted for whe |
| Direction | variant | top-center, top-start, top-end, bottom-start, bottom-center, bottom-end, left-start, left-center, left-end, right-start, right-center, right-end (default top-center) |

**Anatomy (default variant):** pad space/10 space/12 space/12 space/12 · gap space/4 · radius radius/12 · fill surface/inverse · effect elevation/overlay

- Header — gap space/6
  - Icon → `Icon`
  - Title — text label-md/Semibold · fill text/inverse
- Description — text body-sm/Regular · fill text/inverse
- Arrow — fill surface/inverse

**Colour tokens across all variants:** `icon/inverse` `surface/inverse` `text/inverse`
**Text styles:** `body-sm/Regular` `label-md/Semibold` · **Effects:** `elevation/overlay`
<!-- AUTO:END -->
