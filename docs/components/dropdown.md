# Dropdown · Dropdown Item · Dropdown Menu

> **Status:** stable · **Since:** v1.0 · **Figma page:** `1:14`

A field that opens a menu to pick one value from a list.

## Use it for
- 5+ options, or options that need a description (occupation, income range, state, bank account).
- Show the open state with a `Dropdown Menu` (`Content=Fit` up to ~6 rows, `Scroll` beyond) placed 6px under the field.

## Don't use it for
- 2–3 options → Radio Group or Segmented Control.
- Actions (Delete, Exit) → buttons or a sheet. A selection menu never holds actions.

## Rules
- The trigger matches TextField (including the Disabled look): same sizes (`sm`/`md`/`lg`), same `Outline`/`Filled` styles, same label/helper slots. Use the same size as the other fields in the form.
- `Value` shows the placeholder ("Select") until chosen. The state then becomes `Filled`.
- Selected item: `Selection=Selected` (check + `text/selected`).
- `Trailing` on items is for a value (e.g. a price `₹1,386.40` in `num-body-sm`).

## Accessibility
- Error state pairs `border/danger` with helper text that says how to fix it.

## Figma doc drift
- Edges are `border/strong` like TextField. `State=Hover` keeps `border/hover` (Filled, 2.47:1 in Light) and `icon/secondary` (Outline) as its edge: iOS and Android don't hover, so it stays until web is in scope (decided 19 Oct 2026).

<!-- AUTO:START (generated from Figma by scripts/figma/inspect-components.js; do not edit by hand) -->
### Dropdown

| | |
|---|---|
| Node ID | `29:730` (page `1:14`) |
| Key | `f1ef9861660bcf167972b9af1d642fc03f38e1d5` |
| Variants | 42 · default: `Style=Outline, Size=md, State=Default` |
| Default size | 280×74 |

| Property | Type | Values / default |
|---|---|---|
| Show label | boolean | true |
| Label | text | Label |
| Required | boolean | false |
| Value | text | Select |
| Show leading icon | boolean | false |
| Show clear | boolean | false |
| Show helper | boolean | false |
| Helper | text | Helper text |
| Style | variant | Outline, Filled (default Outline) |
| Size | variant | md, sm, lg (default md) |
| State | variant | Default, Hover, Focus, Error, Disabled, Success, Filled (default Default) |

| Size | H | Specs (default variant at that size) |
|---|---|---|
| md | 74 | gap space/6 |
| sm | 62 | gap space/6 |
| lg | 80 | gap space/6 |

**Anatomy (default variant):** gap space/6

- Label row — gap space/2
  - Label — text body-sm/Medium · fill text/secondary
- Field — pad space/0 space/16 space/0 space/16 · gap space/8 · radius radius/12 · fill glass/field · stroke border/strong 1.5px · effect elevation/control
  - Value — text label-lg/Regular · fill text/placeholder
  - Trailing icon → `Icon`

**Colour tokens across all variants:** `border/danger` `border/default` `border/focus` `border/hover` `border/strong` `border/success` `glass/control` `glass/field` `icon/brand` `icon/disabled` `icon/primary` `icon/secondary` `text/danger` `text/disabled` `text/placeholder` `text/primary` `text/secondary` `text/success`
**Text styles:** `body-sm/Medium` `body-sm/Regular` `label-lg/Regular` `label-md/Medium` · **Effects:** `elevation/control`

### Dropdown Item

| | |
|---|---|
| Node ID | `29:829` (page `1:14`) |
| Key | `3ebdad553b9b0970f027e3c80ebedda1b4a54c6e` |
| Variants | 8 · default: `Selection=Unselected, State=Default` |
| Default size | 280×38 |

| Property | Type | Values / default |
|---|---|---|
| Show leading icon | boolean | false |
| Label | text | Option |
| Show description | boolean | false |
| Description | text | Supporting text |
| Show divider | boolean | false |
| Show trailing | boolean | false |
| Trailing | text | ₹1,386.40 |
| Show trailing icon | boolean | true |
| Selection | variant | Unselected, Selected (default Unselected) |
| State | variant | Default, Hover, Focus, Disabled (default Default) |

**Anatomy (default variant):** —

- Row — pad space/10 space/12 space/10 space/12 · gap space/10 · radius radius/8
  - Text — gap space/2
    - Label — text label-md/Regular · fill text/primary

**Colour tokens across all variants:** `focus/ring` `glass/hairline` `glass/selected` `icon/brand` `icon/disabled` `icon/secondary` `surface/selected` `text/disabled` `text/primary` `text/secondary` `text/selected`
**Text styles:** `body-sm/Regular` `label-md/Regular` `num-body-sm/Regular` · **Effects:** —

### Dropdown Menu

| | |
|---|---|
| Node ID | `29:945` (page `1:14`) |
| Key | `fb61ecda039901b5f278b810af61aa6bf8e66ea7` |
| Variants | 2 · default: `Content=Fit` |
| Default size | 296×132 |

| Property | Type | Values / default |
|---|---|---|
| Content | variant | Fit, Scroll (default Fit) |

**Anatomy (default variant):** pad space/6 · gap space/2 · radius radius/12 · fill surface/raised · stroke glass/edge 1px · effect elevation/overlay

- Rows → `Dropdown Item`
- Rows → `Dropdown Item`
- Rows → `Dropdown Item`

**Colour tokens across all variants:** `glass/edge` `glass/hairline` `icon/brand` `icon/secondary` `surface/raised` `surface/selected` `text/primary` `text/secondary` `text/selected`
**Text styles:** `body-sm/Regular` `label-md/Regular` `num-body-sm/Regular` · **Effects:** `elevation/overlay`
<!-- AUTO:END -->
