# Rule: trading UX (build to this)

The must-follow parts of `docs/ux/ux-governance.md`, for building screens. The review method, severity and the full rule list live there;
law definitions live in `docs/ux/ux-laws.md` (reviews only: don't walk the laws while building).

| Area | Build rule | ID |
|---|---|---|
| Money values | `num-*` styles, `₹` + Indian grouping, true minus, signed changes with basis and period ("+₹1,240.50 (+1.09%) today"). L/Cr only, never on review/confirmation screens | `TR-NUM-01…04,07` |
| Gain/loss | `market/gain` / `market/loss` **plus** a sign or arrow. Losses get the same size and position as gains | `TR-NUM-01`, `TR-PF-02` |
| Live data | Show freshness (live, delayed, last close, NAV date). Updates never shift layout under the finger | `TR-NUM-05,06` |
| Order flow | Side restated as text (never colour only). Everything that defines the order is visible before submit. Constraints (lot, tick, minimum SIP, band) explained inline before submit | `TR-ORD-01…03` |
| Review step | Every order and money movement has a review step (`D-03`). Extra warnings only for unusual or high-impact orders | `TR-ORD-04` |
| Submit control | Stable footer CTA in the thumb zone, never next to an opposite action; a disabled CTA says why | `TR-ORD-05`, `M-01` |
| After submit | Placed ≠ executed: show status and lifecycle; rejections say why in plain words with a next step | `TR-ORD-06` |
| Defaults | Visible and safe; nothing raises risk or leverage unless the user picks it | `TR-ORD-07`, `TR-RISK-06` |
| Onboarding/KYC | Progress shown, resumable, never asks twice, says *why* for sensitive data | `TR-ACC-02,03` |
| Money movement | Amount, accounts, settle time, charges and a trackable status | `TR-ACC-01` |
| States | Plan and design loading, empty, error, offline and market-closed states for every data surface | `TR-STATE-01,02`, `M-07` |
| Alerts | Critical alerts never look like promotions | `TR-STATE-03` |
| Honesty | No false urgency, nagging, confirm-shaming, celebration of trades, hidden charges or disguised ads. Disclosures readable at the decision point, never shrunk or hidden | `TR-RISK-01…05`, `GOV-08` |
| One primary | One primary action per view; secondary actions visually subordinate | `M-03` |
| Back | Back never silently discards a filled order or form | `M-08` |

If a PRD asks for something that breaks one of these, **stop and raise it** in the plan's open questions. Don't build it quietly, and don't drop it quietly either.
