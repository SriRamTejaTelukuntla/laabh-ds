# Rule: naming

**Figma layers and frames**
- Screen frames: `<ID> <Screen name> — <Light|Dark>`, e.g. `B03 Order review — Light`. IDs are per feature: a letter + 2 digits, assigned in `plan.md`.
- Group screens into a Section per flow step: `<n> · <Step name>`, e.g. `2 · Identity`.
- Layers inside screens: plain, purposeful names (`Header`, `Holdings card`, `Footer`). Never `Frame 123`.
- Light and Dark frames of one screen share the same name apart from the suffix.

**Components (DS file)**
- Component sets: Title Case nouns (`Option Card`, `App Header`). Sub-parts: `<Parent> <Part>` (`Dropdown Item`).
- Variant properties: `Style`, `Tone`, `Size` (`xs|sm|md|lg|xl`), `State` (`Default|Hover|Pressed|Focus|Disabled|Error|Success`), `Selection`.
- Booleans start with `Show ...`. Text properties are nouns (`Label`, `Title`, `Description`).
- Doc frames on a component page: `<Name> — Variants | Components | Patterns | Reference`, Dark copies suffixed `— Dark` and placed to the right.

**Tokens and styles**
- Variables: lower-case, slash groups, kebab-case leaves (`surface/brand-subtle-hover`).
- Text styles: `<role>/<Weight>`. Effect styles: `elevation/<level>`. Icons: `icon/<lucide-name>`.

**Repo**
- Component docs: `docs/components/<kebab-name>.md`. Feature work: `prds/<kebab-feature>/`.
