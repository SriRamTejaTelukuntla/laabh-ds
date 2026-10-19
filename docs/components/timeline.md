# Timeline · Timeline Item

> **Status:** stable · **Since:** v1.0 · **Figma page:** `49:6`

An ordered, non-interactive status history: KYC review progress, order lifecycle, fund transfer status.

## Rules
- Exactly one `Active` item. Every `Pending` item gets an expected time in `Meta` ("Usually within 24 hours").
- `Error` replaces the step that failed. Pair it with an Alert or a CTA that offers the fix.
- The last item hides its connector (`Show connector` = false).
- Not tappable. Never use it for navigation.

## Figma doc drift
- none (Rail/Text paddings and Connector radius bound to tokens on 16 Oct 2026)

<!-- AUTO:START (generated from Figma by scripts/figma/inspect-components.js; do not edit by hand) -->
### Timeline Item

| | |
|---|---|
| Node ID | `56:39` (page `49:6`) |
| Key | `31f864fc2e309e1df1288e70ed1ca72288906347` |
| Variants | 4 · default: `State=Done` |
| Default size | 313×58 |

| Property | Type | Values / default |
|---|---|---|
| Title | text | Step title |
| Show description | boolean | true |
| Description | text | What happens in this step |
| Show meta | boolean | false |
| Meta | text | Today, 10:42 AM |
| Show connector | boolean | true |
| State | variant | Done, Active, Pending, Error (default Done) |

**Anatomy (default variant):** gap space/12

- Rail — pad 0 0 space/4 0 · gap space/4
  - Marker — radius radius/full · fill surface/brand
    - icon/check → `Icon`
  - Connector — radius radius/full · fill surface/brand
- Text — pad space/2 0 space/18 0 · gap space/2
  - Title — text body-lg/Medium · fill text/primary
  - Description — text body-sm/Regular · fill text/secondary

**Colour tokens across all variants:** `border/brand` `border/default` `data/track` `glass/field` `icon/static-white` `surface/brand` `surface/brand-subtle` `surface/danger` `text/brand` `text/danger` `text/primary` `text/secondary`
**Text styles:** `body-lg/Medium` `body-sm/Medium` `body-sm/Regular` · **Effects:** —

### Timeline

| | |
|---|---|
| Node ID | `56:40` (page `49:6`) |
| Key | `5a37c7d28fba4af35a06872b111a63ce56c5a179` |
| Variants | 1 · default: `Timeline` |
| Default size | 313×290 |

| Property | Type | Values / default |
|---|---|---|
| Show item 5 | boolean | true |

**Anatomy (default variant):** —

- Item 1 → `Timeline Item` — gap space/12
- Item 2 → `Timeline Item` — gap space/12
- Item 3 → `Timeline Item` — gap space/12
- Item 4 → `Timeline Item` — gap space/12
- Item 5 → `Timeline Item` — gap space/12

**Colour tokens across all variants:** `border/brand` `border/default` `data/track` `glass/field` `icon/static-white` `surface/brand` `surface/brand-subtle` `text/brand` `text/primary` `text/secondary`
**Text styles:** `body-lg/Medium` `body-sm/Medium` `body-sm/Regular` · **Effects:** —
<!-- AUTO:END -->
