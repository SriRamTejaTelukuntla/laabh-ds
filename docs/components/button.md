# Button · Icon Button · Compact Button

> **Status:** stable · **Since:** v1.0 · **Figma page:** `1:12`

Actions. Three sets share the same Style × Tone × State model.

## Use it for
| Style | Emphasis | Use |
|---|---|---|
| `Solid` | Highest | The one primary action per view. **Brand · lg** (52) is the screen CTA ("Add ₹25,000", "Continue") |
| `Outline` | Medium | Secondary action next to a Solid |
| `Tonal` | Medium, softer | Tinted alternatives. **Tonal · Neutral** is the glass button (quick-add amounts "+₹5,000") |
| `Ghost` | Lowest | Inline/tertiary ("Change", "View all") |

| Tone | Meaning |
|---|---|
| `Brand` | Default for primary actions |
| `Neutral` | Non-branded actions, glass buttons |
| `Success` | **Buy only** |
| `Danger` | **Sell only**, or destructive confirmation |
| `Accent`, `Warning` | Rare; needs a reason |

- **Icon Button**: icon-only, circular, sizes xs–xl (28 / 32 / 40 / 52 / 56), matching Button heights. Header actions, floating actions.
- **Compact Button**: 16/20/24 icon-only for tight spots: input adornments (clear, copy), table cells, chips, list rows.

## Don't use it for
- Navigation between sections → Tabs / Segmented Control.
- Filters → Tab Item (Solid).
- Links inside a sentence → Ghost button or inline text style in `text/brand`.

## Rules
- **One Solid button per view.**
- `Success` = Buy and `Danger` = Sell. Never use them for anything else.
- Screen CTA: `Solid · Brand · lg` (52), full width inside the 20 page margin, in the footer above the Home Indicator.
- Two actions side by side: equal widths, Solid on the right (primary), Outline/Tonal on the left.
- Size steps with context: `lg` for screen CTAs, `md` in cards and sheets, `sm`/`xs` inline.
- Never place an instance in the `Default` variant when you mean another default. **Always set Style, Tone, Size and State explicitly**: the set's default is `Neutral · xs`.

## Content
- Labels are verbs, sentence case, 1–3 words ("Continue", "Link bank", "Buy"). Amounts use the ₹ symbol with Indian grouping (₹25,000).

## Accessibility
- Hit target ≥ 44pt: xs/sm buttons need surrounding padding in the row. Keep the `Focus` state for keyboard/switch users.
- Icon-only buttons: name the layer after the action.

## Figma doc drift
- The component set's default variant is `Solid · Neutral · xs`. Consider changing it to `Solid · Brand · lg` so that dropped-in instances match the common case.

<!-- AUTO:START (generated from Figma by scripts/figma/inspect-components.js; do not edit by hand) -->
### Button

| | |
|---|---|
| Node ID | `12:3962` (page `1:12`) |
| Key | `5b00919be775498f573806968e533bad32189ada` |
| Variants | 480 · default: `Style=Solid, Tone=Neutral, Size=xs, State=Default` |
| Default size | 59×28 |

| Property | Type | Values / default |
|---|---|---|
| Label | text | Button |
| Show label | boolean | true |
| Leading icon | boolean | false |
| Trailing icon | boolean | false |
| Style | variant | Solid, Outline, Tonal, Ghost (default Solid) |
| Tone | variant | Neutral, Brand, Accent, Success, Danger, Warning (default Neutral) |
| Size | variant | xs, sm, md, lg, xl (default xs) |
| State | variant | Default, Pressed, Focus, Disabled (default Default) |

| Size | H | Specs (default variant at that size) |
|---|---|---|
| xs | 28 | pad space/0 space/10 space/0 space/10 · gap space/4 · radius radius/8 · fill surface/neutral · effect elevation/primary-sm |
| sm | 32 | pad space/0 space/12 space/0 space/12 · gap space/6 · radius radius/10 · fill surface/neutral · effect elevation/primary-sm |
| md | 40 | pad space/0 space/16 space/0 space/16 · gap space/8 · radius radius/12 · fill surface/neutral · effect elevation/primary-sm |
| lg | 52 | pad space/0 space/20 space/0 space/20 · gap space/8 · radius radius/12 · fill surface/neutral · effect elevation/primary-sm |
| xl | 56 | pad space/0 space/24 space/0 space/24 · gap space/10 · radius radius/14 · fill surface/neutral · effect elevation/primary-sm |

**Anatomy (default variant):** pad space/0 space/10 space/0 space/10 · gap space/4 · radius radius/8 · fill surface/neutral · effect elevation/primary-sm

- Label — text body-sm/Semibold · fill text/static-white

**Colour tokens across all variants:** `border/accent` `border/brand` `border/danger` `border/strong` `border/subtle` `border/success` `border/warning` `focus/ring` `glass/control` `glass/hairline` `glass/selected` `icon/accent` `icon/brand` `icon/danger` `icon/disabled` `icon/primary` `icon/static-black` `icon/static-white` `icon/success` `icon/warning` `surface/accent` `surface/accent-active` `surface/accent-subtle` `surface/accent-subtle-active` `surface/brand` `surface/brand-active` `surface/brand-subtle` `surface/brand-subtle-active` `surface/danger` `surface/danger-active` `surface/danger-subtle` `surface/danger-subtle-active` `surface/disabled` `surface/neutral` `surface/neutral-active` `surface/success` `surface/success-active` `surface/success-subtle` `surface/success-subtle-active` `surface/warning` `surface/warning-active` `surface/warning-subtle` `surface/warning-subtle-active` `text/accent` `text/brand` `text/danger` `text/disabled` `text/primary` `text/static-black` `text/static-white` `text/success` `text/warning`
**Text styles:** `body-sm/Semibold` `label-lg/Semibold` `label-md/Semibold` · **Effects:** `elevation/control` `elevation/primary` `elevation/primary-sm`

### Icon Button

| | |
|---|---|
| Node ID | `15:2053` (page `1:12`) |
| Key | `0fab8b7f276083988732d2f053cd67a2309f84ce` |
| Variants | 480 · default: `Style=Solid, Tone=Neutral, Size=xs, State=Default` |
| Default size | 28×28 |

| Property | Type | Values / default |
|---|---|---|
| Style | variant | Solid, Outline, Tonal, Ghost (default Solid) |
| Tone | variant | Neutral, Brand, Accent, Success, Danger, Warning (default Neutral) |
| Size | variant | xs, sm, md, lg, xl (default xs) |
| State | variant | Default, Pressed, Focus, Disabled (default Default) |

| Size | H | Specs (default variant at that size) |
|---|---|---|
| xs | 28 | radius radius/full · fill surface/neutral · effect elevation/primary-sm |
| sm | 32 | radius radius/full · fill surface/neutral · effect elevation/primary-sm |
| md | 40 | radius radius/full · fill surface/neutral · effect elevation/primary-sm |
| lg | 52 | radius radius/full · fill surface/neutral · effect elevation/primary-sm |
| xl | 56 | radius radius/full · fill surface/neutral · effect elevation/primary-sm |

**Anatomy (default variant):** radius radius/full · fill surface/neutral · effect elevation/primary-sm

- Icon → `Icon`

**Colour tokens across all variants:** `border/accent` `border/brand` `border/danger` `border/strong` `border/subtle` `border/success` `border/warning` `focus/ring` `glass/control` `glass/hairline` `glass/selected` `icon/accent` `icon/brand` `icon/danger` `icon/disabled` `icon/primary` `icon/static-black` `icon/static-white` `icon/success` `icon/warning` `surface/accent` `surface/accent-active` `surface/accent-subtle` `surface/accent-subtle-active` `surface/brand` `surface/brand-active` `surface/brand-subtle` `surface/brand-subtle-active` `surface/danger` `surface/danger-active` `surface/danger-subtle` `surface/danger-subtle-active` `surface/disabled` `surface/neutral` `surface/neutral-active` `surface/success` `surface/success-active` `surface/success-subtle` `surface/success-subtle-active` `surface/warning` `surface/warning-active` `surface/warning-subtle` `surface/warning-subtle-active`
**Text styles:** — · **Effects:** `elevation/control` `elevation/primary` `elevation/primary-sm`

### Compact Button

| | |
|---|---|
| Node ID | `15:3287` (page `1:12`) |
| Key | `c92eca2c603b2db9b879ebc83d36394eb869f7aa` |
| Variants | 192 · default: `Style=Solid, Tone=Neutral, Shape=Square, Size=16, State=Default` |
| Default size | 16×16 |

| Property | Type | Values / default |
|---|---|---|
| Style | variant | Solid, Outline, Tonal, Ghost (default Solid) |
| Tone | variant | Neutral, Brand (default Neutral) |
| Shape | variant | Square, Circle (default Square) |
| Size | variant | 16, 20, 24 (default 16) |
| State | variant | Default, Pressed, Focus, Disabled (default Default) |

| Size | H | Specs (default variant at that size) |
|---|---|---|
| 16 | 16 | radius radius/4 · fill surface/neutral |
| 20 | 20 | radius radius/6 · fill surface/neutral |
| 24 | 24 | radius radius/6 · fill surface/neutral |

**Anatomy (default variant):** radius radius/4 · fill surface/neutral

- Icon → `Icon`

**Colour tokens across all variants:** `border/brand` `border/strong` `border/subtle` `focus/ring` `glass/control` `glass/edge` `glass/selected` `icon/brand` `icon/disabled` `icon/primary` `icon/static-white` `surface/brand` `surface/brand-active` `surface/brand-subtle` `surface/brand-subtle-active` `surface/disabled` `surface/neutral` `surface/neutral-active`
**Text styles:** — · **Effects:** —
<!-- AUTO:END -->
