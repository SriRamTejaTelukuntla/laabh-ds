# MF KYC: session handoff

> **Updated:** 2026-10-21 · **Branch:** merged to `main` (PR #12; DS docs in PR #11) · **Owner:** Prasad
> Start a new session with: *"Continue the MF KYC screens from `prds/mf-kyc/handoff.md`."* Then run `/get-latest` checks and read `prds/mf-kyc/plan.md`.

## Files and links
| What | Where |
|---|---|
| Feature Figma file | [Laabh — MF KYC](https://www.figma.com/design/kwRnjJU3KdW28Wi7gSU0mG) · fileKey `kwRnjJU3KdW28Wi7gSU0mG` · page `Screens` (`0:1`) |
| DS Figma file | Laabh — Design System · fileKey `mmAhXn4vJKlmuThcAMgGss` |
| PRD (text) | `prds/mf-kyc/prd.md` |
| Plan (screen list, IDs, statuses, decisions, gaps, log) | `prds/mf-kyc/plan.md` (`python3 scripts/plan-check.py prds/mf-kyc/plan.md`) |
| Review / audit reports | `prds/mf-kyc/review.md` (newest first) · `prds/mf-kyc/audit.md` |
| DS change proposal | `docs/proposals/mf-kyc-ds-updates.md` |
| Section screenshots | Not kept in the repo (removed 21 Oct: stale and 7 MB). Screenshot the Figma sections instead |

## Scope and decisions so far
- Journey A only (MF-only account, Phase 1). 51 screens planned, 32 built, 19 reviewed (Light + Dark); sections `0 · Welcome & contact`, `1 · Identity`, `2 · Bank`, `3 · Profile`, `4 · Submit & invest`, `5 · To be discussed`. `plan.md` has the current list and IDs.
- Answers: KYC validation 1 working day · ₹1 refunded same day · account-number backup after the **2nd** UPI failure · eSign for all users · Welcome screen M00 added.
- Feedback round 1 (all applied in Figma, Light and Dark; later rounds are in `plan.md` Decisions):
  - Top Bar shows **Back + stage bar only**: `Show step` off, `Show trailing` off, `Title` empty, set per instance (component unchanged).
  - Subtext trimmed; no negative phrasing ("Edit anything that's wrong" removed).
  - M08b: primary "Use another PAN", secondary ghost "How to link PAN and Aadhaar".
  - PEP (M14) and foreign tax residency (M15) are **checkboxes** (unchecked = no). This overrides review finding DR-01 by designer decision; M24 declarations restate them.
  - Nominee choice is a **Switch Row on M15** ("Add a nominee"); M15b = On → M17 form. M16/M16b removed; no opt-out confirmation checkbox. Opt-out is still OTP-confirmed (M19b) per PRD S6.4.
  - Communication address: M11 switch "Use a different address for communication" → **M11b** address form (built) → **M11c** proof upload (blocked, below).
- Rules followed: components first, tokens only, Light + Dark, annotations AN-xx on Light frames (Dark copies are clones without annotations).

## DS file changes (published 2026-10-20)
All of these are in the published library; documented in PR #11 (`docs/proposals/mf-kyc-ds-updates.md`).

| Change | Node / key |
|---|---|
| Avatar initials `text/brand-strong` | Avatar set `19:34` |
| Top Bar actions 44×44 + `Show leading` boolean | `51:43` |
| Segmented Control md 44 tall | `23:107`, `23:147` |
| Dark button glow removed: `elevation/primary/shadow-3` Dark → `alpha/transparent` | variable |
| **Icon Tile** (Tone × Size 40/64) | set `259:176` · key `97890c3a90f244f709ce8072a2294aa0e578625c` |
| **Summary Card** / **Summary Row** | `260:15` key `586cc19fd1fdc672336ce55864920ad1a41c7d53` · `260:14` key `7343985773883eb61570a94bfc11eb9b04cc016d` |
| **List Row** | `261:3` · key `8a9e007efa03ad8194019442294831f2c8c241c2` |
| **File Upload** (Empty/Uploading/Uploaded/Error) | `262:245` · key `fde42442ef4a511ddb68c9716a6c5dbd55efad2e` |
| **Keyboard** (Letters, Numbers) | `268:200` · key `a300befb2284dc705799bbbe86aa493adb597869` |
| `icon/brand-google`, `icon/brand-apple` | `267:184` key `ac552a256fd1f62c9149be1945cadacd6cee5165` · `267:187` key `32aadd720cb2698457147bfca2538c43e15d4119` |
| Already in the DS file before this work, released by the same publish | OTP Cell / TextField `border/strong`, Top Bar `Stage`, OTP Input text props |

Not done: no named Figma version was saved before the DS edits (API unavailable). Name the latest autosave in File → Version history if needed.

## Status 2026-10-20
Library published and steps 1–7 below are DONE (keyboards, logos, M10c, M11c, component swaps, Back hidden on M26/M26b, Dark rebuilt). Remaining: steps 8–10.
Feedback round 2 applied the same day (see `plan.md` Decisions and Log): M24 shortened, M24b added, M03/M09/M11/M23/M25/M25b removed, M10/M13/M20 updated, M00 kept. Figma IDs in `plan.md` are current. Steps 8–10 still to do.
Feedback round 3 applied the same day: new flow order (Contact → Identity → Bank → Profile → Submit & invest), MPIN, social-first email, PAN card, fetched bank account, Start-investing screens M27–M31, sheets for bureau details and occupation, and section `5 · To be discussed` for parked screens. Open questions Q10–Q15 in `plan.md`.

## Status 2026-10-21
PRs #11 (DS docs) and #12 (this folder) merged. Final review: ❌ not ready for handoff (2 S1, 3 S2 open, `review.md`). Next:
1. **Designer:** fix DR-01 (M29 says ₹0 charges) and DR-02 (M14 declaration pre-ticked), Light and Dark.
2. **Product / Compliance:** answer Q12, Q16, Q17, Q18 in `plan.md`; DR-03 and DR-04 follow from them.
3. **Designer:** DR-05 to DR-08, then re-run `/ds-audit` and `/design-review` on the changed screens and update `plan.md`.

## Next steps from 2026-10-19 (steps 1–8 and 10 done)
1. **Prasad:** publish the DS library (version note: "MF KYC review updates").
2. In the MF KYC file, accept **Library updates available** (Assets → Review → Update all). Check: `importComponentSetByKeyAsync('fde42442ef4a511ddb68c9716a6c5dbd55efad2e')` succeeds.
3. **Keyboards** (insert above `Home Indicator`, after `Footer`; set the frame to grow if the body no longer fits):

   | Type=Numbers | Type=Letters |
   |---|---|
   | M01 mobile, M02, M02b, M05, M19, M19b (OTP), M22 account number | M04 email, M07b PAN, M11b address, M13 names, M15 place of birth, M17, M17b nominee form |

   Focus the field the keyboard types into (TextField `State=Focus`) and keep the footer CTA visible above the keyboard.
4. **M04 logos:** on "Continue with Google/Apple" set `Leading icon` on and swap the nested Icon `Glyph` to `icon/brand-google` / `icon/brand-apple` (Icon Size 20).
5. **Build M10c** (upload PAN image) and **M11c** (communication address proof: Dropdown "Proof type" + File Upload) with the File Upload component.
6. **Swap hand-built compositions for instances** (the audit now flags them as "lookalike"):
   - `Icon tile` frames → **Icon Tile** (M00 ×4, M08, M08b, M08c, M09, M09b, M12, M12b, M21, M23, M23b, M23c, M23d, M23e, M25c, M26, M26b).
   - `Summary card` frames → **Summary Card** (M06, M09, M09b, M10, M10b, M20, M23, M23c, M24 ×5, M26, M26b). Use `Value type=Number` for numbers.
   - Nominee rows on M18/M18b and M00 highlights → **List Row**.
   - Hide Back on M26/M26b with Top Bar `Show leading` off.
7. Rebuild Dark copies: delete each `— Dark` frame and clone its Light frame, set `Color Tokens` mode Dark, place 80 px to the right (the script pattern is in this session's history; Dark must work by tokens alone).
8. Re-run `/ds-audit` (run `scripts/figma/audit.js` **verbatim**, TARGET `0:1`, save with `--out prds/mf-kyc/audit.md`) and `/design-review` stage final; fix S1/S2.
9. Update `plan.md` (statuses, Figma IDs, Log) and run `plan-check.py`. Screenshots are no longer kept in the repo.
10. `/share-changes` when Prasad asks (two PRs: DS docs/proposal/audit script, and the MF KYC feature folder). Ask before adding a `CHANGELOG.md` entry.

## Open questions
- Q8: final wording of the five declarations (Compliance).
- Avatar doc lists 4 pre-existing raw values in Image/Icon variants (not from this work).

## Screen index (Light · Dark node IDs)
See the Screens table in `plan.md` for the full list with components, states and rules. Section frame IDs from 19 Oct (`6:2`, `11:674`, `16:1667`, `20:2725`, `23:3173`) predate the round 3 re-sectioning; re-read them from Figma.
