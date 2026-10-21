# /ds-audit report

**File:** Document · **Target:** `0:1` · **Run:** 2026-10-20 18:07 UTC
**Screens:** 102 found, 102 checked in depth. Read-only: nothing in Figma was changed.

## Summary

| Severity | Findings | Meaning |
|---|---|---|
| S1 Blocker | 0 | fix before handoff |
| S2 Major | 7 | fix before release, or waive with a reason |
| S3 Minor | 25 | fix when the screen is next touched |
| S4 Polish | 2 | optional tidy-up |

_A finding can cover several layers (×n). `/design-review` may raise a severity (order or first-run flow, repeated on 3+ screens)._

| Check | Findings | Rule |
|---|---|---|
| Tap target too small | 26 (62 layers) | accessibility.md · WCAG 2.5.8 / house 44 pt |
| Border or icon contrast too low | 6 (10 layers) | accessibility.md · WCAG 1.4.11 |
| Local component, not from the library | 2 | components.md |

## Contrast failures (measured)

| Text or part | On | Mode | Kind | Ratio | Needs | Seen | Example |
|---|---|---|---|---|---|---|---|
| `glass/hairline` | surface/page | Light | border | 1.16:1 | 3:1 | 3× | `I88:22363;27:61` |
| `border/brand-subtle` | glass/field | Dark | border | 1.19:1 | 3:1 | 1× | `I99:14963;262:7` |
| `glass/hairline` | surface/page | Dark | border | 1.23:1 | 3:1 | 3× | `I99:16433;27:61` |
| `border/brand-subtle` | glass/field | Light | border | 1.28:1 | 3:1 | 1× | `I68:15174;262:7` |
| `border/success-subtle` | glass/field | Light | border | 1.42:1 | 3:1 | 1× | `I94:11628;262:148` |
| `border/success-subtle` | glass/field | Dark | border | 1.73:1 | 3:1 | 1× | `I99:15063;262:148` |

Fix by choosing a different semantic token (`docs/foundations/colors.md`), never by editing values.

## Inside DS components (fix in the library, not the screen)

These come from a component's own design. Report them to a DS owner (`/new-component` to change a component).

- **[S2] Border or icon contrast too low** · File Upload › Icon Tile: border 1.28:1 (needs 3:1) · `border/brand-subtle` on glass/field · Light · seen 1× (e.g. M11c Address proof — Light) · `I68:15174;262:7`
- **[S2] Border or icon contrast too low** · File Upload › Icon Tile: border 1.42:1 (needs 3:1) · `border/success-subtle` on glass/field · Light · seen 1× (e.g. M11d Address proof · uploaded — Light) · `I94:11628;262:148`
- **[S2] Border or icon contrast too low** · File Upload › Icon Tile: border 1.19:1 (needs 3:1) · `border/brand-subtle` on glass/field · Dark · seen 1× (e.g. M11c Address proof — Dark) · `I99:14963;262:7`
- **[S2] Border or icon contrast too low** · File Upload › Icon Tile: border 1.73:1 (needs 3:1) · `border/success-subtle` on glass/field · Dark · seen 1× (e.g. M11d Address proof · uploaded — Dark) · `I99:15063;262:148`
- **[S2] Tap target too small** · List Row › Radio: Radio inside List Row is 20 pt tall: under 24 (WCAG 2.5.8) unless spaced or an equivalent control exists · seen 8× (e.g. M20b Verify bank with UPI — Dark, M20b Verify bank with UPI — Light) · `I112:11908;261:11`
- **[S2] Border or icon contrast too low** · TextField/Amount › Button: border 1.16:1 (needs 3:1) · `glass/hairline` on surface/page · Light · seen 3× (e.g. M28 Start a SIP — Light) · `I88:22363;27:61`
- **[S2] Border or icon contrast too low** · TextField/Amount › Button: border 1.23:1 (needs 3:1) · `glass/hairline` on surface/page · Dark · seen 3× (e.g. M28 Start a SIP — Dark) · `I99:16433;27:61`
- **[S3] Tap target too small** · Alert › Action: Button Outline inside Alert is 28 pt tall: under 44 pt (house rule) · seen 2× (e.g. M18b Nominees · shares don’t add up — Dark, M18b Nominees · shares don’t add up — Light) · `I19:2785;55:80`
- **[S3] Tap target too small** · Bottom Sheet › Close: Compact Button Tonal inside Bottom Sheet is 24×24: under 44 pt (house rule) · seen 4× (e.g. M02d Verify mobile · what we fetch — Dark, M02d Verify mobile · what we fetch — Light, M14b Occupation · choose — Dark …) · `I80:21141;57:12`
- **[S3] Tap target too small** · List Row › Action: Button Ghost inside List Row is 32 pt tall: under 44 pt (house rule) · seen 14× (e.g. M18 Nominees — Dark, M18 Nominees — Light, M18b Nominees · shares don’t add up — Dark …) · `I68:16371;261:11`
- **[S3] Tap target too small** · List Row › Action: Button Ghost inside List Row is 40×32: under 44 pt (house rule) · seen 2× (e.g. M27 Start investing — Dark, M27 Start investing — Light) · `I96:11469;261:11`
- **[S3] Tap target too small** · Segmented Control/Neutral/md › Segment: Segment Neutral inside Segmented Control/Neutral/md is 36 pt tall: under 44 pt (house rule) · seen 4× (e.g. M22 Enter bank details — Dark, M22 Enter bank details — Light) · `I21:3278;23:108`

## Systemic (same problem on 3+ screens)

- **[S3] Tap target too small** on 8 screens: Button Ghost is 32 pt tall: under 44 pt (house rule). Layer `Change number` · e.g. M02 Verify mobile — Dark, M02 Verify mobile — Light, M02b Verify mobile · wrong code — Dark, M02b Verify mobile · wrong code — Light and 4 more · `9:358`
- **[S3] Tap target too small** on 6 screens: Checkbox is 40 pt tall: under 44 pt (house rule). Layer `Single holder` · e.g. M22 Enter bank details — Dark, M22 Enter bank details — Light, M24 Review — Dark, M24 Review — Light and 2 more · `21:3340`
- **[S3] Tap target too small** on 4 screens: Button Ghost is 40 pt tall: under 44 pt (house rule). Layer `Change my answers` · e.g. M24 Review — Dark, M24 Review — Light, M24b Review · eSign failed — Dark, M24b Review · eSign failed — Light · `71:11332`

## By screen

### M07 Confirm PAN — Dark · `99:12988` · 1 · Identity

- **[S4] Local component, not from the library** · PAN Card Preview: "PAN Card Preview" is a local component, not from the DS library · `99:12995`

### M07 Confirm PAN — Light · `12:882` · 1 · Identity

- **[S4] Local component, not from the library** · PAN Card Preview: "PAN Card Preview" is a local component, not from the DS library · `81:10399`

### M14 Work, income & nominee — Dark · `99:15157` · 3 · Profile

- **[S3] Tap target too small** · Citizenship, tax and PEP declaration: Checkbox is 36 pt tall: under 44 pt (house rule) · `99:15170`

### M14 Work, income & nominee — Light · `16:2014` · 3 · Profile

- **[S3] Tap target too small** · Citizenship, tax and PEP declaration: Checkbox is 36 pt tall: under 44 pt (house rule) · `82:10841`

**No screen-specific findings:** M00 Welcome — Dark, M00 Welcome — Light, M01 Mobile number — Dark, M01 Mobile number — Light, M02 Verify mobile — Dark, M02 Verify mobile — Light, M02b Verify mobile · wrong code — Dark, M02b Verify mobile · wrong code — Light, M02c Verify mobile · locked — Dark, M02c Verify mobile · locked — Light, M02d Verify mobile · what we fetch — Dark, M02d Verify mobile · what we fetch — Light, M03 Set MPIN — Dark, M03 Set MPIN — Light, M03b Confirm MPIN — Dark, M03b Confirm MPIN — Light, M03c MPIN doesn’t match — Dark, M03c MPIN doesn’t match — Light, M04 Email — Dark, M04 Email — Light, M04b Use another email — Dark, M04b Use another email — Light, M05 Verify email — Dark, M05 Verify email — Light, M07b Enter PAN & DOB — Dark, M07b Enter PAN & DOB — Light, M08b PAN can’t be used — Dark, M08b PAN can’t be used — Light, M08c Verifying · no connection — Dark, M08c Verifying · no connection — Light, M10 DigiLocker (placeholder) — Dark, M10 DigiLocker (placeholder) — Light, M20 Confirm bank account — Dark, M20 Confirm bank account — Light, M20b Verify bank with UPI — Dark, M20b Verify bank with UPI — Light, M21 Waiting for ₹1 payment — Dark, M21 Waiting for ₹1 payment — Light, M22 Enter bank details — Dark, M22 Enter bank details — Light, M23b ₹1 payment not received · 1st try — Dark, M23b ₹1 payment not received · 1st try — Light, M23c Bank needs a quick check — Dark, M23c Bank needs a quick check — Light, M23d UPI failed twice — Dark, M23d UPI failed twice — Light, M23e Joint account can’t be linked — Dark, M23e Joint account can’t be linked — Light, M11b Communication address — Dark, M11b Communication address — Light, M11c Address proof — Dark, M11c Address proof — Light, M11d Address proof · uploaded — Dark, M11d Address proof · uploaded — Light, M13 Personal details — Dark, M13 Personal details — Light, M13b Personal details · answered — Dark, M13b Personal details · answered — Light, M14b Occupation · choose — Dark, M14b Occupation · choose — Light, M17 Add nominee — Dark, M17 Add nominee — Light, M17b Add nominee · minor — Dark, M17b Add nominee · minor — Light, M18 Nominees — Dark, M18 Nominees — Light, M18b Nominees · shares don’t add up — Dark, M18b Nominees · shares don’t add up — Light, M26 Submitted — Dark, M26 Submitted — Light, M26b Submitted · KYC validation pending — Dark, M26b Submitted · KYC validation pending — Light, M27 Start investing — Dark, M27 Start investing — Light, M28 Start a SIP — Dark, M28 Start a SIP — Light, M29 Review your SIP — Dark, M29 Review your SIP — Light, M30 Set up autopay — Dark, M30 Set up autopay — Light, M31 SIP scheduled — Dark, M31 SIP scheduled — Light, M09b Name needs a manual check — Dark, M09b Name needs a manual check — Light, M12 KYC in process elsewhere — Dark, M12 KYC in process elsewhere — Light, M12b KYC on hold — Dark, M12b KYC on hold — Light, M19 Nominee OTP — Dark, M19 Nominee OTP — Light, M19b Nominee OTP · opt out — Dark, M19b Nominee OTP · opt out — Light, M24 Review — Dark, M24 Review — Light, M24b Review · eSign failed — Dark, M24b Review · eSign failed — Light, M25c eSign tries used up — Dark, M25c eSign tries used up — Light

## Contrast pairs measured

Colours resolved per mode and composited over everything behind them (glass and alpha included; Screen Atmosphere and background blur left out).

| Text or part | On | Mode | Kind | Lowest | Needs | Seen |
|---|---|---|---|---|---|---|
| `glass/hairline` | surface/page | Light | border | 1.16:1 ❌ | 3:1 | 3× |
| `border/brand-subtle` | glass/field | Dark | border | 1.19:1 ❌ | 3:1 | 1× |
| `glass/hairline` | surface/page | Dark | border | 1.23:1 ❌ | 3:1 | 3× |
| `border/brand-subtle` | glass/field | Light | border | 1.28:1 ❌ | 3:1 | 1× |
| `border/success-subtle` | glass/field | Light | border | 1.42:1 ❌ | 3:1 | 1× |
| `border/success-subtle` | glass/field | Dark | border | 1.73:1 ❌ | 3:1 | 1× |
| `border/strong` | surface/page | Dark | border | 3.34:1 | 3:1 | 58× |
| `border/strong` | glass/field | Dark | border | 3.4:1 | 3:1 | 1× |
| `border/strong` | surface/card over surface/page | Dark | border | 3.4:1 | 3:1 | 3× |
| `border/strong` | surface/page | Light | border | 3.81:1 | 3:1 | 58× |
| `border/strong` | glass/field | Light | border | 3.81:1 | 3:1 | 1× |
| `border/strong` | surface/card | Light | border | 3.81:1 | 3:1 | 3× |
| `border/focus` | surface/page | Dark | border | 4.23:1 | 3:1 | 14× |
| `border/focus` | surface/page | Light | border | 4.78:1 | 3:1 | 14× |
| `surface/brand` | surface/card | Light | border | 4.78:1 | 3:1 | 1× |
| `border/success` | surface/page | Light | border | 5.25:1 | 3:1 | 1× |
| `border/danger` | surface/page | Light | border | 5.48:1 | 3:1 | 8× |
| `border/danger` | surface/page | Dark | border | 8.38:1 | 3:1 | 8× |
| `border/success` | surface/page | Dark | border | 11.12:1 | 3:1 | 1× |
| `surface/brand` | surface/card over surface/page | Dark | border | 19.2:1 | 3:1 | 1× |
| `icon/success` | surface/success-subtle over surface/success-subtle | Light | icon | 4.03:1 | 3:1 | 1× |
| `icon/warning` | surface/warning-subtle over surface/page | Light | icon | 4.16:1 | 3:1 | 8× |
| `icon/brand` | surface/brand-subtle over surface/page | Light | icon | 4.18:1 | 3:1 | 3× |
| `icon/brand` | surface/brand-subtle over surface/card | Light | icon | 4.18:1 | 3:1 | 3× |
| `icon/brand` | surface/brand-subtle over glass/field | Light | icon | 4.18:1 | 3:1 | 1× |
| `icon/success` | surface/success-subtle over glass/field | Light | icon | 4.58:1 | 3:1 | 1× |
| `icon/success` | surface/success-subtle over surface/page | Light | icon | 4.58:1 | 3:1 | 3× |
| `icon/danger` | surface/danger-subtle over surface/page | Light | icon | 4.7:1 | 3:1 | 5× |
| `icon/static-white` | surface/brand | Light | icon | 4.78:1 | 3:1 | 11× |
| `icon/static-white` | surface/brand | Dark | icon | 4.78:1 | 3:1 | 11× |
| `icon/brand` | surface/brand-subtle over glass/field | Dark | icon | 4.99:1 | 3:1 | 1× |
| `icon/secondary` | surface/brand-subtle over surface/page | Light | icon | 5.2:1 | 3:1 | 14× |
| `icon/brand` | surface/brand-subtle over surface/card | Dark | icon | 5.21:1 | 3:1 | 3× |
| `icon/brand` | surface/brand-subtle over surface/page | Dark | icon | 5.61:1 | 3:1 | 3× |
| `icon/secondary` | glass/field | Light | icon | 5.94:1 | 3:1 | 15× |
| `icon/secondary` | glass/control | Light | icon | 5.94:1 | 3:1 | 1× |
| `icon/secondary` | surface/brand-subtle over surface/page | Dark | icon | 6.9:1 | 3:1 | 14× |
| `icon/danger` | surface/danger-subtle over surface/page | Dark | icon | 7.03:1 | 3:1 | 5× |
| `icon/success` | surface/success-subtle over surface/success-subtle | Dark | icon | 7.26:1 | 3:1 | 1× |
| `icon/secondary` | glass/field | Dark | icon | 7.68:1 | 3:1 | 15× |
| `icon/secondary` | glass/control over surface/page | Dark | icon | 7.68:1 | 3:1 | 1× |
| `icon/success` | surface/success-subtle over glass/field | Dark | icon | 8.2:1 | 3:1 | 1× |
| `icon/warning` | surface/warning-subtle over surface/page | Dark | icon | 9.15:1 | 3:1 | 8× |
| `icon/success` | surface/success-subtle over surface/page | Dark | icon | 9.33:1 | 3:1 | 3× |
| `icon/primary` | surface/card over surface/subtle | Dark | icon | 14.15:1 | 3:1 | 12× |
| `icon/primary` | glass/control over glass/form | Dark | icon | 14.32:1 | 3:1 | 2× |
| `icon/primary` | surface/subtle | Dark | icon | 15.22:1 | 3:1 | 10× |
| `icon/primary` | surface/subtle | Light | icon | 15.64:1 | 3:1 | 10× |
| `icon/primary` | surface/page | Dark | icon | 16.62:1 | 3:1 | 44× |
| `icon/primary` | surface/page | Light | icon | 19.23:1 | 3:1 | 44× |
| `icon/primary` | glass/control | Light | icon | 19.23:1 | 3:1 | 2× |
| `icon/primary` | surface/card | Light | icon | 19.23:1 | 3:1 | 12× |
| `text/primary` | surface/brand-subtle over surface/page | Dark | large text | 13.74:1 | 3:1 | 1× |
| `text/primary` | glass/field | Dark | large text | 15.3:1 | 3:1 | 24× |
| `text/primary` | glass/form over surface/static-scrim | Dark | large text | 15.86:1 | 3:1 | 2× |
| `text/primary` | surface/page | Dark | large text | 16.62:1 | 3:1 | 49× |
| `text/primary` | surface/brand-subtle over surface/page | Light | large text | 16.82:1 | 3:1 | 1× |
| `text/primary` | surface/page | Light | large text | 19.23:1 | 3:1 | 49× |
| `text/primary` | glass/field | Light | large text | 19.23:1 | 3:1 | 24× |
| `text/primary` | glass/form | Light | large text | 19.23:1 | 3:1 | 2× |
| `text/static-white` | surface/brand | Light | text | 4.78:1 | 4.5:1 | 42× |
| `text/brand` | surface/page | Light | text | 4.78:1 | 4.5:1 | 7× |
| `text/static-white` | surface/brand | Dark | text | 4.78:1 | 4.5:1 | 42× |
| `text/brand` | surface/card | Light | text | 4.78:1 | 4.5:1 | 12× |
| `text/secondary` | surface/brand-subtle over surface/page | Light | text | 5.2:1 | 4.5:1 | 4× |
| `text/secondary` | glass/track over surface/page | Light | text | 5.32:1 | 4.5:1 | 1× |
| `text/danger` | surface/page | Light | text | 5.48:1 | 4.5:1 | 2× |
| `text/danger` | surface/card | Light | text | 5.48:1 | 4.5:1 | 1× |
| `text/brand-strong` | surface/brand-subtle over surface/page | Light | text | 5.72:1 | 4.5:1 | 5× |
| `text/brand-strong` | surface/brand-subtle over surface/card | Light | text | 5.72:1 | 4.5:1 | 8× |
| `text/brand-strong` | surface/brand-subtle over glass/form | Light | text | 5.72:1 | 4.5:1 | 1× |
| `text/secondary` | surface/page | Light | text | 5.94:1 | 4.5:1 | 115× |
| `text/secondary` | surface/card | Light | text | 5.94:1 | 4.5:1 | 162× |
| `text/secondary` | glass/form | Light | text | 5.94:1 | 4.5:1 | 4× |
| `text/secondary` | glass/field | Light | text | 5.94:1 | 4.5:1 | 4× |
| `text/placeholder` | glass/field | Light | text | 5.94:1 | 4.5:1 | 5× |
| `text/placeholder` | glass/control | Light | text | 5.94:1 | 4.5:1 | 1× |
| `text/warning-strong` | surface/warning-subtle over surface/page | Light | text | 6.28:1 | 4.5:1 | 1× |
| `text/danger-strong` | surface/danger-subtle over surface/page | Light | text | 6.35:1 | 4.5:1 | 2× |
| `text/brand` | surface/card over surface/page | Dark | text | 6.44:1 | 4.5:1 | 12× |
| `text/brand` | surface/page | Dark | text | 6.78:1 | 4.5:1 | 7× |
| `text/secondary` | surface/brand-subtle over surface/page | Dark | text | 6.9:1 | 4.5:1 | 4× |
| `text/secondary` | surface/card over surface/subtle | Dark | text | 7.1:1 | 4.5:1 | 80× |
| `text/placeholder` | glass/field | Dark | text | 7.68:1 | 4.5:1 | 5× |
| `text/secondary` | glass/field | Dark | text | 7.68:1 | 4.5:1 | 4× |
| `text/secondary` | glass/track over surface/page | Dark | text | 7.68:1 | 4.5:1 | 1× |
| `text/placeholder` | glass/control over surface/page | Dark | text | 7.68:1 | 4.5:1 | 1× |
| `text/secondary` | surface/card over surface/page | Dark | text | 7.93:1 | 4.5:1 | 82× |
| `text/secondary` | glass/form over surface/static-scrim | Dark | text | 7.96:1 | 4.5:1 | 4× |
| `text/danger` | surface/card over surface/page | Dark | text | 7.96:1 | 4.5:1 | 1× |
| `text/secondary` | surface/page | Dark | text | 8.34:1 | 4.5:1 | 115× |
| `text/brand-strong` | surface/brand-subtle over surface/card | Dark | text | 8.37:1 | 4.5:1 | 8× |
| `text/danger` | surface/page | Dark | text | 8.38:1 | 4.5:1 | 2× |
| `text/brand-strong` | surface/brand-subtle over glass/form | Dark | text | 8.4:1 | 4.5:1 | 1× |
| `text/brand-strong` | surface/brand-subtle over surface/page | Dark | text | 9.01:1 | 4.5:1 | 5× |
| `text/danger-strong` | surface/danger-subtle over surface/page | Dark | text | 9.82:1 | 4.5:1 | 2× |
| `text/warning-strong` | surface/warning-subtle over surface/page | Dark | text | 10.92:1 | 4.5:1 | 1× |
| `text/neutral` | surface/brand-subtle over surface/page | Dark | text | 11.08:1 | 4.5:1 | 5× |
| `text/primary` | glass/thumb over glass/track | Dark | text | 11.21:1 | 4.5:1 | 1× |
| `text/neutral` | surface/brand-subtle over surface/page | Light | text | 11.79:1 | 4.5:1 | 5× |
| `text/primary` | surface/warning-subtle over surface/page | Dark | text | 12.63:1 | 4.5:1 | 1× |
| `text/primary` | surface/brand-subtle over surface/page | Dark | text | 13.74:1 | 4.5:1 | 17× |
| `text/primary` | surface/success-subtle over surface/page | Dark | text | 13.94:1 | 4.5:1 | 1× |
| `text/primary` | surface/danger-subtle over surface/page | Dark | text | 13.96:1 | 4.5:1 | 3× |
| `text/primary` | surface/card over surface/subtle | Dark | text | 14.15:1 | 4.5:1 | 274× |
| `text/primary` | surface/card over glass/form | Dark | text | 14.86:1 | 4.5:1 | 10× |
| `text/primary` | glass/field | Dark | text | 15.3:1 | 4.5:1 | 35× |
| `text/primary` | glass/control over surface/page | Dark | text | 15.3:1 | 4.5:1 | 3× |
| `text/primary` | surface/card over surface/page | Dark | text | 15.79:1 | 4.5:1 | 87× |
| `text/primary` | glass/form over surface/static-scrim | Dark | text | 15.86:1 | 4.5:1 | 3× |
| `text/primary` | surface/danger-subtle over surface/page | Light | text | 16.49:1 | 4.5:1 | 3× |
| `text/primary` | surface/page | Dark | text | 16.62:1 | 4.5:1 | 90× |
| `text/primary` | surface/success-subtle over surface/page | Light | text | 16.79:1 | 4.5:1 | 1× |
| `text/primary` | surface/brand-subtle over surface/page | Light | text | 16.82:1 | 4.5:1 | 17× |
| `text/primary` | surface/warning-subtle over surface/page | Light | text | 17.07:1 | 4.5:1 | 1× |
| `text/primary` | surface/page | Light | text | 19.23:1 | 4.5:1 | 90× |
| `text/primary` | surface/card | Light | text | 19.23:1 | 4.5:1 | 371× |
| `text/primary` | glass/form | Light | text | 19.23:1 | 4.5:1 | 3× |
| `text/primary` | glass/field | Light | text | 19.23:1 | 4.5:1 | 35× |
| `text/primary` | glass/thumb | Light | text | 19.23:1 | 4.5:1 | 1× |
| `text/primary` | glass/control | Light | text | 19.23:1 | 4.5:1 | 3× |

## Not checked or exempt

- disabled text: 2× — disabled controls are exempt (WCAG 1.4.3)
- text covered by an overlay: 46× — under a scrim or sheet, not readable by design
- Hit areas are measured on component bounds; a larger tappable parent frame, or spacing between small targets, is not seen. Check those by eye.
- Not covered here (judged in `/design-review`): copy, flows, states, focus order, annotations.
