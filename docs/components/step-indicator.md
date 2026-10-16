# Step Indicator · Step

> **Status:** stable · **Since:** v1.0 · **Figma page:** `1:17`

Progress through a short multi-step flow (onboarding, KYC, bank linking).

## Use it for
- Flows of 3–5 steps. `Dot` for compact headers, `Bar` when progress should read as a fill.
- Usually lives inside **Top Bar** (`Progress=On`). Use it standalone only in a custom header.

## Rules
- Always pair it with text "Step n of N" (Top Bar `Show step`, or a `caps-md` overline such as "STEP 2 OF 4").
- Steps aren't tappable unless the person can genuinely jump back.
- Pattern: overline "STEP 2 OF 4" → title ("Link your bank account") → one-line reason ("We'll verify it with a ₹1 deposit.").

## Accessibility
- Progress is also given in text (the step label), not only by dots.

## Figma doc drift
- none (Step radius bound to `radius/full` on 16 Oct 2026)

<!-- AUTO:START (generated from Figma by scripts/figma/inspect-components.js; do not edit by hand) -->
### Step Indicator

| | |
|---|---|
| Node ID | `32:39` (page `1:17`) |
| Key | `a3a1529ee03d8cca689b6808206be2154e100b6b` |
| Variants | 4 · default: `Style=Dot, Size=sm` |
| Default size | 52×6 |

| Property | Type | Values / default |
|---|---|---|
| Style | variant | Dot, Bar (default Dot) |
| Size | variant | sm, md (default sm) |

| Size | H | Specs (default variant at that size) |
|---|---|---|
| sm | 6 | gap space/6 |
| md | 8 | gap space/6 |

**Anatomy (default variant):** gap space/6

- Step 1 → `Step` — radius radius/full · fill surface/brand
- Step 2 → `Step` — radius radius/full · fill surface/brand
- Step 3 → `Step` — radius radius/full · fill surface/neutral-emphasis
- Step 4 → `Step` — radius radius/full · fill surface/neutral-emphasis

**Colour tokens across all variants:** `data/track` `surface/brand` `surface/neutral-emphasis`
**Text styles:** — · **Effects:** —

### Step

| | |
|---|---|
| Node ID | `32:16` (page `1:17`) |
| Key | `8c5d5278fae5d8259a316d49283b756f8a40192a` |
| Variants | 12 · default: `Style=Dot, State=Upcoming, Size=sm` |
| Default size | 6×6 |

| Property | Type | Values / default |
|---|---|---|
| Style | variant | Dot, Bar (default Dot) |
| State | variant | Upcoming, Current, Completed (default Upcoming) |
| Size | variant | sm, md (default sm) |

| Size | H | Specs (default variant at that size) |
|---|---|---|
| sm | 6 | radius radius/full · fill surface/neutral-emphasis |
| md | 8 | radius radius/full · fill surface/neutral-emphasis |

**Anatomy (default variant):** radius radius/full · fill surface/neutral-emphasis

**Colour tokens across all variants:** `data/track` `surface/brand` `surface/neutral-emphasis`
**Text styles:** — · **Effects:** —
<!-- AUTO:END -->
