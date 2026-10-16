# Tabs: Tab Item · Tab Bar

> **Status:** stable · **Since:** v1.0 · **Figma page:** `1:19`

Single-select chips and section tabs within a page.

## Use it for
| Style | Use |
|---|---|
| `Solid` | Filters and periods (All / Gainers / Losers, 1M / 6M / 1Y): watchlist, analysis |
| `Outline` | Secondary filters under a page title |
| `Line` | Sections inside one page (Stock detail: Overview / Technicals / News / Events) |

Bars: `Tab Bar/Solid` `24:443` · `Tab Bar/Outline` `24:504` · `Tab Bar/Line` `24:565`.

## Don't use it for
- Bottom app navigation → Navigation Bar (**not yet in the DS**; see the gap list).
- 2–3 views of the same data → Segmented Control.

## Rules
- Exactly one item selected. Never mix Solid and Outline in one row.
- Chip labels are one word ("All", "Gainers").
- Solid/Outline bars scroll horizontally when they overflow, starting at the page margin (20) and bleeding off the right edge.
- `Line` tabs span the content width and sit directly above the section they control.

## Accessibility
- Selected state changes fill **and** label colour (Line: label weight + 2px indicator).

## Figma doc drift
- none (Reference frame corrected 16 Oct 2026)

<!-- AUTO:START (generated from Figma by scripts/figma/inspect-components.js; do not edit by hand) -->
### Tab Item

| | |
|---|---|
| Node ID | `24:442` (page `1:19`) |
| Key | `88097b74fa0c97717b2dd0dcef9415c86d4403a0` |
| Variants | 30 · default: `Style=Solid, State=Default, Size=sm` |
| Default size | 48×32 |

| Property | Type | Values / default |
|---|---|---|
| Label | text | Tab |
| Leading icon | boolean | false |
| Trailing | boolean | false |
| Trailing swap | instance_swap | 17:254 |
| Style | variant | Solid, Outline, Line (default Solid) |
| State | variant | Default, Hover, Selected, Disabled, Focus (default Default) |
| Size | variant | sm, md (default sm) |

| Size | H | Specs (default variant at that size) |
|---|---|---|
| sm | 32 | pad space/0 space/12 space/0 space/12 · gap space/6 · radius radius/full · fill glass/control · stroke glass/hairline 1px · effect elevation/control |
| md | 36 | pad space/0 space/16 space/0 space/16 · gap space/6 · radius radius/full · fill glass/control · stroke glass/hairline 1px · effect elevation/control |

**Anatomy (default variant):** pad space/0 space/12 space/0 space/12 · gap space/6 · radius radius/full · fill glass/control · stroke glass/hairline 1px · effect elevation/control

- Label — text body-sm/Medium · fill text/secondary

**Colour tokens across all variants:** `border/brand` `border/default` `border/neutral` `border/subtle` `focus/ring` `glass/control` `glass/hairline` `glass/selected` `icon/brand` `icon/disabled` `icon/primary` `icon/secondary` `icon/static-white` `surface/brand` `surface/brand-subtle` `surface/neutral-subtle` `text/brand` `text/disabled` `text/neutral` `text/primary` `text/secondary` `text/static-white`
**Text styles:** `body-sm/Medium` `caps-md/Semibold` `label-md/Medium` · **Effects:** `elevation/control`

### Tab Bar/Solid

| | |
|---|---|
| Node ID | `24:443` (page `1:19`) |
| Key | `56e03ec0b8f776dac953b1a8466bcd4fda8605ed` |
| Variants | 1 · default: `Tab Bar/Solid` |
| Default size | 250×26 |

**Anatomy (default variant):** gap space/8

- Tab Item → `Tab Item` — pad space/0 space/12 space/0 space/12 · gap space/6 · radius radius/full · fill surface/brand
- Tab Item → `Tab Item` — pad space/0 space/12 space/0 space/12 · gap space/6 · radius radius/full · fill glass/control · stroke glass/hairline 1px · effect elevation/control
- Tab Item → `Tab Item` — pad space/0 space/12 space/0 space/12 · gap space/6 · radius radius/full · fill glass/control · stroke glass/hairline 1px · effect elevation/control
- Tab Item → `Tab Item` — pad space/0 space/12 space/0 space/12 · gap space/6 · radius radius/full · fill glass/control · stroke glass/hairline 1px · effect elevation/control

**Colour tokens across all variants:** `border/neutral` `glass/control` `glass/hairline` `icon/secondary` `icon/static-white` `surface/brand` `surface/neutral-subtle` `text/neutral` `text/secondary` `text/static-white`
**Text styles:** `body-sm/Medium` `caps-md/Semibold` · **Effects:** `elevation/control`
<!-- AUTO:END -->
