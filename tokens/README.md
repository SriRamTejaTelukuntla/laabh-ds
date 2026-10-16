# tokens/

Generated from the DS Figma file by `/ds-sync`. **Do not edit by hand.** Change Figma, then re-sync.

| File | Contents |
|---|---|
| `primitives.color.json` | 164 raw colours (blue, navy, neutral, ink, frost, violet, green, red, amber, teal, pink, sky, base, alpha) |
| `primitives.typography.json` | Font families, weights, size and line-height scales |
| `primitives.spacing-radius.json` | `space/*` and `radius/*` |
| `semantic.color.json` | 186 semantic colours. `$value` = **Light**, `$extensions.modes.Dark` = Dark |
| `semantic.typography.json` | Role sizes and line heights. `$value` = **Mobile**, Tablet/Desktop in `$extensions.modes` |
| `styles.text.json` | 99 text styles (references to the tokens above) + Figma style keys |
| `styles.effect.json` | 13 `elevation/*` effect styles (layers bound to `elevation/*` colour tokens) + keys |
| `_meta.*.json` | Export time, file key, collection IDs/keys/modes, counts |

Format: [W3C DTCG](https://tr.designtokens.org/format/) (legacy dialect: hex strings, `px` strings).
References look like `{blue.400}` and resolve across files. Figma's slash names map to dots (`surface/brand` → `surface.brand`).

**How it's produced:** `scripts/figma/export-variables.js` and `export-styles.js` run inside the DS file (via `use_figma` or
`figma_execute`). Their JSON result is written by `python3 scripts/write-tokens.py <result.json>`, which fails if any count
differs from Figma. (Don't use figma-console's `figma_export_tokens`: in Oct 2026 it read a stale cache and dropped variables.)
