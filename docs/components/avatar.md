# Avatar

> **Status:** stable · **Since:** v1.0 · **Figma page:** `1:10`

A circular image, initials or icon representing a person or a company.

## Use it for
| Type | When |
|---|---|
| `Initials` | The account owner (brand-subtle fill), nominees, contacts |
| `Image` | Company and fund logos. The image fills the circle edge to edge |
| `Icon` | Nothing to show yet (glass fill) |

| Size | Where |
|---|---|
| 24 | Dense tables, nav bar |
| 32 | Comments, research cards |
| 36 | Watchlist and holdings rows |
| 40 | Profile header |

## Don't use it for
- Generic icons in lists → an `icon/*` inside the row.

## Rules
- Logos stay circular with the glass edge. Never crop to a square or tint a logo.
- Maximum 2 initials, uppercase.
- Logo + name row pattern: Avatar 36 · gap 12 · name `label-md/Medium` · company `body-sm/Regular` in `text/secondary`.

## Accessibility
- Initials use `text/brand-strong` on `surface/brand-subtle` (5.70:1 Light, 8.39:1 Dark) since 19 Oct 2026. When a name sits next to the avatar, mark the avatar decorative (`AN-08`).
- Decorative when a name sits next to it. Otherwise the layer name carries the person's/company's name.

## Figma doc drift
- none

<!-- AUTO:START (generated from Figma by scripts/figma/inspect-components.js; do not edit by hand) -->
### Avatar

| | |
|---|---|
| Node ID | `19:34` (page `1:10`) |
| Key | `b1a58854a34b70cbc7e3207debd0a77807be2831` |
| Variants | 12 · default: `Type=Initials, Size=24` |
| Default size | 24×24 |

| Property | Type | Values / default |
|---|---|---|
| Initials | text | PG |
| Type | variant | Initials, Image, Icon (default Initials) |
| Size | variant | 24, 32, 36, 40 (default 24) |

| Size | H | Specs (default variant at that size) |
|---|---|---|
| 24 | 24 | radius radius/full · fill surface/brand-subtle · stroke border/brand-subtle 1px |
| 32 | 32 | radius radius/full · fill surface/brand-subtle · stroke border/brand-subtle 1px |
| 36 | 36 | radius radius/full · fill surface/brand-subtle · stroke border/brand-subtle 1px |
| 40 | 40 | radius radius/full · fill surface/brand-subtle · stroke border/brand-subtle 1px |

**Anatomy (default variant):** radius radius/full · fill surface/brand-subtle · stroke border/brand-subtle 1px

- Initials — text caption/Semibold · fill text/brand-strong

**Colour tokens across all variants:** `border/brand-subtle` `glass/control` `surface/brand-subtle` `text/brand-strong`
**Text styles:** `body-lg/Semibold` `body-sm/Semibold` `caption/Semibold` `label-md/Semibold` · **Effects:** —
<!-- AUTO:END -->
