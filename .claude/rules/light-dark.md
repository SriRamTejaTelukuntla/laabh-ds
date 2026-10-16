# Rule: Light and Dark

Every screen ships in both modes.

1. Build in **Light** mode first with semantic tokens only.
2. When Light is approved, duplicate the frame, rename `— Light` to `— Dark`, set the `Color Tokens` mode to **Dark** on the copy, and place it **to the right** of the Light frame (same y, 80px gap, or the next column in the section).
3. Screenshot both. Dark must work through tokens alone. If Dark needs a manual fix, the token is wrong: report it, don't patch it.

**Visual language (it comes from the tokens; don't fake it):**

| | Light | Dark |
|---|---|---|
| Surfaces | Solid white (`surface/card`, `glass/*` resolve to white) | Glass: frost 4–14% fills over `surface/page` (ink 900) |
| Edges | Navy hairlines (`glass/edge`, `glass/hairline`) | Frost hairlines |
| Depth | Soft black shadows | Inner highlights, deeper shadows, background blur |
| Atmosphere | Subtle grid (`Screen Atmosphere`) | Grid + spotlight (same instance; it switches with the mode) |

- `elevation/*` effect styles are mode-aware. Apply the style and let the mode do the rest.
- **Inner cards get no shadow.** Only the outermost card in a stack takes an elevation.
- Keep effects subtle. Never add extra shadows or glows beyond the elevation styles.
