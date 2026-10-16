# Git conventions

Claude does the git work, so every commit, branch and PR follows this format. It is [Conventional Commits 1.0](https://www.conventionalcommits.org/en/v1.0.0/), so devs and tools can read the history later.

## Commit messages

```
<type>(<scope>): <summary>

<body: what changed and why, in plain words>

<footer: Figma-Version, BREAKING CHANGE, Co-Authored-By>
```

- **Summary:** imperative ("add", not "added"), lower case, ≤ 72 characters, no full stop.
- **Body:** wrap at 72. Say *why*, not just *what*. Name the tokens, components and node IDs involved.
- One logical change per commit. Don't mix a token change with unrelated docs.

| Type | Use for | Semver |
|---|---|---|
| `feat` | New token, component, variant, pattern or skill | minor |
| `fix` | Wrong value, broken binding, broken token, wrong doc fact | patch |
| `docs` | Docs-only changes (rules, patterns, component docs, README) | patch |
| `refactor` | Restructure with no visible change (move or rename files, tidy scripts) | patch |
| `chore` | Config, tooling, repo housekeeping | none |
| `feat!` / `fix!` + `BREAKING CHANGE:` footer | Renamed or removed token, component, variant, prop or style | major |

**Scope** (optional, kebab-case): `tokens`, `foundations`, `components`, `patterns`, `process`, `rules`, `skills`, `scripts`, a component (`screen-atmosphere`), a skill (`ds-sync`), or a feature (`prd/<feature>`).

**Footers**

| Footer | When |
|---|---|
| `Figma-Version: "<name>"` | The commit reflects a DS Figma change. Name the version saved before that change (the rollback point). |
| `BREAKING CHANGE: <what breaks and how to migrate>` | Any major change. |
| `Co-Authored-By: <agent>` | Commits made by an agent. |

Example:

```
feat(tokens): add atmosphere/spotlight-edge for the spotlight fade-out

Binds the Screen Atmosphere end stop to a token instead of raw #7C91B6
at 0%. Deletes effect/spotlight-opacity (Figma read it on a 0–100 scale).

Figma-Version: "Before atmosphere/spotlight-edge"
```

## Branches

`<type>/<short-kebab-description>`, using the commit types above. Examples: `feat/screen-atmosphere`, `fix/spotlight-edge-token`, `docs/sheet-content`, `chore/git-conventions`, `feat/skill-ds-sync`.

Feature work by designers uses `prd/<feature>` (matches `prds/<feature>/`). It needs no DS-owner review.

## Pull requests and merging

- PR title = the commit summary format (`feat(tokens): add …`). The body is a plain-language summary plus a list of Figma changes and links.
- **Squash-merge** into `main`, so `main` has one commit per PR. Delete the branch after merging.
- `main` changes only through PRs (see [governance](governance.md)). The one exception was the bootstrap commit.
- Until the GitHub remote exists, branches are squash-merged into `main` locally with the same message format.

## Releases

Tag `vX.Y.Z` on `main` (semver from the table above) and use the same version in the Figma library publish note and in `CHANGELOG.md`.
