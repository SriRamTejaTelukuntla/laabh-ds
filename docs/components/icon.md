# Icon

> **Status:** stable · **Since:** v1.0 · **Figma page:** `1:6`

The icon wrapper: one component set that sizes any Lucide glyph and sets its stroke. Every DS component that shows an icon uses it.

## Use it for
Place `Icon`, pick `Size`, and swap `Glyph` to any `icon/<lucide-name>` component (the Figma description also allows `icon-fill/…`).

| Size | Stroke | Uses on Selected Screens (Oct 2026) |
|---|---|---|
| 10 | 1.25 | 0 |
| 12 | 1.5 | 36 |
| 14 | 1.75 | 60 |
| 16 | 2 | 198 |
| 20 | 2 | 118 |
| 24 | 2 | 5 |
| 28 | 2 | 30 |
| 32 | 2 | 0 |

The stroke keeps the 16 px ratio (2/16) below 16 and stays 2 from 16 up.

## Don't use it for
- An icon-only action → `Icon Button` (or `Compact Button` for 16–24 inline actions). They contain the Icon and the tap area.
- A raw `icon/*` glyph placed on its own → wrap it in `Icon`, so size and stroke follow the rule above.

## Rules
- Colour comes from the glyph (`icon/primary`). To change it, override the colour on the instance with another `icon/*` token (`icon/secondary`, `icon/brand`, …). Never a `text/*` token or a raw colour.
- Keep the glyph inside the frame: don't resize an instance by hand, change `Size`.
- Gain/loss arrows use `icon/success` / `icon/danger` only together with a sign or label (`TR-NUM-01`).

## Accessibility
- Next to a text label it's decorative: the label carries the meaning.
- Icon-only controls (`Icon Button`) need an accessible name in the handoff (`AN-03`).
- An icon that carries meaning on its own (status, error, selection) needs 3:1 against what's behind it (WCAG 1.4.11) and a text equivalent. Never colour alone.

## Figma doc drift
<!-- Differences between what the Figma Reference frame says and what the component actually binds. Remove when fixed. -->
- The default variant is `Size=10` (the first in the set), but the most used sizes are 16 and 20. The review checklist wants the most common variant as the default: a DS owner can move `Size=16` first.
- The Icons page has no `Icon — Reference` frame; the set's description is its only documentation in Figma.

<!-- AUTO:START (generated from Figma by scripts/figma/inspect-components.js; do not edit by hand) -->
### Icon

| | |
|---|---|
| Node ID | `9:194` (page `1:6`) |
| Key | `95ec73f49124285338b2b89dc65fc610480657ac` |
| Variants | 8 · default: `Size=10` |
| Default size | 10×10 |

| Property | Type | Values / default |
|---|---|---|
| Glyph | instance_swap | 101:76895 |
| Size | variant | 10, 12, 14, 16, 20, 24, 28, 32 (default 10) |

| Size | H | Specs (default variant at that size) |
|---|---|---|
| 10 | 10 |  |
| 12 | 12 |  |
| 14 | 14 |  |
| 16 | 16 |  |
| 20 | 20 |  |
| 24 | 24 |  |
| 28 | 28 |  |
| 32 | 32 |  |

**Anatomy (default variant):** —

- Glyph → `icon/circle-dashed`

**Colour tokens across all variants:** `icon/primary`
**Text styles:** — · **Effects:** —
<!-- AUTO:END -->
