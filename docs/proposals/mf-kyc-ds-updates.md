# Change: DS updates from the MF KYC review

**Status:** approved by Prasad (acting DS owner) 2026-10-19 · built in the DS file, published 2026-10-20 · Section: COMPONENTS · Source: `prds/mf-kyc/review.md`, `prds/mf-kyc/audit.md`

## Why
The MF KYC build (`Laabh — MF KYC`, 46 screens) found component-level problems the feature file can't fix, and four compositions that were drawn by hand on 2+ screens.

## Changes to existing components
| Component | Change | Why | Breaking? |
|---|---|---|---|
| Avatar (Initials) | Initials text `text/brand` → `text/brand-strong` | 4.17:1 Light on `surface/brand-subtle` over a card; now 5.70:1 Light, 8.39:1 Dark | No |
| Top Bar | Leading and Trailing Icon Buttons sized 44×44 (Ghost, visually unchanged); new boolean `Show leading` | 40 pt targets under the 44 pt rule; result screens (Submitted) need no Back | No (Top Bar grows 4 px) |
| Segmented Control /md (Neutral, Brand) | Segments 30 → 38 tall, control 38 → 44 | 30 pt targets | No (control grows 6 px) |
| OTP Cell, TextField | none: the DS file already uses `border/strong` for Empty/Default/Filled; the library before 20 Oct still had `glass/hairline`/`glass/edge`. Fixed by the 20 Oct publish. | 1.12–1.16:1 borders in feature files | — |

Also released by the 20 Oct publish: Top Bar `Stage` variant, OTP Input text properties (timer, error, locked message).

## New components
| Component | Where it appears (MF KYC) | Props |
|---|---|---|
| Icon Tile | Result screens (M08, M08b, M09, M12, M21, M23, M26 …), Welcome highlights | `Tone` Brand/Success/Warning/Danger/Neutral · `Size` 40/64 · Icon (exposed Glyph swap) |
| Summary Row | Inside Summary Card | `Label`, `Value` · `Value type` Text/Number · `Show divider` |
| Summary Card | M06, M09, M10, M10b, M20, M23, M23c, M24 ×5, M26 | `Title`, `Show title`, `Show action` (Ghost "Edit", exposed), rows 1–6 (`Show row 4/5/6`) |
| List Row | M18 nominees, M00 highlights | `Title`, `Description`, `Value` · `Show leading` (Avatar, swappable for Icon Tile) · `Show description`, `Show value`, `Show action`, `Show divider` |
| File Upload | M10c (PAN image), M11 correspondence proof | `State` Empty/Uploading/Uploaded/Error · `Label`, `Title`, `Description`, `Helper` (the file name goes in `Title` after picking) |

## Added in feedback round 1 (19 Oct 2026)
| Change | Why |
|---|---|
| `elevation/primary/shadow-3` Dark value `alpha/blue-35` → `alpha/transparent` (same as Light) | Blue glow under Solid lg/xl buttons in Dark |
| `icon/brand-google`, `icon/brand-apple` on the Icons page (frame "Brand logos", `267:178`) | "Continue with Google/Apple" need the brand marks; Lucide has none. Google keeps its brand colours (raw hex by brand rule) |
| `Keyboard` (Letters, Numbers) on System Components (`268:200`) | Input screens show the keyboard; the iOS kits can't be imported into product files |

## Tokens
All existing: `surface/<tone>-subtle`, `border/brand-subtle`, `border/success-subtle`, `icon/<tone>`, `surface/card`, `glass/edge`, `glass/hairline`, `glass/field`, `border/strong`, `border/danger`, `border/success`, `text/*`, `radius/18`, `radius/14`, `radius/full`, `space/*`, `elevation/card`. No new tokens.

## Accessibility
- Icon Tile: decorative (AN-08) unless the screen says otherwise.
- Summary Card: label/value pairs (AN-06); the Edit action gets a 44 pt hit area and a name ("Edit contact details").
- List Row: whole row ≥ 64 pt; Edit action named per row.
- File Upload: role button, name from Title; state changes announced politely, errors assertively (AN-07); accepts camera and files.

## Figma plan
Version "Before MF KYC review DS updates" → Avatar → Top Bar → Segmented Control → pages `↳ File Upload`, `↳ Icon Tile`, `↳ List Row`, `↳ Summary Card` (alphabetical in COMPONENTS) → each with `— Variants` and a Dark copy.

## Open points
- Product screens swap their hand-built compositions for these instances (MF KYC done 20 Oct 2026).

## Added 20 Oct 2026 (round 4, published 20 Oct)
- **Logos** page `274:178`: 67 `logo/<brand>` component sets (Shape: Square, Circle) from the designer's UPI/bank SVGs. Doc: `docs/foundations/logos.md`.
- Gap: Option Card's leading icon is locked at 20 px, so logo pickers use List Row (40) + Radio. Consider an Option Card leading size or logo slot.
- Gap: Option Card has no flat (no-elevation) style for use inside sheets (MF KYC M14b overrides it locally).
