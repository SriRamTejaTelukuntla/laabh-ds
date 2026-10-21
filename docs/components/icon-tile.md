# Icon Tile

> **Status:** beta · **Since:** v1.1 · **Figma page:** `259:2` · **Owner:** @DS-OWNER

A round, tinted tile that holds one status or feature icon: the hero of result screens and the leading mark in rows and highlights.

## Use it for
- Result and waiting screens (Submitted, Verifying, KYC found, PAN blocked): `Size=64` above the title.
- Leading mark in a List Row or a highlights list (Welcome): `Size=40`.

## Don't use it for
- A person or company → Avatar.
- A tappable icon → Icon Button.
- Inline status inside text → Badge or Alert.

## Rules
- `Tone` matches the meaning: Brand (in progress, neutral info), Success (done), Warning (waiting, needs a check), Danger (failed, blocked), Neutral (no state).
- Swap the glyph on the exposed `Icon` (Lucide `icon/*`). Never recolour the tile or the icon by hand: the tone does both.
- One Icon Tile per result screen, centred above the Step Heading (8 px gap).

## Content
- The title next to it carries the meaning; the tile only reinforces it.

## Accessibility
- Decorative by default (`AN-08`): the screen title says the same thing. Icon contrast on its tint is ≥ 4.16:1 Light, ≥ 5.61:1 Dark.

## Figma doc drift
- none

<!-- AUTO:START (generated from Figma by scripts/figma/inspect-components.js; do not edit by hand) -->
### Icon Tile

| | |
|---|---|
| Node ID | `259:176` (page `259:2`) |
| Key | `97890c3a90f244f709ce8072a2294aa0e578625c` |
| Variants | 10 · default: `Tone=Brand, Size=64` |
| Default size | 64×64 |

| Property | Type | Values / default |
|---|---|---|
| Tone | variant | Brand, Success, Warning, Danger, Neutral (default Brand) |
| Size | variant | 40, 64 (default 64) |

| Size | H | Specs (default variant at that size) |
|---|---|---|
| 40 | 40 | radius radius/full · fill surface/brand-subtle · stroke border/brand-subtle 1px |
| 64 | 64 | radius radius/full · fill surface/brand-subtle · stroke border/brand-subtle 1px |

**Anatomy (default variant):** radius radius/full · fill surface/brand-subtle · stroke border/brand-subtle 1px

- Icon → `Icon`

**Colour tokens across all variants:** `border/brand-subtle` `border/success-subtle` `icon/brand` `surface/brand-subtle` `surface/danger-subtle` `surface/subtle` `surface/success-subtle` `surface/warning-subtle`
**Text styles:** — · **Effects:** —
<!-- AUTO:END -->
