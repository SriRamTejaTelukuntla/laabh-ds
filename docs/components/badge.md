# Badge

> **Status:** stable · **Since:** v1.0 · **Figma page:** `1:11`

A short, non-interactive label for status, category or change.

## Use it for
| Pattern | Style · Tone |
|---|---|
| Day change on a holding/stock | `Glass` · `Success` / `Danger`, always signed (+/−) |
| Benchmark & returns info | `Soft` · `Neutral` (navy-tinted: information, not gain/loss) |
| Product / segment tags (EQ, F&O, ETF) | `Solid` · `Brand` · `sm`, or `Soft` · `Accent` · `sm` |
| Time-critical (expiry) | `Solid` · `Danger` · `sm` |

## Don't use it for
- Filters or selectable chips → **Tab Item** (Style=Solid).
- Buttons. Badges are never tappable.

## Rules
- One line, 1–3 words.
- Never put a Solid badge on a Solid button.
- Never colour a price change without a sign. Numbers use `num-body-sm/Medium`; words like "today" stay Inter.
- `Danger` means time-critical or failed, not "loss". For losses use the Glass/Soft danger pattern with a sign.

## Content
- `sm` labels are caps (`caps-md/Semibold`); `md` labels use sentence case.

## Accessibility
- Colour is never the only cue: sign, arrow or word must carry the meaning.

## Figma doc drift
- none

<!-- AUTO:START (generated from Figma by scripts/figma/inspect-components.js; do not edit by hand) -->
### Badge

| | |
|---|---|
| Node ID | `17:650` (page `1:11`) |
| Key | `e7bcab8436500c711e480506c3a356d5f4425462` |
| Variants | 72 · default: `Style=Solid, Tone=Brand, Size=sm, Shape=Pill` |
| Default size | 54×18 |

| Property | Type | Values / default |
|---|---|---|
| Label | text | Badge |
| Show label | boolean | true |
| Leading icon | boolean | false |
| Trailing icon | boolean | false |
| Dot | boolean | false |
| Style | variant | Solid, Soft, Glass (default Solid) |
| Tone | variant | Brand, Neutral, Success, Warning, Danger, Accent (default Brand) |
| Size | variant | sm, md (default sm) |
| Shape | variant | Pill, Rounded (default Pill) |

| Size | H | Specs (default variant at that size) |
|---|---|---|
| sm | 18 | pad space/2 space/6 space/2 space/6 · gap space/4 · radius radius/full · fill surface/brand |
| md | 24 | pad space/4 space/8 space/4 space/8 · gap space/4 · radius radius/full · fill surface/brand |

**Anatomy (default variant):** pad space/2 space/6 space/2 space/6 · gap space/4 · radius radius/full · fill surface/brand

- Label — text caps-md/Semibold · fill text/static-white

**Colour tokens across all variants:** `border/neutral` `glass/control` `glass/edge` `icon/accent` `icon/brand` `icon/danger` `icon/secondary` `icon/static-black` `icon/static-white` `icon/success` `icon/warning` `surface/accent` `surface/accent-subtle` `surface/brand` `surface/brand-subtle` `surface/danger` `surface/danger-subtle` `surface/neutral` `surface/neutral-subtle` `surface/success` `surface/success-subtle` `surface/warning` `surface/warning-subtle` `text/accent` `text/brand` `text/danger` `text/neutral` `text/secondary` `text/static-black` `text/static-white` `text/success` `text/warning`
**Text styles:** `body-sm/Medium` `caps-md/Semibold` · **Effects:** —
<!-- AUTO:END -->
