# Icons

**Lucide 1.57**, 1,890 icons as components named `icon/<lucide-name>` on the Icons page (`1:6`), library frame `101:128882`.
Find names at lucide.dev; the Figma name is `icon/` + the Lucide name (e.g. `icon/arrow-left`, `icon/circle-help`, `icon/trending-up`).

| Property | Value |
|---|---|
| Grid | 24×24 |
| Stroke | 2px, round caps and joins |
| Colour | Stroke bound to `icon/primary`; override with another `icon/*` token only |
| Sizes in components | 24 default · 20 in md controls · 16 in sm controls/badges · 12–14 in Compact Button and badges |

## Rules
- Use the component instance, swap it through the parent's icon slot (instance swap), and colour it with `icon/*` tokens.
- Never import SVGs or icons from other sets. If Lucide lacks a glyph, request one via `/new-component`.
- Meaningful icons need a text label or a layer name that says what they do. Decorative icons sit next to text.
- Common picks: back `arrow-left`, close `x`, help `circle-help`, info `info`, search `search`, add `plus`, gain `trending-up`, loss `trending-down`, bank `landmark`, verify `badge-check`.
