# UX governance: the rule book for reviewing designs

How we review every Laabh design **before handoff**: screens, flows, components in context and prototypes.
It is the UX layer on top of the build rules in `.claude/rules/` and the docs in `docs/`.

> **Rule zero:** a finding is a *real problem in this design with a consequence for a user*. UX laws explain findings; they never create them.
> If you can't point to the element, the user and the harm, there's no finding, however well a law seems to "fit". Zero findings is a valid result.

Law definitions live in [`ux-laws.md`](ux-laws.md). The accessibility floor lives in [`accessibility.md`](accessibility.md).
This file decides *when* they apply, how serious a problem is, and how to report it.
The `/design-review` skill runs this file and `accessibility.md` together and writes **one** report.

### What this review covers, and what it hands off

| Question | Owner |
|---|---|
| Is the task clear, safe, efficient and honest for this user on this platform? | **This file** |
| Does the design meet WCAG 2.2 AA (every A/AA criterion, annotations)? | [`accessibility.md`](accessibility.md), in the same `/design-review` pass |
| Is every colour, space, radius and text bound to a token? ("0 raw") | `/ds-audit` · [`.claude/rules/tokens.md`](../../.claude/rules/tokens.md) |
| Does this colour pair pass WCAG contrast? (measured) | `/ds-audit` · thresholds in [`.claude/rules/accessibility.md`](../../.claude/rules/accessibility.md) |
| Does the component have the right variants, states and Focus state? | [`docs/components/`](../components/) · `/new-component` |
| Is the copy legally correct, and are mandatory disclosures complete? | Compliance. We govern *presentation*, never *content* (`GOV-08`) |

When a UX finding depends on a measurement owned elsewhere (contrast, token binding), say so and hand it off instead of guessing a number.

---

## 1. The governance rules (how to review without force-fitting)

| ID | Rule | What it means in practice |
|---|---|---|
| `GOV-01` | **Problem first, law second.** | Write the finding as *observed problem → user impact*, then attach the law that explains it. If the sentence still makes sense with the law deleted, it's a real finding. |
| `GOV-02` | **Pass the applicability test.** | Raise a finding only if **all four** are yes: ① a trigger from the law's *Apply when* is visibly present; ② you can name the exact element or step; ③ a realistic user in *this* context would be slowed, confused, misled or put at risk; ④ fixing it would actually change the design. Any "no" → drop it. |
| `GOV-03` | **One law per finding.** | One primary principle, plus at most one supporting ID (usually a `TR-*` or `WCAG` rule). Don't stack three laws that say the same thing (`NH-4` + `SR-1` + `V-REPETITION`). Pick the most precise one. |
| `GOV-04` | **No quotas, no tours.** | Don't walk the catalogue law by law. Walk the user's *task* (§8) and let the problems pick the laws. Never pad the report to look thorough. |
| `GOV-05` | **Context decides.** | The same layout can be right for an active trader and wrong for a first-time investor. State the user segment, platform and stage before judging (§2). |
| `GOV-06` | **Laws trade off; name the trade-off.** | When principles pull in opposite directions (density vs simplicity, speed vs confirmation), say so and resolve it with the priority order in §4. |
| `GOV-07` | **Respect decisions already made.** | Check [`decisions.md`](decisions.md) and the feature's waivers in `prds/<feature>/plan.md`. Don't re-raise something already ruled. If new evidence changes the picture, raise the *evidence*, once. |
| `GOV-08` | **Mandatory content isn't negotiable.** | Never recommend removing, hiding or shrinking a regulatory disclosure, risk warning or required consent. Recommend how to make it *visible and understood at the moment of decision*. |
| `GOV-09` | **Separate evidence from opinion.** | Every finding gets a confidence level (§3). If the outcome depends on data you don't have, label it **Needs research** and say what would settle it. |
| `GOV-10` | **Smallest fix, DS first.** | Recommend the smallest change that removes the problem, using existing DS components and tokens. Propose a new component only when no DS part can do the job, and flag it as a DS gap (`/new-component`). |

---

## 2. Review context (gather before judging)

Get these from the PRD, `plan.md`, the file or the person. If one is unknown **and** it would change the verdict, ask (max 3 questions).
Otherwise use the default and state it under *Assumptions* in the report. `/prd-to-screens` fills this in at step 1 and keeps it in `plan.md`.

| Context | Options | Default if unknown |
|---|---|---|
| Platform | iOS · Android (in scope) · web (not in scope yet, `D-04`) | 390-wide frame → mobile, iOS + Android |
| Surface | See §6 (order, watchlist, portfolio, funds, onboarding…) | From the screen content |
| User segment | First-time investor · regular investor · active trader · derivatives/pro trader | Mobile → mixed, novice-safe |
| Task | What the user is trying to get done on this screen | Infer from the primary CTA, and state it |
| Stage | Exploration · in review · final (pre-handoff) | In review |
| States supplied | Default · loading · empty · error · success · market closed · Dark | Only what's in the file. List missing states as gaps, don't invent them |
| Market state | Pre-open · open · closed · holiday · halted/circuit | Open. Note if other states are missing |

**Stage filter:** at *exploration*, report only `S1`–`S2` and flow-level problems. At *in review* (the first-screen checkpoint in `/prd-to-screens`), report `S1`–`S2`.
At *final* (step 6 of `/prd-to-screens`), report everything, including `S4`.

---

## 3. Severity, confidence and the gate

One scale for UX **and** accessibility findings (`accessibility.md` §9 uses the same levels).

### Severity

| Level | Name | Definition | Gate |
|---|---|---|---|
| `S1` | **Blocker** | Can cause an unintended or wrong order or transfer; is likely to make users misread money (P&L, balance, side, quantity, price) in a way that changes what they do; loses user input in a financial flow; fails WCAG 2.2 A/AA on a core task; is a deceptive pattern (`TR-RISK-*`); hides mandatory information. | Fix before handoff. Can't be waived by design alone. |
| `S2` | **Major** | Significant friction, confusion or error-proneness on a core task; breaks a pattern users learned elsewhere in the product; an accessibility failure on a secondary task; a house-rule shortfall on a primary action. | Fix before release, or waive with a recorded reason (§10). |
| `S3` | **Minor** | Slows or confuses on a non-core path; easy to recover from. | Backlog. Fix when the area is next touched. |
| `S4` | **Polish** | Visual refinement with no measurable effect on the task. | Optional. Final stage only. |

**Escalators (bump one level, up to `S1`):** on the order, order confirmation or funds flow · in a first-run flow (onboarding/KYC, first order, first fund-add) · irreversible · repeats on 3+ screens (systemic).
**De-escalators (drop one level):** rarely used, pro-only surface with an alternative path · a clear recovery already exists on the same screen · the pattern follows a strong market convention (`L-JAKOB`) and the risk comes only from a missing extra cue.

### Confidence

| Level | Meaning |
|---|---|
| **High** | Directly visible in the design, or a clear standard/DS rule is broken. |
| **Medium** | Likely, but depends on context you inferred (segment, frequency). State the assumption. |
| **Needs research** | Depends on behaviour or data you don't have. Say what would settle it. Never `S1` unless the possible harm is financial. |

### Verdict

| Verdict | When |
|---|---|
| **Pass** | No `S1`/`S2` findings. |
| **Pass with fixes** | No `S1`; at least one `S2` with a clear fix. |
| **Changes required** | Any `S1`, or systemic `S2` findings. |

---

## 4. When principles conflict: the priority order

Resolve trade-offs in this order and name the trade-off in the finding (`GOV-06`).

1. **Money safety and correctness**: no unintended order, no misread value, no lost funds.
2. **Accessibility floor**: WCAG 2.2 AA ([`accessibility.md`](accessibility.md)).
3. **Honesty and regulation**: no deceptive patterns; mandatory information is visible (`TR-RISK-*`).
4. **Task success**: the user can finish the task without errors.
5. **Efficiency** for the target segment (speed, density, shortcuts).
6. **Consistency** with the DS and the platform.
7. **Aesthetics.**

### Trade-offs you'll meet often

| Tension | Resolution |
|---|---|
| Density (`V-SPACE`, pro need) vs simplicity (`L-HICK`, `L-COG-LOAD`) | Segment decides. Mobile, mixed users → simple by default, depth behind clear entry points. Never hide anything needed to place a correct order. |
| Speed (`L-DOHERTY`, `NH-7`) vs confirmation (`NH-5`, `WCAG 3.3.4`) | Every order has a review step by default (`D-03`). Extra warnings only for unusual or high-impact orders (`TR-ORD-04`). One-tap modes are opt-in, explained, and off for new users. |
| Convention (`L-JAKOB`) vs a better idea | Keep the convention unless the new pattern is tested and clearly better. Conventions never override accessibility: keep red/green *and* add a sign or arrow. |
| Emphasis (`L-VON-RESTORFF`) vs calm | One primary emphasis per view. Warnings outrank promotions; promotions never outrank the user's task. |
| Engagement vs user interest (`L-BIAS`, `L-PEAK-END`) | User interest wins. Mechanics that push trading frequency or risk are `S1` (`TR-RISK-02`). |

---

## 5. Platform rules

Cite these as the supporting ID alongside a law (`GOV-03`).

### Mobile app (iOS + Android, in scope)

| ID | Rule |
|---|---|
| `M-01` | Primary and frequent actions (Buy/Sell, submit, confirm) sit in the thumb zone (bottom half), in a **stable** position that doesn't shift with content. In our screens: the footer CTA (`.claude/rules/layout.md`). |
| `M-02` | Touch targets ≥ **44×44 pt** (our rule, `.claude/rules/accessibility.md`). On Android, primary actions also reach **48×48 dp** (annotate the hit area, `D-04`). Adjacent targets with **opposite** effects (Buy/Sell, Modify/Cancel) are visibly separated. |
| `M-03` | One primary action per view. Secondary actions are visually subordinate. |
| `M-04` | Every gesture (swipe-to-act, long-press, pull-down, drag) has a **visible** alternative (`WCAG 2.5.7`). Gestures are shortcuts, never the only way. |
| `M-05` | Numeric inputs specify the numeric/decimal keypad; the keypad never covers the submit button or the value being edited. |
| `M-06` | Bottom sheets keep drag-to-dismiss **and** a visible way out: the close control, or a Cancel/decline button in the footer (`D-01`). Dismissing a sheet with unsaved order input asks first, or keeps the draft. |
| `M-07` | Designs show loading, offline and poor-network states for live data and submissions. A dropped connection never leaves an order's status ambiguous. |
| `M-08` | Respect platform navigation and back (iOS swipe-back, Android system back). Back never silently discards a filled order (`docs/patterns/navigation.md`). |
| `M-09` | Layouts survive larger system text without clipping key numbers (prices, P&L, qty): one Dynamic Type step in Figma, and the 200% behaviour annotated (`accessibility.md` A11Y-TXT-01). |
| `M-10` | Screens are designed in portrait, and the app never locks orientation. Core screens carry a landscape reflow rule in the handoff (`D-02`). |

### Web platform: not in scope yet (`D-04`)

Kept so IDs stay stable. Don't raise these until web is in scope.

| ID | Rule |
|---|---|
| `W-01` | Density matched to the segment; every number keeps its label, unit and alignment (`TR-NUM-*`). |
| `W-02` | Frequent actions have keyboard access and, on trader surfaces, discoverable shortcuts; focus order follows visual order. |
| `W-03` | No essential information or action only on hover. |
| `W-04` | Avoid deep cascading hover menus (`L-STEERING`). |
| `W-05` | Long tables keep headers (and key columns) sticky. |
| `W-06` | Multi-panel layouts keep panel positions stable; live updates never move a panel or row under the cursor. |
| `W-07` | Layouts reflow at narrow widths (`WCAG 1.4.10`); only tables and charts may scroll in 2-D. |

### Cross-platform

| ID | Rule |
|---|---|
| `X-01` | **Same meaning, platform-appropriate form.** Terms, colour semantics, icons, status names and order-field order are identical on iOS and Android (and web later). |
| `X-02` | The order flow asks for the same inputs, in the same order, with the same defaults, on every platform. |
| `X-03` | Numbers are formatted identically everywhere ([`docs/patterns/lists-cards.md`](../patterns/lists-cards.md) § Numbers). |
| `X-04` | State carries over where users expect it (watchlists, alerts, drafts, preferences). If something doesn't sync, the UI says so. |

---

## 6. Trading domain rules

Each rule names the law(s) that explain it. Check only the sections for surfaces **present** in the design (`GOV-04`).
"Order" includes stock orders and mutual-fund transactions (lumpsum, SIP, redemption, switch).

### 6.1 Numbers and live data (`TR-NUM`): applies to almost every screen

| ID | Rule | Explained by |
|---|---|---|
| `TR-NUM-01` | Gain/loss and up/down are **never shown by colour alone**: `market/gain` / `market/loss` plus a sign (+/−), an arrow or a label. Exception: shapes that already carry the cue (filled vs hollow candles). | `WCAG 1.4.1`, `V-COLOR` |
| `TR-NUM-02` | Numbers users compare use `num-*` text styles, are right-aligned in columns and stacked rows, and keep a consistent number of decimals per instrument. | `V-ALIGN`, `V-TYPE` |
| `TR-NUM-03` | Every value shows its **basis**: absolute vs %, and the period (today, since buy, 1Y). "+2.3%" with no period is ambiguous. Show `₹` at summary level. | `L-MENTAL-MODEL`, `NH-2` |
| `TR-NUM-04` | Indian grouping (₹1,84,250.75) and Indian abbreviations only (L/Cr, never K/M/B), as in `lists-cards.md`. Never abbreviate on the order review or confirmation, where values must be exact. | `L-CHUNKING`, `X-03` |
| `TR-NUM-05` | Data freshness is visible: live vs delayed vs last close (for funds: NAV date), with a timestamp where it matters. Stale and market-closed states look different from live. | `NH-1` |
| `TR-NUM-06` | Live updates don't move targets: no layout shift or reordering under the user's finger. Price flashes are subtle, brief and ≤ 3 per second. | `L-FITTS`, `L-COMMON-FATE`, `WCAG 2.3.1` |
| `TR-NUM-07` | One sign convention for negatives: the true minus (−0.42%, `lists-cards.md`). No accounting parentheses. | `NH-4` |

### 6.2 Orders (`TR-ORD`): the highest-risk surface

| ID | Rule | Explained by |
|---|---|---|
| `TR-ORD-01` | **Buy vs Sell is unmistakable by more than colour**: text label, a consistent position, and the order header restating the side. | `WCAG 1.4.1`, `L-SIMILARITY` |
| `TR-ORD-02` | Before submitting, the user sees everything that defines the order: instrument (exchange, segment; expiry/strike/type for derivatives; plan and option for funds), side, qty or amount, order type, price/trigger, product type, validity, and estimated value / margin (and charges where available). | `WCAG 3.3.4`, `DN-GULFS` |
| `TR-ORD-03` | **Prevent errors rather than report them**: constrain inputs (lot multiples, tick size, price band, minimum SIP amount) inline, before submit, explain the constraint, and accept reasonable formats. | `DN-CONSTRAINTS`, `NH-5`, `L-POSTEL` |
| `TR-ORD-04` | **Review step on every order (house rule, `D-03`)**, off only if the user turns it off in settings. On top of that, confirm in proportion to risk: extra warnings only for unusual or high-impact orders (market order in an illiquid contract, price far from LTP, qty well above usual, margin shortfall). Don't add a second "are you sure?" dialog to every order (`MYTH-9`). | `NH-5`, `WCAG 3.3.4` |
| `TR-ORD-05` | The submit control is stable, in reach (`M-01`), never directly next to an opposite action, and when disabled it **says why** ("Insufficient balance: add ₹X"). | `L-FITTS`, `DN-FEEDBACK` |
| `TR-ORD-06` | After submit, **placed ≠ executed**. Show the lifecycle (placed → open → partially filled → executed / rejected / cancelled; for funds: submitted → NAV allotted → units credited). Rejections explain the reason in plain language, with a next step. | `NH-1`, `NH-9`, `SR-4` |
| `TR-ORD-07` | Defaults are **explicit and safe**: the default order type, product and plan are visible, and no default raises risk or leverage without the user choosing it. | `L-BIAS` (default effect), `SR-7` |
| `TR-ORD-08` | Modify and cancel are easy to find from the order status and the Orders tab. | `NH-3`, `SR-6` |
| `TR-ORD-09` | A filled order survives interruptions (app switch, timeout, re-login, back), or the user is warned before it's lost. | `L-WORKING-MEMORY`, `WCAG 2.2.1`, `WCAG 3.3.7` |

### 6.3 Portfolio, positions and P&L (`TR-PF`)

| ID | Rule | Explained by |
|---|---|---|
| `TR-PF-01` | Labels clearly separate **day's P&L vs total P&L**, **realised vs unrealised**, **invested vs current value**, and **holdings vs positions**. | `L-MENTAL-MODEL`, `DN-CONCEPTUAL` |
| `TR-PF-02` | Losses get the same prominence as gains: same text style and position, never hidden in smaller text or behind taps. | `TR-RISK-03`, `V-HIERARCHY` |
| `TR-PF-03` | The view leads with what the user checks most (current value, total and day's P&L), then the breakdown. | `V-HIERARCHY` |

### 6.4 Charts, depth and option chain (`TR-MKT`)

| ID | Rule | Explained by |
|---|---|---|
| `TR-MKT-01` | Charts show the instrument, time range, interval and axis values. The crosshair readout is legible and doesn't hide the point it reads. | `NH-1`, `V-TYPE` |
| `TR-MKT-02` | Chart gestures (pinch, pan, long-press) have visible alternatives such as range chips and zoom buttons. | `WCAG 2.5.7`, `M-04` |
| `TR-MKT-03` | The option chain follows the market convention (calls one side, puts the other, strike in the centre). ATM row and ITM shading are marked and explained in a legend. | `L-JAKOB`, `WCAG 1.4.1` |
| `TR-MKT-04` | Market depth groups bids and asks clearly, labels each column and keeps alignment while values update. | `L-COMMON-REGION`, `TR-NUM-06` |

### 6.5 Watchlist, search and discovery (`TR-DISC`)

| ID | Rule | Explained by |
|---|---|---|
| `TR-DISC-01` | Search accepts symbol, company name and partial input, and tells apart instruments that look the same (exchange, series, expiry, fund plan). | `L-POSTEL`, `L-PRAGNANZ` |
| `TR-DISC-02` | Swipe/long-press row actions have visible alternatives; destructive ones (remove from watchlist) can be undone. | `M-04`, `SR-6` |
| `TR-DISC-03` | Large sets (funds, screeners) offer sort, filters and a sensible default view instead of an unstructured list. | `L-CHOICE-OVERLOAD` |
| `TR-DISC-04` | Sponsored or promoted items are clearly labelled and never styled as neutral rankings or recommendations. | `TR-RISK-01` |

### 6.6 Funds, onboarding and account (`TR-ACC`)

| ID | Rule | Explained by |
|---|---|---|
| `TR-ACC-01` | Add/withdraw money shows the amount, source/destination account, expected time to settle, any charges, and a status the user can track. | `WCAG 3.3.4`, `NH-1` |
| `TR-ACC-02` | Multi-step onboarding/KYC shows progress (Top Bar stages), can be saved and resumed, and never asks twice for data already given. | `L-GOAL-GRADIENT`, `L-ZEIGARNIK`, `WCAG 3.3.7` |
| `TR-ACC-03` | Sensitive requests (documents, bank, nominee, income) say *why* they're needed, at the point of asking (the Step Heading description). | `L-MENTAL-MODEL`, `NH-10` |
| `TR-ACC-04` | Login and OTP allow paste, OS one-time-code autofill, password managers and biometrics (OTP Input: "paste fills all cells"). | `WCAG 3.3.8`, `L-POSTEL` |

### 6.7 Market states and system states (`TR-STATE`)

| ID | Rule | Explained by |
|---|---|---|
| `TR-STATE-01` | The design shows the market state (pre-open, open, closed, holiday, halted/circuit) and what an action *means* in that state (an after-market order runs at next open; a fund order after cut-off gets the next day's NAV). | `NH-1`, `DN-GULFS` |
| `TR-STATE-02` | Every data surface has defined loading, empty, error and partial-data states. Ask for missing ones; don't assume them. | `NH-1`, `NH-9` |
| `TR-STATE-03` | Critical alerts (margin call, order rejected, auto square-off) look and sound different from promotional notifications, and are never grouped with them. | `L-SELECTIVE-ATTENTION`, `L-VON-RESTORFF` |

### 6.8 Responsible design and deceptive patterns (`TR-RISK`)

Any of these is `S1`. India's CCPA *Guidelines for Prevention and Regulation of Dark Patterns, 2023* list 13 such practices
(false urgency, confirm shaming, interface interference, drip pricing, disguised advertisement, nagging, trick questions and others).
Securities regulators also scrutinise trading-app engagement features.

| ID | Rule |
|---|---|
| `TR-RISK-01` | **No false urgency, nagging, confirm-shaming, trick questions or disguised ads.** Timers, "only X left", repeated prompts to trade, guilt-trip decline copy ("No, I don't want profits") and ads styled as research are out. |
| `TR-RISK-02` | **No gamification of trading.** No confetti or celebration on order placement, no streaks or rewards for trading frequency, no slot-machine-like refresh. Celebrating learning or finishing KYC is fine; celebrating risk-taking isn't. |
| `TR-RISK-03` | **No interface interference.** Charges, risks, losses and the "no"/cancel option get honest visual weight, never de-emphasised against the profitable or engaging choice. |
| `TR-RISK-04` | **No drip pricing.** Brokerage, taxes, exit loads and charges are visible before the user commits. |
| `TR-RISK-05` | **Risk disclosures are visible at the moment of decision**, readable (not `text/tertiary` or `caption` for essential content), and not designed to be dismissed blindly. Wording is compliance's call (`GOV-08`). |
| `TR-RISK-06` | **Leverage and higher-risk products are opt-in.** F&O activation, margin trading and one-tap order modes are deliberate choices with plain-language explanations, never pre-selected. |

---

## 7. What a good finding looks like

If you can't fill **Where**, **What's wrong** and **Why it matters** concretely, delete the finding (`GOV-02`).

| Field (report label) | Content |
|---|---|
| **Where** | Screen/frame name + element (and the Figma node id if available). |
| **What's wrong** (problem) | What you see, stated as fact. |
| **Why it matters** (impact) | Who is affected and what goes wrong (mis-tap, misread, abandonment, loss). |
| **Fix** (recommendation) | The smallest fix, using DS components and tokens (`GOV-10`). Name the trade-off if there is one. |
| **Rule** (principle) | One primary ID (`L-*`, `V-*`, `DN-*`, `NH-*`, `SR-*`, `WCAG *`, `A11Y-*`) + optionally one `TR-*`/`M-*`/`X-*`. |
| **How serious · How sure** | `S1`–`S4` as a word (§9) · High / Medium / Needs research. |

### Worked example: one raised, three rejected

*Design:* mobile order sheet for an equity stock. Buy/Sell is a Segmented Control at the top, green and red. Qty stepper. Price field.
"Place order" at the bottom. A 20-row watchlist sits behind the sheet.

**Raised:**

> **DR-01 · Buy or Sell is shown by colour only · 🔴 Must fix (S1)**
> - **Where:** Order sheet › side Segmented Control and the "Place order" button.
> - **What's wrong:** The selected side is shown only by the segment's fill colour. The submit button reads "Place order" for both sides, and its colour is the only cue.
> - **Why it matters:** A user with red–green colour-vision deficiency, or one glancing in bright sunlight, can submit the opposite side. That's a wrong order with real money.
> - **Fix:** Label the button with the side ("Buy 10 INFY"), restate the side in the sheet title, keep the segment labels as text. Keep the Success/Danger button tones as a second cue.
> - **Rule:** `WCAG 1.4.1` · `TR-ORD-01`
> - **How sure:** High

**Considered and rejected (so you can see the test working):**
- *"Watchlist has 20 rows, which breaks Miller's Law."* → Rejected. Rows are scanned, not memorised (`MYTH-2`); tests ② and ③ fail.
- *"Order types violate Hick's Law."* → Rejected. Only Market/Limit are shown and the user picks one known option. No trigger (test ①).
- *"Use the golden ratio for the sheet height."* → Rejected. Not a usability law (`MYTH-3`). Sheets follow `docs/patterns/overlays.md` (≤ 70% height).

---

## 8. The review procedure

1. **Load context.** Read this file, [`ux-laws.md`](ux-laws.md), [`accessibility.md`](accessibility.md), the vocabulary in [`docs/content/voice.md`](../content/voice.md),
   [`decisions.md`](decisions.md) and the feature's `plan.md`. Fill in §2. Ask only questions that change the verdict.
2. **Look at everything supplied.** Every frame and state, Light **and** Dark. List the states that are **missing** (`TR-STATE-02`). Don't review states you haven't seen.
   - **Content realism:** if placeholder numbers don't add up (P&L ≠ current − invested), note it once under *Assumptions* and ask for realistic data.
     Picture the worst case too: the longest instrument or fund name, the largest value in Indian format, negatives, zero, empty.
3. **Walk the task, not the catalogue.** For the main task on each screen: *What does the user need to see? What do they do? What could go wrong? How do they know it worked?*
4. **Check the surfaces present.** Run only the `TR-*` sections for surfaces in the design (§6), the mobile rules (§5), and the triggered accessibility criteria (`accessibility.md` §5.0).
5. **Explain each candidate.** Find the single best-fitting principle in `ux-laws.md` (read its *Don't cite when*). Run the applicability test (`GOV-02`). Drop anything that fails.
6. **Rate and merge.** Assign severity and confidence (§3). Merge duplicates. A problem on several screens is reported **once** as systemic, listing where.
7. **Self-check before reporting** (all must hold):
   - [ ] Every finding names a specific element and a specific user impact.
   - [ ] Every cited ID exists in `docs/ux/`, and the law's *Apply when* trigger is really present.
   - [ ] No finding cites a `MYTH-*` as its reason.
   - [ ] At most one primary + one supporting ID per finding; no duplicates.
   - [ ] Nothing contradicts a logged decision or waiver (`GOV-07`).
   - [ ] No recommendation removes or hides mandatory content (`GOV-08`).
   - [ ] Every number quoted (size, contrast, spacing) was measured; otherwise it's marked *to verify* and handed to `/ds-audit`.
   - [ ] Recommendations use DS components and tokens; anything new is flagged as a DS gap.
   - [ ] Anything that can cause a wrong order or a misread of money is `S1`.
8. **Report** using §9 and save it to `prds/<feature>/review.md` (newest review on top). Stay read-only: don't edit the design unless the person asks.

---

## 9. Report template (one report for UX + accessibility)

Written for the whole team, not just reviewers: someone who opens it should know in **ten seconds** whether the design is ready, what's wrong, and who fixes it.
Plain words first, rule IDs last. Severity is shown as a word and a colour, with the S-level in brackets:

| Level | In the report | Means |
|---|---|---|
| `S1` | 🔴 Must fix (S1) | Fix before handoff |
| `S2` | 🟠 Should fix (S2) | Fix before release, or waive with a reason |
| `S3` | 🟡 Small fix (S3) | Fix when the screen is next touched |
| `S4` | ⚪ Polish (S4) | Optional |

| Verdict (§3) | In the report |
|---|---|
| Changes required | ❌ Not ready for handoff |
| Pass with fixes | ⚠️ Ready after fixes |
| Pass | ✅ Ready for handoff |

```markdown
# Design review: <screen / flow>
**Result:** <❌ Not ready for handoff | ⚠️ Ready after fixes | ✅ Ready for handoff>. <one plain sentence: why, and who it's waiting on>
**Checked:** <which screens, Light + Dark> · <date> · <stage in words: first-screen check | final check before handoff>
**Open problems:** 🔴 Must fix: <n> · 🟠 Should fix: <n> · 🟡 Small fix: <n> · ⚪ Polish: <n>

## At a glance
| # | Problem | Where | How serious | Fix | Who | Status |
|---|---|---|---|---|---|---|
| DR-01 | <the problem in plain words> | <screens> | 🔴 Must fix | <the fix in a few words> | <Designer / DS owner / Product> | Open |

## What to do next
1. <the next action, who does it>

## Details
### DR-01 · <the problem in plain words> · 🔴 Must fix (S1)
- **Where:** <screen + element (+ node ID); "every screen with X" for a problem on 3+ screens>
- **What's wrong:** <what you see, as a fact>
- **Why it matters:** <who is affected and what goes wrong for them>
- **Fix:** <the smallest fix with DS components and tokens; the trade-off, if any>
- **Rule:** <primary ID> · <optional supporting ID>
- **How sure:** <High | Medium | Needs research>
- **Status:** <Open | Fixed (date)>

## Questions for the team
- <question> (<who decides>)

## Missing screens or states
- <state> (<screen>)

## Good things
- <max 3, specific>

## Checked and fine
- <one line each, only for items someone might expect, naming the exception>

## Notes for the team
- **Annotations missing:** <AN-xx on which screen, or "none">
- **Measured by /ds-audit:** <what, or "to measure: …">
- **Design-system gaps:** <for /new-component, or "none">
- **Needs research:** <question → what would settle it, or "none">
- **About this review:** platform, user segment, task walked, assumptions
```

- Number findings `DR-01`, `DR-02`… most serious first. A problem on 3+ screens is **one** finding whose *Where* lists the screens.
- **Open problems** counts only findings whose *Status* isn't *Fixed*; the result follows those (§3). Fixed findings stay in the report, marked ✅ in the table.
- Keep each detail field to one or two sentences. Use the words the team uses, not the law's name. No "laws checked" list.
- `scripts/review-check.py` checks this format (and still reads older reports).

---

## 10. Waivers and keeping this rule book healthy

- **Waivers.** An `S2`–`S4` finding the team decides to keep is logged with date · finding · why · decided by:
  feature-only waivers in `prds/<feature>/plan.md` (Decisions & waivers), product-wide rulings in [`decisions.md`](decisions.md).
  `S1` findings can't be waived by design alone; they need product and compliance sign-off, recorded the same way.
- **Don't re-raise waived items** (`GOV-07`) unless the design around them changes.
- **New rules.** When the same finding comes up in three or more reviews, consider promoting it to a `TR-*` rule here. Add the date; never renumber, only add or mark *retired*.
- **Overruled rules.** Edit the rule in place and note why. Don't keep two contradictory rules.
- **No token values here.** Values live in `tokens/` and `docs/foundations/`; this file names tokens by role only.
- Changes to `docs/ux/` go through a PR with DS-owner review (`docs/process/governance.md`).
