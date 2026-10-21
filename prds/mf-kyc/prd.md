# Laabh KYC & Account Opening PRD: Phased Launch of MF-Only and Full Accounts

> Source: PDF export from Google Docs, "Laabh KYC & Account Opening PRD" (Oct 12, 2026, @Roshan), received 19 Oct 2026.
> Text extracted as given (20 pages). Tables lost their grid in extraction: each table's header row appears at the END of its cells.

```text
=== PAGE 1 ===
Laabh KYC & Account Opening PRD: Phased Launch of MF-Only and Full
Accounts
Laabh KYC & Account Opening PRD
Oct 12, 2026 · @Roshan
1. Overview
Laabh launches with MF-only accounts (direct plans) through the acquired stock broker's BSE
StAR MF 2.0 membership, then adds demat and all trading segments once equity and
derivatives operations go live. KYC is built as one engine with configurable journeys, so Phase 2
adds steps rather than a second flow.
Phasing
Goals
Phase 1: KRA-validated users submit KYC in under 5 minutes, new-to-KRA users in under 10.
Time to first order is tracked separately, since it also depends on StAR MF UCC activation,
KRA validation for new-to-KRA users and SIP mandate registration.
Phase 1
StAR MF 2.0
access under
the acquired
broker's member
code
A: MF-only
(direct plans)
KRA-validated
client + StAR MF
UCC (SOA
mode), MF
lumpsum and
SIP
Phase 2
Equity and
derivatives
operations live
under the
acquired entity
B: Full account
(open market);
C: MF-only to
full upgrade; A
only for B2B
partner channels
Trading account
(EQ, F&O, CDS,
MCX as
approved) +
demat
(CDSL/NSDL) +
exchange UCCs;
MF continues on
StAR MF
Phase
Trigger
Journeys live
Account
outcome

=== PAGE 2 ===
Phase 2: full-account KYC in under 10 minutes for non-derivatives users; MF-only users
upgrade by completing only the missing steps (target under 4 minutes).
Capture data once: nothing collected in Phase 1 is asked again during upgrade unless
regulation forces a refresh.
Non-goals (this PRD)
Non-individuals (HUF, corporate, trust, partnership), NRI, minors, joint holding, joint bank
accounts.
Regular plans: direct plans only in v1; regular via the entity's ARN can be enabled later.
Offline/assisted KYC, physical forms, branch IPV.
Re-KYC/periodic KYC update and account modification journeys (separate PRD), except
where the upgrade reuses them.
MF order placement, SIP mandate (eNACH/UPI autopay) registration and MF holdings
dematerialisation (separate PRDs; KYC hands off to them).
Success metrics
Signup-to-submitted
conversion
TBD (baseline after 2
weeks)
TBD
Median time to submit
KRA validated under 5
min; new-to-KRA
under 10 min
Under 10 min (no
derivatives)
Submitted-to-active
KRA validated: 95%
within T+1 (UCC +
FATCA); new-to-KRA:
within CVL validation
SLA (TBD)
95% within T+2
Time to first order
Tracked (includes
UCC, KRA and
mandate)
Tracked
Ops-touch rate
(manual review)
Under 10%
Under 15%
Metric
Phase 1 target
Phase 2 target

=== PAGE 3 ===
2. Regulatory and operating model
Laabh operates as a stock broker in both phases through the acquired entity. MF runs on that
entity's BSE StAR MF 2.0 membership, direct plans only, and every MF order routes via StAR MF
in both phases. Items marked verify must be confirmed with compliance, BSE and the KRA
before build sign-off.
Registrations used
MF-only to full upgrade
rate
n/a
TBD, tracked per
cohort at 30/60/90
days
Broker status
Acquired entity, SEBI-
registered stock broker
Same entity; equity
and derivatives go live
MF distribution
Stock broker on StAR
MF 2.0, direct plans
only; ARN kept for
regular plans later
Same; no change to
folios or UCCs at
upgrade
MF platform
BSE StAR MF 2.0
under the entity's
member code
Same membership; all
MF orders via StAR MF
KRA
Entity's KRA
intermediary code:
fetch, and
fresh/modified KYC
push to CVL KRA for
non-KRA users
Same
Depository
n/a
Entity's DP ID (CDSL
and/or NSDL)
Exchanges
StAR MF only
NSE/BSE/MCX
memberships,
CTCL/UCC upload
Item
Phase 1
Phase 2

=== PAGE 4 ===
Rules the journeys must honour
KRA status, not presence. Validated proceeds; Registered (non-Aadhaar OVD) needs
modification via Aadhaar/DigiLocker before new folios; On Hold/Rejected/Under Process
blocks and routes to fresh KYC or wait (verify current KRA rules).
No transactions before KRA Validated. New-to-KRA users have their KYC pushed to CVL
KRA and cannot place MF orders until the status turns Validated.
PAN-Aadhaar linkage. Inoperative PAN blocks onboarding; checked during NSDL/Protean
PAN verification.
Nomination. Each holder opts in (nominees) or opts out, authenticated by OTP 2FA; follow the
current SEBI multi-nominee framework for MF and demat (up to 10 nominees, share %; verify
StAR MF 2.0 field support).
FATCA/CRS. Tax residency, place/country of birth, PEP, occupation and income slab are
mandatory for StAR MF FATCA upload and for the KRA record.
Direct plans. No distributor commission; the AOF's ARN commission clause is replaced by a
direct-plan declaration (verify StAR MF 2.0 AOF wording for execution-only clients).
AOF. Assume StAR MF 2.0 needs an Aadhaar-eSigned AOF for every new client; a 2FA-only
digital AOF for KRA-validated users stays open with BSE.
Phase 2 broking. Account opening kit (rights and obligations, RDD, guidance note, tariff),
segment activation with income proof for derivatives, IPV via Aadhaar eKYC/video or
liveness, DDPI optional, bank via reverse penny drop, demat BSDA eligibility check.
Consent and data. Explicit consent for credit bureau prefill, DigiLocker, Aadhaar eKYC/eSign
and Account Aggregator, logged with timestamp, IP/device and purpose; Aadhaar number
stored masked/vaulted only.
3. Scope
v1 covers resident individual, single-holder accounts on mobile app and web, in both phases. In
Phase 2, open-market users get the full account only; MF-only accounts continue solely for B2B
partner channels (e.g., a consumer app offering MF to its customers).
eSign / Aadhaar
ASP/ESP agreement in
the acquired entity's
name (Laabh-owned)
Same
Dimension
In scope
Out of scope (later)

=== PAGE 5 ===
Step matrix by journey
Holder type
Resident individual,
18+, single holder
NRI (NRE/NRO), minor,
joint, HUF, non-
individual
Channel
Phase 1: open market,
MF-only. Phase 2:
open market full
account; MF-only only
via B2B partners
MF-only for open-
market users in Phase
2
Identity path
KRA fetch; DigiLocker
(Aadhaar + PAN);
NSDL/Protean PAN
verification
Offline OVD upload;
CKYC fallback (open
question)
Platforms
Android, iOS, web
Assisted onboarding
Languages
Same as app launch
set
—
Bank
1 primary individual
bank account in KYC;
up to 5 mandates later
in profile
Joint bank accounts;
multiple banks at
onboarding
Nominee
Opt in (multi-nominee)
or opt out, by OTP
Nominee changes
post-activation
(modification PRD)
Mobile OTP (4-
digit)
Yes
Yes
Already done
Email OTP (4-
digit)
Yes
Yes
Already done
Step
A: MF-only
B: Full account
C: Upgrade (MF
to full)

=== PAGE 6 ===
Credit bureau
prefill
Yes
Yes
Not needed
PAN + DOB, PAN
verification
Yes
Yes
Re-check PAN
status only
KRA fetch +
status branch
Yes
Yes
Re-fetch status
DigiLocker (full
or docs only)
Yes
Yes
Re-fetch if older
than 12 months
Personal, FATCA,
PEP, occupation,
income
Yes
Yes
Prefilled; confirm
Nominees (opt
in/out by OTP)
Yes (MF)
Yes (MF +
demat)
Extend to demat
or confirm
Reverse penny
drop (penny
drop backup)
Yes
Yes
Reuse if same
bank
Segment
selection
No
Yes
Yes
Income proof
No
If derivatives
If derivatives
Selfie/liveness +
face match
No
Yes
Yes
Signature
capture
No (unless BSE
needs it on the
AOF)
Yes
Yes
DDPI (optional)
No
Optional
Optional
eSign
Yes (assumed;
2FA-only path
pending BSE)
Yes (broking +
demat + KRA if
needed)
Yes (broking +
demat)

=== PAGE 7 ===
4. Shared KYC engine
Steps S1 to S7 are identical for Journeys A and B; the journey config ( MF_ONLY or FULL ) only
changes which steps follow penny drop. Each step is a resumable checkpoint with its own state,
vendor call log and retry policy.
[embedded content: KYC engine · shared steps, KRA branch, journeys A, B and C\]
Everything above penny drop is shared; Journey C moves an mf_active client to 
full_active with only the steps Journey A skipped.
Journey config
journey_type : MF\_ONLY | FULL | UPGRADE, set at signup by a server flag (Phase 1
forces MF\_ONLY; Phase 2 forces FULL for open-market users; MF\_ONLY only when the
signup carries a B2B partner ID).
Step list, mandatory flags and copy are config-driven so Phase 2 ships without app release
for ordering changes.
Every step writes to one KYC application record; the upgrade journey opens a new application
linked to the existing client.
S1. Mobile verification
1. User enters mobile; OTP sent (4 digits, 30 s resend, 3 resends, 3 wrong attempts, then 30 min
lock; tighter attempt limit offsets the shorter code).
2. Check mobile against existing clients: active client goes to login; in-progress application
resumes from last checkpoint.
3. Capture device ID, app version, referral/UTM.
4. Declaration: mobile belongs to self or family (SEBI family declaration: self, spouse, dependent
child/parent).
S2. Email verification
1. Email OTP or Google/Apple sign-in (verified email from the provider counts).
2. Dedupe against existing clients; same family declaration as mobile.
KRA push to
CVL
If not found /
Registered /
fixable Hold
Same
Only if status
changed
End status
mf\_submitted
submitted
upgrade\_submit
ted

=== PAGE 8 ===
S3. Credit bureau prefill
1. Consent screen (purpose: prefill identity details only), then bureau lookup on mobile (+ name
if needed).
2. On hit: prefill PAN, name, DOB, address; user confirms PAN and DOB.
3. On miss/timeout (target under 3 s): user types PAN and DOB; no error shown.
S4. PAN verification and KRA prep
1. PAN format check, then NSDL/Protean PAN verification: name, DOB match, PAN status,
Aadhaar-seeding status.
2. Inoperative or invalid PAN: block with reason and help link; record drop reason.
3. Prepopulate PAN, DOB (and masked Aadhaar where available) for the KRA query.
S5. KRA fetch and status branch
K1: fetch KRA data (name, address, father/spouse name, gender, marital status), run name
match (PAN name vs KRA name vs bank later), then pull PAN and Aadhaar from DigiLocker for
the document file only. If DigiLocker is declined, allow PAN image upload + continue (verify
acceptable).
K2: full DigiLocker consent; fetch Aadhaar XML (name, DOB, gender, address, photo) and
PAN; compare DigiLocker PAN with entered PAN; NSDL name verification on the Aadhaar
Validated
Path K1: NSDL name match, then
DigiLocker documents-only fetch
Registered (non-Aadhaar OVD)
Path K2: full DigiLocker journey,
KRA modification upload
Not found
Path K2: full DigiLocker journey,
fresh KYC push to CVL KRA
On Hold / Rejected
Path K2 if hold reason is fixable by
Aadhaar (address/mobile/email
validation); otherwise ops queue
with user message
Under Process (another
intermediary)
Wait state; poll daily up to 7 days,
notify user, then K2
KRA result
Route

=== PAGE 9 ===
name. Address from Aadhaar becomes the KYC address; option to add a different
correspondence address with proof.
Name-match thresholds (fuzzy score) and manual-review band are config values; mismatch
beyond threshold goes to ops review, not rejection.
S6. Personal information and nominees
1. Prefilled and editable as allowed: father/spouse name, mother name, gender, marital status
(from KRA/Aadhaar where present).
2. Mandatory capture: occupation, annual income slab, net worth (optional), PEP/related-to-PEP,
country of tax residence (India only in v1; foreign tax residence routes to ops), place of birth,
country of birth, nationality.
3. Nominees: opt in with 1 to 10 nominees (name, relationship, DOB, share %, ID type/number,
address same-as-holder toggle, guardian if minor) or opt out with explicit declaration. Share
% must total 100.
4. Authenticate nomination opt-in or opt-out by OTP (2FA); where the journey has eSign, the
eSigned AOF also carries it.
S7. Bank verification (penny drop)
1. Primary: reverse penny drop. User pays ₹1 via UPI from the account to be linked; the bank
returns account number, IFSC and holder name; ₹1 refunded.
2. Backup: penny drop, offered when UPI fails or times out, the user has no UPI on that account,
or chooses to enter account number + IFSC.
3. Name match bank holder name vs PAN/KYC name; threshold failure goes to ops review.
4. Individual accounts only: user declares the account is held singly; reject where the bank
response shows a joint holder.
5. Store bank name, branch, IFSC, MICR, account type (savings/current); show last 4 digits in
UI.
5. Journey A: MF-only account (Phase 1)
After S1 to S7, Journey A ends with an authentication step and back-office registration on KRA
and BSE StAR MF 2.0; the user is MF-active once the UCC and FATCA are accepted.
A8. Review and declarations
1. Summary screen of all captured data, editable sections link back to their step.
2. Accept: KYC declaration, direct-plan declaration (replaces the ARN commission clause on the
StAR MF AOF), FATCA/CRS self-certification, nomination declaration, T&C and privacy policy,
consent for KRA upload where applicable.

=== PAGE 10 ===
A9. Authentication (eSign decision)
eSign failure (OTP fail, Aadhaar not linked to mobile): 3 retries, then offer later resume; no
alternative offline path in v1.
A10. Submission and back office
1. Status mf_submitted ; user lands on home in an "account being set up" state and can
browse funds, build a cart or plan a SIP.
2. KRA (K2 cases): push fresh or modified KYC with documents (Aadhaar XML/masked Aadhaar,
PAN, photo) to CVL KRA; store the ack number; poll status daily.
3. BSE StAR MF 2.0: register the UCC (individual, single holding, SOA mode, bank, nominees,
contact), upload FATCA, upload the eSigned AOF, track until activated.
4. Ops checks only for flagged cases: name mismatch band, PEP = yes, foreign tax residence,
KRA hold.
A11. Activation
mf_active only when the StAR MF UCC is active, FATCA is accepted and KRA status is
Validated. New-to-KRA users cannot transact until CVL validates; the app shows KRA status
and expected time.
Lumpsum orders open on activation. SIPs also need a mandate (eNACH/UPI autopay)
registered on StAR MF, covered in the MF transaction PRD; onboarding hands off to mandate
setup, which may start once the UCC exists, in parallel with KRA validation (verify).
Notify via push, SMS, email at each milestone: UCC active, KRA validated, mandate approved.
Rejections (UCC/FATCA/AOF/KRA) map to a reason code and a user fix step, e.g., re-do
reverse penny drop or re-eSign.
Data kept for the Phase 2 upgrade
KRA Validated (default assumption)
Aadhaar eSign on the StAR MF
AOF; nomination opt-in/out by OTP
KRA Validated, only if BSE confirms
a 2FA digital AOF is accepted
OTP 2FA only, no eSign (open
question)
KRA Not found / Registered / fixable
Hold
One Aadhaar eSign session on KYC
form + AOF ("MF eSign")
Case
Action

=== PAGE 11 ===
All S1 to S7 data, consents, DigiLocker artefacts with fetch timestamp, bank verification result,
nominee set, FATCA answers.
Do not collect in Phase 1: segment choice, income proof, selfie/liveness, signature (unless
AOF needs it), DDPI. Each is a step in Journey C.
6. Journey B: Full account, demat + all segments (Phase 2)
Journey B runs S1 to S7, then adds segment selection, income proof for derivatives, liveness,
signature, optional DDPI and a single eSign covering KRA, trading, demat and MF documents. It
ends at submitted and goes live per segment.
B8. Segment selection
1. Cash equity (NSE/BSE) and MF on by default; F&O, currency derivatives, commodity (MCX)
as opt-ins; SLB/MTF out of scope for onboarding (activated later).
2. Show risk disclosure on derivatives (SEBI RDD) before opt-in; capture trading experience
(years) and investment experience.
3. User can skip derivatives and add later from profile (reuses B9).
B9. Income proof (only if derivatives selected)
1. Primary: Account Aggregator bank statement, last 6 months.
2. Fallbacks: ITR acknowledgement, Form 16, salary slip, net worth certificate, demat holding
statement upload (CDSL/NSDL CAS or DP holding statement, holdings above threshold), bank
statement PDF upload (password-protected supported).
3. Auto-validate where possible (AA: average balance/credits vs threshold); otherwise ops
review. Derivatives segment stays pending until approved; cash segment proceeds.
B10. Selfie, liveness and face match
1. Passive liveness selfie; face match against Aadhaar/DigiLocker photo (K2) or KRA photo/PAN
where available (K1).
2. Capture geolocation (must be within India) and timestamp as IPV evidence.
3. Fail: 3 retries with guidance, then ops review or video IPV fallback (verify if v1 needs video).
B11. Signature
1. Draw on screen (default) or upload photo of signature on white paper.
2. Quality checks: not blank, not a single stroke, contrast; crop and store.
B12. DDPI (optional)
1. Offer DDPI for sell authorisation, pledge for margin, MF via exchange; explain that without
DDPI each sell needs TPIN/eDIS.

=== PAGE 12 ===
2. If accepted: include DDPI in eSign pack; stamp duty as applicable.
B13. Review, declarations and eSign
1. Summary + account opening kit: rights and obligations, RDD, guidance note, policies and
procedures, tariff sheet, BSDA eligibility choice, running account settlement preference
(quarterly/monthly), contract note mode (electronic), DIS/eDIS preference.
2. One Aadhaar eSign session covering: KRA form (if needed), trading AOF, demat AOF, StAR
MF AOF, DDPI, nomination.
3. Status submitted .
B14. Back office and activation
Each segment flips independently; home screen shows per-segment status.
Welcome kit email: client ID, BO ID, UCC, tariff, PoA/DDPI copy, eSigned AOF PDF.
7. Journey C: MF-only to full account upgrade (Phase 2)
MF-only users upgrade through both a user-initiated path (pull) and a Laabh-initiated campaign
(push); both land in the same delta journey that asks only for what Journey A did not collect. MF
folios, SIPs and the StAR MF UCC are untouched; units stay in SOA mode.
Entry points
KRA upload/modify
Ack, then Validated
Prerequisite for all
CDSL/NSDL BO
account
BO ID / DP client ID
Holdings, sells via
DDPI/eDIS
NSE/BSE UCC (cash)
UCC + PAN verified on
exchange
Equity trading
NSE/BSE/MCX UCC
(derivatives)
Segment active after
income proof approval
F&O, CDS, commodity
BSE StAR MF 2.0 UCC
+ FATCA
UCC active
MF orders
Registration
Output
Activates
Pull
User taps a stock, ETF,
IPO, F&O screen or
Gate sheet: "Add
stocks and demat in
Type
Trigger
Surface

=== PAGE 13 ===
C1. Eligibility check (system)
1. Account mf_active , no open modification, PAN still operative, KRA status Validated.
2. If KRA no longer Validated, insert the S5 K2 path before C3.
C2. Confirm existing details
1. One screen with prefilled personal, address, FATCA, occupation, income; user confirms or
edits (edit triggers the relevant re-verification).
2. Bank: reuse verified bank (no new penny drop) unless user changes it.
3. Nominee: show MF nominees; choose "use same for demat", edit, or opt out for demat;
authenticate.
C3. Freshness re-checks (system)
"Open demat" in profile
about 3 minutes" with
steps left
Pull
Search result for a
stock/ETF
Inline CTA on the
quote page
Push
Phase 2 go-live
In-app banner + push
+ email to all 
mf_active users,
staggered by cohort
Push
Behavioural
After nth SIP, on
NFO/IPO opening, on
CAS import showing
direct equity elsewhere
Push
Reminder
Drop-off at any
upgrade step: day 1, 3,
7 nudges, then monthly
Aadhaar XML / DigiLocker docs
Reuse if fetched within 12 months;
else re-fetch via DigiLocker
PAN verification
Always re-run (cheap, instant)
Artefact
Reuse rule (config, verify with
compliance)

=== PAGE 14 ===
C4 to C8. Delta steps
Same as Journey B steps B8 (segments), B9 (income proof if derivatives), B10 (liveness), B11
(signature), B12 (DDPI), then B13 eSign on the broking + demat kit only (no MF AOF re-sign).
Status upgrade_submitted .
C9. Back office and cut-over
1. Create BO account and exchange UCCs; the StAR MF UCC is unchanged.
2. MF orders keep routing via BSE StAR MF; folios, SIPs and mandates are untouched.
3. Optional later: offer moving MF units to demat; not part of upgrade.
4. On activation: unified holdings view (MF SOA + demat), status full_active ; segments flip
independently as in B14.
Upgrade UX rules
Show a progress meter with only remaining steps (e.g., 4 of 4 left) and estimated time.
Never re-ask a confirmed field; prefill everything.
Save at every step; resume from the gate sheet or profile.
8. Status model, data and rejections
Status lives at two levels: the application (where the user is in a journey) and the
account/segment (what the user can transact). Pulse, nudges and the app home all read these
states.
Application states
Penny drop
Reuse if same account and verified
within 12 months
Consents
Fresh consent for new purposes
(broking, demat, AA)
started
Mobile verified
in_progress:<step>
Last completed checkpoint, used
for resume
kra_wait
KRA under process with another
intermediary
State
Meaning

=== PAGE 15 ===
Account and segment states
Rejection handling
Every external rejection maps to a reason code, user copy, and a single fix step that reopens
only that checkpoint (e.g., SIGNATURE_UNCLEAR → B11, BANK_NAME_MISMATCH → S7, 
FATCA_INCOMPLETE → S6).
After the fix, only the affected registration is resubmitted.
Ops can override with maker-checker and a mandatory note.
ops_review
Flagged (name mismatch, PEP,
foreign tax, face match, income
proof)
mf_submitted / submitted / 
upgrade_submitted
eSign/2FA done, back office
running
rejected:<reason>
Back office or ops rejection with a
fix step
abandoned
No activity for 90 days; data
retained per policy
Account
mf_active → 
upgrade_in_progress → 
full_active ; full_active
directly for Journey B
KRA
not\_found, under\_process,
validated, registered, on\_hold,
rejected
MF (StAR MF UCC)
pending, active, rejected
Demat (BO)
pending, active, rejected
Equity / F&O / CDS / MCX
not\_requested, pending,
pending\_income\_proof, active,
rejected
Level
States

=== PAGE 16 ===
Data model (core entities)
client : PAN, name, DOB, gender, contact, addresses, KRA status, FATCA block.
kyc_application : journey\_type, state, checkpoint log, consents, vendor call refs.
document : type, source (KRA, DigiLocker, upload, generated), fetched\_at, storage ref, hash.
bank_account , nominee (per holding type: MF, demat), segment_request , 
registration (KRA, StAR MF, BO, exchange UCC with ack IDs).
Retention per SEBI/PMLA (minimum 8 years after account closure; verify); Aadhaar masked
and vaulted.
9. Vendors, ops, notifications and analytics
Vendors are placeholders until contracts close; each capability sits behind an adapter so
primary and fallback can be swapped by config.
Vendor map (to be filled)
SMS/email OTP
S1, S2
TBD
TBD
Credit bureau
prefill
S3
TBD
—
PAN verification
S4, S5
NSDL/Protean
TBD
KRA
fetch/upload
S5, A10, B14
CVL KRA (TBD)
TBD
DigiLocker /
Aadhaar fetch
S5
Digio (TBD)
TBD
Reverse penny
drop (primary) /
penny drop
(backup)
S7
TBD
TBD
Account
Aggregator
B9
TBD
—
Liveness / face
match
B10
HyperVerge
(TBD)
TBD
Capability
Steps
Primary
Fallback

=== PAGE 17 ===
Per vendor: SLA, timeout, retries, cost per call, and fallback trigger to be added in the integration
spec.
Pulse (ops) requirements
Queue by reason (name mismatch, PEP, face match, income proof, KRA hold, back-office
rejection) with SLA timers.
Application view: all steps, documents, vendor responses, consents, timeline; maker-checker
approve/reject/send-back to step.
Search by mobile, PAN, application ID, client ID; audit log of every ops action.
Bulk view of upgrade cohorts and their step drop-off.
Notifications
OCR / document
checks
B9, B11
AiNXT (TBD)
TBD
Aadhaar eSign
A9, B13
TBD
TBD
BSE StAR MF
2.0 APIs
A10
BSE
—
Depository /
exchange UCC
B14
Broker back
office (TBD)
—
Drop-off at a step
Push + SMS/WhatsApp at 1 h, day 1,
day 3
Submitted
Push + email with what happens
next
Activated (MF / each segment)
Push + SMS + email (welcome kit
for full account)
Rejected with fix step
Push + email with deep link to the
step
Upgrade campaign
In-app banner + push + email,
cohort-staggered
Event
Channel

=== PAGE 18 ===
Analytics
Event per step: viewed, started, completed, failed (reason), time spent; vendor latency and
failure by vendor.
Funnels: Journey A, B and C separately, split by KRA path (K1/K2), platform and acquisition
source.
Key KPIs: step conversion, median time to submit, submit-to-active time, ops-touch rate,
rejection rate by reason, upgrade rate by cohort and entry point.
10. Open questions, dependencies and release plan
The Phase 1 build can start on S1 to S7 now; A9 assumes eSign for every MF user until BSE
confirms otherwise. Decisions taken on 13 Oct 2026 are logged below the open questions.
Open questions
Decisions log
BSE StAR MF 2.0: is a 2FA-authenticated digital AOF accepted for KRA-validated clients, or is eSign mandatory? Current
assumption: eSign mandatory.
StAR MF 2.0 support for multi-nominee fields (up to 10, share %).
Can SIP mandate registration start once the UCC exists, while KRA validation is pending?
CKYC fetch as a fallback when KRA is not found.
Mobile/email family declaration (self, spouse, dependent child/parent): allow, or self only?
B2B partner MF-only: partner ID handling, co-branded flow, and whether partner users can later upgrade.
CVL KRA validation SLA for new-to-KRA users, to set user expectations.
Timing for enabling regular plans via ARN, and the AOF/disclosure changes that brings.
Plan type
Direct plans only; regular via ARN
possible later
Broker status
Laabh is a stock broker in both
phases via the acquired entity
MF routing
Always via BSE StAR MF, before
and after upgrade
KRA for new users
Push to CVL KRA; no MF
transactions until Validated
eSign/eKYC agreements
In the acquired entity's name
(Laabh-owned)
Topic
Decision

=== PAGE 19 ===
Dependencies
Nomination
Opt-in and opt-out authenticated by
OTP
OTP length
4 digits, 3 wrong attempts before
lock
Bank verification
Reverse penny drop primary, penny
drop backup; individual accounts
only
Upgrade data reuse
DigiLocker/Aadhaar data reused if
fetched within 12 months
Phase 2 MF-only
Not for open market; only B2B
partner channels
StAR MF 2.0 API
access under broker
member code
A10, A11
Broker ops / BSE
KRA intermediary
access (fetch +
upload)
S5, A10
Compliance
Vendor contracts
(bureau, DigiLocker,
penny drop, eSign,
liveness, OCR, AA)
All steps
Product + procurement
Equity and derivatives
operations live under
the acquired entity
Journeys B, C
Management / legal
DP and exchange
back-office integration
B14, C9
Tech
Pulse ops console
Ops review, rejections
Product
Dependency
Needed for
Owner

=== PAGE 20 ===
Risks
AOF/eSign rules force eSign for every MF user: adds about 1 minute and an Aadhaar-mobile
dependency; mitigation is a clear eSign explainer and resume.
DigiLocker drop-off on the K2 path: mitigation via CKYC fallback and strong prefill.
Upgrade fatigue: mitigation via contextual pull gates rather than repeated blanket push.
Release plan
R1 (Phase 1)
Shared engine S1 to S7, Journey A,
StAR MF UCC + FATCA, KRA
upload, Pulse review queue,
analytics
R2 (Phase 2 launch)
Journey B with cash + MF;
segments, liveness, signature,
DDPI, broking/demat eSign; BO +
exchange UCC
R3 (Phase 2)
Journey C pull gates + push
campaign; derivatives with income
proof (AA + uploads)
R4
Video IPV fallback, CKYC fallback,
multi-bank, NRI/joint (separate
PRDs as needed)
Release
Contents

```
