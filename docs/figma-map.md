# Figma map

IDs verified Oct 2026. Node IDs are valid **in the DS file only**. In feature files, use component/style/variable **keys** (`scripts/build-kit.py`).

## Files

| File | fileKey | Role |
|---|---|---|
| Laabh — Design System | `mmAhXn4vJKlmuThcAMgGss` | Library, published (read-only for product work) |
| Laabh — <Feature> | one file per feature (see below) | Where `/prd-to-screens` builds that feature's screens |

## Feature files

Every feature has its own Figma file, `Laabh — <Feature>`. There's no single product file for the whole app.
The DS library is published to the whole organisation, so a new file gets it by default (if not, turn it on in Assets → Libraries).
When the DS publishes an update, each file shows "Library updates available": accept it there before building or reviewing.
The file's link also goes in the header of `prds/<feature>/plan.md`. `/prd-to-screens` adds the row here.

| Feature | File | fileKey | Plan |
|---|---|---|---|
| — | | | |

## Variable collections

| Collection | Collection ID | Key | Modes (modeId) | Vars |
|---|---|---|---|---|
| Color Primitives | `VariableCollectionId:2:2` | `6a54a2191a1381de06926ce7fbf437348551bf05` | Value `2:0` | 164 |
| Color Tokens | `VariableCollectionId:2:112` | `f10929d83247605f5e490e15a6d3ed57e1ce70ce` | Light `2:1`, Dark `2:2` | 186 |
| Typography Primitives | `VariableCollectionId:2:234` | `00fe2be19c8c4ab791bce372d11b4ef4b13d1e87` | Value `2:3` | 44 |
| Spacing & Radius Primitives | `VariableCollectionId:2:261` | `30e508c183603bcfc4b39e178c4e98a5466fce30` | Value `2:4` | 37 |
| Typography Tokens | `VariableCollectionId:2:290` | `5102cecaeeef8b6305278786c4ecbf7f26aea9ce` | Mobile `2:5`, Tablet `2:6`, Desktop `2:7` | 28 |

Styles: 99 text styles (incl. doc-only `mono/Regular`), 13 effect styles (`elevation/*`), 0 paint styles. Keys in `tokens/styles.*.json`.

## Pages

| Section | Page | Page ID |
|---|---|---|
| FOUNDATIONS | Documentation | `1:2` |
| | Colors | `1:3` |
| | Typography | `1:4` |
| | Spacing & Radius | `1:5` |
| | Icons | `1:6` |
| | Elevation | `1:7` |
| COMPONENTS | Alert | `49:2` |
| | Avatar | `1:10` |
| | Badges | `1:11` |
| | Bottom Sheet | `49:3` |
| | Buttons | `1:12` |
| | Checkbox | `1:13` |
| | Dropdown | `1:14` |
| | Option Card | `49:4` |
| | OTP Input | `49:5` |
| | Radio | `1:15` |
| | Segmented Control | `1:16` |
| | Step Indicator | `1:17` |
| | Switch | `1:18` |
| | System Components | `101:128916` |
| | Tabs | `1:19` |
| | TextArea | `1:20` |
| | TextField | `1:21` |
| | Timeline | `49:6` |
| | Tooltip | `1:22` |
| | Top Bar | `49:7` |
| PRODUCT COMPONENTS | App Header | `107:183567` |
| | Screen Atmosphere | `173:92320` |
| PRODUCT | Selected Screens (reference only) | `101:129022` |
| ARCHIVE | Ignore_Sandbox (never use) | `1:38` |

Each component page has `<Name> — Variants`, `— Reference`, and on most pages `— Components` and `— Patterns` frames,
with `— Dark` copies to the right set to Dark mode.
