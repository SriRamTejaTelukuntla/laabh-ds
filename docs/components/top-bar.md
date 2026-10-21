# Top Bar

> **Status:** stable · **Since:** v1.0 · **Figma page:** `49:7`

The header for onboarding, KYC and other step-by-step flows: back, step caption, title, help, and a stage bar.

## Use it for
- Every screen of a multi-step flow. `Progress=On` while in the flow; `Progress=Off` on result screens (Submitted, Activated).

## Don't use it for
- Main app tabs and their detail screens → App Header.

## Rules
- No fill: it sits on the page atmosphere directly under the Status Bar.
- Keep the step caption and the stage bar in sync ("Step 2 of 5 · Identity" = stage 2 Current).
- KYC uses **5 stages**: Contact · Identity · Profile · Bank · Review.
- Leading = back (`icon/arrow-left`), trailing = help (`icon/circle-help`); both Ghost Neutral Icon Buttons sized 44×44 (44 pt targets). Hide trailing with `Show trailing` when there's no help.
- Result screens after an irreversible step (Submitted) hide Back with `Show leading` = false, so Back can't look like it reopens the step.
- Set the stage with `Stage` (1–5) on `Progress=On`.
- 393 wide in the library. On a 390 canvas set it to Fill container.

## Content
- Caption: "Step n of N · <Stage>". Title: what this screen does, 1–3 words ("Verify mobile").

## Figma doc drift
- The Reference frame still says the actions are "Icon Button Ghost Neutral md (40)"; they are 44×44 since 19 Oct 2026 (`docs/proposals/mf-kyc-ds-updates.md`).

<!-- AUTO:START (generated from Figma by scripts/figma/inspect-components.js; do not edit by hand) -->
### Top Bar

| | |
|---|---|
| Node ID | `51:43` (page `49:7`) |
| Key | `62be1b1e192159c77b9853dec8d1cfb8f635a49c` |
| Variants | 6 · default: `Progress=On, Stage=1` |
| Default size | 393×71 |

| Property | Type | Values / default |
|---|---|---|
| Title | text | Verify mobile |
| Step | text | Step 1 of 5 · Contact |
| Show step | boolean | true |
| Show trailing | boolean | true |
| Show leading | boolean | true |
| Progress | variant | On, Off (default On) |
| Stage | variant | 1, 2, 3, 4, 5 (default 1) |

**Anatomy (default variant):** pad space/4 space/0 space/12 space/0 · gap space/8

- Row — pad space/0 space/8 space/0 space/8 · gap space/4
  - Leading → `Icon Button` — radius radius/full
  - Title block — gap space/2
    - Step — text caps-md/Medium · fill text/secondary
    - Title — text label-md/Medium · fill text/primary
  - Trailing → `Icon Button` — radius radius/full
- Progress — pad space/0 space/20 space/0 space/20 · gap space/4
  - Stage 1 → `Step` — radius radius/full · fill data/track
  - Stage 2 → `Step` — radius radius/full · fill data/track
  - Stage 3 → `Step` — radius radius/full · fill data/track
  - Stage 4 → `Step` — radius radius/full · fill data/track
  - Stage 5 → `Step` — radius radius/full · fill data/track

**Colour tokens across all variants:** `data/track` `icon/primary` `surface/brand` `text/primary` `text/secondary`
**Text styles:** `caps-md/Medium` `label-md/Medium` · **Effects:** —
<!-- AUTO:END -->
