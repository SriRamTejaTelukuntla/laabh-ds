# Lists, cards & data display

## Cards
| Card | Spec |
|---|---|
| Content card | `surface/card` · `glass/edge` 1px · `elevation/card` · `radius/18` · padding `space/20` · gap `space/4`–`space/12` |
| Hero card ("Your investments") | `surface/card` · `border/brand-soft` · `elevation/card-brand` · `radius/18` |
| Summary card (result screens) | Content card with a header row + 2–4 label/value rows |
| Tile (index tiles) | `elevation/tile` · `radius/12` · padding `space/12` · gap `space/4`; fill `surface/page` + `surface/gain-tint`/`loss-tint` |
| Inner card / control inside a card | **No shadow**: `glass/control`, `radius/12`, `elevation/inset` at most |

## List card (watchlist, holdings, orders)
- One card holds the list: content card with padding `space/4` top/bottom and `space/16` sides.
- Rows 64 tall, horizontal, gap `space/12`: Avatar 36 (logo) · name `body-lg/Medium` + subtitle `body-sm/Regular` `text/secondary` · right-aligned price `num-body-lg/Medium` + change `num-body-sm/Medium` in `market/*`.
- Hairlines between rows: 1px `glass/hairline`, **inset 52** from the left so they start after the avatar. No hairline after the last row.
- Lists longer than ~8 rows: show 5–7 and a Ghost "View all" button.

## Numbers
_Formatting from the reference screens; abbreviations (Cr/L) are proposed._
- Figures use `num-*` styles. Currency is `₹` with Indian grouping: ₹1,84,250.75 · ₹25,000 · ₹5,00,000.
- Changes are always signed and coloured with `market/*`: `+1.09%` gain, `−0.42%` loss (true minus sign), `0.00%` flat in `market/flat`.
- Show both absolute and % change where space allows: `+₹1,240.50 (+1.09%)`.
- Large figures can abbreviate: ₹1.2 Cr, ₹45.6 L (Indian units), never "M/B".

## Section headers
- Overline `caps-md/Semibold` `text/secondary`, inset 4 from the card edge, `space/24` above, `space/8`–`12` below. Optional Ghost "View all" on the right.

## Empty, loading, error (proposed: not in the reference screens yet)
- Empty: icon tile + one line + a CTA ("Add stocks to your watchlist").
- Loading: skeleton rows in `surface/neutral-muted` at the row's shape (not spinners for lists).
- Error: Alert `Danger` with a retry action.
