# App Header

> **Status:** stable · **Since:** v1.0 · **Figma page:** `107:183567`

The header of the main app screens (tabs and their detail screens). Sits directly under the Status Bar.

## Use it for
| Type | When |
|---|---|
| `Search` (56 tall) | Explore / home tab: avatar, search field, actions |
| `Greeting` | Personal home moments ("Good morning, Anika") |
| `Title` | Top-level tab screens (Watchlist, Orders, Funds, Portfolio) |
| `Back` | Detail screens where the content carries its own title (Stock detail) |
| `Back + Title` | Detail screens that need a title (Collection detail, Analysis) |
| `Centered title` | Settings-like screens (Account) |

## Don't use it for
- Onboarding, KYC and other step-by-step flows → **Top Bar** (has progress and step).
- Inside sheets → the Bottom Sheet's own header.

## Rules
- Always the first element under `Status Bar`, full width (390), page margin 20 built in. Don't add extra padding around it.
- Show at most the actions the screen needs. Hide the rest with `Show action 1/2/3`. Actions are Icon Buttons (glass, `elevation/control`).
- Title text is set through the `Title` property. Keep it to one line.

## Content
- Titles: 1–2 words, Title Case for tab names ("Watchlist"), sentence case for detail titles.
- Search placeholder names what can be found: "Search stocks, ETFs, funds".

## Accessibility
- Icon-only actions need a clear purpose. Name the layer after the action (`Notifications`, `Add`). Hit targets come from Icon Button (≥ 40 + spacing; keep the 44pt tappable frame).

## Figma doc drift
- The App Header page has no Reference frame yet. It lives under PRODUCT COMPONENTS (moved 16 Oct 2026): it is Laabh-specific app chrome.

<!-- AUTO:START (generated from Figma by scripts/figma/inspect-components.js; do not edit by hand) -->
### App Header

| | |
|---|---|
| Node ID | `107:183679` (page `107:183567`) |
| Key | `4058dba66fcdaf433bab6abab827d61adb89a1db` |
| Variants | 6 · default: `Type=Search` |
| Default size | 390×56 |

| Property | Type | Values / default |
|---|---|---|
| Title | text | Title |
| Greeting | text | Good morning |
| Name | text | Anika |
| Placeholder | text | Search stocks, ETFs, funds |
| Show action 1 | boolean | true |
| Show action 2 | boolean | true |
| Show action 3 | boolean | true |
| Type | variant | Search, Greeting, Title, Back, Back + Title, Centered title (default Search) |

**Anatomy (default variant):** pad 0 space/20 0 space/20 · gap space/12

- Avatar → `Avatar` — radius radius/full · fill surface/brand-subtle · stroke border/brand-subtle 1px
- Search — pad 0 space/14 0 space/12 · gap space/8 · radius radius/12 · fill glass/control · stroke glass/hairline 1px · effect elevation/control
  - Icon / search → `Icon`
  - Placeholder — text label-md/Regular · fill text/secondary
- Action 1 → `Icon Button` — radius radius/full · fill glass/control · stroke glass/hairline 1px · effect elevation/control

**Colour tokens across all variants:** `border/brand-subtle` `glass/control` `glass/hairline` `icon/primary` `icon/secondary` `surface/brand-subtle` `text/brand-strong` `text/primary` `text/secondary`
**Text styles:** `body-sm/Regular` `body-sm/Semibold` `display-md/Semibold` `label-md/Medium` `label-md/Regular` · **Effects:** `elevation/control`
<!-- AUTO:END -->
