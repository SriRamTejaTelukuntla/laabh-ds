# Proposal: Screen Atmosphere

> **Status:** approved and built; documented in [docs/components/screen-atmosphere.md](../components/screen-atmosphere.md). Built in Figma (page `173:92320`, component `173:92321`) · **Proposed:** 16 Oct 2026 · **Section:** PRODUCT COMPONENTS · **Source design:** Sandbox `173:92251`

The Laabh backdrop: a fading grid, plus a top spotlight in Dark mode only. It sits on top of the frame's `surface/page` fill and behind all content.

## Why
- It appears on every full screen. Today it's a hand-built `Screen Atmosphere` frame (25 layers) copied into each screen on Selected Screens.
- Copies drift. The Sandbox "App bg - Dark" frame has lines bound to `surface/card` and `surface/neutral-subtle`, and the spotlight is a raw hex.

## Light / Dark: one mode-aware component, no variants
| Layer | Light | Dark | How |
|---|---|---|---|
| Grid lines | Navy hairlines | Frost hairlines | Fill `atmosphere/grid` |
| Spotlight | Hidden | Visible glow at the top | Fill `atmosphere/spotlight` (transparent in Light) |

Toggling a frame's `Color Tokens` mode switches the background. There's no variant to swap.

## Anatomy (393×852, transparent fill, clip content)
| Layer | Spec |
|---|---|
| `Spotlight` | Ellipse 520×420 at (−63, −250), radial gradient from `atmosphere/spotlight` at 0 to `atmosphere/spotlight-edge` at 1. Constraint: centre |
| `Columns` (8) | 1×852 at x = 20 + 48n, solid `atmosphere/grid`. A `Column fade` alpha mask (100% → 50% at 0.6 → 0%) fades them, because bound gradient stops take the variable's alpha and can't fade. Constraint: left, top |
| `Rows` (17) | 393×1 at y = 40 + 48n. Fill `atmosphere/grid`. Layer opacity fades down the screen: 1, .87, .80, .73, .67, .60, .53, .47, .40, .33, .25, .18, then .15 ×5. Constraint: left-right, top |

Layer order is spotlight, then columns, then rows (the same order as the source design).

## Properties
None. It is decorative, and its only behaviour comes from the mode.

## Usage rules
- Every full screen gets one instance as the **first child** of the screen frame. It is absolute-positioned at (0, 0), constrained left-right and top, behind the Status Bar.
- The screen frame keeps its own `surface/page` fill. The component is transparent.
- Tall scrolling screens: the component stays pinned to the top at 852 tall and doesn't stretch. The grid has faded out by about 600px, so the area below is plain page colour.
- Width follows the frame (left-right constraint), so it also fits the 390-wide canvas.
- Not inside sheets, cards or modals. Those have their own surfaces.

## Tokens
| Value | Token | Status |
|---|---|---|
| Grid line colour | `atmosphere/grid` (Light `alpha/slate-06`, Dark `alpha/frost-06`) | exists |
| Spotlight colour #7C91B6 @ 50% | **`atmosphere/spotlight`**: Light `alpha/transparent`, Dark new primitive **`alpha/frost600-50`** `#7c91b680` | **created** (approved) |
| Spotlight fade-out stop | Same colour at 0% alpha (keeps the edge clean, with no grey fringe): **`atmosphere/spotlight-edge`**: Light `alpha/transparent`, Dark new primitive **`alpha/frost600-00`** `#7c91b600` | **created** 16 Oct 2026 (was an unbound exception) |
| Column fade mask | Black alpha ramp, unbound. It's a mask, so only its alpha is used and the colour never renders | exception, documented |
| Row fade opacities | Fixed layer opacities (decorative). No opacity tokens exist for these | exception, documented |

Primitive naming follows `alpha/ink850-82`. Once it's created, the same token replaces the raw spotlight colour everywhere it appears, including the Selected Screens instances.

## Figma plan
1. Save a named version: "Before Screen Atmosphere". ✅
2. Create the variables `alpha/frost600-50` (Color Primitives) and `atmosphere/spotlight` (Color Tokens). ✅
3. Add a new page `↳ Screen Atmosphere` under PRODUCT COMPONENTS, after App Header. ✅
4. Frames: `Screen Atmosphere — Components` holds the master. `Screen Atmosphere — Reference` shows the component behind a sample screen, with notes. Each has a `— Dark` copy to the right, set to Dark mode. ✅ (on the page: Components 0, Reference 1020, Dark copies at 2320 and 3340)
5. Screenshot both modes and check them. ✅
6. Replace the hand-built `Screen Atmosphere` layers on Selected Screens with instances. ✅ All 118 screens swapped (version saved first: "Before Screen Atmosphere rollout"). A19 Review's stretched 1669-tall frame is now pinned at 852.

## Open points
- ~~`effect/spotlight-opacity` is set to 1 in Dark, but Figma reads opacity variables on a 0–100 scale, so binding it gives 1%.~~ Resolved 16 Oct 2026: deleted (version "Before deleting effect/spotlight-opacity" saved first). Its only bindings were 47 draft `Spotlight` ellipses on `↳ Ignore_Sandbox`; they were unbound and kept their opacity.
- 393×852 differs from the 390×844 canvas in `.claude/rules/layout.md`. The left-right constraint makes it fit both widths. The canvas rule stays as it is.
