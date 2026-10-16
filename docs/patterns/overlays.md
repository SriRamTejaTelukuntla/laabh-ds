# Sheets & overlays

| Need | Use |
|---|---|
| Focused task / decision / consent over a screen | Bottom Sheet (+ Sheet Scrim), content in the `Content` slot |
| Pick from a list | Dropdown Menu under its field |
| Explain a term | Tooltip from an info icon |
| Confirm something destructive | Bottom Sheet, `Footer=Two` (Danger action + Cancel) |
| Transient confirmation ("Added to watchlist") | Toast: **not in the DS yet** (gap) |

## Bottom sheet recipe
1. Duplicate the underlying screen frame as a new state frame (`<ID> <Screen> · <Sheet name> — Light`).
2. Add `Sheet Scrim` (full screen) above the content, then the `Bottom Sheet` instance pinned to the bottom with an 8px inset.
3. Build the content as `Sheet Content/<Name>` (product component, PRODUCT COMPONENTS page) and swap it into `Content`.
4. Keep it under 70% of the screen height.
