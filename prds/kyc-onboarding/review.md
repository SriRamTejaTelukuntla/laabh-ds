# Design review: KYC onboarding S1–S4 (K01–K07b), re-check after the DS fixes
**Result:** ✅ Ready for handoff. All four problems from the first review are fixed; the design system fixes landed with the 19 Oct library update.
**Checked:** 15 screens, Light + Dark (30 frames) in "Laabh — KYC Onboarding" · 19 Oct 2026 · final check before handoff (re-check)
**Open problems:** 🔴 Must fix: 0 · 🟠 Should fix: 0 · 🟡 Small fix: 0 · ⚪ Polish: 0

## At a glance
| # | Problem | Where | How serious | Fix | Who | Status |
|---|---|---|---|---|---|---|
| DR-01 | Text field and OTP box edges were too faint to see | Every screen with a field or OTP | 🔴 Must fix | Field and OTP edges now `border/strong` | DS owner | ✅ Fixed |
| DR-02 | In Dark, empty-field hints looked like typed text | K06b Dark | 🟠 Should fix | `text/placeholder` Dark dimmed | DS owner | ✅ Fixed |
| DR-03 | "OTP" and "code" used for the same thing | K01–K04 | 🟡 Small fix | "OTP" everywhere | Designer | ✅ Fixed |
| DR-04 | PAN-blocked screen only offered "Check again" | K07b | 🟡 Small fix | Progress-saved line + "I'll do this later" | Designer | ✅ Fixed |

## What to do next
1. Hand the screens to developers with the annotations on the Light frames.
2. Product answers the three questions below; each one adds a screen or state later, none blocks handoff.
3. DS owner fixes the Top Bar text bug (Notes) so the screens can use the Top Bar's new Stage setting.

## Details
### DR-01 · Text field and OTP box edges were too faint to see · 🔴 Must fix (S1)
- **Where:** the TextField edge on K01, K01b, K03, K06, K06b, K06c, K06d and the OTP boxes on K02, K02b, K04, Light and Dark.
- **What's wrong:** the edge was 1.16:1 against the page (needs 3:1). Now `border/strong`: 3.81:1 Light, 3.34:1 Dark, measured by /ds-audit on all 17 fields.
- **Why it matters:** people with low vision need to see where to type on the first step of opening an account.
- **Fix:** done in the design system and accepted into this file; no screen change was needed.
- **Rule:** A11Y-COL-03
- **How sure:** High
- **Status:** Fixed (19 Oct 2026)

### DR-02 · In Dark, empty-field hints looked like typed text · 🟠 Should fix (S2)
- **Where:** K06b Enter PAN & DOB — Dark (`3:9447`).
- **What's wrong:** the hint colour was almost as bright as typed text. Now `frost/400`: 7.68:1 against typed text's 15.3:1, measured by /ds-audit, so empty fields read as empty.
- **Why it matters:** a user in Dark mode could think the sample PAN was already filled in.
- **Fix:** done in the design system (`text/placeholder` Dark).
- **Rule:** V-CONTRAST
- **How sure:** High
- **Status:** Fixed (19 Oct 2026)

### DR-03 · "OTP" and "code" used for the same thing · 🟡 Small fix (S3)
- **Where:** K01–K04 headings, descriptions and the K02c alert.
- **What's wrong:** two names for one thing.
- **Why it matters:** first-time users may think the "code" is something other than the OTP.
- **Fix:** "OTP" everywhere, Light and Dark.
- **Rule:** NH-4
- **How sure:** Medium
- **Status:** Fixed (19 Oct 2026)

### DR-04 · PAN-blocked screen only offered "Check again" · 🟡 Small fix (S3)
- **Where:** K07b PAN can't be used.
- **What's wrong:** an immediate retry was the only way on, though the fix takes days.
- **Why it matters:** users could give up, not knowing they can come back.
- **Fix:** "We've saved your progress, so you can pick up here later." and a "I'll do this later" button.
- **Rule:** NH-9 · TR-ACC-02
- **How sure:** Medium
- **Status:** Fixed (19 Oct 2026)

## Questions for the team
- Where does the help (?) button in the top bar go on each step? (Product)
- If the mobile number already belongs to an active client, what does the login hand-off look like? (Product)
- An invalid PAN (not the "not linked to Aadhaar" case): what copy and next step? (Product + compliance)

## Missing screens or states
- Email: invalid email error, and "email already registered" (K03)
- Mobile already registered to an active client (K01/K02)
- Invalid PAN result (K07b covers "not linked to Aadhaar" only)
- "Taking longer than usual" while verifying (K07; in the annotations only)
- Buttons while sending (no loading state in the DS yet; in the annotations)
- Google/Apple sign-in on Email (needs a new DS component)

## Good things
- The locked screen (K02c) now uses the OTP's real Disabled state: grey boxes and "Try again after 4:52 pm", so nothing looks typeable.
- The consent checkbox and the "belongs to me" checkboxes now wrap their full text, including why SEBI asks for the user's own number.
- Every error still says how to fix it, and the prefill consent stays honest and unticked.

## Checked and fine
- Edit (32 pt) and the "belongs to me" checkboxes (40 pt) are small, but 44 pt tap areas are annotated (AN-11).
- Top-bar back/help (40 pt), the sheet's close (24 pt) and its consent row (36 pt) are inside DS components; the sheet has "I'll type them myself" as a way out (D-01).
- Checkbox ticks are white on blue (4.78:1) after the DS update.
- 30-minute lock after 3 wrong OTPs: a security time limit (A11Y-TIM-01); the unlock time is shown three times (alert, under the boxes, on the button).
- OTP paste and SMS autofill are annotated (A11Y-AUT-01).
- All 60 measured colour pairs pass in both modes.

## Notes for the team
- **Annotations missing:** none on the Light frames. Dark frames have none by design.
- **Measured by /ds-audit:** 60 colour pairs, 0 failing; 17 small-tap notes (all annotated or inside DS components). Report: `prds/kyc-onboarding/audit.md`.
- **Design-system gaps:** Top Bar's new Stage 2–5 variants don't show the Step and Title text (it's not linked to the properties), so these screens keep Stage 1 with hand-set progress bars until that's fixed. Timeline's "done" tick is still black on blue (4.03:1, passes) while Checkbox ticks are now white; worth matching. Still open from before: Button loading state, Google/Apple sign-in button, date field.
- **Needs research:** none.
- **About this review:** iOS + Android · first-time investors · task walked: verify mobile and email, allow or skip the prefill, confirm PAN and date of birth, get through PAN verification or learn why the PAN is blocked. Re-check after the 19 Oct DS update; K02c, the checkboxes and the Top Bars were changed on the screens today.

# Design review: KYC onboarding S1–S4 (K01–K07b)
**Result:** ❌ Not ready for handoff. Two problems are left, both inside the design system (not in these screens); they're waiting on a DS owner.
**Checked:** 15 screens, Light + Dark (30 frames) in "Laabh — KYC Onboarding" · 19 Oct 2026 · final check before handoff
**Open problems:** 🔴 Must fix: 1 · 🟠 Should fix: 1 · 🟡 Small fix: 0 · ⚪ Polish: 0

## At a glance
| # | Problem | Where | How serious | Fix | Who | Status |
|---|---|---|---|---|---|---|
| DR-01 | Text field and OTP box edges are too faint to see | Every screen with a field or OTP | 🔴 Must fix | Use `border/strong` for field and OTP edges in the DS | DS owner | Open |
| DR-02 | In Dark, empty-field hints look like typed text | K06b Dark | 🟠 Should fix | Make `text/placeholder` dimmer in Dark | DS owner | Open |
| DR-03 | "OTP" and "code" used for the same thing | K01–K04 | 🟡 Small fix | Say "OTP" everywhere | Designer | ✅ Fixed |
| DR-04 | PAN-blocked screen only offers "Check again" | K07b | 🟡 Small fix | Say progress is saved; add "I'll do this later" | Designer | ✅ Fixed |

## What to do next
1. DS owner fixes DR-01 and DR-02 in the design system and publishes the library (in progress in the "Fix DS bugs found by the KYC PRD test" session).
2. Designer accepts "Library updates available" in "Laabh — KYC Onboarding".
3. Run `/ds-audit` and `/design-review` again; if nothing is left open, the screens are ready for handoff.

## Details
### DR-01 · Text field and OTP box edges are too faint to see · 🔴 Must fix (S1)
- **Where:** the TextField edge on K01, K01b, K03, K06, K06b, K06c, K06d and the OTP boxes on K02, K02c, K04, Light and Dark (e.g. `I3:2522;25:448`, `I3:5565;52:29`).
- **What's wrong:** the edge that shows where to type is 1.16:1 against the page in Light and 1.23:1 in Dark (1.12:1 on the prefilled style); it needs 3:1. Measured by /ds-audit.
- **Why it matters:** someone with low vision can't see where to type their mobile number, email, PAN or OTP, on the very first step of opening an account.
- **Fix:** in the design system, switch the TextField and OTP Cell edges to `border/strong` (3.81:1 Light, 3.34:1 Dark, measured on the checkbox on these screens). No change to the screens; they update with the library. Trade-off: a slightly heavier look on the glass fields, which accessibility outranks.
- **Rule:** A11Y-COL-03
- **How sure:** High
- **Status:** Open

### DR-02 · In Dark, empty-field hints look like typed text · 🟠 Should fix (S2)
- **Where:** K06b Enter PAN & DOB — Dark (`3:9447`): the PAN hint "ABCDE1234F" and the DOB hint "DD MMM YYYY".
- **What's wrong:** in Dark the hint colour (`text/placeholder`, 12.34:1, measured by /ds-audit) is almost as bright as typed text (15.3:1) and brighter than secondary text. In Light it matches secondary text.
- **Why it matters:** a first-time user in Dark mode can think the sample PAN is already filled in, or is theirs, then tap Verify PAN and get an error.
- **Fix:** in the design system, set `text/placeholder` in Dark to the same step as `text/secondary` (7.68:1 on the field, checked with token-contrast).
- **Rule:** V-CONTRAST
- **How sure:** High
- **Status:** Open

### DR-03 · "OTP" and "code" used for the same thing · 🟡 Small fix (S3)
- **Where:** the "Send OTP" button and "Resend OTP" / "Incorrect OTP" helper, against the heading "Enter the code we sent" and "4-digit code" (K01–K04).
- **What's wrong:** two names for one thing within two screens.
- **Why it matters:** a first-time user may wonder whether the "code" is different from the OTP they were promised; screen-reader users hear two names for one field.
- **Fix:** use "OTP" everywhere: "Enter the OTP we sent", "We texted a 4-digit OTP…", "Too many wrong OTPs".
- **Rule:** NH-4
- **How sure:** Medium
- **Status:** Fixed (19 Oct 2026, Light + Dark)

### DR-04 · PAN-blocked screen only offers "Check again" · 🟡 Small fix (S3)
- **Where:** K07b PAN can't be used (`3:8111`).
- **What's wrong:** the only action was an immediate retry, while the text says linking PAN and Aadhaar can take a few days, and nothing said the application was saved.
- **Why it matters:** the user retries, fails again, and may give up or start over without knowing they can come back.
- **Fix:** add "We've saved your progress, so you can pick up here later." and a "I'll do this later" ghost button under "Check again" (one main button stays).
- **Rule:** NH-9 · TR-ACC-02
- **How sure:** Medium
- **Status:** Fixed (19 Oct 2026, Light + Dark)

## Questions for the team
- Where does the help (?) button in the top bar go on each step? (Product)
- If the mobile number already belongs to an active client, what does the login hand-off look like? (Product)
- An invalid PAN (not the "not linked to Aadhaar" case): what copy and next step? (Product + compliance)

## Missing screens or states
- Email: invalid email error, and "email already registered" (K03)
- Mobile already registered to an active client (K01/K02)
- Invalid PAN result (K07b covers "not linked to Aadhaar" only)
- "Taking longer than usual" while verifying (K07; described in the annotations only)
- Buttons while sending (no loading state in the DS yet; described in the annotations)
- Google/Apple sign-in on Email (needs a new DS component)

## Good things
- Every error says how to fix it: "like ABCDE1234F" (K06c), "the date of birth shown on your PAN card" (K06d), and the unlock time on the locked screen (K02c).
- The prefill consent is honest: unticked, says what's fetched and that it's "Not a credit check", and "I'll type them myself" is a full-size way out.
- "Welcome back" (K02d) picks up where the user left off without asking anything again, and reads each stage's state in words.

## Checked and fine
- Edit (32 pt) and the "belongs to me" checkboxes (40 pt) are small, but 44 pt tap areas are annotated (AN-11).
- Top-bar back/help (40 pt), the sheet's close (24 pt) and its consent row (36 pt) are inside DS components (sent to the DS owner); the sheet also has "I'll type them myself" as a way out (D-01).
- The first OTP box looks active while locked (K02c): the team accepted this until the DS adds a locked state (plan.md, Decisions & waivers).
- Consent checkbox plus "Allow and continue": explicit consent is required and stays (GOV-08).
- 30-minute lock after 3 wrong OTPs: a security time limit, allowed (A11Y-TIM-01); the unlock time is shown.
- OTP can be pasted and auto-filled from SMS (annotated, A11Y-AUT-01).
- "Verifying PAN" moves on by itself: not a surprise change, and it's announced (A11Y-FRM-03).
- The PAN field doesn't need an autofill type (not on the WCAG list, A11Y-FRM-02).
- Light hint text (5.94:1) is readable.

## Notes for the team
- **Annotations missing:** none on the Light frames (every screen has the IDs it needs). Dark frames have none by design: annotations live on Light.
- **Measured by /ds-audit:** 62 colour pairs, 4 failing, all the DS edges in DR-01. Full report: `prds/kyc-onboarding/audit.md`. Nothing left to measure.
- **Design-system gaps:** OTP Input locked state and editable helper text · Button loading state · Google/Apple sign-in button · date field · Top Bar "current stage" setting. DS bugs: the prefill consent ships pre-ticked (unticked on K05), a stray "Enter at least ₹100" line in error fields (hidden on K06c/K06d), checkbox text doesn't wrap.
- **Needs research:** none.
- **About this review:** iOS + Android · first-time investors · task walked: verify mobile and email, allow or skip the prefill, confirm PAN and date of birth, get through PAN verification or learn why the PAN is blocked. Assumes the market state doesn't matter here and that K04 reuses the wrong-OTP and locked screens of K02. The library was up to date when checked.
