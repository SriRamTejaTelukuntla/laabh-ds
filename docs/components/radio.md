# Radio · Radio Group

> **Status:** stable · **Since:** v1.0 · **Figma page:** `1:15`

Pick exactly one option from a short list of short labels.

## Use it for
- 2–5 short, parallel options (order type, gender, marital status). Always inside a **Radio Group** with a `Legend`.
- `Direction=Horizontal` for 2–3 very short options; otherwise `Vertical`.

## Don't use it for
- 6+ options → Dropdown. Options that need explanation → Option Card. On/off → Switch.

## Rules
- Pre-select the safest option when there's a sensible default (Delivery over Intraday).
- Keep labels parallel and short.
- In screens set it to **Fill container**: `Label` and `Description` then wrap. The master keeps its narrow default width, so a hugging instance doesn't wrap. `Direction=Vertical` items fill the group; horizontal items hug.
- Show validation with `Show error` + `Error` text, not by colouring items.

## Accessibility
- Row hit area ≥ 44pt; the label is tappable. Focus: 2px `focus/ring`, 2px gap.

## Figma doc drift
- With `Required` on and the component filling the width, the asterisk sits at the end of the label's first line (the label fills the row so it can wrap). Accepted 19 Oct 2026.

<!-- AUTO:START (generated from Figma by scripts/figma/inspect-components.js; do not edit by hand) -->
### Radio

| | |
|---|---|
| Node ID | `21:118` (page `1:15`) |
| Key | `2c88d3e9a1220fc01673502703f3e34de8c687cd` |
| Variants | 16 · default: `Selection=Unselected, State=Default, Size=sm` |
| Default size | 60×18 |

| Property | Type | Values / default |
|---|---|---|
| Show label | boolean | true |
| Label | text | Label |
| Show description | boolean | false |
| Description | text | Supporting description |
| Required | boolean | false |
| Selection | variant | Unselected, Selected (default Unselected) |
| State | variant | Default, Hover, Focus, Disabled (default Default) |
| Size | variant | sm, md (default sm) |

| Size | H | Specs (default variant at that size) |
|---|---|---|
| sm | 18 | gap space/8 |
| md | 20 | gap space/10 |

**Anatomy (default variant):** gap space/8

- Control — radius radius/full · fill glass/field · stroke border/strong 1.5px
- Text — gap space/2
  - Label row — gap space/2
    - Label — text label-md/Regular · fill text/primary

**Colour tokens across all variants:** `border/brand` `border/hover` `border/strong` `focus/ring` `glass/field` `surface/brand` `surface/brand-hover` `surface/disabled` `surface/static-white` `text/danger` `text/disabled` `text/primary` `text/secondary`
**Text styles:** `body-lg/Regular` `body-sm/Regular` `label-md/Regular` · **Effects:** —

### Radio Group

| | |
|---|---|
| Node ID | `21:189` (page `1:15`) |
| Key | `6bcbb8e7923c093b0ec01b4d5d1c7881becafd62` |
| Variants | 2 · default: `Direction=Vertical` |
| Default size | 249×142 |

| Property | Type | Values / default |
|---|---|---|
| Show legend | boolean | true |
| Legend | text | Order type |
| Required | boolean | false |
| Show item 3 | boolean | true |
| Show item 4 | boolean | false |
| Show helper | boolean | true |
| Helper | text | Market orders fill at the best available |
| Show error | boolean | false |
| Error | text | ⚠ Choose an order type |
| Direction | variant | Vertical, Horizontal (default Vertical) |

**Anatomy (default variant):** gap space/12

- Legend row — gap space/2
  - Legend — text label-md/Medium · fill text/primary
- Items — gap space/12
  - Item 1 → `Radio` — gap space/10
  - Item 2 → `Radio` — gap space/10
  - Item 3 → `Radio` — gap space/10
- Helper — text body-sm/Regular · fill text/secondary

**Colour tokens across all variants:** `border/strong` `glass/field` `surface/brand` `surface/static-white` `text/danger` `text/primary` `text/secondary`
**Text styles:** `body-lg/Regular` `body-sm/Medium` `body-sm/Regular` `label-md/Medium` `label-md/Regular` · **Effects:** —
<!-- AUTO:END -->
