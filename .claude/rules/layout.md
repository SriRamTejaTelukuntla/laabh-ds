# Rule: layout

Verified against the DS file in Oct 2026.

**Screen frame**
- Canvas **390×844** (default). Full-height scroll screens grow in height; keep the width fixed.
- Stack, top to bottom: `Status Bar` (48) → header (`App Header` 48/56 in the app, `Top Bar` 68 in onboarding/flows) → body → footer/CTA → `Home Indicator` (34).
- Frame fill `surface/page`. A `Screen Atmosphere` instance is the first child: absolute at (0,0), constraints left-right + top.
- Everything uses **auto layout**. Children that span the width use *Fill container*, not fixed widths.

**Spacing**
| Use | Token |
|---|---|
| Page side margin | `space/20` |
| Card padding | `space/20` (compact rows/cards: `space/14`–`space/16`) |
| Between sections | `space/24` (major break after a hero: `space/32`) |
| Section header inset from the card edge | `space/4` |
| Inside a list/card stack | `space/8`–`space/12` |
| Form body (heading and fields) | `space/24` |

**Radius by size**
| Element | Radius |
|---|---|
| Cards, option cards, alerts | `radius/18` |
| Buttons xs / sm / md / lg / xl | `radius/8` / `10` / `12` / `12` / `14` |
| Fields sm / md / lg | `radius/10` / `12` / `14` |
| Pills, chips, segmented thumbs | `radius/full` |
| Bottom sheet | `radius/40`, floating with an 8px inset from the screen edges (iOS style) |

**Controls**
- Button heights: xs 28, sm 32, md 40, **lg 52**, xl 56. The primary screen CTA is `lg`, full width inside the page margin.
- Icon Button heights match Buttons: 28 / 32 / 40 / 52 / 56.
- Text fields: field heights sm 40 / md 52 / lg 56 (radius 10 / 12 / 14). Forms use `md` (matches the lg CTA); a single hero input uses `lg`. Input text is 16px (`label-lg/Regular`).
- Minimum hit target 44×44 (see the accessibility rule).
