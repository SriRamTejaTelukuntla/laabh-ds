# /ds-audit report

**File:** PRD Test · **Target:** `0:1` · **Run:** 2026-10-19 11:53 UTC
**Screens:** 30 found, 30 checked in depth. Read-only: nothing in Figma was changed.

## Summary

| Severity | Findings | Meaning |
|---|---|---|
| S1 Blocker | 0 | fix before handoff |
| S2 Major | 6 | fix before release, or waive with a reason |
| S3 Minor | 17 | fix when the screen is next touched |
| S4 Polish | 0 | optional tidy-up |

_A finding can cover several layers (×n). `/design-review` may raise a severity (order or first-run flow, repeated on 3+ screens)._

| Check | Findings | Rule |
|---|---|---|
| Tap target too small | 17 (78 layers) | accessibility.md · WCAG 2.5.8 / house 44 pt |
| Border or icon contrast too low | 6 (36 layers) | accessibility.md · WCAG 1.4.11 |

## Contrast failures (measured)

| Text or part | On | Mode | Kind | Ratio | Needs | Seen | Example |
|---|---|---|---|---|---|---|---|
| `glass/edge` | surface/page | Light | border | 1.12:1 | 3:1 | 3× | `I3:6548;25:756` |
| `glass/hairline` | surface/page | Light | border | 1.16:1 | 3:1 | 15× | `I3:2522;25:448` |
| `glass/hairline` | surface/page | Dark | border | 1.23:1 | 3:1 | 15× | `I3:8352;25:448` |
| `glass/edge` | surface/page | Dark | border | 1.23:1 | 3:1 | 3× | `I3:9347;25:756` |

Fix by choosing a different semantic token (`docs/foundations/colors.md`), never by editing values.

## Inside DS components (fix in the library, not the screen)

These come from a component's own design. Report them to a DS owner (`/new-component` to change a component).

- **[S2] Border or icon contrast too low** · OTP Cell › Cell 1: border 1.16:1 (needs 3:1) · `glass/hairline` on surface/page · Light · seen 9× (e.g. K02 Verify mobile — Light, K02c Verify mobile · locked — Light, K04 Verify email — Light) · `I3:5565;52:29`
- **[S2] Border or icon contrast too low** · OTP Cell › Cell 1: border 1.23:1 (needs 3:1) · `glass/hairline` on surface/page · Dark · seen 9× (e.g. K02 Verify mobile — Dark, K02c Verify mobile · locked — Dark, K04 Verify email — Dark) · `I3:8563;52:29`
- **[S2] Border or icon contrast too low** · TextField › Field: border 1.16:1 (needs 3:1) · `glass/hairline` on surface/page · Light · seen 6× (e.g. K01 Mobile number — Light, K01b Mobile number · no connection — Light, K03 Email — Light …) · `I3:2522;25:448`
- **[S2] Border or icon contrast too low** · TextField › Field: border 1.23:1 (needs 3:1) · `glass/hairline` on surface/page · Dark · seen 6× (e.g. K01 Mobile number — Dark, K01b Mobile number · no connection — Dark, K03 Email — Dark …) · `I3:8352;25:448`
- **[S2] Border or icon contrast too low** · TextField › Field: border 1.12:1 (needs 3:1) · `glass/edge` on surface/page · Light · seen 3× (e.g. K06 Confirm PAN & DOB — Light, K06d Confirm PAN & DOB · details don’t match — Light) · `I3:6548;25:756`
- **[S2] Border or icon contrast too low** · TextField › Field: border 1.23:1 (needs 3:1) · `glass/edge` on surface/page · Dark · seen 3× (e.g. K06 Confirm PAN & DOB — Dark, K06d Confirm PAN & DOB · details don’t match — Dark) · `I3:9347;25:756`
- **[S3] Tap target too small** · Bottom Sheet › Close: Compact Button Tonal inside Bottom Sheet is 24×24: under 44 pt (house rule) · seen 2× (e.g. K05 Prefill consent — Dark, K05 Prefill consent — Light) · `I3:7744;57:41`
- **[S3] Tap target too small** · Bottom Sheet › Consent: Checkbox inside Bottom Sheet is 36 pt tall: under 44 pt (house rule) · seen 2× (e.g. K05 Prefill consent — Dark, K05 Prefill consent — Light) · `I3:7744;57:46;104:183140`
- **[S3] Tap target too small** · Top Bar › Leading: Icon Button Ghost inside Top Bar is 40×40: under 44 pt (house rule) · seen 60× (e.g. K01 Mobile number — Light, K01b Mobile number · no connection — Light, K02 Verify mobile — Light …) · `I3:1396;51:4`

## Systemic (same problem on 3+ screens)

- **[S3] Tap target too small** on 8 screens: Button Ghost is 32 pt tall: under 44 pt (house rule). Layer `Edit number` · e.g. K02 Verify mobile — Dark, K02 Verify mobile — Light, K02b Verify mobile · wrong code — Dark, K02b Verify mobile · wrong code — Light and 4 more · `3:5524`
- **[S3] Tap target too small** on 6 screens: Checkbox is 40 pt tall: under 44 pt (house rule). Layer `Own number declaration` · e.g. K01 Mobile number — Dark, K01 Mobile number — Light, K01b Mobile number · no connection — Dark, K01b Mobile number · no connection — Light and 2 more · `3:2780`

## By screen

**No screen-specific findings:** K01 Mobile number — Dark, K01 Mobile number — Light, K01b Mobile number · no connection — Dark, K01b Mobile number · no connection — Light, K02 Verify mobile — Dark, K02 Verify mobile — Light, K02b Verify mobile · wrong code — Dark, K02b Verify mobile · wrong code — Light, K02c Verify mobile · locked — Dark, K02c Verify mobile · locked — Light, K02d Welcome back — Dark, K02d Welcome back — Light, K03 Email — Dark, K03 Email — Light, K04 Verify email — Dark, K04 Verify email — Light, K05 Prefill consent — Dark, K05 Prefill consent — Light, K06 Confirm PAN & DOB — Dark, K06 Confirm PAN & DOB — Light, K06b Enter PAN & DOB — Dark, K06b Enter PAN & DOB — Light, K06c Enter PAN & DOB · format error — Dark, K06c Enter PAN & DOB · format error — Light, K06d Confirm PAN & DOB · details don’t match — Dark, K06d Confirm PAN & DOB · details don’t match — Light, K07 Verifying PAN — Dark, K07 Verifying PAN — Light, K07b PAN can’t be used — Dark, K07b PAN can’t be used — Light

## Contrast pairs measured

Colours resolved per mode and composited over everything behind them (glass and alpha included; Screen Atmosphere and background blur left out).

| Text or part | On | Mode | Kind | Lowest | Needs | Seen |
|---|---|---|---|---|---|---|
| `glass/edge` | surface/page | Light | border | 1.12:1 ❌ | 3:1 | 3× |
| `glass/hairline` | surface/page | Light | border | 1.16:1 ❌ | 3:1 | 15× |
| `glass/hairline` | surface/page | Dark | border | 1.23:1 ❌ | 3:1 | 15× |
| `glass/edge` | surface/page | Dark | border | 1.23:1 ❌ | 3:1 | 3× |
| `border/strong` | surface/page | Dark | border | 3.34:1 | 3:1 | 2× |
| `border/strong` | glass/form over surface/static-scrim | Dark | border | 3.4:1 | 3:1 | 1× |
| `border/strong` | surface/page | Light | border | 3.81:1 | 3:1 | 2× |
| `border/strong` | glass/form | Light | border | 3.81:1 | 3:1 | 1× |
| `border/focus` | surface/page | Dark | border | 4.23:1 | 3:1 | 3× |
| `border/focus` | surface/page | Light | border | 4.78:1 | 3:1 | 3× |
| `border/danger` | surface/page | Light | border | 5.48:1 | 3:1 | 6× |
| `border/danger` | surface/page | Dark | border | 8.38:1 | 3:1 | 6× |
| `icon/primary` | surface/brand | Dark | icon | 3.93:1 | 3:1 | 4× |
| `icon/primary` | surface/brand | Light | icon | 4.03:1 | 3:1 | 4× |
| `icon/warning` | surface/warning-subtle over surface/page | Light | icon | 4.16:1 | 3:1 | 1× |
| `icon/brand` | surface/brand-subtle over glass/form | Light | icon | 4.18:1 | 3:1 | 3× |
| `icon/danger` | surface/danger-subtle over surface/page | Light | icon | 4.7:1 | 3:1 | 3× |
| `icon/brand` | surface/brand-subtle over glass/form | Dark | icon | 5.23:1 | 3:1 | 3× |
| `icon/secondary` | glass/control | Light | icon | 5.94:1 | 3:1 | 2× |
| `icon/secondary` | glass/field | Light | icon | 5.94:1 | 3:1 | 2× |
| `icon/danger` | surface/danger-subtle over surface/page | Dark | icon | 7.03:1 | 3:1 | 3× |
| `icon/secondary` | glass/control over surface/page | Dark | icon | 7.68:1 | 3:1 | 2× |
| `icon/secondary` | glass/field | Dark | icon | 7.68:1 | 3:1 | 2× |
| `icon/warning` | surface/warning-subtle over surface/page | Dark | icon | 9.15:1 | 3:1 | 1× |
| `icon/primary` | glass/control over glass/form | Dark | icon | 14.32:1 | 3:1 | 1× |
| `icon/primary` | surface/page | Dark | icon | 16.62:1 | 3:1 | 28× |
| `icon/primary` | surface/page | Light | icon | 19.23:1 | 3:1 | 28× |
| `icon/primary` | glass/control | Light | icon | 19.23:1 | 3:1 | 1× |
| `text/primary` | glass/field | Dark | large text | 15.3:1 | 3:1 | 12× |
| `text/primary` | glass/form over surface/static-scrim | Dark | large text | 15.84:1 | 3:1 | 1× |
| `text/primary` | surface/page | Dark | large text | 16.62:1 | 3:1 | 14× |
| `text/primary` | surface/page | Light | large text | 19.23:1 | 3:1 | 14× |
| `text/primary` | glass/field | Light | large text | 19.23:1 | 3:1 | 12× |
| `text/primary` | glass/form | Light | large text | 19.23:1 | 3:1 | 1× |
| `text/static-white` | surface/brand | Light | text | 4.78:1 | 4.5:1 | 13× |
| `text/brand` | surface/page | Light | text | 4.78:1 | 4.5:1 | 4× |
| `text/static-white` | surface/brand | Dark | text | 4.78:1 | 4.5:1 | 13× |
| `text/danger` | surface/page | Light | text | 5.48:1 | 4.5:1 | 3× |
| `text/secondary` | surface/page | Light | text | 5.94:1 | 4.5:1 | 62× |
| `text/placeholder` | glass/field | Light | text | 5.94:1 | 4.5:1 | 2× |
| `text/secondary` | glass/form | Light | text | 5.94:1 | 4.5:1 | 4× |
| `text/warning-strong` | surface/warning-subtle over surface/page | Light | text | 6.28:1 | 4.5:1 | 1× |
| `text/danger-strong` | surface/danger-subtle over surface/page | Light | text | 6.35:1 | 4.5:1 | 2× |
| `text/brand` | surface/page | Dark | text | 6.78:1 | 4.5:1 | 4× |
| `text/secondary` | glass/form over surface/static-scrim | Dark | text | 7.95:1 | 4.5:1 | 4× |
| `text/secondary` | surface/page | Dark | text | 8.34:1 | 4.5:1 | 62× |
| `text/danger` | surface/page | Dark | text | 8.38:1 | 4.5:1 | 3× |
| `text/danger-strong` | surface/danger-subtle over surface/page | Dark | text | 9.82:1 | 4.5:1 | 2× |
| `text/warning-strong` | surface/warning-subtle over surface/page | Dark | text | 10.92:1 | 4.5:1 | 1× |
| `text/placeholder` | glass/field | Dark | text | 12.34:1 | 4.5:1 | 2× |
| `text/primary` | surface/warning-subtle over surface/page | Dark | text | 12.63:1 | 4.5:1 | 1× |
| `text/primary` | surface/danger-subtle over surface/page | Dark | text | 13.96:1 | 4.5:1 | 2× |
| `text/primary` | glass/field | Dark | text | 15.3:1 | 4.5:1 | 3× |
| `text/primary` | glass/control over surface/page | Dark | text | 15.3:1 | 4.5:1 | 4× |
| `text/primary` | glass/form over surface/static-scrim | Dark | text | 15.72:1 | 4.5:1 | 5× |
| `text/primary` | surface/danger-subtle over surface/page | Light | text | 16.49:1 | 4.5:1 | 2× |
| `text/primary` | surface/page | Dark | text | 16.62:1 | 4.5:1 | 40× |
| `text/primary` | surface/warning-subtle over surface/page | Light | text | 17.07:1 | 4.5:1 | 1× |
| `text/primary` | surface/page | Light | text | 19.23:1 | 4.5:1 | 40× |
| `text/primary` | glass/field | Light | text | 19.23:1 | 4.5:1 | 3× |
| `text/primary` | glass/control | Light | text | 19.23:1 | 4.5:1 | 4× |
| `text/primary` | glass/form | Light | text | 19.23:1 | 4.5:1 | 5× |

## Not checked or exempt

- disabled text: 2× — disabled controls are exempt (WCAG 1.4.3)
- text covered by an overlay: 22× — under a scrim or sheet, not readable by design
- Hit areas are measured on component bounds; a larger tappable parent frame, or spacing between small targets, is not seen. Check those by eye.
- Not covered here (judged in `/design-review`): copy, flows, states, focus order, annotations.
