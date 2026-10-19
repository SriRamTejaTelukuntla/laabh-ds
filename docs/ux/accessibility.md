# Accessibility: WCAG 2.2 AA, checked at design time

The deep reference for accessibility. [`ux-governance.md`](ux-governance.md) names WCAG 2.2 AA as the floor; this file says what that floor means
for each Laabh screen and how to check it in a design. The `/design-review` skill reads it together with the governance file.
The always-on build rules are the short version in [`.claude/rules/accessibility.md`](../../.claude/rules/accessibility.md).

**The rule that governs everything below: raise only what the design actually triggers.** Every criterion has a *Skip when* line.
If the screen has no trigger for a criterion, the criterion doesn't appear in the report. A long list of "not applicable" items,
or a finding stretched to fit, makes the report worse, not more thorough.

> Colours are named by **role** (`text/secondary`, `surface/danger-subtle`), never by value. Contrast is **measured** by `/ds-audit`
> against the thresholds in `.claude/rules/accessibility.md` (4.5:1 text, 3:1 large text and UI parts). This file never restates the formula.

---

## 1. Scope

| In scope | Out of scope |
|---|---|
| Figma frames and prototypes (official Figma plugin; figma-console for DS owners) | Code audits, DOM/ARIA inspection, automated scanners |
| Screenshots of designs or of the live app | Testing a build with a real screen reader |
| Flows: the steps a user takes to finish a task | Legal interpretation (compliance's call; e.g. the RPwD Act 2016) |
| Handoff annotations the designer owes developers (§8) | Token "0 raw" checks and contrast arithmetic (`/ds-audit`) |

A design can't prove that code will expose the right name or role. It *can* fail to specify it. So for code-level criteria (4.1.2, 4.1.3, 1.3.1, 1.3.5)
the design-time check is: **is the annotation there?** A missing annotation is a finding; a wrong implementation is a code audit's job.

### Sources
| Source | Used for |
|---|---|
| W3C WAI, *Introduction to Web Accessibility* | Who accessibility serves; disability groups |
| *WCAG 2.2* Recommendation (w3.org/TR/WCAG22/) | Every SC number, level and requirement below |
| *Understanding WCAG 2.2* | Exceptions, edge cases, what "essential" means |
| WAI *Designing for Web Accessibility* tips | Design-stage checks |
| WAI *WCAG2Mobile* Group Draft Note (May 2025), *WCAG2ICT* | Applying WCAG to native iOS/Android apps |

---

## 2. Who we design for

Accessibility covers **auditory, cognitive, neurological, physical, speech and visual** disabilities. It also helps people who are older,
temporarily injured, or limited by their situation: bright sunlight on a commute, one hand holding a rail, no sound in an office.

In an investing app, the people most often blocked are: low-vision users zooming dense lists; colour-blind users reading red/green P&L;
screen-reader users (VoiceOver, TalkBack) placing orders; people with tremor hitting small steppers; people with cognitive disabilities facing OTP timers, passwords and jargon.

| Principle | WCAG wording (short) | Where it bites |
|---|---|---|
| **Perceivable** | Information and UI must be presentable in ways users can perceive | Gain/loss colour, chart lines, tiny grey numbers, live price flashes |
| **Operable** | UI and navigation must be operable | Swipe-to-buy, sliders, small steppers, session timeouts |
| **Understandable** | Information and operation must be understandable | Order-type jargon, vague errors ("Invalid input"), unexpected screen jumps |
| **Robust** | Content must work with assistive tech | Custom toggles and list cells with no name, role or state |

---

## 3. Target conformance

- **Floor: WCAG 2.2 Level AA** = every Level A and AA success criterion: 55 criteria (31 A + 24 AA); 4.1.1 Parsing is obsolete in 2.2. All are in §5.
- **AAA is a recommendation**, never a blocker. The useful ones are in §6 (`A11Y-R-` IDs).
- **Native apps.** W3C's *WCAG2Mobile* note applies WCAG to apps: read "web page" as **screen** and "set of web pages" as **set of screens**.
  "CSS pixel" becomes **pt on iOS, dp on Android**. So 24×24 CSS px = 24×24 pt = 24×24 dp.
- **Platforms** (`D-04`): iOS and Android are in scope; web isn't yet. Web-only criteria (1.4.12, 2.4.1, 2.4.5) are kept and marked, but not raised.
- **Set-of-screens criteria on native:** apply the three consistency criteria (3.2.3, 3.2.4, 3.2.6) to both platforms.
- **House rules** (stricter than WCAG, labelled **House** in reports):
  - Every tappable target has a **44×44 pt** hit area (`.claude/rules/accessibility.md`). On Android, primary actions also reach **48×48 dp** (§7.1, `D-04`).
  - Every order submission (stock order, SIP, lumpsum, redemption, switch, money movement) has a **review step**, unless the user turns it off in settings (`D-03`).
  - Screens are designed in portrait; the app **never locks orientation**, and core screens carry a landscape reflow rule (`D-02`).
  - Text: Figma check at **one Dynamic Type step larger** (our rule), plus the 200% behaviour annotated (A11Y-TXT-01).

---

## 4. How to apply this file (the trigger rule)

1. **Walk the user's task**, not the frame list. "Log in → find RELIANCE → buy 10 at limit → see confirmation." Note every element the task touches.
2. **Look up triggers** in the index (§5.0). A criterion is *triggered* only if the design contains its trigger. No trigger, no line in the report.
3. **Read the criterion's exceptions before raising it.** Many fail-looking designs pass through an exception: Equivalent control (2.5.8), Essential (2.2.2, 1.3.4),
   Inline (2.5.8), Real-time (2.2.1), 2D layout (1.4.10). Name the exception when you clear an item.
4. **Unknown ≠ fail.** If the design can't show it (does Buy fire on press or on release?), it becomes **Needs annotation** or a **Question**, not a finding.
5. **Contrast goes to `/ds-audit`.** Never estimate a ratio from a screenshot and call it a fail; measure it, or mark it "to measure".
6. **Verify every finding before reporting**: the trigger is really there, no exception covers it, the SC number and level are right, the severity follows §9.

`/prd-to-screens` uses the index at **plan time**: each screen in `plan.md` lists the criteria it triggers, so the build covers them before the review.

---

## 5. Criteria by design concern (all A and AA)

### 5.0 Index: what triggers each criterion

| ID | SC | Name | Level | Triggered by |
|---|---|---|---|---|
| A11Y-COL-01 | 1.4.1 | Use of Color | A | Any colour-coded meaning: P&L, Buy/Sell, status, selection, chart series, required fields |
| A11Y-COL-02 | 1.4.3 | Contrast (Minimum) | AA | Any text or image of text |
| A11Y-COL-03 | 1.4.11 | Non-text Contrast | AA | Control boundaries, state indicators, meaningful icons, chart lines, focus rings |
| A11Y-TXT-01 | 1.4.4 | Resize Text | AA | Any text, especially fixed-height rows, pills, tabs, numeric cells |
| A11Y-TXT-02 | 1.4.5 | Images of Text | AA | Text baked into an image: banners, IPO cards, chart labels as bitmaps |
| A11Y-TXT-03 | 1.4.12 | Text Spacing | AA | Web only (not in scope yet) |
| A11Y-LAY-01 | 1.3.1 | Info and Relationships | A | Headings, lists, grouped fields, label/value pairs shown visually |
| A11Y-LAY-02 | 1.3.2 | Meaningful Sequence | A | Multi-column layouts, cards, overlays, where read order changes meaning |
| A11Y-LAY-03 | 1.3.4 | Orientation | AA | Any screen (house rule `D-02`: never lock; landscape reflow rule) |
| A11Y-LAY-04 | 1.4.10 | Reflow | AA | Narrow width / large text / landscape; wide tables and toolbars |
| A11Y-LAY-05 | 2.4.1 | Bypass Blocks | A | Web only (not in scope yet) |
| A11Y-LAY-06 | 2.4.5 | Multiple Ways | AA | Web only (not in scope yet) |
| A11Y-LAY-07 | 3.2.3 | Consistent Navigation | AA | Navigation repeated across two or more screens |
| A11Y-TGT-01 | 2.5.8 | Target Size (Minimum) | AA | Any tappable target |
| A11Y-TGT-02 | 2.5.1 | Pointer Gestures | A | Swipe, flick, pinch, two-finger, or traced-path gestures |
| A11Y-TGT-03 | 2.5.7 | Dragging Movements | AA | Drag to operate: sliders, swipe-to-confirm, chart lines, reorder |
| A11Y-TGT-04 | 2.5.2 | Pointer Cancellation | A | Actions specified to fire on touch-down, or press-and-hold |
| A11Y-TGT-05 | 2.5.4 | Motion Actuation | A | Shake, tilt or other device motion that operates something |
| A11Y-TGT-06 | 1.4.13 | Content on Hover or Focus | AA | Tooltips, chart crosshair popovers (focus-triggered on native) |
| A11Y-FOC-01 | 2.1.1 | Keyboard | A | Any interactive element (external keyboard / Switch Control / Full Keyboard Access) |
| A11Y-FOC-02 | 2.1.2 | No Keyboard Trap | A | Sheets, embedded charts, custom widgets, pickers |
| A11Y-FOC-03 | 2.1.4 | Character Key Shortcuts | A | Single-key hotkeys |
| A11Y-FOC-04 | 2.4.3 | Focus Order | A | Any screen with more than one focusable element, sheets |
| A11Y-FOC-05 | 2.4.7 | Focus Visible | AA | Any keyboard-operable element |
| A11Y-FOC-06 | 2.4.11 | Focus Not Obscured (Minimum) | AA | Sticky footers, Navigation Bar, banners |
| A11Y-FOC-07 | 3.2.1 | On Focus | A | Anything specified to act when it receives focus |
| A11Y-FOC-08 | 4.1.2 | Name, Role, Value | A | Every control, especially custom ones and icon-only buttons |
| A11Y-MOT-01 | 2.3.1 | Three Flashes or Below Threshold | A | Flashing: tick flashes, alert blinks, full-screen colour flashes |
| A11Y-MOT-02 | 1.4.2 | Audio Control | A | Audio that plays automatically for more than 3 seconds |
| A11Y-FRM-01 | 3.3.2 | Labels or Instructions | A | Any input |
| A11Y-FRM-02 | 1.3.5 | Identify Input Purpose | AA | Inputs collecting the user's own data on WCAG's input-purpose list |
| A11Y-FRM-03 | 3.2.2 | On Input | A | A control whose change navigates, submits, or moves focus by itself |
| A11Y-FRM-04 | 3.3.7 | Redundant Entry | A | Multi-step process asking for the same information twice |
| A11Y-ERR-01 | 3.3.1 | Error Identification | A | Any automatically detected input error |
| A11Y-ERR-02 | 3.3.3 | Error Suggestion | AA | An error where the fix is known (range, format, multiple) |
| A11Y-ERR-03 | 3.3.4 | Error Prevention (Legal, Financial, Data) | AA | Orders, SIPs, money movements, mandates, eSign, deleting user data |
| A11Y-AUT-01 | 3.3.8 | Accessible Authentication (Minimum) | AA | Login, OTP, MPIN, password, captcha, re-auth |
| A11Y-TIM-01 | 2.2.1 | Timing Adjustable | A | Session timeouts, countdowns, timed steps, auto-dismiss with no other access |
| A11Y-LIV-01 | 2.2.2 | Pause, Stop, Hide | A | Auto-moving or auto-updating content shown alongside other content |
| A11Y-LIV-02 | 4.1.3 | Status Messages | AA | Confirmations, inline results, progress, error counts that appear without focus |
| A11Y-CPY-01 | 1.1.1 | Non-text Content | A | Icons, images, charts, sparklines, logos |
| A11Y-CPY-02 | 1.3.3 | Sensory Characteristics | A | Instructions that refer to colour, shape, position or sound |
| A11Y-CPY-03 | 2.4.2 | Page Titled | A | Every screen |
| A11Y-CPY-04 | 2.4.4 | Link Purpose (In Context) | A | Links, especially "Know more", "View" |
| A11Y-CPY-05 | 2.4.6 | Headings and Labels | AA | Headings and labels present on the screen |
| A11Y-CPY-06 | 2.5.3 | Label in Name | A | Controls with visible text |
| A11Y-CPY-07 | 3.1.1 | Language of Page | A | Non-English screens |
| A11Y-CPY-08 | 3.1.2 | Language of Parts | AA | Mixed-language content (Hindi disclaimer on an English screen) |
| A11Y-CPY-09 | 3.2.4 | Consistent Identification | AA | Same function appearing on two or more screens |
| A11Y-CPY-10 | 3.2.6 | Consistent Help | A | Help/contact/chat repeated across screens |
| A11Y-MED-01…05 | 1.2.1–1.2.5 | Media alternatives and captions | A/AA | Prerecorded or live audio/video (§5.12) |

Each block below gives: **Requires** (plain words), **Check** (in the design), **Trading** (a typical case), **Skip when** (no trigger, or an exception applies).

---

### 5.1 Colour and contrast

#### A11Y-COL-01 · 1.4.1 Use of Color · A
- **Requires:** colour is never the *only* visual way to convey information, show an action, prompt a response, or distinguish an element.
- **Check:** view the screen in greyscale. Every colour-coded meaning needs a second cue: sign, arrow, icon, text, pattern, position.
- **Trading:** P&L shown only in `market/gain` / `market/loss` with no `+`/`−` or arrow. A Buy/Sell toggle where only the fill shows the active side. Chart series with a colour-only legend. A red border as the only error signal (our fields pair `State=Error` with ⚠ helper text).
- **Skip when:** the colour is decorative, or the meaning is already carried by text (a "SELL" label that's also red is fine).

#### A11Y-COL-02 · 1.4.3 Contrast (Minimum) · AA
- **Requires:** text and images of text meet 4.5:1 (normal) or 3:1 (large text: ≥ 24 regular / ≥ 19 bold).
- **Check:** **hand off to `/ds-audit`.** List the (text role → background role) pairs the screen renders, in Light and Dark. Usual suspects:
  `text/placeholder`, `text/secondary` on `surface/subtle`, timestamps, sub-labels, tone text on a tinted surface (must be `text/<tone>-strong`, `docs/foundations/colors.md`),
  text over glass (measure on the composited colour), text over charts or images.
- **Trading:** grey "Qty" and "Avg" sub-labels in a holdings row; LTP on a tick-flash background (measure the flash state too); `text/static-white` on the `Solid · Success` Buy button in Dark.
- **Skip when:** the text belongs to a disabled control, is pure decoration, is part of a logo, or is incidental in a photo. Never skip because "it looks fine".
- `text/disabled`, `text/placeholder` and `text/tertiary` are **not** for essential content (`.claude/rules/accessibility.md`).

#### A11Y-COL-03 · 1.4.11 Non-text Contrast · AA
- **Requires:** 3:1 against adjacent colours for (a) whatever identifies a control and its state, and (b) parts of graphics needed to understand the content.
- **Check:** list the non-text pairs for `/ds-audit`: field borders, Checkbox/Radio outlines, Switch track and thumb, selected-segment indicator, `focus/ring`, meaningful icons, chart lines.
- **Trading:** the unselected Buy/Sell segment; a price-alert bell icon with no label; a P&L sparkline; a slider thumb.
- **Skip when:** the control is disabled; the boundary isn't needed to identify the control (a Ghost button passes on its text); the graphic is decorative; states that never sit side by side.

---

### 5.2 Text and type

#### A11Y-TXT-01 · 1.4.4 Resize Text · AA
- **Requires:** text can be resized up to 200% without losing content or function.
- **Check:** in Figma, the screen at **one Dynamic Type step larger** must not clip (our rule). For 200%, the handoff states the behaviour: rows grow, prices wrap below the name rather than truncate, tab labels wrap or drop to icons. Look for fixed-height rows, single-line price truncation, pills and tabs that clip.
- **Trading:** a watchlist row with a fixed 64 height and LTP + change on one line; Navigation Bar labels that clip; truncated "Available to trade ₹1,2…".
- **Skip when:** captions and images of text (excepted). For a single static frame with nothing visibly fixed-size, raise a **Question** ("How does this row behave at 200%?") instead of a finding.

#### A11Y-TXT-02 · 1.4.5 Images of Text · AA
- **Requires:** real text, not pictures of text, when the technology can render it.
- **Check:** find text that is part of a bitmap or flattened vector.
- **Trading:** an IPO promo card exported as one image; a "Market closed" banner as a PNG; chart axis labels baked into an image.
- **Skip when:** logos and brand names (company logo tiles); an essential presentation (a contract-note screenshot shown as evidence).

#### A11Y-TXT-03 · 1.4.12 Text Spacing · AA
- Web only. Not in scope yet (`D-04`). Native screens are covered by TXT-01.

---

### 5.3 Layout, structure and reflow

#### A11Y-LAY-01 · 1.3.1 Info and Relationships · A
- **Requires:** structure shown visually (headings, lists, groups, label-value pairs) is available to assistive tech.
- **Check:** does the handoff mark headings (with levels), field groups (Radio Group, Segmented Control), and label↔value pairs? See §8.
- **Trading:** a summary card where "Day's P&L" and its value must be read together; a holdings list whose columns must be announced with their labels.
- **Skip when:** the screen has no visual structure beyond plain text. A missing annotation on a simple screen is `S3`.

#### A11Y-LAY-02 · 1.3.2 Meaningful Sequence · A
- **Requires:** when order affects meaning, a correct reading order can be determined.
- **Check:** number the reading order (AN-01) on screens with columns, cards, sticky footers or sheets. Is a sheet read after the price it refers to?
- **Trading:** a stock detail page where a screen reader reads "Buy · Sell" before the stock name and price.
- **Skip when:** single-column, top-to-bottom screens where visual order is the only sensible order.

#### A11Y-LAY-03 · 1.3.4 Orientation · AA
- **Requires:** don't restrict a screen to portrait or landscape unless the orientation is essential.
- **Our ruling (`D-02`):** we design portrait frames only; the app never locks orientation; core screens (orders, money, KYC) carry a landscape reflow rule in the handoff.
- **Check:** is a landscape reflow rule present for core screens? Missing → **Needs annotation**. A spec that locks orientation → finding.
- **Skip when:** orientation is essential (e.g. a document-capture camera step that genuinely needs landscape). "A nicer chart" isn't essential.

#### A11Y-LAY-04 · 1.4.10 Reflow · AA
- **Requires:** content works without two-direction scrolling at narrow width / high zoom, except parts that need a 2D layout.
- **Check:** native: the narrowest supported width (375, `CLAUDE.md`) with the largest text size, and landscape (`D-02`). Only the excepted part may scroll in two directions.
- **Trading:** option chain and market-depth tables are data tables (excepted) in their own scroll container; the rest of the screen still reflows.
- **Skip when:** content that genuinely needs 2D layout (tables, charts). The exception covers only that part.

#### A11Y-LAY-05 · 2.4.1 Bypass Blocks · A  ·  A11Y-LAY-06 · 2.4.5 Multiple Ways · AA
- Web only. Not in scope yet (`D-04`).

#### A11Y-LAY-07 · 3.2.3 Consistent Navigation · AA
- **Requires:** navigation repeated across screens appears in the same relative order each time, unless the user changes it.
- **Check:** compare the Navigation Bar, App Header and Top Bar across all frames in the flow.
- **Trading:** "Explore · Watchlist · Orders · Portfolio · Funds" on one screen and a different order on another (`docs/patterns/navigation.md` fixes the order).
- **Skip when:** only one screen is under review (raise a Question if the nav is visible), or the user reordered it.

---

### 5.4 Touch targets, pointer and hover

#### A11Y-TGT-01 · 2.5.8 Target Size (Minimum) · AA
- **Requires:** targets are at least 24×24 pt, **or** pass an exception.
- **Check:** measure the **hit area**, not the glyph. Under 24×24: draw a 24 circle centred on it; it must not touch another target or another undersized target's circle (Spacing). Then check the other exceptions. Then the house rule (§7.1).
- **Trading:** qty `−` / `+` steppers close together fail Spacing, **but pass through Equivalent** if the qty field can be typed into and meets the size. Sheet close icons; the info "i" next to "Margin required"; chart range chips packed tight.
- **Skip when:** **Spacing**, **Equivalent**, **Inline** (a link in a sentence), **User agent control**, **Essential** (dense chart markers, with an equivalent route where practical).

#### A11Y-TGT-02 · 2.5.1 Pointer Gestures · A
- **Requires:** anything done with a multipoint or path-based gesture also works with a single pointer without a path.
- **Check:** list every gesture in the prototype. Is there a tap equivalent?
- **Trading:** swipe a watchlist row to reveal "Buy / Sell / Alert" with no other route; pinch-zoom with no zoom buttons; swipe between stocks with no next/previous control.
- **Skip when:** OS or screen-reader gestures (system back, scrolling); an essential path (a signature).

#### A11Y-TGT-03 · 2.5.7 Dragging Movements · AA
- **Requires:** anything done by dragging also works with a single pointer without dragging.
- **Check:** list every drag. Is there a tap or text-entry alternative?
- **Trading:** **swipe-to-buy / slide-to-confirm** with no "Confirm" button (also unusable with VoiceOver/TalkBack, §7.3). A qty or amount slider with no typed input. Drag-to-reorder watchlist with no "Move up/down". Dragging a sheet is fine: our sheets also have a close or Cancel (`D-01`).
- **Skip when:** dragging is essential (free-hand chart drawing), or it's an OS behaviour.

#### A11Y-TGT-04 · 2.5.2 Pointer Cancellation · A
- **Requires:** single-pointer actions don't complete on the down-event, or can be aborted/undone.
- **Check:** triggered only if the spec says an action fires on touch-down or uses press-and-hold. Otherwise add "actions fire on release" to the handoff.
- **Trading:** hold-to-place-order that places the order the instant the hold completes with no release step.
- **Skip when:** the design doesn't specify down-event behaviour (default is up-event).

#### A11Y-TGT-05 · 2.5.4 Motion Actuation · A
- **Requires:** anything operated by moving the device also works through a UI control, and the motion response can be turned off.
- **Trading:** "shake to refresh prices" with no button and no setting.
- **Skip when:** the app uses no device or user motion.

#### A11Y-TGT-06 · 1.4.13 Content on Hover or Focus · AA
- **Requires:** extra content that appears on hover or focus is **dismissible**, **hoverable** and **persistent**.
- **Check:** native has no hover; check Tooltips or popovers that open on **focus** (external keyboard). Our Tooltip opens on tap, which is a disclosure, not this SC.
- **Skip when:** the content opens on tap; an input-error message.

---

### 5.5 Focus, keyboard and screen readers

These apply to native apps used with an external keyboard, Switch Control, Full Keyboard Access, or a screen reader.

#### A11Y-FOC-01 · 2.1.1 Keyboard · A
- **Requires:** every function works through a keyboard interface.
- **Check:** custom widgets need a keyboard path: Segmented Controls, steppers, chart tools, drag-only features.
- **Trading:** a custom date picker for SIP date with no keyboard support.
- **Skip when:** the function depends on the path of movement (free-hand chart drawing).

#### A11Y-FOC-02 · 2.1.2 No Keyboard Trap · A
- **Requires:** if focus can get into something by keyboard, it can get out by keyboard.
- **Check:** every sheet, embedded chart and picker has an exit in the focus order: the close control, or a Cancel/decline in the footer (`D-01`).
- **Trading:** an embedded charting widget that captures Tab; a consent sheet with the close hidden and no decline button.
- **Skip when:** the screen has no embedded widgets or overlays.

#### A11Y-FOC-03 · 2.1.4 Character Key Shortcuts · A
- **Requires:** single-character shortcuts can be turned off, remapped, or only work when their component has focus.
- **Skip when:** the screen has no shortcuts (current mobile designs have none).

#### A11Y-FOC-04 · 2.4.3 Focus Order · A
- **Requires:** focus moves in an order that preserves meaning.
- **Check:** annotate focus order (AN-02) on screens with sheets and sticky footers. When a sheet opens, focus moves into it; when it closes, focus returns to the trigger (`docs/components/bottom-sheet.md`).
- **Trading:** opening the order sheet from a watchlist row, focus stays behind the sheet; after "Order placed", focus jumps to the top instead of the confirmation.
- **Skip when:** a simple single-column screen where order is obviously right.

#### A11Y-FOC-05 · 2.4.7 Focus Visible · AA
- **Requires:** keyboard-operable UI has a visible focus indicator.
- **Check:** every interactive DS component keeps its `Focus` state (`focus/ring`). Product compositions (rows, chips, cards) that are tappable need one too. `/ds-audit` measures the ring (COL-03).
- **Trading:** watchlist rows and chart range chips with no focus state.
- **Skip when:** the element isn't keyboard operable (static text).

#### A11Y-FOC-06 · 2.4.11 Focus Not Obscured (Minimum) · AA
- **Requires:** a focused component is not *entirely* hidden by author-created content.
- **Check:** sticky layers: the floating Navigation Bar, sticky Buy/Sell footers, banners. Content must scroll clear of them (`docs/patterns/screen-anatomy.md`: leave bottom padding).
- **Skip when:** proper modals (they take focus); partial overlap only (that's AAA 2.4.12, §6).

#### A11Y-FOC-07 · 3.2.1 On Focus · A
- **Requires:** focusing a component doesn't change context.
- **Check:** only triggered if the spec says something happens on focus. "On focus, open the order sheet" is a fail.
- **Skip when:** focus only shows things (a ring). Activation (tap/Enter) opening a sheet is fine.

#### A11Y-FOC-08 · 4.1.2 Name, Role, Value · A
- **Requires:** every UI component has a name and role; states and values can be set and changes are announced.
- **Check:** annotation check (§8): every icon-only button (Icon Button, Compact Button, App Header actions) has a name, every custom control has a role and states, every value-bearing control states its value.
- **Trading:** the watchlist star ("Add RELIANCE to watchlist", pressed/not); the Buy/Sell segment (radio group, selected); a swipe-to-buy control; the eye toggle that hides values on Portfolio.
- **Skip when:** standard native components used unmodified; you still owe names for icon-only ones.

---

### 5.6 Motion, flashing and audio

#### A11Y-MOT-01 · 2.3.1 Three Flashes or Below Threshold · A
- **Requires:** nothing flashes more than three times in any one second, unless below the general and red flash thresholds.
- **Check:** every flash or blink: tick-flash highlights, blinking alerts, full-screen colour pulses. How often, and how big is the combined area (W3C: about 341×256 CSS px in any 10° field)?
- **Trading:** many watchlist rows flashing together on every tick in a volatile market; a full-screen red flash on rejection. **Always `S1` if confirmed** (seizure risk). Fix: ≤ 3/s per area, fades instead of flashes, flash only the changed digit.
- **Skip when:** nothing flashes; a single small cell flashing ≤ 3 times per second.

#### A11Y-MOT-02 · 1.4.2 Audio Control · A
- **Requires:** audio that plays automatically for more than 3 seconds can be paused/stopped or has its own volume.
- **Skip when:** no autoplay audio; sounds under 3 seconds (an order-executed chime).

Reduced motion: honour the OS setting in prototypes (`.claude/rules/accessibility.md`); see A11Y-R-05.

---

### 5.7 Forms

#### A11Y-FRM-01 · 3.3.2 Labels or Instructions · A
- **Requires:** inputs have labels or instructions.
- **Check:** every field has a visible, persistent label (our TextField always shows its label; a placeholder alone fails). Required fields and format rules are stated before entry.
- **Trading:** a trigger-price field with no hint that it must be below LTP for a sell SL; a PAN field with no format hint; an IFSC field with no example.
- **Skip when:** the screen has no input.

#### A11Y-FRM-02 · 1.3.5 Identify Input Purpose · AA
- **Requires:** fields collecting the user's own data on WCAG's input-purpose list (name, email, tel, address parts, postal code, birthday, username, password…) have that purpose identified in code.
- **Check:** annotation check (AN-09): mark each matching field so developers set iOS content type / Android autofill hints.
- **Trading:** KYC full name, email, mobile number, address, PIN code, date of birth.
- **Skip when:** the field isn't on the list: **PAN, Aadhaar, demat/BO ID, client ID, quantity, price, amount**. OTP is covered by AUT-01.

#### A11Y-FRM-03 · 3.2.2 On Input · A
- **Requires:** changing a setting doesn't automatically change context unless the user was told.
- **Check:** selects, radios or toggles that navigate, submit or move focus by themselves.
- **Trading:** a "Delivery / Intraday" toggle that submits the order. Revealing a trigger-price field when "SL" is chosen is a content change, and fine.
- **Skip when:** the change only updates content in place.

#### A11Y-FRM-04 · 3.3.7 Redundant Entry · A
- **Requires:** information already given in the same process is auto-filled or selectable, not typed again.
- **Check:** walk the multi-step flow and list repeated fields.
- **Trading:** KYC asking for the address after DigiLocker supplied it, with no prefill (our pattern: `Style=Filled` prefilled fields, `docs/patterns/forms.md`).
- **Skip when:** re-entry is essential, needed for security (confirming a new MPIN), or the earlier value is no longer valid.

---

### 5.8 Errors

#### A11Y-ERR-01 · 3.3.1 Error Identification · A
- **Requires:** when an input error is detected automatically, the field is identified and the error is described **in text**.
- **Check:** every error state has a text message tied to the field (`State=Error` + ⚠ helper text, `docs/patterns/forms.md`), not just a red border.
- **Trading:** a price outside the circuit band shown only by a red outline; a lot-size violation that just disables "Place order".
- **Skip when:** no automatic validation on the screen.

#### A11Y-ERR-02 · 3.3.3 Error Suggestion · AA
- **Requires:** when the fix is known, suggest it (unless that would compromise security).
- **Check:** does each error message say how to fix it?
- **Trading:** "Enter a price between ₹2,812.40 and ₹3,437.60 (today's circuit limits)". "This contract trades in lots of 50: enter 50, 100, 150…". "Minimum SIP is ₹500". "Add ₹1,240 to place this order".
- **Skip when:** the fix isn't known, or suggesting it would weaken security (don't hint which part of a login was wrong).

#### A11Y-ERR-03 · 3.3.4 Error Prevention (Legal, Financial, Data) · AA
- **Requires:** for legal commitments, financial transactions, or changing/deleting user data, at least one of: **Reversible**, **Checked**, or **Confirmed**.
- **Check:** for each submission, which is present? Orders can't be reversed once executed, so they need Checked or Confirmed.
- **Trading:** orders, SIP/mandate setup, redemptions, "Exit all positions", withdrawals, eSign, pledge/unpledge, deleting a watchlist or alert.
  **House rule (`D-03`):** every order submission gets a review step (Confirmed) unless the user turns it off. A missing review step is a **House** finding even when inline validation (Checked) passes WCAG.
- **Skip when:** the action isn't legal, financial or a change to user data (switching a chart range).

---

### 5.9 Authentication

#### A11Y-AUT-01 · 3.3.8 Accessible Authentication (Minimum) · AA
- **Requires:** no step of authentication needs a cognitive function test (remembering a password, transcribing a code, a puzzle) unless there's an **Alternative**, a **Mechanism** to help (autofill, paste), or the test is object recognition / personal content.
- **Check:** for each auth step: can the field be autofilled and pasted into? Is there a non-memory route (biometric)? Is there a captcha?
- **Trading:**
  - **OTP:** separate cells that accept one character each, so pasting fills one cell → fail. Our OTP Input annotates "paste fills all cells" and SMS autofill (`docs/components/otp-input.md`); check the annotation is on the screen.
  - **MPIN / password:** a custom keypad that blocks paste and password managers → fail unless biometric login is offered.
  - **Captcha** with no alternative → fail.
  - **Transaction PINs / OTP on sell or withdraw** are authentication steps too: same checks.
- **Skip when:** the step isn't authentication; biometric steps; the OTP's expiry itself (a security time limit, TIM-01).

---

### 5.10 Timing, status messages and live data

#### A11Y-TIM-01 · 2.2.1 Timing Adjustable · A
- **Requires:** for each time limit, users can turn it off, adjust it (≥ 10×), or extend it (warned first, ≥ 20 s to extend, at least 10 times), unless an exception applies.
- **Check:** list every timer: session timeout, auto-logout, "quote valid for", OTP resend countdown (OTP Input: 30 s, 3 resends), auto-dismissing confirmations.
- **Trading:** idle logout with no warning ("You'll be logged out in 60 s · Stay logged in"); a KYC step that expires mid-entry and discards data; a confirmation that auto-dismisses and is the *only* place the order ID appears.
- **Skip when:** **Real-time** (market session close, a call-auction window, the fund cut-off time); **Essential** security limits (a time-based OTP; AUT-01 still applies); limits over 20 hours; a confirmation whose information is also elsewhere (the order is in the Orders tab).

#### A11Y-LIV-01 · 2.2.2 Pause, Stop, Hide · A
- **Requires:** (a) moving, blinking or scrolling content that starts automatically, lasts over 5 s and sits alongside other content can be paused, stopped or hidden;
  (b) **auto-updating** content shown alongside other content can be paused, stopped, hidden, or have its update frequency controlled, unless essential.
- **Check:** list what moves or updates on its own. Is it essential to the task on this screen? If not, is there a pause/hide control or a frequency setting?
- **Trading:**
  - Scrolling **ticker / marquee** of indices → needs pause or hide. When resumed, it jumps to current values.
  - **Auto-advancing promo carousel** (IPO, offers) → needs pause.
  - **Watchlist / holdings live prices** while the user reads or fills a form → a pause or refresh-rate setting, *or* a ruling that live prices are essential there (log it in [`decisions.md`](decisions.md) so it isn't re-raised).
  - **LTP on the order** at the moment of ordering → reasonable to treat as essential; note the ruling instead of raising it.
- **Skip when:** the update is essential and the ruling is logged; motion under 5 s; content not shown alongside other content.

#### A11Y-LIV-02 · 4.1.3 Status Messages · AA
- **Requires:** status messages (success, results, progress, errors) that appear without moving focus can be announced by assistive tech.
- **Check:** annotation check (AN-07): every confirmation, inline result, progress state and error summary has an announcement and politeness (polite for success/progress, assertive for urgent errors). Toasts aren't in the DS yet (`docs/patterns/overlays.md`); whatever replaces them still needs AN-07.
- **Trading:** "Order placed · ID 2410…"; "Fetching option chain…"; "3 errors on this form"; "Price alert triggered". **Don't** announce every live price tick.
- **Skip when:** the message comes with a change of context (a sheet that takes focus, a new screen); content revealed by the user's own action.

---

### 5.11 Content and copy

#### A11Y-CPY-01 · 1.1.1 Non-text Content · A
- **Requires:** non-text content has a text alternative; decorative content is hidden from assistive tech.
- **Check:** every icon, image and chart is marked **meaningful** (with alt text, AN-08) or **decorative**. Charts need a text summary or an accessible data view. `Screen Atmosphere` is decorative.
- **Trading:** a sparkline ("Down 1.2% today"); a candlestick chart with no summary; the exchange logo as the only label of the exchange.
- **Skip when:** purely decorative (mark it so); the information is already in adjacent text.

#### A11Y-CPY-02 · 1.3.3 Sensory Characteristics · A
- **Requires:** instructions don't rely only on shape, colour, size, position or sound.
- **Trading:** "Tap the green button to buy"; "Positions in red need attention".
- **Skip when:** the instruction also names the control ("Tap **Buy**").

#### A11Y-CPY-03 · 2.4.2 Page Titled · A
- **Requires:** every screen has a title that describes its topic or purpose, announced on arrival (Top Bar / App Header title, or an annotated title for screens without one).
- **Skip when:** sheets (they need an accessible name, FOC-08, not a screen title).

#### A11Y-CPY-04 · 2.4.4 Link Purpose (In Context) · A
- **Requires:** each link's purpose is clear from its text, or its text plus context.
- **Trading:** five "View all" buttons on Explore, each only clear from its section header (fine if annotated with that context; better: "View all IPOs").
- **Skip when:** buttons with a clear name (FOC-08).

#### A11Y-CPY-05 · 2.4.6 Headings and Labels · AA
- **Requires:** headings and labels describe topic or purpose.
- **Trading:** a section headed "More"; a field labelled "Value" that is really "Trigger price"; a card titled "Details".
- **Skip when:** no headings or labels present.

#### A11Y-CPY-06 · 2.5.3 Label in Name · A
- **Requires:** for controls with visible text, the accessible name **contains** that text (best: starts with it).
- **Trading:** a button showing "Buy" named "Place order"; "Add money" named "Deposit". "Buy RELIANCE" for a "Buy" button is fine.
- **Skip when:** icon-only controls.

#### A11Y-CPY-07 · 3.1.1 Language of Page · A  ·  A11Y-CPY-08 · 3.1.2 Language of Parts · AA
- **Requires:** the screen language, and passages in another language, are identified (AN-13).
- **Trading:** a Hindi version of a screen; a Hindi risk disclaimer on an English screen.
- **Skip when:** English screens in the app's default language; proper names and loan words ("Nifty", "SIP", "demat").

#### A11Y-CPY-09 · 3.2.4 Consistent Identification · AA
- **Requires:** the same function across screens has the same label, icon and name.
- **Check:** compare labels and icons for the same function across frames, and against the vocabulary in `docs/content/voice.md`.
- **Trading:** "Add to watchlist" as a star on one screen and a bookmark on another; "Exit" vs "Square off"; "Funds" vs "Wallet".
- **Skip when:** only one screen in scope; the functions actually differ.

#### A11Y-CPY-10 · 3.2.6 Consistent Help · A
- **Requires:** help repeated across screens sits in the same relative place.
- **Trading:** the KYC help icon in the Top Bar on step 1 and at the bottom on step 3.
- **Skip when:** no help mechanism, or it's on one screen only.

### 5.12 Media (only if the screen has audio or video)

| ID | SC | Level | Requires | Skip when |
|---|---|---|---|---|
| A11Y-MED-01 | 1.2.1 Audio-only and Video-only (Prerecorded) | A | Text alternative (or audio track for video-only) | No such media |
| A11Y-MED-02 | 1.2.2 Captions (Prerecorded) | A | Captions for prerecorded video with audio | No video with audio |
| A11Y-MED-03 | 1.2.3 Audio Description or Media Alternative | A | Audio description or full text alternative | Video adds nothing visual beyond its audio |
| A11Y-MED-04 | 1.2.4 Captions (Live) | AA | Captions for live video with audio | No live video |
| A11Y-MED-05 | 1.2.5 Audio Description (Prerecorded) | AA | Audio description | Visuals fully described in the audio |

Design-time check: there's a place in the design for the caption toggle, the transcript link and the audio-described version.

---

## 6. AAA recommendations (never blockers)

Report as `S3` · **Recommendation**, and only when the screen triggers them.

| ID | SC | Name | Recommendation |
|---|---|---|---|
| A11Y-R-01 | 1.4.6 | Contrast (Enhanced) | Aim higher on dense numeric lists (holdings, option chain); `/ds-audit` measures |
| A11Y-R-02 | 2.5.5 | Target Size (Enhanced) | 44×44 for all targets: already our house rule |
| A11Y-R-03 | 2.4.12 | Focus Not Obscured (Enhanced) | No part of the focused item hidden by sticky layers |
| A11Y-R-04 | 2.4.13 | Focus Appearance | Focus indicator ≥ a 2 px perimeter with a 3:1 change; check our `Focus` states with `/ds-audit` |
| A11Y-R-05 | 2.3.3 | Animation from Interactions | Honour "Reduce motion": chart transitions, parallax |
| A11Y-R-06 | 2.2.5 | Re-authenticating | After a session expires, keep the draft order or KYC entries after re-login |
| A11Y-R-07 | 2.2.6 | Timeouts | Tell users how long inactivity can last before data is lost |
| A11Y-R-08 | 2.2.4 | Interruptions | Promo pop-ups and "rate us" prompts can be postponed or turned off |
| A11Y-R-09 | 3.1.3 | Unusual Words | Inline definitions (Tooltip) for LTP, NAV, XIRR, OI, IV, circuit limit |
| A11Y-R-10 | 3.1.4 | Abbreviations | Expand CNC, MIS, NRML, SL-M, GTT, F&O, ELSS on first use or on tap |
| A11Y-R-11 | 3.1.5 | Reading Level | A plain-language summary next to risk disclosures and margin rules |
| A11Y-R-12 | 3.3.5 | Help | Context help on order types, product types and margin |
| A11Y-R-13 | 3.3.6 | Error Prevention (All) | Review or undo for every submission, not just financial ones |
| A11Y-R-14 | 3.3.9 | Accessible Authentication (Enhanced) | No object-recognition or personal-content tests in login |
| A11Y-R-15 | 1.4.8 | Visual Presentation | Research reports: line length ≤ 80 characters, no justified text |
| A11Y-R-16 | 2.4.10 | Section Headings | Long stock pages and reports broken up with headings |
| A11Y-R-17 | 1.3.6 | Identify Purpose | Mark up regions and icon purposes so personalisation tools can adapt them |

**AAA not tracked** (raise only if the team opts in): 1.2.6–1.2.9, 1.4.7, 1.4.9, 2.1.3, 2.2.3 (markets are real-time), 2.3.2, 2.4.8, 2.4.9, 2.5.6, 3.1.6, 3.2.5.

---

## 7. Mobile notes (iOS and Android)

### 7.1 Touch targets: three numbers, three meanings

| Standard | Minimum | Status here |
|---|---|---|
| WCAG 2.5.8 Target Size (Minimum), AA | 24×24 pt / dp, or the Spacing/Equivalent exceptions | **The floor.** Below this with no exception = WCAG fail |
| Our rule (`.claude/rules/accessibility.md`) = Apple HIG | **44×44 pt** for every tappable target | **House rule**, iOS and Android designs |
| Android Material Design | **48×48 dp** | **House rule** for primary actions on Android (`D-04`): annotate the hit area (AN-11) |

- Measure the **hit area**, not the drawn icon. A 20 pt icon with 12 pt padding on each side is a 44 pt target; annotate it so developers don't shrink it.
- Our control heights (`.claude/rules/layout.md`): Button and Icon Button **xs 28 · sm 32 · md 40 · lg 52 · xl 56**. xs–md need extra hit area to reach 44;
  md (40) on a primary action also needs a 48 dp hit area on Android. lg and xl meet both. The primary screen CTA is `lg`.
- Severity: a primary action (Buy, Sell, Place order, Confirm, Exit, Invest, Withdraw) below the house minimum is `S2` · House; anything else is `S3` · House. Below 24 with no exception is a WCAG finding.

### 7.2 Gestures
- Every custom gesture needs a single-tap route (TGT-02, TGT-03): swipe-to-buy, swipe-row actions, pinch-zoom charts, drag-to-set price lines,
  pull-to-refresh as the *only* refresh. Sheets: drag-to-dismiss plus a close or Cancel (`D-01`).
- OS gestures (back swipe, notification shade) aren't ours; don't raise them.

### 7.3 Screen readers (VoiceOver, TalkBack)
- With a screen reader on, **swipe moves between elements and double-tap activates.** A custom swipe gesture is intercepted, so it needs an accessible action or a button.
- Row swipe actions are exposed as **custom actions** so users pick "Buy / Sell / Set alert" from a menu (AN-05).
- Per element, developers need: **label**, **trait/role**, **value**, **hint** (optional). iOS: `accessibilityLabel`, `accessibilityTraits`, `accessibilityValue`, `accessibilityHint`.
  Android: `contentDescription`, role description, `stateDescription`. The designer supplies the words (§8).
- Group a watchlist row into one element ("RELIANCE, NSE, ₹2,941.10, up 1.2%") instead of four stops.
- Live prices: don't announce every tick. Announce the user's own order and alert events (LIV-02).

### 7.4 Orientation and text size
- Portrait frames only; the app never locks orientation; core screens carry a landscape reflow rule (`D-02`, LAY-03).
- Text size: one Dynamic Type step larger checked in Figma; 200% behaviour annotated (TXT-01): rows grow, prices wrap below the name rather than truncate.

---

## 8. Handoff annotations the designer owes

A design without these can't be built accessibly, however good it looks. `/prd-to-screens` adds them at step 5½; `/design-review` checks presence, not implementation.
Use Figma's native annotations (Dev Mode), with the `AN-xx` ID at the start of each label.

| ID | Annotation | What to mark | Example |
|---|---|---|---|
| AN-01 | Reading order | The order a screen reader reads | Stock name → price → change → chart summary → Buy/Sell |
| AN-02 | Focus order | Keyboard order; where focus goes when a sheet opens and closes | Order sheet: focus to the sheet title on open, back to the row's Buy on close |
| AN-03 | Accessible name | Name for every icon-only control and any control whose visible text isn't enough | Star: "Add RELIANCE to watchlist"; close: "Close order sheet" |
| AN-04 | Role | Role for custom controls | Buy/Sell segment = radio group; swipe-to-buy = button |
| AN-05 | State, value and actions | Selected/pressed/expanded/disabled states; current values; custom actions | "CNC, selected"; stepper "Qty 10"; row actions "Buy, Sell, Set alert" |
| AN-06 | Headings and structure | Heading levels; groups; label/value pairs | "Holdings" heading 1, "Equity" heading 2 |
| AN-07 | Live regions | Which messages announce, polite or assertive | Order placed = polite; order rejected = assertive; prices = off |
| AN-08 | Text alternatives | Alt text for meaningful images/charts; "decorative" for the rest | Sparkline summary; `Screen Atmosphere` = decorative |
| AN-09 | Input purpose | Purpose for user-data fields on WCAG's list | Email = email; mobile = tel; DOB = birthday |
| AN-10 | Errors | Message text; which field it belongs to; error summary behaviour | "Price must be a multiple of ₹0.05", tied to Price |
| AN-11 | Hit areas | Target size where it's larger than the visual; 48 dp on Android primary actions | Steppers: 44×44 pt hit area around 24 pt icons |
| AN-12 | Gesture and motion alternatives | The non-gesture route; reduced-motion behaviour | Swipe-to-buy → "Confirm buy" button; tick flash → fade when Reduce Motion is on |
| AN-13 | Language | Screen language; passages in another language | Hindi disclaimer `hi` on an English screen |
| AN-14 | Timing behaviour | Timeout length, warning, extend action | "Warn at 14 min, 60 s countdown, Stay logged in" |
| AN-15 | Text size and orientation | 200% text behaviour and landscape reflow for core screens (`D-02`) | "Rows grow; price wraps below the name; landscape = same single column" |

---

## 9. Severity

Same scale as [`ux-governance.md`](ux-governance.md) §3.

| Severity | Use when | Examples |
|---|---|---|
| `S1` (Blocker) | An AA failure on a **core task** (log in, KYC, add/withdraw money, place/modify/cancel an order or SIP, act on an alert) that stops or seriously misleads a user with a disability, **or** any confirmed 2.3.1 flashing failure, **or** a 3.3.4 failure on a financial submission. Fix before handoff. | Swipe-to-buy with no tap route; OTP cells that block paste with no alternative |
| `S2` (Major) | An AA failure off the core path, or on the core path where a workaround exists; a house-rule shortfall on a **primary** action. | Colour-only P&L on the Portfolio summary; Buy button 36 pt tall (House) |
| `S3` (Minor) | AAA recommendations; house-rule gaps on secondary controls; missing annotations where the intent is obvious; copy polish. | No inline definition for "XIRR"; a close icon below 44 pt but passing 2.5.8 |

Tags alongside severity: **WCAG** (fails an SC), **House** (fails a house rule only), **Recommendation** (AAA), **Needs annotation** (design can't show it yet), **Question** (needs a decision or more frames).

---

## 10. Report

Accessibility findings go in the **single** `/design-review` report ([`ux-governance.md`](ux-governance.md) §9), alongside UX findings, with one verdict.
For accessibility, fill in: the Tag, the `A11Y-*` ID with SC and level (e.g. `A11Y-TGT-03 · 2.5.7 (AA)`), **Needs annotation**, **Questions**,
**Considered and cleared** (one line each, naming the exception), and the contrast pairs sent to `/ds-audit`.

---

## 11. Worked example: mobile order sheet (iOS, final)

**Task walked:** from the RELIANCE detail page, tap Buy → set Qty 10, Limit ₹2,940 → swipe to buy → see confirmation.

**Triggered** (from the index): COL-01, COL-02, COL-03, TXT-01, LAY-02, TGT-01, TGT-02, TGT-03, FOC-04, FOC-05, FOC-08, FRM-01, ERR-01, ERR-02, ERR-03, LIV-01, LIV-02, CPY-06.
**Not triggered**, so not listed: authentication, timing, media, motion actuation, shortcuts, language.

| # | Severity | Tag | ID · SC (level) | Where | Issue | Fix |
|---|---|---|---|---|---|---|
| 1 | S1 | WCAG | A11Y-TGT-03 · 2.5.7 (AA) | Footer, swipe-to-buy | The only way to submit is dragging; VoiceOver users can't do it either | Add a "Buy 10 RELIANCE" button (`Button Solid · Success · lg`) that opens the review step; keep the swipe as a shortcut |
| 2 | S2 | WCAG | A11Y-COL-01 · 1.4.1 (A) | Header, day change "12.40 (0.42%)" | Up/down shown only by `market/gain` / `market/loss` | Add sign and arrow: "▲ +12.40 (+0.42%)" |
| 3 | S2 | WCAG | A11Y-ERR-02 · 3.3.3 (AA) | Price field error | "Invalid price" when the tick size is known | "Price must be a multiple of ₹0.05" |
| 4 | S2 | House | A11Y-ERR-03 · 3.3.4 (AA) | Swipe-to-buy | Inline validation exists (Checked, so WCAG passes) but there's no review step | Add the review step (`D-03`) |
| 5 | S3 | Needs annotation | A11Y-LIV-02 · 4.1.3 (AA) | "Order placed" confirmation | No announcement spec | AN-07: polite; include order ID and status |
| 6 | S3 | Needs annotation | A11Y-FOC-08 · 4.1.2 (A) | Buy/Sell segment, CNC/MIS toggle | Role and selected state not specified | AN-04/AN-05: radio group, "Buy, selected" |

**Considered and cleared:**
- A11Y-TGT-01 · 2.5.8: Qty `−`/`+` steppers 20×20 pt with 4 pt between them fail Spacing, but **Equivalent** applies: the Qty field takes typed input and is 52 tall. No WCAG finding; the house rule makes it `S3`, folded into AN-11 (44 pt hit areas).
- A11Y-LIV-01 · 2.2.2: live LTP on the order is **essential** at the point of ordering; no finding (record the ruling in `decisions.md` the first time).
- A11Y-COL-02 · 1.4.3: `text/placeholder` in empty fields sent to `/ds-audit` rather than judged from the screenshot.

**Self-check notes:** finding 2 was first drafted as `S1`; downgraded because the order itself doesn't depend on the day-change colour.
A draft finding on 2.4.11 (sticky footer) was dropped: the footer only partly overlaps the last focusable row (partial overlap is AAA 2.4.12).

---

## 12. Checklist (designer, before handoff)

- [ ] Walked the main task end to end; every gesture has a tap route; every sheet has a close or Cancel.
- [ ] No meaning carried by colour alone (P&L, Buy/Sell, status, chart series, errors).
- [ ] Contrast pairs sent to `/ds-audit` in Light and Dark, including tick-flash and error states.
- [ ] Targets ≥ 44×44 pt; Android primary actions annotated to 48 dp; anything under 24 has a named exception.
- [ ] Focus state on every interactive component and tappable composition; nothing sticky can fully cover a focused item.
- [ ] Every field has a persistent label; every error says what's wrong and how to fix it.
- [ ] Orders and money movements have a review step (`D-03`).
- [ ] Login and OTP accept paste/autofill, or there's a biometric alternative.
- [ ] Timers warn and extend, or a named exception applies.
- [ ] Moving and auto-updating content can be paused, or is ruled essential and logged.
- [ ] Nothing flashes more than three times a second over a large area.
- [ ] Annotations AN-01 to AN-15 present where triggered.
- [ ] Core screens checked one Dynamic Type step larger; 200% text and landscape behaviour annotated (AN-15).
