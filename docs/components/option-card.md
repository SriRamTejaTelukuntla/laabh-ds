# Option Card

> **Status:** stable · **Since:** v1.0 · **Figma page:** `49:4`

A large, card-shaped choice for questions where each option needs a sentence of explanation.

## Use it for
- Onboarding/KYC questions with explanations: nominee choice, account type, income range with context, plan selection.
- `Control=Radio` for single choice, `Check` for multi-choice, `None` for navigation-like choices that advance on tap.

## Don't use it for
- Short plain labels → Radio Group.
- Instant settings → Switch Row.

## Rules
- 2–6 cards per question, stacked with `space/12` between them, full width inside the page margin.
- Never mix `Radio` and `Check` controls in one group.
- `Show leading` adds a 40px round tile (icon or logo). Use it for every card in the group or for none.
- `Show badge` marks a recommended option, on one card at most ("Recommended").
- Pre-select the safest/most common option when the PRD allows.
- Inner content only. Never nest an Option Card inside another card (inner cards get no shadow).

## Content
- Title: short noun phrase. Description: one sentence on the consequence of choosing it.

## Accessibility
- The whole card is the hit target. The selected state changes border, fill **and** control, so it's not colour-only.

## Figma doc drift
- none (Reference frame corrected 16 Oct 2026)

<!-- AUTO:START (generated from Figma by scripts/figma/inspect-components.js; do not edit by hand) -->
### Option Card

| | |
|---|---|
| Node ID | `53:120` (page `49:4`) |
| Key | `6c20d02889cc7f90f7266abc2563ce1042d2869b` |
| Variants | 6 · default: `Selection=Unselected, Control=Radio` |
| Default size | 353×50 |

| Property | Type | Values / default |
|---|---|---|
| Title | text | Option title |
| Show description | boolean | false |
| Description | text | Supporting description |
| Show leading | boolean | false |
| Show badge | boolean | false |
| Selection | variant | Unselected, Selected (default Unselected) |
| Control | variant | Radio, Check, None (default Radio) |

**Anatomy (default variant):** pad space/14 space/16 space/14 space/16 · gap space/12 · radius radius/18 · fill surface/card · stroke glass/edge 1px · effect elevation/card

- Text — gap space/2
  - Title row — gap space/6
    - Title — text body-lg/Medium · fill text/primary
- Control — fill glass/field · stroke border/strong 1.5px

**Colour tokens across all variants:** `border/brand` `border/strong` `glass/control` `glass/edge` `glass/field` `glass/hairline` `icon/brand` `icon/primary` `surface/brand` `surface/brand-subtle` `surface/card` `surface/static-white` `text/brand` `text/brand-strong` `text/neutral` `text/primary` `text/secondary`
**Text styles:** `body-lg/Medium` `body-sm/Regular` `caps-md/Semibold` · **Effects:** `elevation/card`
<!-- AUTO:END -->
