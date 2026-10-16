# Rule: tokens only

Applies to every node you create or edit in Figma.

| Property | Bind to | Never |
|---|---|---|
| Fill / stroke colour | `Color Tokens` semantic variable (`surface/*`, `text/*`, `icon/*`, `border/*`, `glass/*`, `market/*`, `data/*`) | Raw hex, or a `Color Primitives` variable directly |
| Corner radius | `radius/*` | Typed numbers |
| Padding, gap | `space/*` | Typed numbers |
| Text | A text style (`<role>/<weight>`, `num-<role>/<weight>`) | Local font settings |
| Shadow, blur, highlight | An `elevation/*` effect style | Hand-made effects |

- Primitives (`blue/400`, `alpha/frost-06`, ...) exist only to feed semantic tokens. If no semantic token fits, **stop and ask**. A new token goes through `/new-component` or a DS-owner request.
- Pick tokens by role, not by looks: text on a card is `text/primary`, not "whatever is dark".
- Gain/loss always uses `market/gain` / `market/loss` (and `*-subtle`, `surface/gain-tint`, `surface/loss-tint`). Never `success` or `danger`.
- Corner smoothing is **0.6** on every rounded rectangle.
- Space scale: 0 2 3 4 6 8 10 12 14 16 18 20 22 24 28 32 34 36 40 48 52. Radius: 0 2 4 6 8 9 10 12 14 16 18 20 24 28 40 full.
- If the value you need is not on the scale, you are probably off-pattern. Check `docs/patterns/` before asking for a new token.
- Exact names and values: `docs/foundations/` or `tokens/*.json`.
