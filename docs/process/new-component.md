# Process: adding a new component

Agent drafts, designer refines, DS owner approves. Run with `/new-component`.

```
1 Propose → 2 Spec → 3 Tokens → 4 Agent draft → 5 Designer refine → 6 Review → 7 Document → 8 Publish
```

| # | Step | Who | Output |
|---|---|---|---|
| 1 | **Propose**: the need, where it appears (2+ screens or a clear system gap), why existing components can't do it | Anyone | Short proposal in chat → `docs/proposals/<name>.md` |
| 2 | **Spec**: anatomy, variants/props, states, sizes, content rules, a11y, Light/Dark behaviour; check naming against `.claude/rules/naming.md` | Agent + designer | Spec section in the proposal |
| 3 | **Tokens**: map every value to existing tokens. If a new token is truly needed, propose name + Light/Dark values | Agent, DS owner approves new tokens | Token list (new ones flagged) |
| 4 | **Agent draft** in the DS file: new page `↳ <Name>` under COMPONENTS (or PRODUCT COMPONENTS for product-specific), frames `— Variants` (component set), `— Reference`; all values bound; screenshot | Agent | Draft component set, `Status: draft` |
| 5 | **Designer refine**: visual polish in Figma; agent re-checks bindings after every round | Designer | Refined set |
| 6 | **Review checklist** (below) | DS owner | Approve / changes |
| 7 | **Document**: `docs/components/<name>.md` from `_template.md` + AUTO block via `scripts/figma/inspect-components.js` (later refreshes: `scripts/write-component-docs.py`); add a row to `docs/index.md`; update rules/patterns if behaviour is new; CHANGELOG entry (minor) | Agent | PR via `/share-changes` |
| 8 | **Publish**: DS owner merges the PR, publishes the Figma library with the same version note, runs `/ds-sync` | DS owner | Version tag, library update |

## Review checklist
- [ ] Component set with sensible defaults (the most common variant is the default)
- [ ] Properties: variants for Style/Tone/Size/State/Selection; booleans `Show …`; text props for every editable string; instance-swap for icons/content
- [ ] Every fill/stroke/radius/padding/gap bound to a token; every text uses a style; effects use `elevation/*`; corner smoothing 0.6
- [ ] All states: Default, Pressed/Hover, Focus, Disabled, and Error/Success where relevant
- [ ] `— Dark` copies of the doc frames to the right, set to Dark; looks right through tokens alone
- [ ] Contrast AA in both modes; hit target ≥ 44; non-colour cues
- [ ] Auto layout, resizes correctly (Fill/Hug), no detached nested instances
- [ ] Doc written, index updated, CHANGELOG entry, `Status` set (`beta` first, `stable` after use in 2 features)

## Changing or removing a component
- Breaking changes (renamed/removed props or variants) are a **major** version. Mark the old one `deprecated` in its doc with the replacement, keep it for one release, then remove.
