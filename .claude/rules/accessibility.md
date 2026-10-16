# Rule: accessibility (WCAG 2.2 AA)

Check in **both** Light and Dark.

| Check | Requirement |
|---|---|
| Body text contrast | ≥ 4.5:1 against its actual background (glass fills: measure on the composited colour) |
| Large text (≥ 24px regular / ≥ 19px bold) and UI parts (borders of inputs, icons that carry meaning, focus ring) | ≥ 3:1 |
| Hit targets | ≥ 44×44 pt (an icon can be smaller if its tappable frame is 44) |
| Colour alone | Never the only signal. Gain/loss always pairs colour with a sign (+/−) or an arrow; errors pair red with an icon and text |
| Focus | Interactive components keep their `Focus` state; use `focus/ring` |
| Text size | Minimum 11 (see the typography rule). Layouts must survive one Dynamic Type step larger without clipping |
| Disabled | Disabled states can be low-contrast but must still read as disabled *and* be identifiable from the label |
| Motion | Respect reduced motion in prototypes; nothing auto-plays essential information |

- Text tokens `text/disabled`, `text/placeholder` and `text/tertiary` are **not** for essential content.
- `/ds-audit` reports contrast failures it can compute. Fix them by choosing a different semantic token, not by editing values.
