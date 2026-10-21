# List Row

> **Status:** beta · **Since:** v1.1 · **Figma page:** `261:2` · **Owner:** @DS-OWNER

One row in a list: a leading Avatar or Icon Tile, a title and description, an optional value and an optional action.

## Use it for
- Lists of people or items with a value: nominees with their share, linked accounts.
- Feature highlights with an Icon Tile (Welcome).

## Don't use it for
- Label/value details → Summary Card.
- A choice the user makes → Option Card.
- Settings → Switch Row.

## Rules
- Swap `Leading` between Avatar (people, companies) and Icon Tile (features, states); set the Avatar's initials on the exposed instance.
- `Value` uses num-label-md: shares, amounts, counts (with ₹ and Indian grouping, `TR-NUM`).
- Stack rows inside a card with no gap; turn `Show divider` off on the last row.

## Content
- Title: name or short noun phrase. Description: one line of context ("Brother · PAN ••••678L").

## Accessibility
- At least 64 pt tall. When the whole row is tappable, annotate it as one button; otherwise name each action ("Edit Rohan Sharma", `AN-03`) with a 44 pt hit area (`AN-11`).
- Avatar initials are decorative when the title names the person (`AN-08`).

## Figma doc drift
- none

<!-- AUTO:START (generated from Figma by scripts/figma/inspect-components.js; do not edit by hand) -->
### List Row

| | |
|---|---|
| Node ID | `261:3` (page `261:2`) |
| Key | `8a9e007efa03ad8194019442294831f2c8c241c2` |
| Variants | 1 · default: `List Row` |
| Default size | 350×65 |

| Property | Type | Values / default |
|---|---|---|
| Leading | instance_swap | 19:8 |
| Show leading | boolean | true |
| Title | text | Title |
| Description | text | Supporting text |
| Show description | boolean | true |
| Value | text | 100% |
| Show value | boolean | true |
| Show action | boolean | true |
| Show divider | boolean | true |

**Anatomy (default variant):** —

- Row — pad space/12 0 space/12 0 · gap space/12
  - Leading → `Avatar` — radius radius/full · fill surface/brand-subtle · stroke border/brand-subtle 1px
  - Text — gap space/2
    - Title — text label-md/Medium · fill text/primary
    - Description — text body-sm/Regular · fill text/secondary
  - Value — text num-label-md/Medium · fill text/primary
  - Action → `Button` — pad space/0 space/12 space/0 space/12 · gap space/6 · radius radius/10
- Divider — fill glass/hairline

**Colour tokens across all variants:** `border/brand-subtle` `glass/hairline` `surface/brand-subtle` `text/brand` `text/brand-strong` `text/primary` `text/secondary`
**Text styles:** `body-lg/Semibold` `body-sm/Regular` `body-sm/Semibold` `label-md/Medium` `num-label-md/Medium` · **Effects:** —
<!-- AUTO:END -->
