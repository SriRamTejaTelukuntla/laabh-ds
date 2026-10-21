# Design review: MF KYC, rounds 3–4 (M00–M31, Light + Dark)
**Result:** ❌ Not ready for handoff. The SIP review shows ₹0 charges, and the citizenship/tax/PEP declaration on M14 is already ticked. Both are must-fix and waiting on the designer.
**Checked:** 51 Light frames reviewed by content, components and annotations (sections 0–5; section 5 "To be discussed" read but not judged as main flow); Dark measured by /ds-audit only, not screenshotted in this pass · 2026-10-20 · final check before handoff
**Open problems:** 🔴 Must fix: 2 · 🟠 Should fix: 3 · 🟡 Small fix: 2 · ⚪ Polish: 1

## At a glance
| # | Problem | Where | How serious | Fix | Who | Status |
|---|---|---|---|---|---|---|
| DR-01 | SIP review says charges are ₹0, but stamp duty and the fund's expense ratio apply | M29 | 🔴 Must fix | List stamp duty, expense ratio and exit load in the summary | Designer + Compliance | Open |
| DR-02 | The citizenship, tax and PEP declaration is already ticked | M14 | 🔴 Must fix | Show it unticked, Continue disabled with a reason | Designer | Open |
| DR-03 | A politically exposed person or a foreign tax resident has no way forward | M14 | 🟠 Should fix | Add "This doesn't apply to me" below the declaration, leading to an ops/FATCA path | Product + Designer | Open |
| DR-04 | Auto-verify can submit the OTP before the user ticks the bureau consent, so most people lose the PAN prefill | M02, M02b | 🟠 Should fix | Move the consent to M01 above "Send OTP", or keep a Verify button on M02 | Designer | Open |
| DR-05 | The fetched bank account has no "in my name only" declaration | M20 | 🟠 Should fix | Put the single-holder Checkbox back above the CTA, or confirm the bank response covers it | Designer + Product | Open |
| DR-06 | The status screens opened from "Application submitted" have no Back | M26, M26b | 🟡 Small fix | Turn on the Top Bar Back, back to M27 | Designer | Open |
| DR-07 | The declaration checkbox on M14 is small text with no 44 pt hit-area note | M14 | 🟡 Small fix | Annotate the whole row as the target (AN-11) | Designer | Open |
| DR-08 | Sample dates don't line up between screens | M26, M26b, M31 | ⚪ Polish | Use one submission day across the post-submit screens | Designer | Open |

## What to do next
1. Designer: fix DR-01 and DR-02 (M29 charges, M14 declaration), Light and Dark.
2. Product and Compliance: answer Q12 (PEP / foreign tax path), Q16 (email self-declaration), Q17 (consent vs auto-verify) and Q18 (PAN card header). DR-03 and DR-04 follow from them.
3. Designer: DR-05 to DR-08, then re-run /ds-audit and this review on the changed screens.

## Details
### DR-01 · SIP review says charges are ₹0, but stamp duty and the fund's expense ratio apply · 🔴 Must fix (S1)
- **Where:** M29 Review your SIP, Summary Card row "Charges: ₹0 (direct plan, no commission)" (`88:22696`, Dark `99:16549`)
- **What's wrong:** The review states ₹0 charges. Every MF purchase pays 0.005% stamp duty, the fund deducts its expense ratio from NAV, and some funds have an exit load.
- **Why it matters:** A first-time investor reads "₹0" as "no cost at all" at the moment of committing money. That's a misread of money and hides charges until after the decision.
- **Fix:** Replace the row with "Transaction charges: ₹0", then add rows for stamp duty (0.005%, about ₹0.03 on ₹500), expense ratio (e.g. 0.20% a year, taken from NAV) and exit load (as per scheme). Same Summary Card, no new component.
- **Rule:** DN-GULFS · TR-RISK-04
- **How sure:** High
- **Status:** Open

### DR-02 · The citizenship, tax and PEP declaration is already ticked · 🔴 Must fix (S1)
- **Where:** M14 Work, income & nominee, footer Checkbox "I'm an Indian citizen and a tax resident of India only, and I'm not a politically exposed person" (`82:10841`, Dark `99:15170`); Selection=Checked
- **What's wrong:** The legal declaration is pre-ticked on the default screen, and its own annotation says "unticked by default". M14b still shows it unticked, so the two frames disagree.
- **Why it matters:** A pre-ticked self-declaration lets a user agree to a FATCA/PEP statement without reading it. It's a deceptive default, and the declaration may not hold up later.
- **Fix:** Set the Checkbox to Unchecked on M14 Light and Dark, keep Continue disabled with the reason "Tick the declaration to continue", and match the label on M14b (it still says "(FATCA/CRS)").
- **Rule:** L-BIAS · TR-RISK-01
- **How sure:** Medium (it may have been ticked to show a filled state; then it needs its own state frame)
- **Status:** Open

### DR-03 · A politically exposed person or a foreign tax resident has no way forward · 🟠 Should fix (S2)
- **Where:** M14, declaration Checkbox and Continue (`82:10841`, `16:2025`)
- **What's wrong:** The only path is to tick "I'm not a politically exposed person … tax resident of India only". Someone for whom that isn't true can't tick it and can't continue; the annotation leaves the path to be discussed (Q12).
- **Why it matters:** A legitimate applicant hits a dead end in onboarding with no explanation, or ticks a false declaration to get through.
- **Fix:** Add a Button Ghost sm "This doesn't apply to me" under the declaration. It opens a short screen saying our team will contact them to complete the extra forms (PRD: PEP and foreign tax residence go to ops).
- **Rule:** NH-3 · TR-ACC-02
- **How sure:** High
- **Status:** Open

### DR-04 · Auto-verify can submit the OTP before the user ticks the bureau consent · 🟠 Should fix (S2)
- **Where:** M02 and M02b, Checkbox "I allow Laabh to fetch and verify my personal details from a credit bureau" under the OTP Input (`80:9974`, `80:9981`)
- **What's wrong:** The OTP verifies itself on the 4th digit and moves on, so the consent has to be ticked before typing the last digit. SMS autofill fills all four digits at once.
- **Why it matters:** Most users won't see or tick the consent in time, so they miss the PAN-card prefill on M07 and type everything on M07b: the opposite of what the prefill is for.
- **Fix:** Move the consent to M01 above "Send OTP" (one decision, before the code), or keep a Verify button on M02 only. Recorded as Q17.
- **Rule:** NH-7 · TR-ACC-03
- **How sure:** High
- **Status:** Open

### DR-05 · The fetched bank account has no "in my name only" declaration · 🟠 Should fix (S2)
- **Where:** M20 Confirm bank account (`85:10705`, Dark `112:12406`); the CTA's annotation still refers to a checkbox that is no longer there
- **What's wrong:** The single-holder Checkbox was removed, and nothing on the screen says the account was checked as individually held or that the holder name matched the PAN.
- **Why it matters:** PRD S7.4 needs the user to declare the account is held singly. Without it, a joint account can be confirmed in one tap and is rejected later.
- **Fix:** Put the Checkbox "This account is in my name only" back above "Yes, use this account" (disabled with a reason until ticked), or add a verified row "Account holder · Matches your PAN" if the fetch returns holder type.
- **Rule:** NH-5 · TR-ACC-01
- **How sure:** Medium (depends on what the fetch vendor returns, Q10)
- **Status:** Open

### DR-06 · The status screens opened from "Application submitted" have no Back · 🟡 Small fix (S3)
- **Where:** M26 and M26b, Top Bar with Show leading off (`24:3852`, `29:3823`)
- **What's wrong:** M26/M26b are now opened from the banner on M27, but have no Back; the only exit is "Go to home".
- **Why it matters:** A user checking their status can't return to the investment-ready screen they came from.
- **Fix:** Top Bar Show leading on; Back returns to M27.
- **Rule:** NH-3 · M-08
- **How sure:** High
- **Status:** Open

### DR-07 · The declaration checkbox on M14 is small text with no 44 pt hit-area note · 🟡 Small fix (S3)
- **Where:** M14 Checkbox sm (`82:10841`), 36 pt tall, measured by /ds-audit
- **What's wrong:** The Checkbox is 36 pt tall and its annotation doesn't say the whole row is the target.
- **Why it matters:** Users with less precise touch may miss it, and it gates the Continue button.
- **Fix:** Add AN-11 "the whole row, label included, is the target (at least 44 pt)", as on the other declarations.
- **Rule:** L-FITTS · M-02
- **How sure:** High
- **Status:** Open

### DR-08 · Sample dates don't line up between screens · ⚪ Polish (S4)
- **Where:** M26/M26b "Submitted 19 Oct 2026, 5:52 PM" vs M31 "Autopay approved Today, 10:48 AM" and M27 landing straight after submit
- **What's wrong:** The post-submit screens show different days for what is one sitting.
- **Why it matters:** Reviewers and developers read the sample data as the intended timeline.
- **Fix:** Use one submission date and time across M26, M26b, M27 and M31.
- **Rule:** NH-4
- **How sure:** High
- **Status:** Open

## Questions for the team
- Should eSign come back into the main flow before M27? Profile currently goes straight to "Application submitted" while Review and eSign sit in "To be discussed" (Prasad / Product).
- Where does the "this number/email belongs to me" self-declaration go now that email is social-first (Q16, Product / Compliance)?
- Is the PAN card header "INCOME TAX DEPARTMENT / GOVT. OF INDIA" acceptable over bureau data that NSDL hasn't verified yet (Q18, Compliance)?
- Can a SIP be registered before the account is active, and what happens to it if autopay is skipped (Q13, Q20, Product / BSE)?
- Should M27/M30 mention that the bank may charge for a failed autopay debit (bounce charge), and where (Product / Compliance)?

## Missing screens or states
- Review and eSign in the main flow (M24/M24b parked)
- "Welcome back" resume state (annotated on M02 only)
- Weak MPIN error (M03), too many MPIN mismatches (M03c)
- No bank account found for the mobile number (M20b alert, annotated only)
- Autopay declined or timed out (M30, annotated only)
- Amount below ₹100 (M28 error state)
- Fund search results and no results (M27)
- Declaration unticked with Continue disabled (M14)
- Loading on "Yes, this is my PAN" while PAN and KRA are checked (M07)
- DigiLocker flow (M10 placeholder)

## Good things
- M29 restates fund, plan, amount, date, first debit and bank before confirming, and M31 says "scheduled", not "invested", with an honest timeline.
- M30 frames ₹15,000 as an autopay limit "used for your SIPs, on their dates", with a neutral "Skip for now".
- M18b offers a one-tap "Divide equally" right where the error is.

## Checked and fine
- Radio inside the UPI app rows on M20b measures 20 pt, but the whole List Row is the target (annotated AN-04), so WCAG 2.5.8 passes.
- "Change number/email" Ghost buttons measure 32 pt; each has an AN-11 44 pt hit-area note.
- File Upload's Icon Tile border (1.28:1) is decorative, not the control's boundary; the dashed `border/strong` boundary measures 3.81:1.
- TextField/Amount quick-add buttons (`glass/hairline` border 1.16:1) are identified by their text labels, so their boundary isn't needed (WCAG 1.4.11 exception).
- Fund rows show the riskometer level and "Min ₹100" before choosing (TR-ORD-03), and the disclosure sits at the decision point in body size.
- Top Bar stage order (Contact · Identity · Bank · Profile · Review) matches the section order.

## Notes for the team
- **Annotations missing:** M03/M03b/M03c carry OTP annotations (SMS autofill, resend, 30-minute lock) that don't apply to an MPIN; M07 frame annotation still routes to M08/M10b/M12; M28 "SIP date" annotation sits on a layer named "Annual income"; M20 annotations mention a checkbox and a local logo that are gone; M14 declaration lacks AN-11.
- **Measured by /ds-audit:** 102 frames, 0 S1, 7 S2, 25 S3, 2 S4; all S2s are inside DS components and cleared above (`prds/mf-kyc/audit.md`).
- **Design-system gaps:** Bottom Sheet close is 24×24 (house rule 44); List Row action Button is 32 pt; Alert action Button is 28 pt; Option Card has no flat style for sheets and no larger leading slot for logos.
- **Needs research:** whether users understand "MPIN" as different from their UPI PIN → a 5-user test of M03 with first-time investors.
- **About this review:** iOS + Android, first-time MF investor (novice-safe), tasks walked: sign up, confirm PAN, link bank, add profile and nominees, then set up autopay and a first SIP. Assumed KRA-validated user with a bank account found from the mobile number. Section 5 screens are parked by decision and not judged.

---

# Design review: MF KYC, Journey A, re-check after fixes (M00–M26b, Light + Dark)
**Platform:** iOS + Android · **Segment:** first-time investor, novice-safe · **Stage:** final · **Reviewed:** 2026-10-19
**Task walked:** same as the first review below, starting at the new Welcome (M00), plus the outcomes added since: M08c no connection, M09b name check, M23c bank name check, M23d second UPI failure → account number, M23e joint account, M25c eSign tries used up, M26b KYC validation pending (1 working day).
**Assumptions:** as below; the OTP cells' drop shadow (`elevation/control`) is not counted by /ds-audit.
**States reviewed:** 46 Light + 46 Dark frames, annotated (AN-01, 03, 04, 05, 06, 07, 08, 09, 11, 14, 15). · **Missing states:** upload PAN image only (blocked: no upload component).

## Verdict: Pass with fixes
S1: 0 · S2: 1 · S3: 0 · S4: 0

## Findings (most severe first)
### [S2] Empty OTP cells have a 1.16:1 border · DR-01
- **Where:** OTP Input, empty cells, on M02, M05, M19, M19b (Light `I9:398;52:36`, Dark `I30:3885;52:36`).
- **Problem:** the empty cell edge is `glass/hairline` (1.16:1 Light, 1.23:1 Dark), measured by /ds-audit; only the component's soft shadow outlines it.
- **Impact:** low-vision users may not see how many digits are left to type on the OTP steps.
- **Principle:** A11Y-COL-03 · TR-ACC-04
- **Tag:** WCAG
- **Recommendation:** DS owner: move the OTP Cell `Empty` border to `border/strong` (3.81:1 Light, 3.34:1 Dark, as TextField already uses). It sits inside the component, so it can't be fixed from this file; screens update automatically after the library publish.
- **Confidence:** Medium (the shadow may carry it; measure the shadow by hand)

## Systemic issues (seen on 3+ screens)
- none left at screen level. DS-level tap sizes (Top Bar 40 pt, Segment 30 pt) are annotated with 44 pt hit areas and handed to the DS owner.

## Needs annotation   (accessibility.md §8: AN-xx missing)
- none: every Light frame carries AN-15 and AN-08; controls carry AN-03/04/05/07/09/11/14 as triggered. Dark frames share the Light annotations.

## Questions          (decisions the design can't show yet)
- Q8 final declaration wording (Compliance). Q5, Q6, Q7 and Q9 are answered and applied (1 working day, same-day refund with backup after 2 UPI failures, eSign for all, Welcome screen).

## Considered and cleared (one line each, only for items someone might expect)
- First review DR-01 (pre-answered PEP and tax residency): fixed, no option selected (M14, M15).
- First review DR-02 (field borders): fixed for every TextField (Outline/Filled, `border/strong` 3.81:1 Light, 3.34:1 Dark); only the OTP cells remain (DR-01 above).
- First review DR-03 (tap targets): "Add another nominee" is now lg (52 pt); every other small target has a 44 pt AN-11 hit area; primary CTAs carry the 48 dp note.
- First review DR-04 (missing outcomes): M23c and M26b added; the missing states it listed are now built too (M08c, M09b, M23d, M23e, M25c).
- First review DR-05 (Back on Submitted): annotated "Back goes to Home, never back into eSign" (AN-03); `Show leading` requested as a DS gap.
- Avatar initials 4.18:1: decorative duplicate of the name (AN-08).

## Hand-offs
- Contrast to measure → `/ds-audit`: done, `prds/mf-kyc/audit.md` (re-run on 92 frames, 3 failing pairs, all inside DS components).
- Raw values / token binding → `/ds-audit`: none.
- DS owner: OTP Cell empty border, Avatar initials pairing, Top Bar 40 pt buttons and `Show leading`, Segment height, TextField Default and Style=Filled borders, unpublished DS changes.
- DS gaps (no component exists) → `/new-component`: File Upload, brand logos.

## Needs research
- Does the ₹1 UPI route beat account-number entry for first-time investors? → funnel split by bank method after launch.

## What works (max 3, specific)
- Declarations now need an explicit answer, and opt-out of nomination needs a checkbox plus OTP: no legal choice is made by default.
- Every waiting and post-submit state names the next step and when it happens (M08, M12, M21, M23c, M26, M26b).
- Dark works through tokens alone: 46 copies, no manual fixes.

---

# Design review: MF KYC, Journey A (M01–M26, Light)
**Platform:** iOS + Android · **Segment:** first-time investor, novice-safe · **Stage:** final · **Reviewed:** 2026-10-19
**Task walked:** open an MF-only account: verify mobile and email → PAN and KYC check → profile, FATCA and nominees → link bank with ₹1 → review, declare and eSign → submitted.
**Assumptions:** persona is KRA-validated (K1 path) unless the screen says otherwise; market state n/a (onboarding); library assumed current (file created and library enabled today).
**States reviewed:** 38 Light frames (default, wrong code, locked, resume, bureau hit and miss, verifying, PAN blocked, KYC found, DigiLocker K1/K2, KRA elsewhere, KRA hold, opt-in/opt-out, minor nominee, shares ≠ 100%, UPI wait, UPI timeout, eSign failed, submitted). Dark: not built yet. · **Missing states:** bank name mismatch → manual check (PRD S7.3); submitted while KRA validation is pending for new-to-KRA users (PRD A11); network/offline on vendor waits (M08, M21); PAN/KRA name mismatch → ops review (PRD S5); eSign out of retries; joint-account rejection; upload PAN image (blocked: no upload component).

## Verdict: Changes required
S1: 2 · S2: 2 · S3: 1 · S4: 0

## Findings (most severe first)
### [S1] Regulatory declarations are pre-answered "No" · DR-01
- **Where:** M14 Occupation & income, "Are you, or a close relative, a politically exposed person?" Segmented Control (`16:2014`); M15 Tax residency, "tax resident of any country other than India?" (`16:2686`).
- **Problem:** both legal declarations open with "No" already selected.
- **Impact:** a user who skims can submit a false PEP or FATCA/CRS declaration without ever answering; PEP = yes and foreign tax residency must route to ops (PRD S6, A10). Legal data entered by default, in a first-run flow.
- **Principle:** A11Y-ERR-03 · TR-ORD-07
- **Tag:** UX
- **Recommendation:** show both Segmented Controls with no segment selected; on Continue with no answer, show the label's error text ("Choose Yes or No"). Trade-off: one more tap per question.
- **Confidence:** High

### [S1] Field and OTP boundaries are below 3:1 on core inputs · DR-02
- **Where:** M01 mobile field (`6:2521`), M04 email (`10:512`), M07 PAN and DOB (`12:1052`, `12:1111`, Style=Filled), M07b empty PAN and DOB (`12:1261`, `12:1319`), M13 parent names (`16:1764`, `16:1823`); empty OTP cells on M02, M05, M19, M19b.
- **Problem:** the field edge is `glass/hairline` (1.16:1) or `glass/edge` (1.12:1) on `surface/page`, measured by /ds-audit; the fill doesn't stand out either. Outline/Filled fields elsewhere use `border/strong` (3.81:1).
- **Impact:** low-vision users can't find the input to tap on the very first KYC screens (mobile, PAN, OTP).
- **Principle:** A11Y-COL-03 · TR-ACC-02
- **Tag:** WCAG
- **Recommendation:** in the screens, use `TextField Outline/Filled` (border/strong) for entered and prefilled values (M01, M04, M07, M07b, M13). For the DS owner: the TextField Default state, the `Style=Filled` border and the empty OTP Cell border should move to `border/strong` (they can't be fixed from a product file).
- **Confidence:** High (measured by /ds-audit)

### [S2] Tap targets under 44 pt on onboarding actions · DR-03
- **Where:** "Change" / "Edit" Ghost sm buttons, 32 pt (M02, M02b, M05, M18, M18b, M24 ×5); "Add another nominee" Outline md, 40 pt (M18, M18b); consent and declaration Checkboxes, 40 pt (M01, M04, M20, M22, M24 ×5); Top Bar back/help, 40 pt (all); Segments, 30 pt (M13, M14, M15, M22).
- **Problem:** visual targets below the 44 pt house rule; no hit areas annotated.
- **Impact:** mis-taps on first-run screens, worst for users with tremor or large thumbs; "Edit" on the review card sits close to the card content.
- **Principle:** M-02 · A11Y-TGT-01
- **Tag:** House
- **Recommendation:** "Add another nominee" → Button Outline lg (52). Annotate 44 pt hit areas (`AN-11`) on Ghost sm, Checkbox rows (whole row incl. label) and Segments; DS owner: Top Bar Icon Buttons and Segment height.
- **Confidence:** High (measured by /ds-audit)

### [S2] Two PRD outcomes have no screen · DR-04
- **Where:** Bank flow after M21; Submitted (M26).
- **Problem:** the PRD sends a bank name mismatch to ops review (S7.3) and keeps new-to-KRA users from transacting until CVL validates (A11), but no screen shows either; M26 only shows the KRA-validated path ("Usually by tomorrow").
- **Impact:** those users get no status or expected time, so they retry, re-link or call support; placed ≠ active isn't explained for them.
- **Principle:** TR-STATE-02 · TR-ORD-06
- **Tag:** UX
- **Recommendation:** add M23c "Bank account needs a quick check" (Warning tile, what happens next, no action required) and M26b "Submitted · KYC validation pending" (Timeline with the KRA step and its expected time, Q5).
- **Confidence:** High

### [S3] Back arrow on the Submitted screen · DR-05
- **Where:** M26 Submitted, Top Bar leading button (`24:3852`).
- **Problem:** the only header action after submitting is Back, which visually leads into eSign again.
- **Impact:** a user may think going back re-opens or undoes the signed application.
- **Principle:** M-08 · TR-ORD-06
- **Tag:** UX
- **Recommendation:** annotate Back as "goes to Home, never to eSign"; DS gap: Top Bar needs a `Show leading` option for result screens.
- **Confidence:** Medium

## Systemic issues (seen on 3+ screens)
- DR-02 field boundaries (8 screens) and DR-03 tap targets (every screen): same component choices repeated; fixed by variant choice and hit-area annotations.

## Needs annotation   (accessibility.md §8: AN-xx missing)
- AN-03 names for Top Bar back/help and each "Edit" ("Edit contact details", …) on every screen.
- AN-09 input purpose: mobile = tel, email = email, OTP = one-time-code (paste fills all, SMS autofill), DOB = bday; account number numeric keypad (`M-05`).
- AN-07 live regions: wrong code, locked, shares ≠ 100%, eSign failed, payment not received = assertive; Verifying and Waiting timelines, Bank linked, Submitted = polite.
- AN-11 hit areas (DR-03) and 48 dp on every primary CTA (`D-04`).
- AN-14 timing: OTP resend 30 s × 3, 30-minute lock (security exception), UPI wait timeout, eSign 3 tries.
- AN-04 role: Segmented Controls = radio group.
- AN-08 decorative: Screen Atmosphere, icon tiles, avatar initials (the name is read instead).
- AN-01 M24: sticky footer CTA (`M-01`) and reading order card by card, declarations last.
- AN-15 core screens: 200% text scrolls the body, footer stays; landscape = same single column (`D-02`).

## Questions          (decisions the design can't show yet)
- Q5 CVL KRA validation SLA for new-to-KRA users (Compliance), needed for M26b.
- Q6 ₹1 refund time and UPI timeout (Product), M20–M23.
- Q7 eSign for everyone vs 2FA-only for KRA-validated users (Product/BSE).
- Q8 final wording of the five declarations, including direct-plan (Compliance).

## Considered and cleared (one line each, only for items someone might expect)
- Avatar initials 4.18:1 (M18): decorative duplicate of the visible name; annotate AN-08 decorative (WCAG 1.4.3 decoration exception).
- Consent decline ("I'll type them myself", M06): full-width ghost, visible and equal in reach (TR-RISK-03 met).
- Opt-out copy (M16): states a consequence, no guilt wording (TR-RISK-01 met).
- "₹10 lakh to ₹25 lakh" (M14): abbreviations allowed off the review screen; M24 shows full figures (TR-NUM-04 met).
- Disabled "Confirm nominees" (M18b): the Danger alert says why (TR-ORD-05 met).
- 30-minute OTP lock (M02c): security exception to A11Y-TIM-01; unlock time is shown.

## Hand-offs
- Contrast to measure → `/ds-audit`: done, `prds/mf-kyc/audit.md` (3 failing pairs, all component-level).
- Raw values / token binding → `/ds-audit`: none found.
- DS owner: TextField Default + Style=Filled borders, OTP Cell empty border, Avatar initials pairing, Top Bar 40 pt buttons and missing `Show leading`, Segment 30 pt, unpublished DS changes (Top Bar `Stage`, OTP Input text props).
- DS gaps (no component exists) → `/new-component`: File Upload (M10c, M11 proof), brand logos (Google, Apple, banks).

## Needs research
- Does the ₹1 UPI route actually beat account-number entry for first-time investors? → funnel split by bank method after launch.

## What works (max 3, specific)
- Every sensitive request says why at the point of asking (consent cards on M06, M10, M10b; "SEBI asks every investor" on M14).
- Waiting states (M08, M12, M21, M26) use one Timeline pattern with an expected time on each pending step.
- The review screen restates every section with Edit links and full figures before eSign (`D-03`).
