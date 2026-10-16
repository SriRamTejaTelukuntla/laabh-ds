# Alert

> **Status:** stable · **Since:** v1.0 · **Figma page:** `49:2`

An inline, non-blocking message inside a screen that explains a state and, optionally, offers the fix.

## Use it for
- Status the person should know about on this screen: a failed bank verification, a pending KYC step, a market notice.
- Tone: `Info` (neutral information, brand-tinted), `Success`, `Warning` (needs attention soon), `Danger` (failed, action required).

## Don't use it for
- Confirming an action just taken → toast (not in the DS yet; propose via `/new-component`).
- Blocking decisions or consent → Bottom Sheet.
- Field-level errors → the field's `Error` state and helper text.

## Rules
- Keep it to two lines of description at most. Title is optional.
- Put the fix in the action (`Show action`, e.g. "Retry with penny drop").
- Maximum **one** alert per screen. Place it directly under the header or above the content it refers to, inside the page margin.
- Use `Danger` only when the person can act on it.
- Full width inside the page margin (Fill container).

## Content
- Title: 2–5 words, sentence case, no full stop. Description: plain language, say what happened and what to do.

## Accessibility
- The tone is carried by the icon and the words, not just the colour. Keep `Show icon` on.

## Figma doc drift
- none (Reference frame corrected 16 Oct 2026)

<!-- AUTO:START (generated from Figma by scripts/figma/inspect-components.js; do not edit by hand) -->
### Alert

| | |
|---|---|
| Node ID | `55:92` (page `49:2`) |
| Key | `11ceb16526d98a6e6d36d63ec00aefbe83a14906` |
| Variants | 4 · default: `Tone=Info` |
| Default size | 353×76 |

| Property | Type | Values / default |
|---|---|---|
| Show title | boolean | true |
| Title | text | Title |
| Description | text | Supporting message that explains what ha |
| Show icon | boolean | true |
| Show action | boolean | false |
| Tone | variant | Info, Success, Warning, Danger (default Info) |

**Anatomy (default variant):** pad space/12 space/14 space/12 space/14 · gap space/10 · radius radius/18 · fill surface/brand-subtle

- Icon → `Icon`
- Text — gap space/2
  - Title — text label-md/Semibold · fill text/neutral
  - Description — text body-sm/Regular · fill text/primary

**Colour tokens across all variants:** `icon/brand` `icon/danger` `icon/secondary` `icon/success` `icon/warning` `surface/brand-subtle` `surface/danger-subtle` `surface/success-subtle` `surface/warning-subtle` `text/brand` `text/danger` `text/danger-strong` `text/neutral` `text/primary` `text/success` `text/success-strong` `text/warning` `text/warning-strong`
**Text styles:** `body-sm/Regular` `body-sm/Semibold` `label-md/Semibold` · **Effects:** —
<!-- AUTO:END -->
