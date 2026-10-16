# Screen anatomy

Four screen types cover almost everything. Build top to bottom in **auto layout** on a **390×844** frame filled with `surface/page`.
Taken from the reference screens (`docs/references/selected-screens.md`).

## 1 · Flow step (onboarding, KYC, any multi-step task)
```
Screen frame (390×844, fill surface/page)
├─ Screen Atmosphere      instance, first child, absolute (0,0), left-right + top: grid + spotlight (Dark)
├─ Status Bar             instance, 48
├─ Top Bar                instance, Progress=On, "Step n of N · <Stage>", title
├─ Body                   vertical, padding 16 top / 20 sides, gap space/24, Fill
│  ├─ Step Heading        vertical, gap space/8
│  │  ├─ Title            display-md/Semibold, text/primary ("What's your mobile number?")
│  │  └─ Description      body-lg/Regular, text/secondary (one or two lines: why we ask)
│  └─ Fields / choices    TextField md, Dropdown md, Segmented Control (with label), Option Cards
├─ Footer                 vertical, padding 12 / 20, gap space/12
│  └─ Primary CTA         Button Solid · Brand · lg (52), Fill width ("Continue", "Send OTP")
└─ Home Indicator         instance, 34
```

## 2 · Result (submitted, success, failure)
Same as a flow step but **no Top Bar** (or `Progress=Off`). The Step Heading gains an **icon tile** above the title:
64×64, `radius/full`, fill `surface/<tone>-subtle`, icon in `icon/<tone>`. Follow with a **summary card** and one CTA ("Go to home").

## 3 · App tab screen (Explore, Watchlist, Orders, Funds, Portfolio)
```
Screen frame
├─ Screen Atmosphere      instance (as above): grid + spotlight, "colour behind glass"
├─ Status Bar
├─ App Header             Type=Title (or Search on Explore)
├─ Content sections       each: padding 20 sides; 24 between sections
│  e.g. index tiles row · chips row (Tab Bar/Solid) · list card · summary cards
├─ Navigation bar         floating glass pill above the Home Indicator (see navigation.md: not yet a component)
└─ Home Indicator
```
Content scrolls under the navigation bar; leave bottom padding so the last item clears it.

## 4 · Detail screen (Stock detail, Collection detail, Analysis)
App Header `Back` / `Back + Title` → hero (name, price `num-display-xl`, change badge) → `Tab Bar/Line` for sections →
section content → sticky footer with the action (e.g. Buy `Solid · Success` + Sell `Solid · Danger`, equal widths).

## Always
- Status Bar and Home Indicator on every full screen. Library instances are 393 wide, so set them to Fill on 390 frames.
- One primary CTA per screen, in the footer.
- Name frames `<ID> <Screen name> — Light|Dark`. Dark copy to the right.
