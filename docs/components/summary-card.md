# Summary Card · Summary Row

> **Status:** beta · **Since:** v1.1 · **Figma page:** `260:2` · **Owner:** @DS-OWNER

A titled card of label/value rows that restates details the user gave or we found: KYC record, linked bank, review sections, application details.

## Use it for
- Review steps (one card per section, with `Show action` for Edit).
- Result screens that confirm what was set up (Bank linked, Submitted).
- "What we'll fetch / what we compared" explanations on consent and check screens.

## Don't use it for
- Editable fields → TextField / Dropdown.
- A status sequence → Timeline.
- Rows with an avatar or a per-row action → List Row.

## Rules
- 2–6 rows (`Show row 4/5/6`). Turn `Show divider` off on the last visible row.
- `Value type=Number` for amounts, IDs, account and PAN numbers (num-label-md); `Text` for words.
- On review and confirmation screens show exact values (₹10,00,000, never ₹10 L) (`TR-NUM-04`).
- Outermost card only: never nest it inside another card.

## Content
- Title: the section noun ("Identity", "Linked account"). Labels: 1–3 words, sentence case. Values: right-aligned, may wrap.

## Accessibility
- Read as label/value pairs (`AN-06`).
- The Edit action is a Ghost sm button: give it a 44 pt hit area (`AN-11`) and a full name ("Edit contact details", `AN-03`).

## Figma doc drift
- none

<!-- AUTO:START (generated from Figma by scripts/figma/inspect-components.js; do not edit by hand) -->
### Summary Card

| | |
|---|---|
| Node ID | `260:15` (page `260:2`) |
| Key | `586cc19fd1fdc672336ce55864920ad1a41c7d53` |
| Variants | 1 · default: `Summary Card` |
| Default size | 350×343 |

| Property | Type | Values / default |
|---|---|---|
| Title | text | Section title |
| Show title | boolean | true |
| Show action | boolean | true |
| Show row 4 | boolean | true |
| Show row 5 | boolean | true |
| Show row 6 | boolean | true |

**Anatomy (default variant):** pad space/20 space/20 space/8 space/20 · gap space/4 · radius radius/18 · fill surface/card · stroke glass/edge 1px · effect elevation/card

- Header — gap space/8
  - Title — text label-lg/Semibold · fill text/primary
  - Action → `Button` — pad space/0 space/12 space/0 space/12 · gap space/6 · radius radius/10
- Row 1 → `Summary Row`
- Row 2 → `Summary Row`
- Row 3 → `Summary Row`
- Row 4 → `Summary Row`
- Row 5 → `Summary Row`
- Row 6 → `Summary Row`

**Colour tokens across all variants:** `glass/edge` `glass/hairline` `surface/card` `text/brand` `text/primary` `text/secondary`
**Text styles:** `body-sm/Regular` `body-sm/Semibold` `label-lg/Semibold` `label-md/Medium` · **Effects:** `elevation/card`

### Summary Row

| | |
|---|---|
| Node ID | `260:14` (page `260:2`) |
| Key | `7343985773883eb61570a94bfc11eb9b04cc016d` |
| Variants | 2 · default: `Value type=Text` |
| Default size | 311×43 |

| Property | Type | Values / default |
|---|---|---|
| Label | text | Label |
| Value | text | Value |
| Show divider | boolean | true |
| Value type | variant | Text, Number (default Text) |

**Anatomy (default variant):** —

- Row — pad space/12 0 space/12 0 · gap space/16
  - Label — text body-sm/Regular · fill text/secondary
  - Value — text label-md/Medium · fill text/primary
- Divider — fill glass/hairline

**Colour tokens across all variants:** `glass/hairline` `text/primary` `text/secondary`
**Text styles:** `body-sm/Regular` `label-md/Medium` `num-label-md/Medium` · **Effects:** —
<!-- AUTO:END -->
