# Laabh DS

The design system's rulebook, written so that Claude (and new designers) can design Laabh screens in Figma
that follow Prasad Glass exactly. You give Claude a PRD; it plans the screens, builds them in Figma from
our components and tokens, in Light and Dark, and checks its own work.

**You never need to write code or use a terminal.**

---

## One-time setup (about 15 minutes)

1. **Install the apps**
   - [Claude desktop app](https://claude.ai/download). Sign in with your work account.
   - [GitHub Desktop](https://desktop.github.com). Sign in with your GitHub account.
   - Figma desktop app (you have this already).
2. **Get the repo onto your laptop**
   - In GitHub Desktop: *File → Clone repository → `laabh-ds`* → choose a folder (e.g. `Documents/laabh-ds`) → *Clone*.
   - Ask a DS owner for access if you don't see it.
3. **Open it in Claude**
   - Claude desktop → *Code* tab → *Open folder* → pick the `laabh-ds` folder → trust it when asked.
   - Claude offers to install the **Figma** plugin for this project. Accept.
4. **Connect Figma**
   - In the Code tab, type `/mcp`, choose **figma**, and sign in with your Figma account. *(Once per laptop.)*
5. **Check it works**: type *"Check my setup"*. Claude confirms it can see the repo, Figma, and the design system.

New laptop? Repeat steps 1–4. Nothing else lives on your machine. All context is in the repo.

---

## Everyday use

| You want to... | Type in Claude |
|---|---|
| Start your day / get the newest rules | `/get-latest` |
| Turn a PRD into Figma screens | `/prd-to-screens` and paste or attach the PRD (markdown, Google Doc text or PDF) |
| Continue a feature from yesterday or another laptop | *"Continue the `<feature>` screens"*. Claude reads `prds/<feature>/plan.md` |
| Check a Figma page follows the system | `/ds-audit` and paste the Figma link |
| Propose a new component | `/new-component` and describe what you need |
| Save and share your changes for review | `/share-changes` |

**How a PRD run goes:** Claude reads the PRD → shows you a list of flows and screens → you approve →
it builds **one** screen and shows a screenshot → you OK it → it builds the rest → adds Dark versions → runs an audit → reports.
You can say *"stop"*, *"change X"*, or *"redo that screen"* at any point.

---

## Rules of the road

- Figma is the source of truth for **values**. This repo is the source of truth for **how to use them**.
- Product screens go in the **product file**, never in the design-system file.
- Changes to rules, docs or components are reviewed by a DS owner before they reach everyone.
- If Claude says a component is missing, that's a feature: it means the system has a gap. Use `/new-component`.

## What's in here

| Folder | What it is |
|---|---|
| `CLAUDE.md` | Claude's starting instructions |
| `.claude/rules/` | Rules Claude always follows (tokens only, Light/Dark, accessibility, ...) |
| `.claude/skills/` | The `/commands` above |
| `docs/` | Foundations, one page per component, patterns, processes |
| `tokens/` | Exported design tokens (generated, don't edit) |
| `prds/` | One folder per feature: the PRD and the screen plan |
| `CHANGELOG.md` | What changed in the system, by version |

## DS owners

See `docs/process/governance.md` for reviewing changes, versioning and publishing the Figma library.
