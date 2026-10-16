# Navigation

| Situation | Pattern |
|---|---|
| Step-by-step flow | **Top Bar**: back (arrow-left), step caption, title, help; stage bar. Ends on a result screen with `Progress=Off` or no Top Bar |
| Main app tabs | **App Header** `Title`/`Search` + bottom **Navigation Bar** (5 tabs: Explore, Watchlist, Orders, Portfolio, Funds) |
| Drill-in from a tab | App Header `Back` or `Back + Title`; the navigation bar stays hidden on deep detail screens unless the PRD says otherwise |
| Sections within a page | `Tab Bar/Line` |
| Views of the same data | Segmented Control |
| Focused sub-task | Bottom Sheet over the current screen |
| Account / settings | Avatar in App Header → Account screen (`Centered title`) |

## Navigation Bar: gap in the DS
The reference screens use a local floating glass pill: 358×64 inside a 390 frame, padding 6, gap 2, fill `glass/nav`,
`elevation/nav`, `radius/full`. It has 5 tabs (icon + label, 67×50) and the selected tab is `surface/brand-subtle`.
It is **not a component yet**. Until it is:
- Copy it from the reference screen `Watchlist` (`101:139639`) rather than drawing one.
- Flag it in the plan as a gap. **First `/new-component` candidate.**

## Back behaviour (annotate in plans)
- Flow back goes to the previous step with data kept. Leaving a flow mid-way asks for confirmation (sheet).
- Result screens have no back; the CTA moves forward.
