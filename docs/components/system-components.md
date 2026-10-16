# System Components: Status Bar · Home Indicator

> **Status:** stable · **Since:** v1.0 · **Figma page:** `101:128916`

iOS chrome placed on every full screen so layouts account for the real safe areas.

## Rules
- Every full-screen frame starts with **Status Bar** (48 tall) and ends with **Home Indicator** (34 tall), as instances.
- They are 393 wide in the library. On a 390 canvas set them to **Fill container** (or resize to 390) so nothing overhangs.
- Colours follow the mode automatically (`icon/primary`, `surface/inverse`).
- Bottom sheets float above the Home Indicator (8px inset), so it stays visible.

## Figma doc drift
- Status Bar `Time` text is unstyled (SF Pro system font, intentional for iOS chrome). Exempt from `/ds-audit`.
- No Reference frame on this page.

<!-- AUTO:START (generated from Figma by scripts/figma/inspect-components.js; do not edit by hand) -->
### Status Bar

| | |
|---|---|
| Node ID | `101:128929` (page `101:128916`) |
| Key | `7e8a5a702487213ede1b4720eb943d74214055c1` |
| Variants | 1 · default: `Status Bar` |
| Default size | 393×48 |

**Anatomy (default variant):** —

- Left Side
  - Time — text UNSTYLED · fill text/primary
- Battery
  - Outline — radius 4 · stroke icon/primary 1px
  - Battery End — fill icon/primary
  - Fill — radius 2 · fill icon/primary
- Wifi — fill icon/primary
- Icon / Mobile Signal — fill icon/primary

**Colour tokens across all variants:** `icon/primary` `text/primary`
**Text styles:** — · **Effects:** —

### Home Indicator

| | |
|---|---|
| Node ID | `101:128930` (page `101:128916`) |
| Key | `fab68770a62da3aa9c67fda8f87db98916679908` |
| Variants | 1 · default: `Home Indicator` |
| Default size | 393×34 |

**Anatomy (default variant):** —

- Bar — radius radius/full · fill surface/inverse

**Colour tokens across all variants:** `surface/inverse`
**Text styles:** — · **Effects:** —
<!-- AUTO:END -->
