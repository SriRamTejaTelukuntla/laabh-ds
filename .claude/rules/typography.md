# Rule: typography

- Every text node uses a text style: `<role>/<Regular|Medium|Semibold|Bold>`.
- **Numbers** (prices, %, quantities, P&L, OTP digits, counts) use `num-<role>/<Regular|Medium|Bold>` (Space Grotesk). Labels around numbers stay Inter.
- `caps-*` styles are uppercase with 8% tracking. Use them for overlines and section labels only, never for sentences.
- **Titles are Space Grotesk Bold:** `display-md/Semibold` (screen titles) and `display-xl/Semibold` (hero titles) render in Space Grotesk Bold by design (decided 16 Oct 2026), despite the "Semibold" in the name. Other display weights stay Inter.
- `mono/Regular` (JetBrains Mono 11/14) is for DS documentation only (token names, values). Never use it in product screens.
- Sizes come from Typography Tokens in **Mobile** mode for phone screens.

| Role | Size / line height (Mobile) | Typical use |
|---|---|---|
| display-2xl | 40 / 48 | Hero numbers (portfolio value) |
| display-xl | 32 / 40 | Screen hero titles |
| display-lg | 28 / 36 | Large section heroes (available, use sparingly) |
| display-md | 24 / 30 | Screen titles |
| display-sm | 20 / 26 | Card hero values, sheet titles |
| label-lg | 16 / 22 | Buttons lg/xl, list titles |
| label-md | 14 / 18 | Buttons sm/md, field labels |
| body-lg | 14 / 20 | Default reading text |
| body-md | 14 / 18 | Compact body: dense lists, secondary copy |
| body-sm | 12 / 16 | Helper text, meta |
| caps-lg / caps-md | 12 / 11 | Overlines, section labels, tags |
| caps-sm | 10 / 14 | **Exception:** dense data badges only, never for reading text |
| caption | 11 / 14 | Fine print, chart axes |

**Scale: even sizes, minimum 11.** The only exception is `caps-sm` (10) for dense data badges.
When a size falls between steps, round **down** to the nearest role.
Tablet matches Mobile except for the display roles. Desktop sizes (with some odd values) are not in use yet; don't design for Desktop until it's in scope.
