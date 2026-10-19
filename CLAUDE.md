# Laabh DS: agent guide

This repo is the **written half of the Prasad Glass design system** used by the Laabh app.
Figma holds the values (variables, styles, components). This repo holds how to use them:
rules, component docs, patterns, the token export, and the skills that turn PRDs into Figma screens.

Read this file fully. Then load only the docs your task needs (see "Where to look").

## Key facts

| | |
|---|---|
| DS Figma file | "Laabh — Design System", fileKey `mmAhXn4vJKlmuThcAMgGss` (library: read, don't edit) |
| Product Figma file | Separate file that uses the DS as a published library. Key is in `docs/figma-map.md` |
| Default canvas | **390×844** (iPhone 16e/17e, the smallest current iPhone). Check dense screens at 375×667 (SE) |
| Modes | Color Tokens: `Light` / `Dark`. Typography Tokens: `Mobile` / `Tablet` / `Desktop` |
| Fonts | Inter (UI), Space Grotesk (numbers `num-*`, and titles `display-md/xl/Semibold`), JetBrains Mono (docs only) |
| Icons | Lucide, components named `icon/<lucide-name>`, 24px, 2px stroke |
| Accessibility bar | WCAG 2.2 AA + house rules (`docs/ux/accessibility.md`) |
| Platforms | iOS + Android (web not in scope yet). Decisions that shape the rules: `docs/ux/decisions.md` |

## Golden rules (details in `.claude/rules/`)

1. **Components first.** Build from DS component instances. Never redraw something a component already does.
2. **Tokens only.** Every fill, stroke, radius, gap and padding is bound to a variable. Every text node uses a text style. Every shadow uses an `elevation/*` effect style. No raw hex or px.
3. **Light and Dark, always.** Build Light, duplicate, set the copy to Dark mode, place it to the right, and check both.
4. **Ask before structural or destructive changes**, in any Figma file. Never edit DS masters from a product task.
5. **Checkpoint, don't sprint.** Show a plan, build one screen, show a screenshot, wait for an OK, then continue.
6. **Verify visually.** Screenshot after every build step. Fix clipping, overflow, hug-vs-fill mistakes and misalignment before reporting.
7. **No gaps filled silently.** If a PRD needs something the DS lacks, stop and propose `/new-component`. Don't improvise a one-off.
   The same goes for a PRD request that breaks a trading-UX or accessibility rule: raise it, don't build it quietly.
8. **Safe, honest, accessible.** Build to `.claude/rules/trading-ux.md` and `accessibility.md`. Before handoff, `/design-review` checks UX and accessibility
   against `docs/ux/`; any `S1` finding is fixed first.
9. **Save progress in the repo**, never only in chat: `prds/<feature>/plan.md` holds the screen list, Figma links and status.
10. **Don't commit, push or publish** unless the person asks. Use `/share-changes` for that.
   Every commit, branch and PR follows `docs/process/git-conventions.md` (Conventional Commits).

## Where to look

| Task | Read / run |
|---|---|
| Build screens from a PRD | `/prd-to-screens` → `docs/process/prd-to-screens.md` |
| Which component does X? | `docs/index.md`, then `docs/components/<name>.md` |
| Token names and values | `docs/foundations/*.md` (readable) or `tokens/*.json` (exact) |
| Screen layout, navigation, forms, sheets | `docs/patterns/*.md` |
| Example screens (reference only, not canonical) | `docs/references/selected-screens.md` |
| Add or change a component | `/new-component` → `docs/process/new-component.md` |
| Check a Figma page against the rules (tokens, instances, Light/Dark, contrast, hit targets) | `/ds-audit` (read-only report) |
| Review a design for UX and accessibility (severity, findings, verdict) | `/design-review` → `docs/ux/ux-governance.md`, `docs/ux/accessibility.md` |
| What a UX law means, and when to cite it | `docs/ux/ux-laws.md` (reviews only) |
| Product decisions, waivers, "essential" rulings | `docs/ux/decisions.md` |
| Refresh tokens and docs after a Figma change | `/ds-sync` (DS owners) |
| Get the newest docs and skills / share your changes | `/get-latest`, `/share-changes` |
| Commit, branch and PR format | `docs/process/git-conventions.md` |
| Node IDs, page IDs, collection keys | `docs/figma-map.md` |

## Figma access

- **Everyone:** the official Figma plugin for Claude (`figma@claude-plugins-official`), enabled by this repo's `.claude/settings.json`.
  It provides the Figma MCP server (`use_figma`, `get_screenshot`, `search_design_system`, ...) and Figma's own skills.
  **Load the `figma:figma-use` skill before any `use_figma` call**, and `figma:figma-generate-design` when building screens.
- **DS owners (optional):** figma-console MCP (Desktop Bridge plugin) for bulk audits and token export. With figma-console:
  call `figma_navigate` with `lock: true` on the DS file first, and pass `fileKey` + `timeout: 30000` to `figma_execute`.
- Node IDs in docs are stable in the DS file. In product files, find components by **key** (`importComponentSetByKeyAsync`)
  or by library search. Never by a node ID copied from another file.

## Context across people and machines

Everything an agent needs lives in this repo. Personal Claude memory is a convenience, never the record.
When you start work: run `/get-latest`, then read `prds/<feature>/plan.md` if continuing a feature.
When you stop: update `plan.md` (what's done, what's next, Figma links) before ending the session.

**"Check my setup"** means: confirm the Figma plugin is signed in (`whoami`), the DS file is reachable (screenshot page `1:12`),
the product file key is set in `docs/figma-map.md`, and `git status` shows the repo up to date with GitHub. Report each check in plain words.

## Editing this repo

- `tokens/*.json` is generated by `/ds-sync`. Never hand-edit it.
- In docs, content between `<!-- AUTO:START -->` and `<!-- AUTO:END -->` is regenerated from Figma. Edit outside those markers.
- DS changes need a `CHANGELOG.md` entry and a DS owner's review (see `.github/CODEOWNERS`).
- Keep docs short and tabular: token names, props, node IDs. No essays.
