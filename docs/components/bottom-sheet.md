# Bottom Sheet

> **Status:** stable · **Since:** v1.0 · **Figma page:** `49:3`

A floating, iOS-style modal panel for a focused task, choice or consent, shown over the current screen with a scrim.

## Use it for
- Short tasks that don't deserve a screen: confirm an order, pick an option, give consent, enter an OTP for a nominee.
- `Footer=One` (single primary action) or `Footer=Two` (primary + secondary).

## Don't use it for
- Content taller than **70% of the screen** → a full screen.
- Non-blocking information → Alert.

## Rules
- Floats **8px** from the screen sides and bottom; all four corners `radius/40`; the home indicator stays visible underneath.
- Always place a `Sheet Scrim` instance (full screen, `surface/static-scrim`) between the screen and the sheet.
- Put screen-specific content in the **`Content` instance-swap slot** (the placeholder is `radius/12`; real contents have no radius of their own). Build the content as a product component named `Sheet Content/<name>` (on PRODUCT COMPONENTS), never by detaching the sheet.
- Dismiss: drag down or tap the scrim. For blocking consent sheets hide the close button (`Show close` = false).
- Title `display-md/Semibold` (one line), description `label-md/Regular` in `text/secondary`.

## Content
- Title states the decision ("Link your bank"). Description says why we ask, in one line. Primary button = the verb.

## Accessibility
- Focus moves into the sheet when it opens. Close is always reachable unless the sheet is blocking consent.

## Figma doc drift
- none (sheet Content instances follow the placeholder master, `radius/12`, since 16 Oct 2026). Product sheet contents (`Sheet Content/*`) have no radius by design: they sit inside the sheet.

<!-- AUTO:START (generated from Figma by scripts/figma/inspect-components.js; do not edit by hand) -->
### Bottom Sheet

| | |
|---|---|
| Node ID | `57:69` (page `49:3`) |
| Key | `2bbc857e103e2f59d264874f4c8ead6f21b9abf5` |
| Variants | 2 · default: `Footer=One` |
| Default size | 377×282 |

| Property | Type | Values / default |
|---|---|---|
| Title | text | Sheet title |
| Show description | boolean | true |
| Description | text | One line that explains why we’re asking. |
| Show close | boolean | true |
| Content | instance_swap | 57:2 |
| Footer | variant | One, Two (default One) |

**Anatomy (default variant):** pad space/8 space/20 space/20 space/20 · gap space/16 · radius radius/40 · fill glass/form · stroke glass/edge 1px · effect elevation/sheet

- Grabber
  - Rectangle — radius radius/full · fill surface/handle
- Header — gap space/12
  - Heading — gap space/4
    - Title — text display-md/Semibold · fill text/primary
    - Description — text label-md/Regular · fill text/secondary
  - Close → `Compact Button` — radius radius/full · fill glass/control · stroke glass/hairline 1px · effect elevation/control
- Content → `Sheet Content/Placeholder` — radius radius/12 · fill glass/control · stroke border/default 1px
- Footer — gap space/8
  - Primary → `Button` — pad space/0 space/20 space/0 space/20 · gap space/8 · radius radius/12 · fill surface/brand · effect elevation/primary

**Colour tokens across all variants:** `border/default` `glass/control` `glass/edge` `glass/form` `glass/hairline` `icon/primary` `icon/static-white` `surface/brand` `surface/handle` `text/primary` `text/secondary` `text/static-white`
**Text styles:** `body-sm/Medium` `display-md/Semibold` `label-lg/Semibold` `label-md/Regular` · **Effects:** `elevation/control` `elevation/primary` `elevation/sheet`

### Sheet Scrim

| | |
|---|---|
| Node ID | `57:4` (page `49:3`) |
| Key | `95963d9c7dd54c86ae38a90dd0e90c2e453387fe` |
| Variants | 1 · default: `Sheet Scrim` |
| Default size | 393×852 |

**Anatomy (default variant):** fill surface/static-scrim

**Colour tokens across all variants:** `surface/static-scrim`
**Text styles:** — · **Effects:** —

### Sheet Content/Placeholder

| | |
|---|---|
| Node ID | `57:2` (page `49:3`) |
| Key | `c0f40bc3b96fef7a292517fb6b737bb0c83c1245` |
| Variants | 1 · default: `Sheet Content/Placeholder` |
| Default size | 353×96 |

**Anatomy (default variant):** radius radius/12 · fill glass/control · stroke border/default 1px

- Swap content — text body-sm/Medium · fill text/secondary

**Colour tokens across all variants:** `border/default` `glass/control` `text/secondary`
**Text styles:** `body-sm/Medium` · **Effects:** —
<!-- AUTO:END -->
