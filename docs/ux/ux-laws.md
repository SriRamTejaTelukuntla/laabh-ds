# UX laws catalogue: what each law says, and when to cite it

The reference library behind [`ux-governance.md`](ux-governance.md): UX laws, Gestalt principles, visual design principles, HCI laws,
and the classic heuristic sets (Nielsen, Shneiderman, Norman), written for Laabh (investing and trading on mobile).

> **Read `ux-governance.md` first.** This file tells you what a law means. The governance file tells you *whether a finding exists at all*.
> A law is never the reason for a finding. The reason is an observed problem with a user consequence; the law only explains it (`GOV-01`).
> This file is for **reviews**. Don't walk it while building screens; the build rules are in `.claude/rules/`.

---

## How to read an entry

| Field | Meaning |
|---|---|
| **Says** | The law in one or two plain sentences. |
| **Apply when** | Triggers you can actually see in the design. If none are present, the law isn't relevant to this screen. |
| **Don't cite when** | Situations where the law looks relevant but isn't, or where citing it would push the design the wrong way. |
| **In trading** | Where it bites in an investing/trading app. |
| **Check** | What to look at or measure. |

### ID scheme (used across `docs/ux/`)

| Prefix | What | Defined in |
|---|---|---|
| `GOV-nn` | Governance rules (how to review) | `ux-governance.md` §1 |
| `M-nn` · `W-nn` · `X-nn` | Mobile · web (not in scope yet) · cross-platform rules | `ux-governance.md` §5 |
| `TR-AREA-nn` | Trading domain rules | `ux-governance.md` §6 |
| `D-nn` | Product decisions and rulings | `decisions.md` |
| `L-NAME` | Laws and principles (Gestalt, cognition, decision, HCI) | this file §1–§4 |
| `V-NAME` | Visual design principles | this file §5 |
| `DN-NAME` · `NH-n` · `SR-n` | Norman's principles · Nielsen's heuristics · Shneiderman's rules | this file §6 |
| `WCAG x.y.z` · `A11Y-*` | WCAG 2.2 success criteria (the accessibility floor) | this file §7 · `accessibility.md` |
| `MYTH-n` | Misapplications. Never cite these as rules. | this file §8 |

### Quick selector: where to start looking (starting points, not a checklist)

| Surface | Laws that most often explain real problems here |
|---|---|
| Order (stock order, SIP, lumpsum, redemption) | `L-FITTS`, `DN-CONSTRAINTS`, `NH-5`, `L-PROXIMITY`, `L-DOHERTY`, `WCAG 3.3.4` |
| Order status / confirmation | `NH-1`, `DN-FEEDBACK`, `L-PEAK-END`, `SR-4` |
| Watchlist / market lists | `L-SIMILARITY`, `L-COMMON-FATE`, `V-TYPE`, `L-JAKOB` |
| Portfolio / P&L | `V-HIERARCHY`, `L-MENTAL-MODEL`, `V-COLOR`, `WCAG 1.4.1` |
| Charts | `L-PRAGNANZ`, `DN-MAPPING`, `WCAG 2.5.7`, `L-JAKOB` |
| Option chain / market depth | `L-JAKOB`, `V-ALIGN`, `L-COMMON-REGION`, `SR-2` |
| Onboarding / KYC | `L-GOAL-GRADIENT`, `L-ZEIGARNIK`, `L-COG-LOAD`, `WCAG 3.3.7`, `WCAG 3.3.8` |
| Add / withdraw money | `NH-5`, `NH-1`, `L-MENTAL-MODEL`, `WCAG 3.3.4` |
| Discovery (funds, stocks, collections) | `L-CHOICE-OVERLOAD`, `L-HICK`, `L-SERIAL-POSITION`, `L-POSTEL` |
| Alerts / notifications | `L-SELECTIVE-ATTENTION`, `L-VON-RESTORFF`, `NH-8` |

If a law in this table doesn't match an actual problem you can see, skip it.

---

## 1. Perception and visual organisation (Gestalt)

### L-PROXIMITY · Law of Proximity
- **Says:** Things that are close together are seen as belonging together.
- **Apply when:** a label sits as close to the wrong value as to its own; spacing between groups is equal to or smaller than spacing inside groups; an action sits closer to an unrelated item than to the one it acts on.
- **Don't cite when:** grouping is already clear from cards or hairlines and the spacing only looks uneven in a crop. Uniform spacing in a dense list is fine; rows do the grouping there.
- **In trading:** order fields (qty / price / trigger), P&L label–value pairs, a row's action icons drifting toward the next row.
- **Check:** inner spacing is visibly smaller than outer spacing, using the spacing table in `.claude/rules/layout.md`.

### L-SIMILARITY · Law of Similarity
- **Says:** Elements that look alike are seen as related, or as doing the same thing.
- **Apply when:** things with different functions share a style (a non-tappable Badge styled like a chip button), or things with the same function look different on different screens.
- **Don't cite when:** the visual difference is intentional and carries meaning, like selected vs unselected.
- **In trading:** `market/*` colours used for non-price text; "Buy" styled differently on the stock page vs the order sheet; segment tags (NSE/BSE, EQ/F&O) looking tappable.
- **Check:** same component and token for the same function everywhere (`docs/components/`).

### L-COMMON-REGION · Law of Common Region
- **Says:** Elements inside a shared boundary (card, panel, background) are seen as a group.
- **Apply when:** related items are split across cards, unrelated items share one, or there are so many nested cards that grouping stops meaning anything ("card soup").
- **Don't cite when:** proximity and alignment already group things clearly; another container only adds noise.
- **In trading:** option-strategy legs, a position and its exit actions, market-depth bid vs ask sides.
- **Check:** at most two levels of nested containers; inner cards get no shadow (`.claude/rules/light-dark.md`).

### L-UNIFORM-CONNECTEDNESS · Law of Uniform Connectedness
- **Says:** Elements joined by a line, colour band or frame are seen as more related than unconnected ones.
- **Apply when:** a sequence (steps, timeline, legs) needs to read as one unit and doesn't; or a connecting line wrongly suggests a relationship.
- **Don't cite when:** the items aren't actually related.
- **In trading:** order lifecycle (placed → open → executed), KYC stages in the Top Bar, the account-setup Timeline.

### L-PRAGNANZ · Law of Prägnanz (simplicity)
- **Says:** People read complex or ambiguous visuals in their simplest possible form.
- **Apply when:** an icon, chart or illustration is ambiguous or overloaded, so users "simplify" it into the wrong meaning.
- **Don't cite when:** the complexity is real domain content (a candlestick chart with indicators the user switched on).
- **In trading:** custom icons for order types, overlapping chart overlays, decorative graphs that look like real price charts.

### L-FIGURE-GROUND · Figure–Ground
- **Says:** People separate a scene into foreground and background. If that split is unclear, attention and interaction suffer.
- **Apply when:** a sheet or popover doesn't clearly sit above the page (no scrim, weak elevation), or the background looks active.
- **Don't cite when:** a non-modal panel is meant to coexist with the page.
- **In trading:** an order sheet over a live chart; tooltips over dense lists.
- **Check:** overlays use `Sheet Scrim` + `elevation/sheet` or `elevation/overlay` ([`docs/foundations/elevation.md`](../foundations/elevation.md)).

### L-COMMON-FATE · Common Fate
- **Says:** Elements that move or change together are seen as a group, and motion grabs attention.
- **Apply when:** live updates (price flashes, tickers, reorders) pull attention away from the user's task, or animate unrelated items together.
- **Don't cite when:** the motion is a single, brief, user-triggered transition.
- **In trading:** flashing LTP cells, auto-sorting gainers lists, scrolling tickers above an order form.
- **Check:** `TR-NUM-06`. Flashes are subtle, short, never more than 3 per second (`WCAG 2.3.1`).

---

## 2. Cognition, memory and attention

### L-COG-LOAD · Cognitive Load
- **Says:** Every interface costs mental effort. *Intrinsic* load comes from the task; *extraneous* load comes from the design. Cut the extraneous load.
- **Apply when:** decoration, jargon, duplicated info, unexplained abbreviations or mode switches make a task harder than it has to be.
- **Don't cite when:** the effort is intrinsic (options Greeks for a derivatives trader). Support it (Tooltip, defaults), but you can't remove it. See `L-TESLER`.
- **In trading:** "MIS/CNC/NRML" or "XIRR" with no plain-language label for novices; margin maths left to the user.

### L-MILLER · Miller's Law
- **Says:** People can hold only a handful of items in short-term memory. Miller (1956) said roughly 7 ± 2; later research (Cowan) puts it nearer 4.
- **Apply when:** the user has to *remember* something from one view to use in another (an order ID, a price, a margin figure, an OTP).
- **Don't cite when:** items are visible and scanned rather than memorised. It does **not** cap menu items, tabs or list rows at 7 (`MYTH-2`).
- **In trading:** carrying LTP into the price field from memory; reading a bank account number off one screen to type on another.
- **Check:** information needed to finish a step is visible during that step.

### L-WORKING-MEMORY · Working Memory
- **Says:** The mental "scratchpad" is small and fades fast, especially under stress or interruption.
- **Apply when:** a flow is interrupted (app switch for OTP, UPI or DigiLocker, a timeout) and the user has to rebuild context.
- **Don't cite when:** it adds nothing beyond `L-MILLER`. Pick one.
- **In trading:** returning from a UPI app to a blank Add money screen; a re-login that clears a filled order.

### L-CHUNKING · Chunking
- **Says:** Breaking information into meaningful groups makes it easier to scan, understand and remember.
- **Apply when:** long strings or long forms are shown as one unbroken block.
- **Don't cite when:** the content is already short.
- **In trading:** account/DP IDs, IFSC, phone numbers ("+91 98765 43210"), order IDs; long KYC forms split into steps; Indian digit grouping (`TR-NUM-04`).

> **Recognition over recall** is Nielsen's `NH-6` (§6). Cite it when the fix is "show it, don't make them remember it".

### L-MENTAL-MODEL · Mental Model
- **Says:** Users act on their own picture of how the system works. If the design contradicts it, they make errors.
- **Apply when:** the UI's terms, structure or behaviour clash with how users think about money and markets.
- **Don't cite when:** you're only guessing what users think. If it matters, mark it **Needs research** (`GOV-09`).
- **In trading:** "Balance" vs "Available to trade" vs "Withdrawable"; lots vs units for F&O; "Invested" vs "Current value"; "Placed" read as "Bought"; NAV date vs order date for funds.

### L-SERIAL-POSITION · Serial Position Effect
- **Says:** People remember the first and last items in a series best.
- **Apply when:** an important item is buried in the middle of a sequence people must remember or choose from (nav items, a carousel, an onboarding sequence).
- **Don't cite when:** the list is sorted data users scan or search (holdings, a watchlist, an option chain).
- **In trading:** Navigation Bar tab order; where key terms sit in a long risk explainer.

### L-VON-RESTORFF · Von Restorff (Isolation) Effect
- **Says:** The item that differs from its neighbours is noticed and remembered.
- **Apply when:** the single most important item (primary CTA, a critical warning) doesn't stand out, *or* too many items are emphasised so nothing stands out.
- **Don't cite when:** emphasis would rely on colour alone (fix that under `WCAG 1.4.1`), or the "isolated" item is promotional and competes with the user's task.
- **In trading:** a promo banner louder than "Place order"; three Danger Badges on one card.

### L-SELECTIVE-ATTENTION · Selective Attention (incl. banner blindness)
- **Says:** People focus on what serves their goal and filter out the rest, including anything that looks like an ad.
- **Apply when:** critical information (risk disclosures, margin shortfall, rejection reason) is styled or placed like promotional content, so users skip it.
- **Don't cite when:** the content really is optional.
- **In trading:** a margin warning in a carousel slot; a rejection reason in `text/tertiary` fine print.

### L-ZEIGARNIK · Zeigarnik Effect
- **Says:** People remember unfinished tasks better than finished ones.
- **Apply when:** an incomplete state (draft order, half-done KYC, partially filled order) is invisible, so users forget or lose it.
- **Don't cite when:** it's used to justify nagging. Reminders must be proportionate (`TR-RISK-01`).
- **In trading:** open/pending orders on Home; a "Resume KYC" entry point; the A22 "setting up" Timeline.

### L-GOAL-GRADIENT · Goal-Gradient Effect
- **Says:** Motivation grows as people get closer to a goal, so visible progress helps them finish.
- **Apply when:** a multi-step flow (KYC, account opening, first SIP) gives no sense of progress or remaining effort.
- **Don't cite when:** the flow is one or two steps. Never fake progress (a bar starting at 30% for no reason).
- **In trading:** "Step 2 of 5" in the Top Bar; a document checklist.

### L-PEAK-END · Peak-End Rule
- **Says:** People judge an experience mostly by its most intense moment and how it ends.
- **Apply when:** the peak or end moment (order result, withdrawal success, KYC completion, a failure) is unclear, cold or alarming.
- **Don't cite when:** someone proposes celebration on order execution. That's a deceptive engagement pattern in finance (`TR-RISK-02`). The "good ending" is clarity: what happened, what it cost, what's next.
- **In trading:** order confirmation; failed-payment recovery; the A21 Submitted result screen.

### L-AESTHETIC-USABILITY · Aesthetic-Usability Effect
- **Says:** People perceive attractive designs as easier to use, and forgive their flaws.
- **Apply when:** (a) judging test results, where polish can hide real problems; (b) trust-critical surfaces (login, money, orders) look broken or inconsistent, which in finance reads as "unsafe".
- **Don't cite when:** asking for decoration. It's never a reason to add ornament.

### L-ACTIVE-USER · Paradox of the Active User
- **Says:** Users skip manuals and tutorials and start using the product straight away.
- **Apply when:** essential understanding depends on a tutorial, coach marks or a help article instead of the UI itself.
- **Don't cite when:** the help is optional depth for advanced features.
- **In trading:** first-time option buyers who'll never open "How options work"; the explanation must be inline at the decision point (Tooltip, Step Heading description).

### L-FLOW · Flow
- **Says:** People do their best work absorbed in a task that's challenging but manageable, without interruption.
- **Apply when:** pop-ups, upsell sheets or forced tours break a focused task.
- **Don't cite when:** the interruption is a required safety check (margin shortfall, risk disclosure). That's justified friction; govern how it looks, not whether it exists (`GOV-08`).

---

## 3. Decision-making and behaviour

### L-HICK · Hick's Law (Hick–Hyman)
- **Says:** Decision time grows with the number and complexity of choices, logarithmically, not linearly.
- **Apply when:** users must choose between many similar, unfamiliar, roughly equally likely options at once (all order types shown to a novice; ten equal-weight CTAs).
- **Don't cite when:** users scan for a known target (a strike, a symbol); experts already know where options are; the options are needed together to compare. Hiding needed information isn't "applying Hick's" (`MYTH-4`).
- **In trading:** Market/Limit first with SL/SL-M behind "More" for novices.

### L-CHOICE-OVERLOAD · Choice Overload
- **Says:** Too many options can stall a decision or lower satisfaction with it. The effect depends heavily on context; treat it as a risk, not a certainty.
- **Apply when:** users must *compare and pick* from a large set without help (sort, filters, curated shortlists, defaults).
- **Don't cite when:** the user already knows what they want and can search for it.
- **In trading:** thousands of mutual funds with no filters; twenty SIP dates. Fix it with structure (filters, collections, a recommended default), not by removing access.

### L-BIAS · Cognitive biases in money decisions
- **Says:** Systematic shortcuts shape financial choices: **loss aversion**, **anchoring**, **framing**, the **default effect**, and the **disposition effect** (selling winners early, holding losers too long).
- **Apply when:** the design frames, anchors or defaults a financial decision. Raise it when the design exploits a bias against the user, or when a neutral design would protect them.
- **Don't cite when:** you'd only say "users are biased" without pointing to a specific frame, anchor or default.
- **In trading:** a default leverage or product type that raises risk; only "% up since buy" with no absolute loss; a "most bought" list as an anchor. See `TR-RISK-*`.

### L-OCCAM · Occam's Razor
- **Says:** Among solutions that work equally well, prefer the one with the fewest assumptions and parts.
- **Apply when:** two elements do one job (duplicate CTAs; a label, an icon and a Tooltip all saying the same thing), or a simpler existing DS pattern would work.
- **Don't cite when:** you mean a generic "simplify". Name the redundant part or don't raise it.

### L-PARETO · Pareto Principle
- **Says:** Roughly 80% of effects come from 20% of causes.
- **Apply when:** you have usage data showing a few actions dominate, and the layout doesn't prioritise them.
- **Don't cite when:** you have no data (mark **Needs data**), or it's used to drop accessibility or minority use cases.

### L-PARKINSON · Parkinson's Law
- **Says:** A task expands to fill the time available for it.
- **Apply when:** rarely. Only when a flow asks for effort the system could do itself (autofill, prefill, defaults).
- **Don't cite when:** almost always. `L-COG-LOAD` or `WCAG 3.3.7` are more precise.

---

## 4. Interaction, motor and system response (HCI)

### L-FITTS · Fitts's Law
- **Says:** The time to reach a target depends on its distance and size: far, small targets are slower and cause more mis-taps.
- **Apply when:** a frequent or high-stakes target is small, far from the thumb, or crowded by neighbours, *especially* when the neighbour does the opposite (Buy next to Sell, Modify next to Cancel).
- **Don't cite when:** the target already meets our minimum and sits in a normal position; or the distance is a deliberate safeguard (keeping "Exit all positions" away from routine actions is correct).
- **In trading:** submit button, qty steppers, chart range chips, close icons in dense rows.
- **Check:** ≥ 44×44 pt hit area (our rule); Android primary actions 48×48 dp (`D-04`); the WCAG 2.5.8 floor is 24×24. Opposite actions are separated, not adjacent.

### L-STEERING · Steering Law
- **Says:** Moving a pointer through a narrow path is slow and error-prone; the longer and narrower, the worse.
- **Apply when:** narrow sliders or drag paths make the user steer precisely (web hover menus once web is in scope).
- **Don't cite when:** the interaction is a tap, not a path.
- **In trading:** a thin quantity or amount slider.

### L-DOHERTY · Doherty Threshold
- **Says:** Productivity soars when the system responds within about 400 ms, so neither the person nor the computer waits.
- **Apply when:** an interaction gives no immediate feedback (no Pressed/loading state), or a slow step shows no progress.
- **Don't cite when:** someone wants "optimistic UI" for money. **Never show an order as executed, or money as added, before the system confirms it.** Instant feedback means "we got your tap / submitting…", not a fake result.
- **In trading:** Pressed state + "Placing order…" within 400 ms; skeleton rows for watchlist load (`lists-cards.md`).

### L-RESPONSE-TIMES · Response-time limits
- **Says:** About 0.1 s feels instant; about 1 s keeps the train of thought; around 10 s is the limit of attention. Beyond that, show progress and allow cancel.
- **Apply when:** a wait over ~1 s has no indicator, or a wait over ~10 s has no progress, explanation or way out.
- **Don't cite when:** it duplicates `L-DOHERTY`. Use this one for long waits, Doherty for immediate response.
- **In trading:** KYC verification (A08), bank linking (penny drop), payment confirmation, report downloads.

### L-TESLER · Tesler's Law (Conservation of Complexity)
- **Says:** Every system has complexity that can't be removed. The question is who deals with it: the system or the user.
- **Apply when:** complexity the system could absorb is pushed onto the user (lots, margin, charges, tax, exit load; choosing an exchange the app could default).
- **Don't cite when:** it's used to excuse complexity ("trading is just complex").
- **In trading:** auto-calc margin required; default exchange with a switch; prefill from KYC/DigiLocker.

### L-POSTEL · Postel's Law (Robustness Principle)
- **Says:** Be liberal in what you accept and conservative in what you send.
- **Apply when:** inputs reject reasonable formats, or outputs are formatted inconsistently.
- **Don't cite when:** accepting loose input would hide an error with money consequences (silently rounding a price to the tick size: snap it, *and say so*).
- **In trading:** qty "1,000" or "1000"; search by name, ticker or partial; pasting an OTP; phone with spaces or +91.

### L-JAKOB · Jakob's Law
- **Says:** Users spend most of their time on *other* products, so they expect yours to work the same way.
- **Apply when:** the design breaks a convention users know from iOS/Android or the dominant Indian investing apps, with no clear benefit.
- **Don't cite when:** the convention itself is harmful or inaccessible, or a tested design beats it.
- **In trading:** option chain with calls left, puts right, strike centre; bid/ask layout in depth; tapping a watchlist row opens the instrument; Android back.

---

## 5. Visual design principles

### V-HIERARCHY · Visual hierarchy
- **Says:** Size, weight, colour, position and spacing tell users what matters first, second and third.
- **Apply when:** the most important information or action isn't the most prominent, or several elements compete for first place.
- **Don't cite when:** the hierarchy is correct and you only prefer another style.
- **In trading:** instrument → price and change first; portfolio → current value and total P&L first; order → side, qty, price and submit.
- **Check:** squint/blur test; one primary per view (`M-03`).

### V-CONTRAST · Visual contrast (emphasis)
- **Says:** Differences in size, weight or colour create emphasis and separation. This is *not* WCAG colour contrast (`WCAG 1.4.3` / `1.4.11`, measured by `/ds-audit`).
- **Apply when:** elements that should differ look too alike (primary vs secondary button, header vs body), or everything is loud so nothing reads as important.
- **Don't cite when:** the problem is legibility. That's WCAG contrast: measure it, don't eyeball it.

### V-ALIGN · Alignment and grid
- **Says:** Aligning to a shared grid creates order and makes scanning faster.
- **Apply when:** misalignment breaks scanning (numbers not aligned in a column, ragged label edges), or similar screens ignore the same layout.
- **Don't cite when:** a 1–2 px offset has no effect on scanning. Report it at most as `S4` at the final stage.
- **In trading:** right-aligned price columns in `num-*` styles (`TR-NUM-02`); page margins `space/20` (`.claude/rules/layout.md`).

### V-REPETITION · Repetition and consistency
- **Says:** Repeating the same visual and interaction patterns builds familiarity and trust.
- **Apply when:** the same thing is drawn or behaves differently on different screens or platforms.
- **Don't cite when:** the difference is a deliberate platform convention (`X-01`). Overlaps with `NH-4`/`SR-1`; cite one, not all three.
- **Check:** DS component used, not a lookalike (`/ds-audit`).

### V-SPACE · White space and density
- **Says:** Space separates, groups and gives room to breathe. The right density depends on the user and the task.
- **Apply when:** crowding causes mis-taps or misreads, or excess space hides data experts need.
- **Don't cite when:** density is appropriate for the segment (`GOV-05`).

### V-BALANCE · Balance
- **Says:** Visual weight should be distributed so the layout feels stable and the eye isn't pulled to one side for no reason.
- **Apply when:** the imbalance draws attention to the wrong thing, or makes the screen feel broken.
- **Don't cite when:** the asymmetry is deliberate and supports the hierarchy. Polish level; rarely above `S4`.

### V-TYPE · Typography and readability
- **Says:** Type must be legible (size, weight, line height) and readable (line length, hierarchy, truncation).
- **Apply when:** text outside our type scale or below 11 (`.claude/rules/typography.md`); numbers not in `num-*` styles; important names truncated so they become ambiguous; body copy running far beyond 45–75 characters per line.
- **Don't cite when:** a short label or list cell is involved; line-length rules are for running text.
- **In trading:** fund or contract names truncated so two look the same ("Parag Parikh Flexi Cap Fund Dir…" twice); a text style on every text.

### V-COLOR · Colour meaning (semantics)
- **Says:** Colour carries meaning. Use it consistently, sparingly, and never as the only signal.
- **Apply when:** a semantic colour (gain, loss, error, warning) is used for something else; meaning relies on colour alone; or Dark mode flips a meaning.
- **Don't cite when:** a long-standing convention carries its own non-colour cue (filled vs hollow candles).
- **In trading:** roughly 1 in 12 men has some colour-vision deficiency, most often red–green: exactly the gain/loss pair. See `TR-NUM-01`.
- **Check:** semantic tokens only, `market/*` for price movement only (`.claude/rules/tokens.md`), plus a non-colour cue (sign, arrow, label).

### V-ICON · Icons and signifiers
- **Says:** Icons are faster than text only when they're familiar; unfamiliar icons need labels.
- **Apply when:** an icon-only button does something important or uncommon (order type, exit position), or the same icon means different things in different places.
- **Don't cite when:** the icon is universal (search, close, back) and the target has an accessible name (`accessibility.md` AN-03).

---

## 6. Interaction-design principle sets

Use these when a finding is about **interaction**, not visuals. Within one finding, cite only the single entry that explains it best (`GOV-03`).

### Don Norman: principles of interaction design (*The Design of Everyday Things*)

| ID | Principle | Apply when (trading example) |
|---|---|---|
| `DN-AFFORDANCE` | **Affordances and signifiers:** what an element lets you do, and what *shows* you can do it | A tappable P&L row has no chevron or other cue; a swipe action has no visible hint |
| `DN-MAPPING` | **Mapping:** controls relate naturally to their effect | A qty stepper whose "+" sits below "−"; a chart zoom slider moving the wrong way |
| `DN-FEEDBACK` | **Feedback:** every action gets an immediate, clear response | Tapping "Place order" shows nothing until a result arrives |
| `DN-CONSTRAINTS` | **Constraints:** prevent invalid actions up front | Qty accepts non-lot multiples; SIP amount accepts values below the minimum |
| `DN-CONCEPTUAL` | **Conceptual model:** the UI tells a coherent story of how things work | Holdings, positions and orders overlap with no clear distinction |
| `DN-GULFS` | **Gulfs of execution and evaluation:** "how do I do it?" and "did it work?" | User can't tell whether an after-market order will execute tomorrow or was rejected |

### Jakob Nielsen: 10 usability heuristics

| ID | Heuristic | Apply when (trading example) |
|---|---|---|
| `NH-1` | Visibility of system status | No market-state, data-freshness or order-status indicator |
| `NH-2` | Match between system and the real world | Exchange jargon with no plain label ("CNC", "NRML") for novices |
| `NH-3` | User control and freedom | No way to cancel a pending order or go back without losing input |
| `NH-4` | Consistency and standards | "Exit" here, "Square off" there, "Close" elsewhere for the same action |
| `NH-5` | Error prevention | A market order in an illiquid contract goes through with no warning |
| `NH-6` | Recognition rather than recall | User must remember the strike from the chain while on the order |
| `NH-7` | Flexibility and efficiency of use | No shortcuts, saved orders or presets for frequent investors |
| `NH-8` | Aesthetic and minimalist design | Promo content competes with the order |
| `NH-9` | Help users recognise, diagnose and recover from errors | "Order rejected: RMS error 16283" with no reason or next step |
| `NH-10` | Help and documentation | No in-context help for margin or charges at the point of decision |

### Ben Shneiderman: 8 golden rules of interface design

| ID | Rule | Apply when (trading example) |
|---|---|---|
| `SR-1` | Strive for consistency | Same as `NH-4`; cite only one |
| `SR-2` | Seek universal usability (incl. shortcuts for frequent users) | Frequent users have no quick path to repeat an order |
| `SR-3` | Offer informative feedback | A major action gets the same tiny confirmation as a minor one |
| `SR-4` | Design dialogs to yield closure | Flow ends without a clear "done" state (withdrawal requested… then nothing) |
| `SR-5` | Prevent errors | Same as `NH-5`; cite only one |
| `SR-6` | Permit easy reversal of actions | No undo for removing a watchlist item; no modify/cancel for an open order |
| `SR-7` | Keep users in control | Auto-refresh moves the scroll position; the app auto-selects a product type |
| `SR-8` | Reduce short-term memory load | Same as `NH-6`; cite only one |

---

## 7. Accessibility floor: WCAG 2.2 (Level AA)

Accessibility is a **floor**, not a law to weigh against others. A failure on a core task is `S1` (`ux-governance.md` §3).
These are the criteria trading designs trigger most often. For the full set (all 55 A/AA criteria, mobile notes, annotations)
use [`accessibility.md`](accessibility.md); contrast is measured by `/ds-audit` against the thresholds in `.claude/rules/accessibility.md`.

| SC | Level | Requirement (plain words) | Typical trading trigger |
|---|---|---|---|
| `WCAG 1.4.1` Use of Color | A | Colour isn't the only way to convey meaning | Gain/loss, buy/sell, ITM/OTM shown by colour only |
| `WCAG 1.4.3` Contrast (Minimum) | AA | Text 4.5:1; large text 3:1 | `text/secondary` prices on tinted chips |
| `WCAG 1.4.11` Non-text Contrast | AA | UI parts and meaningful graphics 3:1 against neighbours | Field borders, chart lines, selected-tab indicators |
| `WCAG 1.4.10` Reflow | AA | No 2-D scrolling at narrow width, except content that needs it (tables, charts) | Landscape and large text on core screens (`D-02`) |
| `WCAG 1.4.12` Text Spacing | AA | Nothing breaks when users increase text spacing | Web only: not in scope yet |
| `WCAG 2.2.1` Timing Adjustable | A | Time limits can be turned off, adjusted or extended (with exceptions) | Session timeout wiping an order; OTP expiry with no resend |
| `WCAG 2.2.2` Pause, Stop, Hide | A | Auto-moving or auto-updating content can be paused, *unless essential* | Scrolling tickers (pausable); live prices in place are usually essential |
| `WCAG 2.3.1` Three Flashes or Below Threshold | A | Nothing flashes more than 3 times per second | Rapid price-flash animations |
| `WCAG 2.4.11` Focus Not Obscured (Minimum) | AA | A focused item isn't fully hidden by sticky content | Sticky Buy/Sell footer or Navigation Bar covering focused rows |
| `WCAG 2.5.7` Dragging Movements | AA | Anything done by dragging also works with a single tap | Swipe-to-buy, sliders, chart pan, reorder watchlist |
| `WCAG 2.5.8` Target Size (Minimum) | AA | Targets ≥ 24×24 (or enough spacing), with exceptions | Dense row icons, chart chips, close "×" |
| `WCAG 3.3.4` Error Prevention (Legal, Financial, Data) | AA | Financial submissions are reversible, checked, or confirmed | Orders, SIP/mandate setup, withdrawals, eSign |
| `WCAG 3.3.7` Redundant Entry | A | Don't make users re-enter info already given in the same process | Re-typing PAN or bank details across KYC steps |
| `WCAG 3.3.8` Accessible Authentication (Minimum) | AA | No memory test to log in without paste, a password manager or biometrics | OTP cells that block paste |
| `WCAG 4.1.3` Status Messages | AA | Status updates are announced without moving focus | "Order placed" confirmations (annotate for dev) |
| `WCAG 3.2.6` Consistent Help | A | Help appears in the same relative place across screens | Help icon moving around in the Top Bar |

Platform guidelines set larger targets than WCAG: **iOS 44×44 pt** (our rule for every target) and **Android 48×48 dp** (primary actions, `D-04`).
Button and Icon Button heights are xs 28 · sm 32 · md 40 · lg 52 · xl 56 (`.claude/rules/layout.md`): xs–md need extra hit area.

---

## 8. Misapplications: never cite these as rules

If you catch yourself writing one of these, delete the finding or rebuild it on a real problem.

| ID | Myth or misuse | What's actually true |
|---|---|---|
| `MYTH-1` | "Three-click rule: everything within 3 clicks" | Not supported by research. Users are fine with more taps when each step is clearly right. Judge information scent, not tap count. |
| `MYTH-2` | "Miller's Law: max 7 menu items / tabs / rows" | Miller is about *memorising*, not seeing. Visible, scannable options don't tax memory the same way. |
| `MYTH-3` | "Golden ratio makes layouts usable" | An aesthetic proportion, not a usability law. Use our spacing scale and layout rules. |
| `MYTH-4` | "Hick's Law means fewer options are always better" | Hiding options users need adds steps and recall. Hick's applies to choosing among unfamiliar, equally likely options. |
| `MYTH-5` | "Users don't scroll" | Users scroll when the content above the fold signals more is worth seeing. Judge the signal, not the fold. |
| `MYTH-6` | "Design for the F-pattern" | The F-pattern describes how people scan *poorly structured* text. Fix it with headings and hierarchy; it isn't a layout target. |
| `MYTH-7` | "Aesthetic-usability effect: make it prettier" | It explains why people forgive flaws: a warning for testing, not a call for decoration. |
| `MYTH-8` | "Pareto: drop the 80% of features few people use" | Only with usage data, and never for accessibility, error recovery or regulatory paths. |
| `MYTH-9` | "Add a confirmation dialog to be safe" | Confirming everything trains users to tap through every dialog. Our orders get one review step (`D-03`); extra warnings only in proportion to risk (`TR-ORD-04`). |
| `MYTH-10` | "Red/green is fine, every trading app uses it" | The convention is fine (`L-JAKOB`); colour *alone* isn't (`WCAG 1.4.1`). Keep `market/gain`/`market/loss` and add a sign or arrow. |
