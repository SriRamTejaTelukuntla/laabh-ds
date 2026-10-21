# Segmented Control · Segment

> **Status:** stable · **Since:** v1.0 · **Figma page:** `1:16`

Switch between 2–3 mutually exclusive views of the same content, in place.

## Use it for
- Chart ranges and views (1D / 1W / 1M), Buy/Sell form switching on the order ticket, Delivery/Intraday.
- Bars: `Segmented Control/<Neutral|Brand>/<sm|md>` (`Show segment 3` for a third option). `Neutral` by default; `Brand` only when the choice is the screen's primary control.

## Don't use it for
- Navigating between screens → bottom navigation (not yet a DS component).
- Sibling content sections with their own content → Tabs.
- Filters with 4+ options → Tab Bar/Solid chips.

## Rules
- Order ticket: the segmented control only switches the form. The Buy/Sell CTA is a `Button` `Solid · Success/Danger`.
- Segments share the width equally; labels are 1–2 words.

## Accessibility
- The selected segment uses a thumb (fill + `elevation/thumb`) **and** a stronger label colour.

## Figma doc drift
- `md` controls are 44 tall since 19 Oct 2026; `sm` stays for dense, non-primary filters. Open: the `Segment` `md` variant is 32 tall in Figma, while the proposal says segments are 38 and this note said 36. Confirm each option has a 44 pt tap area (`docs/proposals/mf-kyc-ds-updates.md`).

<!-- AUTO:START (generated from Figma by scripts/figma/inspect-components.js; do not edit by hand) -->
### Segment

| | |
|---|---|
| Node ID | `23:106` (page `1:16`) |
| Key | `1ff503e5f9fcffcc73873342dcc96b56fea046c9` |
| Variants | 20 · default: `Style=Neutral, State=Default, Size=sm` |
| Default size | 76×28 |

| Property | Type | Values / default |
|---|---|---|
| Label | text | Segment |
| Leading icon | boolean | false |
| Style | variant | Neutral, Brand (default Neutral) |
| State | variant | Default, Hover, Selected, Disabled, Focus (default Default) |
| Size | variant | sm, md (default sm) |

| Size | H | Specs (default variant at that size) |
|---|---|---|
| sm | 28 | pad space/0 space/12 space/0 space/12 · gap space/6 · radius radius/full |
| md | 32 | pad space/0 space/16 space/0 space/16 · gap space/6 · radius radius/full |

**Anatomy (default variant):** pad space/0 space/12 space/0 space/12 · gap space/6 · radius radius/full

- Label — text body-sm/Medium · fill text/secondary

**Colour tokens across all variants:** `focus/ring` `glass/selected` `glass/thumb` `surface/brand` `text/disabled` `text/primary` `text/secondary` `text/static-white`
**Text styles:** `body-sm/Medium` · **Effects:** `elevation/thumb`

### Segmented Control/Neutral/md

| | |
|---|---|
| Node ID | `23:107` (page `1:16`) |
| Key | `ee87b0ca3cb90a4343e29feba3fbb895f43aef8a` |
| Variants | 1 · default: `Segmented Control/Neutral/md` |
| Default size | 197×44 |

| Property | Type | Values / default |
|---|---|---|
| Show segment 3 | boolean | false |

**Anatomy (default variant):** pad space/3 · radius radius/full · fill glass/track · stroke glass/edge 1px

- Segment → `Segment` — pad space/0 space/16 space/0 space/16 · gap space/6 · radius radius/full · fill glass/thumb · effect elevation/thumb
- Segment → `Segment` — pad space/0 space/16 space/0 space/16 · gap space/6 · radius radius/full

**Colour tokens across all variants:** `glass/edge` `glass/thumb` `glass/track` `text/primary` `text/secondary`
**Text styles:** `body-sm/Medium` · **Effects:** `elevation/thumb`
<!-- AUTO:END -->

Other bars: `Segmented Control/Neutral/sm` `23:127` · `Segmented Control/Brand/md` `23:147` · `Segmented Control/Brand/sm` `23:167`
