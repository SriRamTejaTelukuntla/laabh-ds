# Checkbox · Checkbox Group

> **Status:** stable · **Since:** v1.0 · **Figma page:** `1:13`

Independent on/off choices and consents that take effect when the form is submitted.

## Use it for
- Consents and declarations in onboarding/KYC ("I confirm I'm not a PEP").
- Multi-select lists (several independent choices). Group them in **Checkbox Group** with a legend and helper.

## Don't use it for
- A setting that applies instantly → **Switch**.
- One choice out of several → Radio Group / Option Card.

## Rules
- Never pre-tick risk disclosures or consents.
- `Required` shows a `text/danger` asterisk. Use it on mandatory consents.
- Size `sm` (16 control) in dense forms, `md` (20 control) for standalone consents.
- Long legal text: put the summary in `Label` and the detail in `Description`, or link to a sheet.
- In screens set it to **Fill container**: `Label` and `Description` then wrap. The master keeps its narrow default width, so a hugging instance doesn't wrap.

## Accessibility
- Pad the whole row to a 44pt hit area; the label is tappable.
- Focus ring: 2px `focus/ring`, 2px gap.
- The tick and dash are `icon/static-white` on the brand fill (4.78:1 both modes). Disabled uses `icon/disabled`, like the label, so it doesn't read as active (disabled controls are exempt from 3:1).

## Figma doc drift
- With `Required` on and the component filling the width, the asterisk sits at the end of the label's first line (the label fills the row so it can wrap). Accepted 19 Oct 2026.

<!-- AUTO:START (generated from Figma by scripts/figma/inspect-components.js; do not edit by hand) -->
### Checkbox

| | |
|---|---|
| Node ID | `20:208` (page `1:13`) |
| Key | `81ffa2c81ad8a3644134ca3ab25aef43a5ab7827` |
| Variants | 24 · default: `Selection=Unchecked, State=Default, Size=sm` |
| Default size | 60×18 |

| Property | Type | Values / default |
|---|---|---|
| Show label | boolean | true |
| Label | text | Label |
| Show description | boolean | false |
| Description | text | Supporting description |
| Required | boolean | false |
| Selection | variant | Unchecked, Checked, Indeterminate (default Unchecked) |
| State | variant | Default, Hover, Focus, Disabled (default Default) |
| Size | variant | sm, md (default sm) |

| Size | H | Specs (default variant at that size) |
|---|---|---|
| sm | 18 | gap space/8 |
| md | 20 | gap space/10 |

**Anatomy (default variant):** gap space/8

- Control — radius radius/4 · fill glass/field · stroke border/strong 1.5px
- Text — gap space/2
  - Label row — gap space/2
    - Label — text label-md/Regular · fill text/primary

**Colour tokens across all variants:** `border/brand` `border/strong` `focus/ring` `glass/field` `icon/disabled` `icon/static-white` `surface/brand` `surface/brand-hover` `surface/disabled` `text/danger` `text/disabled` `text/primary` `text/secondary`
**Text styles:** `body-lg/Regular` `body-sm/Regular` `label-md/Regular` · **Effects:** —

### Checkbox Group

| | |
|---|---|
| Node ID | `20:209` (page `1:13`) |
| Key | `4dc6f3929d8480467c5d88122692a771c77f602a` |
| Variants | 1 · default: `Checkbox Group` |
| Default size | 360×174 |

**Anatomy (default variant):** gap space/12

- Legend — text label-md/Medium · fill text/primary
- Checkbox → `Checkbox` — gap space/10
- Checkbox → `Checkbox` — gap space/10
- Checkbox → `Checkbox` — gap space/10
- Checkbox → `Checkbox` — gap space/10
- Helper — text body-sm/Regular · fill text/secondary

**Colour tokens across all variants:** `border/strong` `glass/field` `icon/static-white` `surface/brand` `text/danger` `text/primary` `text/secondary`
**Text styles:** `body-lg/Regular` `body-sm/Regular` `label-md/Medium` `label-md/Regular` · **Effects:** —
<!-- AUTO:END -->
