# KYC onboarding (S1–S4): screen plan

> **Status:** handed off (ready; 3 open questions) · **Updated:** 2026-10-19 · **Branch:** `prd/kyc-onboarding` · **Figma file:** https://www.figma.com/design/uX1kcZaXFqPT8CHAKZt8Y6/Laabh-KYC-Onboarding

First real `/prd-to-screens` run (started as a test). Figma file "Laabh — KYC Onboarding" (renamed from "PRD Test" on 2026-10-19; same file key). It is the first file to use the "Laabh — <Feature>" name; the team hasn't confirmed that scheme yet.
**In scope:** PRD steps S1–S4 (mobile, email, bureau prefill consent, PAN + DOB, PAN verification). **Out of scope:** S5 KRA fetch onward, Journeys A/B/C endings (`prd.md`).

## Review context
| Context | Value |
|---|---|
| Platform | iOS + Android (`D-04`) |
| Surface | onboarding (`TR-ACC`) |
| User segment | first-time investor (novice-safe) |
| Market states | n/a (account opening works the same in every market state) |
| Entry points | Welcome → "Get started" (A01); resume from a drop-off nudge (push/SMS) lands on the last checkpoint |

## Flows
1. Contact: Mobile number → Verify mobile (OTP) → Email → Verify email (OTP)
2. Identity: Prefill consent (sheet) → Confirm PAN & DOB (prefilled on bureau hit, empty on miss or decline) → Verifying PAN → next: KRA fetch (out of scope) · or PAN blocked (inoperative / invalid)

Stages in the Top Bar: Contact (1) · Identity (2) · Profile (3) · Bank (4) · Review (5). Caption "Step n of 5 · <Stage>".

## Screens
| ID | Screen | Type | Surface | Components | States | Rules that apply | Reference | Status | Figma |
|---|---|---|---|---|---|---|---|---|---|
| K01 | Mobile number | flow step | onboarding | Top Bar, TextField lg (+91 prefix), Checkbox (own-number declaration, unticked), Button lg | default (filled); error = field Error state (format) | TR-ACC-02, TR-ACC-03 · A11Y-FRM-01, A11Y-FRM-02 (tel), A11Y-ERR-01/02, A11Y-FOC-08 | A02 `101:129199` | reviewed | Light `3:4` · Dark `3:8344` |
| K01b | Mobile number · no connection | flow step | onboarding | as K01, Alert Warning (Retry action) | offline / vendor timeout on OTP send | TR-STATE-02 · A11Y-LIV-02, A11Y-ERR-02, A11Y-COL-01 | A02 | reviewed | Light `3:5194` · Dark `3:8440` |
| K02 | Verify mobile | flow step | onboarding | Top Bar, OTP Input 4, Button Ghost sm (Edit number), Button lg | typing, resend countdown | TR-ACC-04 · A11Y-AUT-01, A11Y-LIV-02, A11Y-TGT-01 | A03 `101:129363` | reviewed | Light `3:5399` · Dark `3:8549` |
| K02b | Verify mobile · wrong code | flow step | onboarding | as K02, OTP Input Error | error (attempts left) | TR-ACC-04 · A11Y-ERR-01/02, A11Y-LIV-02 (assertive) | A03 | reviewed | Light `3:5597` · Dark `3:8648` |
| K02c | Verify mobile · locked | flow step | onboarding | as K02, Alert Danger | locked 30 min (unlock time shown) | A11Y-ERR-02, A11Y-LIV-02, A11Y-COL-01 | A03 | reviewed | Light `3:5721` · Dark `3:8746` |
| K02d | Welcome back | result | onboarding | Top Bar Progress=On, Timeline (5 stages: Done/Active/Pending), Button lg | in-progress application found after mobile OTP (resume) | TR-ACC-02 · A11Y-LIV-02, A11Y-COL-01, A11Y-LAY-01 | A08 (layout) | reviewed | Light `3:5985` · Dark `3:8854` |
| K03 | Email | flow step | onboarding | Top Bar, TextField md (email), Checkbox (own-email declaration), Google/Apple sign-in (gap), Button lg | default (filled) | TR-ACC-03 · A11Y-FRM-01, A11Y-FRM-02 (email), A11Y-ERR-01/02 | A04 `101:129529` | reviewed | Light `3:6174` · Dark `3:8979` |
| K04 | Verify email | flow step | onboarding | Top Bar, OTP Input 4, Button Ghost sm (Edit email), Button lg | typing, resend countdown | TR-ACC-04 · A11Y-AUT-01, A11Y-LIV-02 | A05 `101:129721` | reviewed | Light `3:6351` · Dark `3:9075` |
| K05 | Prefill consent | sheet state | onboarding | K06b underneath, Sheet Scrim, Bottom Sheet Footer=Two, Sheet Content/Prefill consent | consent unticked (CTA explains), decline route | D-01 · TR-ACC-03, TR-RISK (no pre-ticked consent) · A11Y-FOC-02, A11Y-FOC-04, A11Y-FRM-01 | A06 `101:129890` | reviewed | Light `3:7631` · Dark `3:9174` |
| K06 | Confirm PAN & DOB | flow step | onboarding | Top Bar, TextField md Filled ×2 (PAN, DOB + calendar icon), Button lg | prefilled (bureau hit) | TR-ACC-02, TR-ACC-03 · A11Y-FRM-01, A11Y-FRM-02 (bday), A11Y-FRM-04 | A07 `101:130150` | reviewed | Light `3:6540` · Dark `3:9339` |
| K06b | Enter PAN & DOB | flow step | onboarding | Top Bar, TextField md Outline ×2, Button lg | empty (bureau miss, timeout or declined; no error shown) | TR-ACC-03 · A11Y-FRM-01, A11Y-FRM-02 | A07 | reviewed | Light `3:6781` · Dark `3:9447` |
| K06c | Enter PAN & DOB · format error | flow step | onboarding | as K06b, TextField Error | error (PAN format, fix in words) | A11Y-ERR-01, A11Y-ERR-02, A11Y-COL-01 | A07 | reviewed | Light `3:7014` · Dark `3:9555` |
| K06d | Confirm PAN & DOB · details don't match | flow step | onboarding | as K06, Alert Danger, TextField Error (DOB) | error (NSDL name/DOB mismatch; correct and retry) | A11Y-ERR-01, A11Y-ERR-02, A11Y-LIV-02 (assertive), A11Y-COL-01 | A07 | reviewed | Light `3:7244` · Dark `3:9664` |
| K07 | Verifying PAN | result | onboarding | Top Bar Progress=On, Timeline (3 items) | loading (checks in progress, expected time) | TR-STATE-02 · A11Y-LIV-02, A11Y-LIV-01 | A08 `101:130338` | reviewed | Light `3:7937` · Dark `3:9785` |
| K07b | PAN can't be used | result | onboarding | Icon tile (Icon in a token frame), Button lg (Check again) | blocked (inoperative: not linked to Aadhaar; says how to fix) | TR-ACC · A11Y-ERR-02, A11Y-COL-01 | A09 `101:130536` (layout) | reviewed | Light `3:8111` · Dark `3:9886` |

## Open questions
| # | Question | Why it matters | Owner | Answer |
|---|---|---|---|---|
| Q1 | Family declaration on mobile and email: allow self, spouse, dependent child or parent, or self only? (PRD §10 open) | K01 and K03 show a "Whose number/email is this?" choice only if family is allowed. Plan: build K01 with the choice, "Mine" selected by default | Product | Self only (2026-10-19). K01/K03: one unticked declaration checkbox, no family choice |
| Q2 | Google/Apple sign-in on Email (S2.1): in this build? | Needs brand sign-in buttons the DS doesn't have (Lucide has no brand logos). Plan: email + OTP only; listed as a gap | Product + DS owner | Yes (2026-10-19). Blocked on the sign-in button gap |
| Q3 | Mobile already belongs to an active client, or an application is in progress (S1.2): what does the person see? | A login hand-off or "Welcome back, continue where you left off" state isn't specified. Plan: not built in this slice | Product | Resume (2026-10-19). K02d Welcome back: stages done so far, Continue |
| Q4 | PAN verification returns a name or DOB mismatch (S4.1): block, let them edit, or send to ops? | K06c covers format only; a mismatch needs its own copy and route | Product + compliance | Show the error and ask them to correct it (2026-10-19). K06d |
| Q5 | PAN blocked (S4.2): where does the help link go, and can the person come back after linking PAN and Aadhaar? | K07b needs a real destination and a "check again" route | Product | Not needed now (2026-10-19). K07b says how to fix, no help link |
| Q6 | Offline or vendor timeout on OTP send and PAN check: what does the person see? | `TR-STATE-02` needs an error state per data surface; no offline pattern in the DS yet. Plan: Alert Warning at the top of the Body with Retry, not built in this slice | Product | "Check your internet connection and try again in a moment" (2026-10-19). K01b shows the pattern |
| Q7 | Where does the Top Bar help (?) go on each step? (review) | Every step shows it; a dead button fails users who need help | Product | |
| Q8 | Mobile already belongs to an active client: what does the login hand-off look like? (review; Q3 covered in-progress applications only) | S1.2 path not designed | Product | |
| Q9 | Invalid PAN (not inoperative): copy and next step? (review) | S4.2 blocks both cases; K07b covers inoperative only | Product + compliance | |

## Gaps
| Need | Proposed handling | Status |
|---|---|---|
| Button loading state ("Sending…", "Verifying…") | Button has no `State=Loading`. Not drawn; annotate the loading behaviour. Propose adding it via `/new-component` (change to Button) | open |
| Date of birth picker | No date picker in the DS. TextField md with a trailing calendar icon + annotation "opens the native date picker" (`textfield.md`: dates use a picker). Propose a Date Field later | open |
| Google/Apple sign-in buttons | Product wants them (Q2). Lucide has no brand logos and Button has no brand variant: needs `/new-component` (Social sign-in button, with official Google/Apple marks). K03 built without them until then | open |
| OTP Input locked state (K02c) | OTP Input has no Disabled/Locked state: `Empty` still shows the first cell focused, which suggests typing works. Built with `Empty` + helper hidden + Alert Danger + disabled CTA. Propose `State=Disabled` via `/new-component` (change to OTP Input) | done (19 Oct: OTP Input `State=Disabled` + `Disabled message`, used on K02c) |
| `text/placeholder` in Dark (K06b) | Dark placeholder (`frost.200`) is brighter than `text/secondary` (`frost.400`) and close to `text/primary` (`frost.100`), so empty-field hints look like typed values. In Light it equals `text/secondary`. Token issue, not patched in the screen: DS owner to lower it (e.g. `frost.400`) | done (19 Oct: Dark = `frost/400`, 7.68:1) |
| Field and OTP Cell edges below 3:1 (review DR-01, S1) | TextField and OTP Cell use `glass/hairline`/`glass/edge` (1.12–1.23:1). DS owner switches to `border/strong` via `/new-component`; screens update after "Update all". Blocks handoff (S1 can't be waived by design) | done (19 Oct: `border/strong`, 3.81:1 Light / 3.34:1 Dark) |
| Top Bar `Stage` 2–5 text not linked (DS bug, found 19 Oct) | The new Stage 2–5 variants show "Step 1 of 5 · Contact / Verify mobile" whatever the Step/Title properties say. Screens keep `Stage=1` with nested Step overrides until the DS owner links the text in those variants | open |
| Result icon tile (64×64 circle + icon) | `screen-anatomy.md` §2 describes it as a token-bound frame + `Icon` instance, not a component. Build it that way; propose promoting it if it repeats | open |

## Decisions & waivers
| Date | Decision or waived finding | Why | Decided by |
|---|---|---|---|
| 2026-10-19 | *Retired 19 Oct (OTP Input now has State=Disabled):* K02c: OTP Input shown as Empty with helper hidden while locked | Alert + disabled CTA carry the message until OTP Input gets a Disabled state | Product designer |
| 2026-10-19 | *No longer needed 19 Oct (master now unticked):* K05: consent checkbox in `Sheet Content/Prefill consent` overridden to Unchecked | The library master is pre-ticked, which breaks the never-pre-ticked consent rule; reported to DS owner | Claude (flagged to designer) |
| 2026-10-19 | *No longer needed 19 Oct (layer removed from the DS):* K06c/K06d: TextField Error's stray "Message" layer ("Enter at least ₹100") hidden | DS bug: unbound layer in the Error variant; helper text carries the real error | Claude (flagged to designer) |
| 2026-10-19 | OTP Input left-aligned with the Body (K02, K02b, K02c, K04), not centred | Designer's choice: lines up with the heading and fields. Differs from `otp-input.md` ("Centre the cells under the screen title"); that doc needs a decision | Product designer |
| 2026-10-19 | "Edit" sits right after the destination ("Sent to +91 98765 •••10 Edit") on K02, K02b, K02c, K04, Light + Dark | Designer's choice: keeps the action next to what it changes | Product designer |
| 2026-10-19 | One term: "OTP" everywhere (headings, descriptions, alert); review DR-03 fixed | The DS helper text says OTP and can't be changed | Product designer |
| 2026-10-19 | K07b: "We've saved your progress…" + Ghost "I'll do this later"; review DR-04 fixed | A retry alone is a dead end when the fix takes days | Product designer |

## Log
- 2026-10-19: PRD extracted (S1–S4 slice), plan written. Figma file linked, DS library on. Next: approve the plan.
- 2026-10-19: answers to Q1–Q6 added; K01b, K02d, K06d added (15 frames). Next: approve the updated plan.
- 2026-10-19: page renamed to Screens, sections 1 · Contact and 2 · Identity added. K01 built (Light `3:4`); ds-audit: 0 screen S2s (TextField border = DS issue, Dark not built yet). Next: OK on K01.
- 2026-10-19: K01 approved. Section 1 · Contact built in Light: K01b, K02, K02b, K02c, K02d, K03, K04 (copies of K01/K02). New gap: OTP locked state. Next: OK on section 1.
- 2026-10-19: section 1 approved (K02c workaround kept). Section 2 · Identity built in Light: K05, K06, K06b, K06c, K06d, K07, K07b. Next: OK on section 2, then Dark.
- 2026-10-19: section 2 approved. Dark copies of all 15 screens made (Color Tokens → Dark, 80 px right of each Light frame) and screenshotted. Dark works through tokens; one token issue (text/placeholder Dark) logged as a gap. Next: OK on Dark, then annotations.
- 2026-10-19: Dark approved. Handoff annotations (Accessibility category) on all 15 Light frames: AN-01, 03, 05, 06, 08, 11, 15 everywhere; AN-09/10 on fields; AN-04/09/14 on OTP; AN-02/12 on the sheet; AN-07 on alerts, errors and Verifying. Checked with review-context.js (anIds per screen). Next: /ds-audit and /design-review (step 6).
- 2026-10-19: step 6. /ds-audit on page 0:1 (30 frames): S1 0 · S2 6 (all inside DS: field/OTP edges) · S3 17 → `audit.md`. /design-review final: Changes required, S1 1 (DR-01 field/OTP edges, DS) · S2 1 (DR-02 Dark placeholder, DS token) · S3 2 (DR-03 OTP vs code, DR-04 K07b way out) → `review.md`. Screens stay `annotated` until DR-01 is fixed in the DS. Next: designer decides on DR-03/DR-04 screen fixes; DS owner takes DR-01/DR-02.
- 2026-10-19: designer's file edits checked: OTP rows left-aligned on K02/K02b/K02c (L+D); K02c Light Edit moved next to the number (others unchanged, asked); K06/K06d touched but no visible change. Fixed DR-03 (OTP wording on K01–K04, Light+Dark, annotations updated) and DR-04 (K07b saved-progress line + I'll do this later), and left-aligned K04. Audit not re-run (text and one DS button only). Next: answer the K02c Edit question; DR-01/DR-02 wait on the DS.
- 2026-10-19: Edit moved next to the destination on all OTP screens (K02, K02b, K02c, K04, Light + Dark), matching the designer's K02c edit. Next: DR-01/DR-02 wait on the DS; then /share-changes when the designer wants to save.
- 2026-10-19: Figma file renamed "PRD Test" → "Laabh — KYC Onboarding" (designer's choice; same key, links unchanged). Next: share with /share-changes.
- 2026-10-19: review.md rewritten in the plain-language format (designer's request; template change in PR #6). Same findings: DR-01/DR-02 open (DS), DR-03/DR-04 fixed.
- 2026-10-19: DS fixes published (PR #7) and accepted in the file. K02c uses OTP `State=Disabled` ("Try again after 4:52 pm"), Light + Dark; declaration checkboxes wrap with the full SEBI copy; Top Bar `Stage` tried, but Stage 2–5 variants don't show Step/Title text (DS bug), so screens stay on Stage 1 + nested overrides. /ds-audit: S1 0 · S2 0 · S3 17 (annotated / inside DS). /design-review re-check: ✅ Ready for handoff, DR-01–DR-04 fixed. Screens → reviewed. Next: product answers Q7–Q9; DS owner fixes the Top Bar text bug.
