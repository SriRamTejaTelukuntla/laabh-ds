# File Upload

> **Status:** beta · **Since:** v1.1 · **Figma page:** `262:3` · **Owner:** @DS-OWNER

Pick a photo or file and show its upload progress: PAN image when DigiLocker is declined, address proof, income proof.

## Use it for
- One document per control, with a visible label and a helper that says what a good file looks like.

## Don't use it for
- Several files at once → a list of File Upload controls, one per document type.
- Signatures → a signature pad (not in the DS yet).

## Rules
- States: `Empty` (dashed border, "Choose file") → `Uploading` (Cancel) → `Uploaded` (success, Remove) or `Error` (danger border, "Try again").
- After picking, `Title` becomes the file name and `Description` the progress or size.
- `Error` helper starts with ⚠ and says how to fix it ("The file is over 5 MB. Choose a smaller photo.").
- State the accepted types and size limit in `Description` before the user picks.

## Content
- Label: the document ("PAN card"). Title: an instruction ("Upload a photo of your PAN card").

## Accessibility
- The whole box is one button named by the Title; it offers camera and files.
- Announce Uploading/Uploaded politely and errors assertively (`AN-07`). Error pairs red with ⚠ and text (`TR-STATE`, WCAG 1.4.1).
- The action button inside is Ghost/Outline sm: give it a 44 pt hit area (`AN-11`).

## Figma doc drift
- none

<!-- AUTO:START (generated from Figma by scripts/figma/inspect-components.js; do not edit by hand) -->
### File Upload

| | |
|---|---|
| Node ID | `262:245` (page `262:3`) |
| Key | `fde42442ef4a511ddb68c9716a6c5dbd55efad2e` |
| Variants | 4 · default: `State=Empty` |
| Default size | 350×153 |

| Property | Type | Values / default |
|---|---|---|
| Label | text | PAN card |
| Show label | boolean | true |
| Title | text | Upload a photo of your PAN card |
| Description | text | JPG, PNG or PDF, up to 5 MB |
| Helper | text | Take a clear photo on a plain background |
| Show helper | boolean | true |
| State | variant | Empty, Uploading, Uploaded, Error (default Empty) |

**Anatomy (default variant):** gap space/8

- Label — text body-sm/Medium · fill text/secondary
- Box — pad space/16 · gap space/12 · radius radius/14 · fill glass/field · stroke border/strong 1.5px
  - Icon Tile → `Icon Tile` — radius radius/full · fill surface/brand-subtle · stroke border/brand-subtle 1px
  - Text — gap space/2
    - Title — text label-md/Medium · fill text/primary
    - Description — text body-sm/Regular · fill text/secondary
  - Action → `Button` — pad space/0 space/12 space/0 space/12 · gap space/6 · radius radius/10 · stroke border/strong 1px
- Helper — text body-sm/Regular · fill text/secondary

**Colour tokens across all variants:** `border/brand-subtle` `border/danger` `border/focus` `border/strong` `border/success` `border/success-subtle` `glass/field` `icon/brand` `surface/brand-subtle` `surface/danger-subtle` `surface/success-subtle` `text/danger` `text/primary` `text/secondary`
**Text styles:** `body-sm/Medium` `body-sm/Regular` `body-sm/Semibold` `label-md/Medium` · **Effects:** —
<!-- AUTO:END -->
