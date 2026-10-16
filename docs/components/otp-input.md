# OTP Input · OTP Cell

> **Status:** stable · **Since:** v1.0 · **Figma page:** `49:5`

One-time-code entry for phone, email, eSign and nominee verification.

## Use it for
- `Length=4` for SMS/email OTPs in Laabh flows; `6` where a partner (e.g. Aadhaar eSign) requires it.
- Show states: `Empty`, `Typing` (one active cell), `Filled`, `Error`, `Success`.

## Rules
- Behaviour to annotate in the design: auto-advance per digit, auto-submit on the last, paste fills all cells, read SMS automatically on Android where allowed.
- Resend unlocks after 30 s, up to 3 resends. Show a countdown ("Resend in 0:24") in the helper row.
- 3 wrong attempts lock verification for 30 minutes. Show the unlock time, never a blank error.
- Centre the cells under the screen title. Put the destination ("Sent to +91 98••• ••210", with an Edit ghost button) above the cells.

## Accessibility
- Digits use `num-display-md/Medium`. Error pairs `border/danger` with helper text that says what to do.

## Figma doc drift
- none (Reference frame corrected 16 Oct 2026). The helper mixes `body-sm/Regular` with a `num-body-sm/Regular` timer ("Resend OTP in 0:24"); errors and success use `body-sm/Medium`.

<!-- AUTO:START (generated from Figma by scripts/figma/inspect-components.js; do not edit by hand) -->
### OTP Input

| | |
|---|---|
| Node ID | `52:158` (page `49:5`) |
| Key | `0cb4798c487c4f7cd3cc39cec53d986ab3d14333` |
| Variants | 10 · default: `Length=4, State=Empty` |
| Default size | 260×84 |

| Property | Type | Values / default |
|---|---|---|
| Show helper | boolean | true |
| Length | variant | 4, 6 (default 4) |
| State | variant | Empty, Typing, Filled, Error, Success (default Empty) |

**Anatomy (default variant):** gap space/12

- Cells — gap space/12 · effect elevation/control
  - Cell 1 → `OTP Cell` — radius radius/12 · fill glass/field · stroke border/focus 2px · effect elevation/control
  - Cell 2 → `OTP Cell` — radius radius/12 · fill glass/field · stroke glass/hairline 1.5px · effect elevation/control
  - Cell 3 → `OTP Cell` — radius radius/12 · fill glass/field · stroke glass/hairline 1.5px · effect elevation/control
  - Cell 4 → `OTP Cell` — radius radius/12 · fill glass/field · stroke glass/hairline 1.5px · effect elevation/control
- Helper row — gap space/6
  - Helper — text body-sm/Regular + num-body-sm/Regular · fill text/secondary

**Colour tokens across all variants:** `border/danger` `border/focus` `border/success` `glass/field` `glass/hairline` `text/danger` `text/primary` `text/secondary` `text/success`
**Text styles:** `body-sm/Medium` `num-display-md/Medium` · **Effects:** `elevation/control`

### OTP Cell

| | |
|---|---|
| Node ID | `52:13` (page `49:5`) |
| Key | `e0e8f1261050022b955612ce4b10e83869dfe1e0` |
| Variants | 5 · default: `State=Empty` |
| Default size | 56×56 |

| Property | Type | Values / default |
|---|---|---|
| Digit | text | 4 |
| State | variant | Empty, Active, Filled, Error, Success (default Empty) |

**Anatomy (default variant):** radius radius/12 · fill glass/field · stroke glass/hairline 1.5px · effect elevation/control

**Colour tokens across all variants:** `border/danger` `border/focus` `border/success` `glass/field` `glass/hairline` `text/primary`
**Text styles:** `num-display-md/Medium` · **Effects:** `elevation/control`
<!-- AUTO:END -->
