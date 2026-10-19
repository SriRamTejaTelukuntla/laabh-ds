# Laabh KYC & Account Opening PRD (extract)

> **Source:** "Laabh KYC & Account Opening PRD: Phased Launch of MF-Only and Full Accounts", Oct 12, 2026, @Roshan (20-page PDF, not committed).
> **In scope for this build:** the start of the shared KYC engine, steps S1 to S4, plus the rules and decisions they depend on.
> Text below is the PDF's wording for those parts, cleaned of PDF line breaks. The rest of the PRD (S5 KRA fetch onward, Journeys A/B/C, status model, ops, vendors) is out of scope for now.

## 1. Overview (summary)
Laabh launches with MF-only accounts (direct plans) through the acquired stock broker's BSE StAR MF 2.0 membership, then adds demat and all trading segments once equity and derivatives operations go live.
KYC is built as one engine with configurable journeys, so Phase 2 adds steps rather than a second flow.

**Goals.** Phase 1: KRA-validated users submit KYC in under 5 minutes, new-to-KRA users in under 10.
Capture data once: nothing collected in Phase 1 is asked again during upgrade unless regulation forces a refresh.

**Non-goals.** Non-individuals, NRI, minors, joint holding; regular plans; offline/assisted KYC; re-KYC; MF order placement and SIP mandates.

## 2. Rules the journeys must honour (relevant to S1–S4)
- **PAN-Aadhaar linkage.** Inoperative PAN blocks onboarding; checked during NSDL/Protean PAN verification.
- **Consent and data.** Explicit consent for credit bureau prefill, DigiLocker, Aadhaar eKYC/eSign and Account Aggregator, logged with timestamp, IP/device and purpose; Aadhaar number stored masked/vaulted only.

## 3. Scope (relevant rows)
| Dimension | In scope | Out of scope (later) |
|---|---|---|
| Holder type | Resident individual, 18+, single holder | NRI, minor, joint, HUF, non-individual |
| Identity path | KRA fetch; DigiLocker (Aadhaar + PAN); NSDL/Protean PAN verification | Offline OVD upload; CKYC fallback (open question) |
| Platforms | Android, iOS, web | Assisted onboarding |

Step matrix (rows in scope): Mobile OTP (4-digit), Email OTP (4-digit), Credit bureau prefill, PAN + DOB / PAN verification: Yes for Journey A (MF-only) and B (full).

## 4. Shared KYC engine
Steps S1 to S7 are identical for Journeys A and B. Each step is a resumable checkpoint with its own state, vendor call log and retry policy.
Step list, mandatory flags and copy are config-driven.

### S1. Mobile verification
1. User enters mobile; OTP sent (4 digits, 30 s resend, 3 resends, 3 wrong attempts, then 30 min lock; tighter attempt limit offsets the shorter code).
2. Check mobile against existing clients: active client goes to login; in-progress application resumes from last checkpoint.
3. Capture device ID, app version, referral/UTM.
4. Declaration: mobile belongs to self or family (SEBI family declaration: self, spouse, dependent child/parent).

### S2. Email verification
1. Email OTP or Google/Apple sign-in (verified email from the provider counts).
2. Dedupe against existing clients; same family declaration as mobile.

### S3. Credit bureau prefill
1. Consent screen (purpose: prefill identity details only), then bureau lookup on mobile (+ name if needed).
2. On hit: prefill PAN, name, DOB, address; user confirms PAN and DOB.
3. On miss/timeout (target under 3 s): user types PAN and DOB; no error shown.

### S4. PAN verification and KRA prep
1. PAN format check, then NSDL/Protean PAN verification: name, DOB match, PAN status, Aadhaar-seeding status.
2. Inoperative or invalid PAN: block with reason and help link; record drop reason.
3. Prepopulate PAN, DOB (and masked Aadhaar where available) for the KRA query.

## 8. Status (relevant)
Application states: `started` (mobile verified), `in_progress:<step>` (last completed checkpoint, used for resume).

## 9. Notifications and analytics (relevant)
- Drop-off at a step: push + SMS/WhatsApp at 1 h, day 1, day 3.
- Event per step: viewed, started, completed, failed (reason), time spent.

## 10. Open questions and decisions (relevant)
- Open: mobile/email family declaration (self, spouse, dependent child/parent): allow, or self only?
- Decided 13 Oct 2026: OTP length 4 digits, 3 wrong attempts before lock.
