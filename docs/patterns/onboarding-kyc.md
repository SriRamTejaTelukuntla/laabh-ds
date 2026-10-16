# Onboarding & KYC flow

Reference: the 23 onboarding screens on Selected Screens (`101:129024` Light, `101:140793` Dark). These are reference only, not canonical.
KYC uses 5 stages in the Top Bar: **Contact · Identity · Profile · Bank · Review**.

| Section | Screens (reference IDs) | Patterns |
|---|---|---|
| 0 · Welcome | A01 Welcome | Brand hero, value props, CTA "Get started", secondary "I have an account" |
| 1 · Contact | A02 Mobile number · A03 Verify mobile · A04 Email · A05 Verify email | Hero TextField (+91 prefix) → OTP Input (4) with resend timer |
| 2 · Identity | A06 Prefill consent · A07 Confirm PAN · A08 Verifying · A09 KYC found · A10 DigiLocker | Consent sheet (`Sheet Content/Prefill consent`), PAN field, loading state, result card, DigiLocker hand-off |
| 3 · Profile & nominees | A11 Personal details · A12 Tax & income · A13 Nominee choice · A14 Add nominee · A15 Nominees · A16 Nominee OTP | Prefilled fields, Segmented Controls, Option Cards, list of nominees, OTP in a sheet (`Sheet Content/Nominee OTP`) |
| 4 · Bank | A17 Link bank · A18 Bank linked | Bank search/IFSC, penny-drop verification (₹1), success state |
| 5 · Review & eSign | A19 Review (long scroll) · A20 eSign · A21 Submitted | Summary cards per section with Edit ghost buttons, Aadhaar eSign hand-off, result screen |
| 6 · Activation | A22 Home · setting up · A23 Home · active | Home with a progress Timeline, then the active home |

## Rules
- One question per screen. Title as a question or a short instruction; description says why.
- Every step screen: Top Bar with the stage and "Step n of N", footer CTA `lg`.
- Waiting states (Verifying, setting up) show what's happening and the expected time; use Timeline for multi-step waits.
- Regulatory consents are Checkboxes, never pre-ticked, with the summary in the label and detail in a sheet.
- Failures always offer the next step (retry, alternative method, contact support).
