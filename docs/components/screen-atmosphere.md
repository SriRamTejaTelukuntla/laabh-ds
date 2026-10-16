# Screen Atmosphere

> **Status:** beta · **Since:** unreleased (16 Oct 2026) · **Figma page:** `173:92320` · **Proposal:** [screen-atmosphere](../proposals/screen-atmosphere.md)

The Laabh screen backdrop: a fading grid in both modes, plus a top spotlight in Dark only. One mode-aware component with no props.

## Use it for
- The background of every full screen (flow steps, results, app tabs, detail screens).

## Don't use it for
- Sheets, cards, modals or popovers. They have their own surfaces (`surface/*`, `glass/*`).
- Hand-built grids or glows. Never redraw it or detach it to tweak lines.

## Rules
- One instance per screen, as the **first child** of the screen frame. Set it to absolute position at (0, 0), with constraints **left-right + top**.
- The screen frame keeps its own `surface/page` fill. The component is transparent.
- There are no variants. The frame's `Color Tokens` mode switches it: grid only in Light, grid plus spotlight in Dark. Never fake the glow in Light.
- Size is 393×852. On taller scrolling screens, keep it pinned to the top at 852 and don't stretch it. The grid fades out by about 600px.
- Width follows the frame, so it also fits a 390-wide canvas.

## Content
- None. It's decorative.

## Accessibility
- Purely decorative and behind all content. Measure text contrast against `surface/page`; the grid (≤ 6% alpha) and the spotlight don't change the AA result in a meaningful way.

## Figma doc drift
- `Column fade` (the alpha mask on the columns) has an unbound black fill. Only its alpha is used, so the colour never renders. This is accepted.
- The spotlight's fade-out gradient stop is bound to `atmosphere/spotlight-edge` (Dark `alpha/frost600-00`, #7C91B6 at 0%) since 16 Oct 2026. Bound stops take the variable's alpha, and fading to `alpha/transparent` (black) would leave a grey fringe, so it needs its own token.
- The row fade uses fixed layer opacities (1 → 0.15). No opacity tokens exist for these.
- `effect/spotlight-opacity` was deleted on 16 Oct 2026. Figma reads opacity variables on a 0–100 scale, so its Dark value of 1 gave 1%. The spotlight's colour token (`atmosphere/spotlight`, transparent in Light) is the only switch.

<!-- AUTO:START (generated from Figma by scripts/figma/inspect-components.js; do not edit by hand) -->
### Screen Atmosphere

| | |
|---|---|
| Node ID | `173:92321` (page `173:92320`) |
| Key | `c3c521d2c0d86f6869761556385c954cc83b517f` |
| Variants | 1 · default: `Screen Atmosphere` |
| Default size | 393×852 |

**Anatomy (default variant):** —

- Spotlight — fill atmosphere/spotlight, atmosphere/spotlight-edge
- Columns
  - Column fade — fill RAW
  - Column — fill atmosphere/grid
  - Column — fill atmosphere/grid
  - Column — fill atmosphere/grid
  - Column — fill atmosphere/grid
  - Column — fill atmosphere/grid
  - Column — fill atmosphere/grid
  - Column — fill atmosphere/grid
  - Column — fill atmosphere/grid
- Rows
  - Row — fill atmosphere/grid
  - Row — fill atmosphere/grid
  - Row — fill atmosphere/grid
  - Row — fill atmosphere/grid
  - Row — fill atmosphere/grid
  - Row — fill atmosphere/grid
  - Row — fill atmosphere/grid
  - Row — fill atmosphere/grid
  - Row — fill atmosphere/grid
  - Row — fill atmosphere/grid
  - Row — fill atmosphere/grid
  - Row — fill atmosphere/grid
  - Row — fill atmosphere/grid

**Colour tokens across all variants:** `atmosphere/grid` `atmosphere/spotlight` `atmosphere/spotlight-edge`
**Text styles:** — · **Effects:** —
<!-- AUTO:END -->
