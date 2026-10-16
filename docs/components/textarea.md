# TextArea

> **Status:** stable · **Since:** v1.0 · **Figma page:** `1:20`

Multi-line free text (feedback, reason for request, address line if long).

## Rules
- Show a count (`Show count`, `Count` "0/280" in `num-body-sm`) whenever there's a limit.
- Never for numbers, dates, amounts or anything with a format → TextField / Dropdown.
- Same label/helper/error behaviour as TextField. Use the same `Style` as the other fields in the form.

## Figma doc drift
- none (Reference frame corrected 16 Oct 2026)

<!-- AUTO:START (generated from Figma by scripts/figma/inspect-components.js; do not edit by hand) -->
### TextArea

| | |
|---|---|
| Node ID | `28:112` (page `1:20`) |
| Key | `ef5b15cfb465d06660a0381642c34e3d6a347c0c` |
| Variants | 12 · default: `Style=Outline, State=Default` |
| Default size | 320×140 |

| Property | Type | Values / default |
|---|---|---|
| Show label | boolean | true |
| Label | text | Label |
| Required | boolean | false |
| Value | text | Value |
| Show helper | boolean | true |
| Helper | text | Helper text |
| Show count | boolean | false |
| Count | text | 0/280 |
| Style | variant | Outline, Filled (default Outline) |
| State | variant | Default, Hover, Focus, Error, Disabled, Filled (default Default) |

**Anatomy (default variant):** gap space/6

- Label row — gap space/2
  - Label — text body-sm/Medium · fill text/secondary
- Field — pad space/10 space/16 space/10 space/16 · radius radius/12 · fill glass/field · stroke glass/hairline 1.5px · effect elevation/control
  - Value — text label-md/Regular · fill text/placeholder
- Helper row — gap space/8
  - Helper — text body-sm/Regular · fill text/secondary

**Colour tokens across all variants:** `border/danger` `border/focus` `border/hover` `glass/control` `glass/edge` `glass/field` `glass/hairline` `icon/secondary` `surface/disabled` `text/danger` `text/disabled` `text/placeholder` `text/primary` `text/secondary`
**Text styles:** `body-sm/Medium` `body-sm/Regular` `label-md/Regular` `num-body-sm/Regular` · **Effects:** `elevation/control`
<!-- AUTO:END -->
