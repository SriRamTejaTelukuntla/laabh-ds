# UX decisions and rulings

Product-wide decisions that the UX and accessibility rules depend on, and rulings that stop a finding from being raised again (`GOV-07`).
`/design-review` reads this file before every review. Feature-only waivers go in `prds/<feature>/plan.md` under **Decisions & waivers**.

- IDs are stable: never renumber. To change a decision, edit it in place and add the date and reason; to drop it, mark it *retired*.
- `S1` findings can't be waived by design alone: they need product and compliance sign-off, recorded here.

## Decisions

| ID | Date | Decision | Why | Decided by | Rules affected |
|---|---|---|---|---|---|
| `D-01` | 2026-10-19 | **Sheet close.** Every Bottom Sheet keeps drag-to-dismiss and a visible way out. The close (X) may be hidden only when the footer already has a clear exit (Cancel, or a decline such as "I'll type them myself"). | A blocking consent sheet still needs an exit for keyboard and screen-reader users. | Product designer | `M-06`, `A11Y-FOC-02`, `docs/components/bottom-sheet.md` |
| `D-02` | 2026-10-19 | **Orientation.** Design portrait frames only. The app never locks orientation; core screens (orders, money, KYC) carry a landscape reflow rule in the handoff (`AN-15`). No landscape frames. | WCAG 1.3.4 (AA) fails on a locked orientation; a written rule covers it without doubling the frames. | Product designer | `M-10`, `A11Y-LAY-03`, `A11Y-LAY-04` |
| `D-03` | 2026-10-19 | **Order review step.** Every order submission (stock order, SIP, lumpsum, redemption, switch, add/withdraw money) has a review step by default. One-tap mode is opt-in, explained, and off for new users. Extra warnings only for unusual or high-impact orders. | WCAG 3.3.4 needs Checked or Confirmed; we choose Confirmed by default to prevent wrong orders. | Product designer | `TR-ORD-04`, `A11Y-ERR-03`, `MYTH-9` |
| `D-04` | 2026-10-19 | **Platforms.** iOS and Android are in scope; web is not yet. Touch targets: 44×44 pt everywhere (our rule); Android primary actions also reach 48×48 dp via an annotated hit area. Web rules (`W-*`) and web-only criteria are kept but not raised. | Matches the 390×844 canvas and the current product. | Product designer | `M-02`, `W-*`, `A11Y-TGT-01`, `accessibility.md` §7.1 |

## Rulings ("essential", exceptions, waivers)

| ID | Date | Finding or criterion | Ruling | Scope | Decided by |
|---|---|---|---|---|---|
| — | | | | | |

## Open (needs a decision; reviews raise these as Questions)

| Topic | Question | Raised by |
|---|---|---|
| Live prices (`A11Y-LIV-01`) | Are live prices on Watchlist, Explore and Portfolio essential, or do they need a pause / refresh-rate setting? (LTP on the order itself is treated as essential.) | `accessibility.md` §5.10 |
| Vocabulary (`NH-4`, `A11Y-CPY-09`) | One term per concept (e.g. "Exit" vs "Square off", "Funds" vs "Wallet"): fill in `docs/content/voice.md` § Vocabulary. | `ux-governance.md` §8 |
| Toast (`A11Y-LIV-02`) | Toasts aren't in the DS yet. What carries transient confirmations, and how is it announced? | `docs/patterns/overlays.md` |
