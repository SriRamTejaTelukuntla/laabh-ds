# Light & Dark

Every screen ships in both. The mode lives on the **Color Tokens** collection (`Light` `2:1`, `Dark` `2:2`). Set it on the screen frame
and everything inside follows: colours, glass fills, and mode-aware elevation styles.

| | Light | Dark |
|---|---|---|
| Page | `surface/page` = white | `surface/page` = ink 900 |
| Cards & controls | Solid white | Glass: frost 4–14% fills |
| Edges | Navy hairlines (`glass/edge`, `glass/hairline`) | Frost hairlines |
| Depth | Soft black shadows | Inner highlights, deeper shadows, background blur (24–30px) |
| Atmosphere | Grid only | Grid + spotlight (`Screen Atmosphere` component; `atmosphere/spotlight` is transparent in Light) |
| Brand / market colours | Same hues, Dark uses lighter steps for text and icons (e.g. `text/brand` blue 400 → 250) |

## Process
1. Build Light with tokens only.
2. Duplicate → rename `— Dark` → set Color Tokens mode **Dark** on the frame → place it **to the right** of Light.
3. Screenshot both. Any problem in Dark is a token problem: report it, never patch with raw values.

## Checks
- Text contrast in both modes (glass surfaces: check against the composited colour).
- Images and logos: keep the logo tile (`elevation/logo`, white tile) in Dark so dark logos stay visible.
- The `Screen Atmosphere` instance must stay behind content (first child) in both modes.
