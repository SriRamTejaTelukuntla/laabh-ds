# Rule: accessibility (WCAG 2.2 AA)

Build to this while designing. Check in **both** Light and Dark. Full reference and review method: `docs/ux/accessibility.md`.

| Check | Requirement |
|---|---|
| Body text contrast | ≥ 4.5:1 against its actual background (glass fills: measure on the composited colour) |
| Large text (≥ 24px regular / ≥ 19px bold) and UI parts (borders of inputs, icons that carry meaning, focus ring) | ≥ 3:1 |
| Hit targets | ≥ 44×44 pt (an icon can be smaller if its tappable frame is 44). Android primary actions: annotate a 48×48 dp hit area (`D-04`) |
| Colour alone | Never the only signal. Gain/loss always pairs colour with a sign (+/−) or an arrow; errors pair red with an icon and text |
| Focus | Interactive components keep their `Focus` state; use `focus/ring`. Tappable compositions (rows, chips) need one too |
| Text size | Minimum 11 (see the typography rule). Layouts must survive one Dynamic Type step larger without clipping; annotate the 200% behaviour (`AN-15`) |
| Orientation | Design portrait; never lock it. Core screens get a landscape reflow note (`D-02`) |
| Disabled | Disabled states can be low-contrast but must still read as disabled *and* be identifiable from the label |
| Motion | Respect reduced motion in prototypes; nothing auto-plays essential information; nothing flashes more than 3 times a second |

**While building, every screen also needs:**
- Fields with a persistent label (never placeholder-only); errors in text that say how to fix it (`docs/patterns/forms.md`).
- A tap route for every gesture (swipe, drag, pinch). Sheets: drag-to-dismiss **and** a close or Cancel (`D-01`).
- OTP and login fields that accept paste and autofill (annotate it), or a biometric alternative.
- Timers (session, resend, quote validity) that warn and can be extended, or a named exception.
- Auto-moving content (tickers, carousels) that can be paused.
- Handoff annotations `AN-01…AN-15` where triggered (`docs/ux/accessibility.md` §8): names for icon-only buttons, reading/focus order, live regions, hit areas.

- Text tokens `text/disabled`, `text/placeholder` and `text/tertiary` are **not** for essential content.
- `/ds-audit` reports contrast failures it can compute. Fix them by choosing a different semantic token, not by editing values.
- Don't walk WCAG criterion by criterion while building. The review (`/design-review`) does that, using the trigger index.
