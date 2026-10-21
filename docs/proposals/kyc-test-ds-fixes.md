# Change: TextField, OTP Input, Checkbox, Top Bar, Sheet Content/Prefill consent, `text/placeholder`

> **Status:** approved and built 19 Oct 2026 (DS owner); documented in the component docs. Figma version `Before KYC test DS fixes` saved first. Not yet published · **Proposed:** 19 Oct 2026 · **Section:** COMPONENTS (+ PRODUCT for the sheet content) · **Source:** KYC onboarding test (`prds/kyc-onboarding/review.md` DR-01, DR-02; test findings #10, #15, #16, #19, #20, #22)

Six fixes found by the first `/prd-to-screens` run. Each one is small; together they unblock the KYC feature's handoff (DR-01 is an S1).

## Changes

| # | Component / token | Problem today | Change | Breaking? |
|---|---|---|---|---|
| 1 | `Sheet Content/Prefill consent` | Consent Checkbox is pre-ticked (`Selection=Checked`), against "never pre-tick consents" (`checkbox.md`, `TR-RISK`) | Set it to `Unchecked`. Expose the nested Checkbox (`exposedInstances`) so screens can show the ticked state after the person taps it | No (overrides kept) |
| 2 | TextField `State=Error` (all Style × Size) | Extra text layer `Message` ("⚠ Enter at least ₹100"), not bound to any property, shows under the real helper | Delete the `Message` layer. The `Helper` row carries the error | No (screens that hid it lose nothing) |
| 3 | TextField `Field` edge (Outline: `glass/hairline`, Filled: `glass/edge`) and OTP Cell edge (`glass/hairline`) | 1.16:1 Light / 1.30:1 Dark on `glass/field`. WCAG 1.4.11 needs 3:1 (DR-01, S1) | Stroke → `border/strong` in Default and Filled states (Focus, Error, Success already pass; Disabled is exempt). Width stays 1.5px | No (visual only) |
| 4 | `text/placeholder` Dark | `frost/200`: brighter than `text/secondary`, empty fields look filled (DR-02) | Dark → `frost/400` (same as `text/secondary`, as Light already is). **Edits an existing variable value**: DS-owner approval needed | No |
| 5a | Checkbox `Text` / `Label` / `Description` | Hug width: long consents run off the screen | `Text` → Fill, `Label` and `Description` → auto height (wrap). The Checkbox gets a fixed default width (343 = 390 − 2 × `space/20`); instances use Fill container | No, but default size changes |
| 5e | Checkbox tick/dash: Checked + Indeterminate → `icon/static-white`; Disabled → `icon/disabled` (16 variants; was `icon/primary`). Added 19 Oct 2026 at the DS owner's request | checkbox.md accessibility |
| 5f | Switch `State=Disabled` thumb `surface/static-white` → `surface/neutral-strong`, flat (4 variants; white read as active in Dark, 16.43:1). Added 19 Oct 2026 at the DS owner's request | switch.md accessibility; Reference frame text |
| 5g | Timeline Item Done/Error and Option Card selected-check marks `icon/primary` → `icon/static-white` (4.78:1 on brand, 5.48:1 on danger). Figma version `Before glyph on brand fix` | timeline.md, option-card.md AUTO blocks |
| 5h | Disabled look for TextField, TextArea, Dropdown and OTP Cell/Input: `glass/control` fill, `border/default` edge, no shadow (was a solid `surface/disabled` block) | textfield, textarea, dropdown, otp-input docs; OTP Reference text |
| 5b | Top Bar stage | Current stage isn't a property: 5 nested `Step` overrides per screen, easy to get out of sync with the caption | New variant `Stage` = `1`–`5` (`Progress=On`): stages before it Completed, it Current, after it Upcoming. `Progress=Off` keeps one variant | No (default `Stage=1` = today's look) |
| 5c | OTP Input helper | Helper strings are hard-coded per variant ("Resend OTP in 0:24", "⚠ Incorrect OTP · 2 attempts left", "✓ Verified") | Split the helper into `Helper` (text prop, `body-sm`) + `Timer` (text prop, `num-body-sm`, boolean `Show timer`), so "Resend OTP in" + "0:24" keeps numbers in Space Grotesk | No (`Show helper` kept) |
| 5d | OTP Input / OTP Cell | No Disabled state (the locked screen shows an active first cell) | `State=Disabled` on OTP Cell and OTP Input (both lengths): fill `surface/disabled`, digits `text/disabled`, edge as TextField Disabled | No (new variant) |

## Tokens (all exist; no new tokens)

| Pair | Light | Dark | Needs |
|---|---|---|---|
| `border/strong` on `glass/field` (field edge) | 3.81:1 ✅ | 3.41:1 ✅ | 3:1 |
| `border/strong` on `surface/page` / `glass/card` (outside the field) | 3.81:1 ✅ | 3.35 / 3.41:1 ✅ | 3:1 |
| `glass/hairline` on `glass/field` (today) | 1.16:1 ❌ | 1.30:1 ❌ | 3:1 |
| `text/placeholder` on `glass/field` (today) | 5.94:1 | 12.34:1 (too close to `text/primary` 15.30) | 4.5:1 |
| `text/placeholder` Dark → `frost/400` (= `text/secondary` on `glass/field`) | 5.94:1 ✅ | 7.68:1 ✅ | 4.5:1 |

Measured with `scripts/token-contrast.py` (`--ui` for edges).

## Where it's used
- KYC onboarding file (`Laabh — KYC Onboarding`): TextField, OTP Input, Checkbox, Top Bar, Prefill consent on K01–K07b. After publish: "Update all", remove the K05 consent override and the K06c/K06d `Message` hide overrides (they become no-ops), re-run `/ds-audit`.
- Selected Screens in the DS file use the same components; they pick the changes up directly.

## Figma plan
1. Save version `Before KYC test DS fixes`.
2. One change per step, in the order 3 → 2 → 1 → 4 → 5a–5d. Screenshot the set (Light and Dark) after each.
3. Run `inspect-components.js` on each changed set: `raw` = 0.

## Decisions (19 Oct 2026, DS owner)
- Change 3 also covers the Textarea `Field` and Dropdown `Field` edges (same 1.4.11 failure).
- Radio and Switch rows: check them and apply the 5a wrap fix where they don't wrap.
- Hover edge (`border/hover`, 2.47:1 Light): leave it and note it in `textfield.md`; iOS and Android don't hover. Revisit when web is in scope.
- `CHANGELOG.md` entries are paused: none added.
- Message layer (change 2): also on TextField Success, Dropdown Error/Success and TextArea Error. Removed from all 26 variants; the helper is `text/danger` / `text/success`, `body-sm/Medium` there.
- Wrap (5a): masters keep today's narrow width (no 343 default), so doc grids don't move. Text wraps when an instance is Fill container. The 119 hugging instances in the DS file were pinned to their old width. The required asterisk sits at the end of the label's first line when filling: accepted.
- OTP (5c/5d): one text property shows the same words in every state, so Error, Success and Disabled have their own (`Error message`, `Success message`, `Disabled message`). The Disabled variants sit in a third row of the grid so the doc frame keeps its width.

## Built (19 Oct 2026)
| # | Figma | Repo |
|---|---|---|
| 3 | 30 variants: TextField, TextArea, Dropdown `Default`/`Filled` edges and OTP Cell `Empty`/`Filled` → `border/strong`. Also reaches TextField/Search | AUTO blocks; textfield/textarea/dropdown drift notes; Reference frame text |
| 2 | `Message` removed (26 variants); Patterns example uses the helper | textfield.md rule |
| 1 | `Sheet Content/Prefill consent`: Consent `Unchecked`, exposed instance | onboarding-kyc.md |
| 4 | `text/placeholder` Dark → `{frost.400}`; Colors page row | tokens/semantic.color.json, colors.md (via /ds-sync) |
| 5a | Checkbox, Radio, Switch: Text Fill, Label/Description wrap; Checkbox Group and vertical Radio Group items Fill | checkbox/radio/switch rules |
| 5b | Top Bar `Stage` 1–5 (6 variants) | top-bar.md, index row |
| 5c | OTP Input `Helper`, `Timer`, `Show timer`, `Error message`, `Success message` | otp-input.md, index row |
| 5d | OTP Cell and OTP Input `State=Disabled` + `Disabled message` | otp-input.md |

`inspect-components.js`: `raw` 0 on all 8 docs. `/ds-sync`: one token changed, `Counts match.`
