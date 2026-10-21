# OTP Input · OTP Cell

> **Status:** stable · **Since:** v1.0 · **Figma page:** `49:5`

One-time-code entry for phone, email, eSign and nominee verification.

## Use it for
- `Length=4` for SMS/email OTPs in Laabh flows; `6` where a partner (e.g. Aadhaar eSign) requires it.
- Show states: `Empty`, `Typing` (one active cell), `Filled`, `Error`, `Success`, `Disabled` (verification locked after 3 wrong attempts).
- Helper row text is set through the `Helper`, `Timer`, `Error message`, `Success message` and `Disabled message` properties; toggle the row with `Show helper` and the countdown with `Show timer`.

## Rules
- Behaviour to annotate in the design: auto-advance per digit, auto-submit on the last, paste fills all cells, read SMS automatically on Android where allowed.
- Resend unlocks after 30 s, up to 3 resends. Show a countdown ("Resend in 0:24") in the helper row.
- 3 wrong attempts lock verification for 30 minutes. Show the unlock time, never a blank error.
- Centre the cells under the screen title. Put the destination ("Sent to +91 98••• ••210", with an Edit ghost button) above the cells.

## Accessibility
- Digits use `num-display-md/Medium`. Error pairs `border/danger` with helper text that says what to do.

## Figma doc drift
- none (Reference frame corrected 16 Oct 2026; Figma checked 21 Oct 2026). The helper row is two text nodes: `Helper` in `body-sm/Regular` and `Timer` in `num-body-sm/Regular` ("Resend OTP in" + "0:24"); errors, success and the disabled message use `body-sm/Medium`.
- Cell edges use `border/strong` (Empty, Default, Filled) so they meet the 3:1 UI-part contrast; `Disabled` uses `glass/control` + `border/default` with no shadow.

<!-- AUTO:START (generated from Figma by scripts/figma/inspect-components.js; do not edit by hand) -->
### OTP Input

| | |
|---|---|
| Node ID | `52:158` (page `49:5`) |
| Key | `0cb4798c487c4f7cd3cc39cec53d986ab3d14333` |
| Variants | 12 · default: `Length=4, State=Empty` |
| Default size | 260×84 |

| Property | Type | Values / default |
|---|---|---|
| Show helper | boolean | true |
| Helper | text | Resend OTP in |
| Timer | text | 0:24 |
| Show timer | boolean | true |
| Error message | text | ⚠ Incorrect OTP · 2 attempts left |
| Success message | text | ✓ Verified |
| Disabled message | text | Too many attempts. Try again in 30 min |
| Length | variant | 4, 6 (default 4) |
| State | variant | Empty, Typing, Filled, Error, Success, Disabled (default Empty) |

**Anatomy (default variant):** gap space/12

- Cells — gap space/12 · effect elevation/control
  - Cell 1 → `OTP Cell` — radius radius/12 · fill glass/field · stroke border/focus 2px · effect elevation/control
  - Cell 2 → `OTP Cell` — radius radius/12 · fill glass/field · stroke border/strong 1.5px · effect elevation/control
  - Cell 3 → `OTP Cell` — radius radius/12 · fill glass/field · stroke border/strong 1.5px · effect elevation/control
  - Cell 4 → `OTP Cell` — radius radius/12 · fill glass/field · stroke border/strong 1.5px · effect elevation/control
- Helper row — gap space/4
  - Helper — text body-sm/Regular · fill text/secondary
  - Timer — text num-body-sm/Regular · fill text/secondary

**Colour tokens across all variants:** `border/danger` `border/default` `border/focus` `border/strong` `border/success` `glass/control` `glass/field` `text/danger` `text/secondary` `text/success`
**Text styles:** `body-sm/Medium` `body-sm/Regular` `num-body-sm/Regular` · **Effects:** `elevation/control`

### OTP Cell

| | |
|---|---|
| Node ID | `52:13` (page `49:5`) |
| Key | `e0e8f1261050022b955612ce4b10e83869dfe1e0` |
| Variants | 6 · default: `State=Empty` |
| Default size | 56×56 |

| Property | Type | Values / default |
|---|---|---|
| Digit | text | 4 |
| State | variant | Empty, Active, Filled, Error, Success, Disabled (default Empty) |

**Anatomy (default variant):** radius radius/12 · fill glass/field · stroke border/strong 1.5px · effect elevation/control

**Colour tokens across all variants:** `border/danger` `border/default` `border/focus` `border/strong` `border/success` `glass/control` `glass/field` `text/disabled` `text/primary`
**Text styles:** `num-display-md/Medium` · **Effects:** `elevation/control`
<!-- AUTO:END -->
