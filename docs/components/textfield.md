# TextField · TextField/Search · TextField/Amount

> **Status:** stable · **Since:** v1.0 · **Figma page:** `1:21`

Single-line input with label, helper, prefix/suffix and validation states.

## Use it for
| Size | Field height | Use |
|---|---|---|
| `sm` | 40 | Dense forms, inline filters |
| `md` | 52 | **Default for onboarding/KYC forms**; matches the lg (52) CTA |
| `lg` | 56 | Hero inputs (mobile number on its own screen) |

- **TextField/Search** (52): search inside a screen. The App Header has its own search.
- **TextField/Amount**: money entry with `num-display-md` value and quick-add Tonal buttons ("+₹5,000").

## Rules
- Label always visible (placeholders disappear). Value and placeholder text are **16px** (`label-lg/Regular`, numbers `num-label-lg/Regular`) so iOS doesn't zoom on focus; value `text/primary`, placeholder `text/placeholder`.
- `Outline` on plain pages; `Filled` (glass) inside cards. Don't mix styles within a form.
- Prefix ₹ via `Show prefix`, never typed into the value. Amounts use Indian grouping: ₹1,84,250.75.
- Phone numbers: `+91` as prefix; PAN uppercase; dates use a picker pattern, not free text.
- Show errors only after the person leaves the field. Error = `State=Error` + helper text with ⚠ and words.
- Stack fields `space/24` apart (the form Body gap), heading included.

## Accessibility
- Never rely on red alone: the error message carries ⚠ and words. Labels stay visible for screen readers and memory.

## Figma doc drift
- The set's default variant is `sm`. Always set `Size` explicitly (forms use `md`).
- **Accessibility check needed:** field edges use `glass/hairline` (navy 8% in Light), well under the 3:1 contrast WCAG 2.2 asks for input borders. Consider `border/strong` for the Outline style.

<!-- AUTO:START (generated from Figma by scripts/figma/inspect-components.js; do not edit by hand) -->
### TextField

| | |
|---|---|
| Node ID | `25:928` (page `1:21`) |
| Key | `42fe67336659ed271c5ced1c914d24c0d9ea571b` |
| Variants | 42 · default: `Style=Outline, Size=sm, State=Default` |
| Default size | 280×62 |

| Property | Type | Values / default |
|---|---|---|
| Show label | boolean | true |
| Label | text | Label |
| Required | boolean | false |
| Value | text | Value |
| Show leading icon | boolean | false |
| Show trailing icon | boolean | false |
| Show prefix | boolean | false |
| Prefix | text | ₹ |
| Show suffix | boolean | false |
| Suffix | text | INR |
| Show clear | boolean | false |
| Show helper | boolean | false |
| Helper | text | Helper text |
| Show count | boolean | false |
| Count | text | 0/40 |
| Style | variant | Outline, Filled (default Outline) |
| Size | variant | sm, md, lg (default sm) |
| State | variant | Default, Hover, Focus, Error, Disabled, Success, Filled (default Default) |

| Size | H | Specs (default variant at that size) |
|---|---|---|
| sm | 62 | gap space/6 |
| md | 74 | gap space/6 |
| lg | 80 | gap space/6 |

**Anatomy (default variant):** gap space/6

- Label row — gap space/2
  - Label — text body-sm/Medium · fill text/secondary
- Field — pad space/0 space/12 space/0 space/12 · gap space/8 · radius radius/10 · fill glass/field · stroke glass/hairline 1.5px · effect elevation/control
  - Value — text label-lg/Regular · fill text/placeholder

**Colour tokens across all variants:** `border/danger` `border/focus` `border/hover` `border/success` `glass/control` `glass/edge` `glass/field` `glass/hairline` `icon/disabled` `icon/primary` `icon/secondary` `surface/disabled` `text/danger` `text/disabled` `text/placeholder` `text/primary` `text/secondary` `text/success`
**Text styles:** `body-sm/Medium` `body-sm/Regular` `label-lg/Regular` `label-md/Medium` `num-body-sm/Regular` `num-display-md/Medium` `num-label-lg/Regular` · **Effects:** `elevation/control`

### TextField/Search

| | |
|---|---|
| Node ID | `27:2` (page `1:21`) |
| Key | `a4c6a4396d94b0ff2c916dfda023fad79e3c0202` |
| Variants | 1 · default: `TextField/Search` |
| Default size | 353×52 |

**Anatomy (default variant):** —

- TextField → `TextField` — gap space/6

**Colour tokens across all variants:** `glass/control` `glass/edge` `icon/primary` `icon/secondary` `text/danger` `text/placeholder` `text/primary` `text/secondary`
**Text styles:** `body-sm/Medium` `body-sm/Regular` `label-lg/Regular` `num-body-sm/Regular` `num-label-lg/Regular` · **Effects:** `elevation/control`

### TextField/Amount

| | |
|---|---|
| Node ID | `27:33` (page `1:21`) |
| Key | `2a993159e9eeabc41e83cb37f6753a1a1a05960b` |
| Variants | 1 · default: `TextField/Amount` |
| Default size | 311×122 |

**Anatomy (default variant):** gap space/14

- TextField → `TextField` — gap space/6
- Quick add — gap space/8
  - Button → `Button` — pad space/0 space/10 space/0 space/10 · gap space/4 · radius radius/8 · fill glass/control · stroke glass/hairline 1px · effect elevation/control
  - Button → `Button` — pad space/0 space/10 space/0 space/10 · gap space/4 · radius radius/8 · fill glass/control · stroke glass/hairline 1px · effect elevation/control
  - Button → `Button` — pad space/0 space/10 space/0 space/10 · gap space/4 · radius radius/8 · fill glass/control · stroke glass/hairline 1px · effect elevation/control

**Colour tokens across all variants:** `glass/control` `glass/field` `glass/hairline` `icon/primary` `icon/secondary` `text/danger` `text/primary` `text/secondary`
**Text styles:** `body-sm/Regular` `body-sm/Semibold` `label-lg/Regular` `label-md/Medium` `num-body-sm/Regular` `num-display-md/Medium` · **Effects:** `elevation/control`
<!-- AUTO:END -->
