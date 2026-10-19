# Switch · Switch Row · Switch Group

> **Status:** stable · **Since:** v1.0 · **Figma page:** `1:18`

On/off settings that apply instantly, without a Save button.

## Use it for
- Settings and preferences (price alerts, biometrics, notifications). In lists use **Switch Row** (label + description + switch + divider), grouped in a **Switch Group** with a legend.

## Don't use it for
- Choices inside a form that has a Submit button → Checkbox.
- Consents → Checkbox.

## Rules
- The label states what is on ("Price alerts"), never a question.
- In screens set it to **Fill container**: `Label` and `Description` then wrap. The master keeps its narrow default width, so a hugging instance doesn't wrap. Switch Row already wraps.
- Switch Rows sit inside a card (`surface/card`, `radius/18`, padding 20 horizontally). The last row hides its divider (`Show divider` = false).

## Accessibility
- The whole row is the hit target. On/off is shown by thumb position **and** track colour.
- Disabled: track `surface/disabled`, thumb `surface/neutral-strong` with no shadow (2.75:1 Light, 2.76:1 Dark). A white thumb read as active in Dark. On/off is then shown by thumb position.

## Figma doc drift
- none (Reference frame corrected 16 Oct 2026)

<!-- AUTO:START (generated from Figma by scripts/figma/inspect-components.js; do not edit by hand) -->
### Switch

| | |
|---|---|
| Node ID | `22:102` (page `1:18`) |
| Key | `3bccd06b932b39adf24432c8f1dccdd7a9a40747` |
| Variants | 16 · default: `Selection=Off, State=Default, Size=sm` |
| Default size | 72×18 |

| Property | Type | Values / default |
|---|---|---|
| Show label | boolean | true |
| Label | text | Label |
| Show description | boolean | false |
| Description | text | Supporting description |
| Selection | variant | Off, On (default Off) |
| State | variant | Default, Hover, Focus, Disabled (default Default) |
| Size | variant | sm, md (default sm) |

| Size | H | Specs (default variant at that size) |
|---|---|---|
| sm | 18 | gap space/8 |
| md | 20 | gap space/10 |

**Anatomy (default variant):** gap space/8

- Track — radius radius/full · fill surface/neutral-emphasis
  - Thumb — fill surface/static-white · effect elevation/thumb
- Text — gap space/2
  - Label — text label-md/Regular · fill text/primary

**Colour tokens across all variants:** `focus/ring` `surface/brand` `surface/brand-hover` `surface/disabled` `surface/neutral-emphasis` `surface/neutral-strong` `surface/neutral-strong-hover` `surface/static-white` `text/disabled` `text/primary` `text/secondary`
**Text styles:** `body-lg/Regular` `body-sm/Regular` `label-md/Regular` · **Effects:** `elevation/thumb`

### Switch Row

| | |
|---|---|
| Node ID | `22:127` (page `1:18`) |
| Key | `e70158b5fb8678fab8206fb8e0bf5cd8c9806a62` |
| Variants | 2 · default: `State=Default` |
| Default size | 360×67 |

| Property | Type | Values / default |
|---|---|---|
| Label | text | Push notifications |
| Show description | boolean | true |
| Description | text | Order fills, price alerts and margin cal |
| Show divider | boolean | true |
| State | variant | Default, Disabled (default Default) |

**Anatomy (default variant):** —

- Row — pad space/14 space/0 space/14 space/0 · gap space/16
  - Text — gap space/2
    - Label — text body-lg/Medium · fill text/primary
    - Description — text body-sm/Regular · fill text/secondary
  - Switch → `Switch` — gap space/10
- Divider — fill glass/hairline

**Colour tokens across all variants:** `glass/hairline` `surface/brand` `surface/disabled` `surface/neutral-strong` `surface/static-white` `text/disabled` `text/primary` `text/secondary`
**Text styles:** `body-lg/Medium` `body-lg/Regular` `body-sm/Regular` `label-md/Regular` · **Effects:** `elevation/thumb`

### Switch Group

| | |
|---|---|
| Node ID | `22:128` (page `1:18`) |
| Key | `a91d6cf5f47e3bac41eb04ea606a621bd8ba8deb` |
| Variants | 1 · default: `Switch Group` |
| Default size | 360×230 |

**Anatomy (default variant):** gap space/4

- Legend — text label-md/Medium · fill text/primary
- Switch Row → `Switch Row`
- Switch Row → `Switch Row`
- Switch Row → `Switch Row`

**Colour tokens across all variants:** `glass/hairline` `surface/brand` `surface/disabled` `surface/neutral-strong` `surface/static-white` `text/disabled` `text/primary` `text/secondary`
**Text styles:** `body-lg/Medium` `body-lg/Regular` `body-sm/Regular` `label-md/Medium` `label-md/Regular` · **Effects:** `elevation/thumb`
<!-- AUTO:END -->
