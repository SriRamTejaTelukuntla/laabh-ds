# Design review: KYC onboarding S1–S4 (Contact and Identity, K01–K07b)
**Platform:** iOS + Android · **Segment:** first-time investor (novice-safe) · **Stage:** final · **Reviewed:** 2026-10-19
**Task walked:** a new user verifies their mobile and email, allows (or declines) the bureau prefill, confirms PAN and date of birth, and gets through PAN verification or learns why their PAN is blocked.
**Assumptions:** market state n/a (account opening behaves the same in every state); K04 reuses K02b/K02c for wrong code and lock; the Figma file "PRD Test" (since renamed "Laabh — KYC Onboarding") has no pending library updates (confirmed by the designer); annotations live on the Light frames only.
**States reviewed:** K01, K01b offline, K02, K02b wrong code, K02c locked, K02d resume, K03, K04, K05 consent sheet, K06 prefilled, K06b empty, K06c format error, K06d mismatch, K07 verifying, K07b blocked, each in Light + Dark (30 frames) · **Missing states:** K03 invalid email and "email already registered" (S2.2 dedupe) · mobile already belongs to an active client (login hand-off) · PAN invalid (not inoperative) · K07 "taking longer" (annotated only) · loading on submit (annotated only; Button has no Loading state) · Google/Apple sign-in (DS gap)

## Verdict: Changes required
S1: 1 · S2: 1 · S3: 2 · S4: 0

**Update 2026-10-19:** DR-03 and DR-04 fixed and re-reviewed on K01–K04 and K07b (Light + Dark). DR-01 and DR-02 wait on DS changes, so the verdict stands.

## Findings (most severe first)
### [S1] Field and code-box edges are almost invisible · DR-01
- **Where:** TextField `Field` on K01, K01b, K03, K06, K06b, K06c, K06d (e.g. `I3:2522;25:448`, `I3:6548;25:756`) and OTP Cells on K02, K02c, K04 (`I3:5565;52:29`), Light and Dark.
- **Problem:** the edge that shows where to type is `glass/hairline` (Outline) or `glass/edge` (Filled): 1.16:1 Light, 1.23:1 Dark, 1.12:1 Light on Filled, against 3:1 needed (measured by /ds-audit). The field fill doesn't stand out 3:1 either.
- **Impact:** a low-vision user on the very first signup step can't see where the mobile number, email, PAN or code goes, so they can't start KYC. WCAG AA failure on the core task of a first-run flow.
- **Principle:** A11Y-COL-03
- **Tag:** WCAG
- **Recommendation:** inside the DS (no screen change): DS owner switches the TextField Outline/Filled edge and the OTP Cell edge to `border/strong` (measured 3.81:1 Light, 3.34:1 Dark on the checkbox on these screens) via `/new-component`, publishes, then the screens pick it up after "Update all" and the audit is re-run. Trade-off: a slightly heavier look on the glass fields, which the accessibility floor outranks (governance §4).
- **Confidence:** High

### [S2] Empty-field hints in Dark look like typed values · DR-02
- **Where:** K06b Enter PAN & DOB — Dark (`3:9447`): PAN hint "ABCDE1234F" and DOB hint "DD MMM YYYY".
- **Problem:** `text/placeholder` in Dark (12.34:1 on `glass/field`, measured by /ds-audit) is almost as bright as entered text (`text/primary` 15.3:1) and brighter than `text/secondary`. In Light the hint matches secondary text. Empty and filled fields look the same in Dark.
- **Impact:** a first-time user in Dark mode can think the sample PAN is already filled in (or is theirs), tap Verify PAN, and hit an error, or doubt what the app has stored.
- **Principle:** V-CONTRAST
- **Tag:** UX
- **Recommendation:** DS owner sets `text/placeholder` Dark to the same step as `text/secondary` (`frost.400`), as Light already does; check with `python3 scripts/token-contrast.py text/placeholder glass/field` that it stays ≥ 4.5:1. No screen change.
- **Confidence:** High

### [S3] "OTP" and "code" name the same thing · DR-03
- **Where:** K01/K03 button "Send OTP" and K02/K02b/K04 helper "Resend OTP in 0:24" / "Incorrect OTP · 2 attempts left", against the K02/K04 heading "Enter the code we sent" and description "4-digit code".
- **Problem:** two names for one thing within two screens.
- **Impact:** a first-time user may wonder whether the "code" is something other than the OTP they were promised; a screen-reader user hears both names for the same field.
- **Principle:** NH-4
- **Tag:** UX
- **Recommendation:** use "OTP" everywhere (the DS helper text can't be changed and already says OTP): heading "Enter the OTP we sent", description "We texted a 4-digit OTP…". Add the term to `docs/content/voice.md` § Vocabulary.
- **Confidence:** Medium

### [S3] PAN blocked: "Check again" is the only way on, though the fix takes days · DR-04
- **Where:** K07b PAN can't be used — Light (`3:8111`): footer "Check again", description ending "The update can take a few days."
- **Problem:** the only action is an immediate retry, and nothing says the application is saved for later.
- **Impact:** the user retries, fails again, and may abandon or start over, not knowing K02d will resume them later.
- **Principle:** NH-9 · TR-ACC-02
- **Tag:** UX
- **Recommendation:** add "We've saved your progress, so you can pick up here later." to the description and a `Button Ghost · Neutral · lg` "I'll do this later" under "Check again" (one primary stays, `M-03`). Severity: S3 base, +1 first-run flow, −1 because K02d already resumes on return.
- **Confidence:** Medium

## Systemic issues (seen on 3+ screens)
- DR-01 (field and code-box edges) appears on 10 Light and 10 Dark frames. One DS fix covers all of them.

## Needs annotation   (accessibility.md §8: AN-xx missing)
- None on the Light frames (review-context: every screen has AN-01, 03, 05, 06, 08, 11, 15 plus the field, OTP, sheet and live-region IDs it triggers). Dark frames carry none by design (annotations live on Light).

## Questions          (decisions the design can't show yet)
- Where does the Top Bar help (?) go on each step? (Product)
- A mobile number that belongs to an active client: what does the login hand-off look like? Q3 only covered in-progress applications. (Product)
- An invalid PAN (not inoperative): same K07b layout with what copy and next step? (Product + compliance)

## Considered and cleared (one line each, only for items someone might expect)
- Edit (32 pt) and declaration checkboxes (40 pt): 44 pt hit areas annotated (AN-11).
- Top Bar back/help 40×40, sheet Close 24×24, sheet consent row 36 pt: inside DS components (hand-off); K05 also has "I'll type them myself" as its exit (`D-01`).
- K02c first code box looks active while locked: waived in plan Decisions & waivers (`GOV-07`).
- Consent checkbox plus "Allow and continue": explicit consent is required (`GOV-08`); unticked by default, decline is a full-size button.
- 30-minute OTP lock: security exception to A11Y-TIM-01; the unlock time is shown and the disabled button says why.
- OTP entry: paste and SMS/one-time-code autofill annotated (A11Y-AUT-01, AN-09).
- K07 moves on by itself: not a user-input change (A11Y-FRM-03), announced politely (AN-07).
- PAN field purpose: not on the WCAG input-purpose list (A11Y-FRM-02 skip).
- Light placeholder `text/placeholder` 5.94:1 on `glass/field`: passes.

## Hand-offs
- Contrast to measure → `/ds-audit`: done, 62 pairs measured, 4 failing (all DS edges, DR-01). Report: `prds/kyc-onboarding/audit.md`.
- Raw values / token binding → `/ds-audit`: none found (0 raw values, 0 unstyled text).
- DS gaps (no component exists) → `/new-component`: OTP Input Disabled state and editable helper text · Button Loading state · Google/Apple sign-in button · date field · Top Bar stage property.
- DS fixes → DS owner: `Sheet Content/Prefill consent` master is pre-ticked (overridden on K05) · TextField Error has a stray "Enter at least ₹100" layer (hidden on K06c/K06d) · Checkbox text doesn't wrap · `text/placeholder` Dark (DR-02) · field/OTP edges (DR-01).

## Needs research
- None.

## What works (max 3, specific)
- Every error says how to fix it: K06c "like ABCDE1234F", K06d "the date of birth shown on your PAN card", K02c the unlock time on the disabled button.
- The prefill consent is honest: unticked, purpose and "Not a credit check" stated, and "I'll type them myself" is a full-size way out.
- K02d resumes without re-asking anything and reads each stage's state in words, not just ticks.
