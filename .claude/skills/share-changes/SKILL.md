---
name: share-changes
description: Save and share repo changes for review, with Claude doing all the git work. Checks the changes (secrets, big or local files, hand-edited tokens or AUTO blocks, CHANGELOG, plan.md), groups them into Conventional Commits on a properly named branch, pushes and opens or updates the GitHub pull request, and says who needs to review. Works locally when there is no GitHub remote yet. Use when someone says "share", "save my changes", "commit", "push", "open a PR", "send this for review", or finishes a feature or a /ds-sync.
argument-hint: "[what the changes are about]"
---

# /share-changes

Turn the person's changes into reviewed history: right branch, clean commits, a pull request with a plain summary.
The person never needs to know git. Explain each step in plain words ("I'll save these 3 files as one change called …").
Format: `docs/process/git-conventions.md`. Review rules: `docs/process/governance.md` and `.github/CODEOWNERS`.

## Rules
- **Show the plan and wait for an OK** before the first commit. Commit only what the person agreed to share.
- **Stage files by name** (`git add <path> …`). Never `git add -A` or `git add .`: other sessions may be working in the same folder.
- **Never** push to `main`, force-push, rebase a shared branch, or `reset --hard` (the last two are blocked in `.claude/settings.json`).
- Never share anything `scripts/share-check.py` marks **BLOCK**. Fix it first, or leave that file out.
- Don't create the GitHub repo, add a remote or merge into `main` unless the person asks.

## 0 · Preflight
1. `git status` and `git branch --show-current`.
2. `git remote -v`. If there's a remote: `gh auth status`, then `git fetch origin`. If there isn't, say the changes will stay on this computer (see step 6).
3. If the tree is clean and the branch has no commits ahead of `main` (`git log main..HEAD`), say there's nothing to share and stop.

## 1 · Check the changes
Run `python3 scripts/share-check.py` (add paths to check only some files). It lists every changed file with its review rule, then:

| Mark | Meaning | What to do |
|---|---|---|
| `BLOCK` | Secret (Figma/GitHub/API key), `*.local.json`, `scratch/`, `.env`, file over 5 MB | Remove it or leave the file out. Never share it |
| `ASK` `tokens/*.json` | Token files changed | Confirm they came from `/ds-sync`. Hand edits are never shared: redo them through Figma and `/ds-sync` |
| `ASK` CHANGELOG | DS files changed without a `CHANGELOG.md` entry | Ask whether to add one under `[Unreleased]` (the team may have paused entries) |
| `ASK` plan.md | `prds/<feature>/` changed without its `plan.md` | Update `plan.md` (done, next, Figma links) before sharing |
| `WARN` AUTO block | Edit inside `AUTO:START`/`AUTO:END` | Fine if a script made it (`/ds-sync`, `render-docs.py`, `write-component-docs.py`). A hand edit: move it outside the block |

Then read `git diff` (and new files) yourself, so the commit messages say what really changed.

## 2 · Plan the commits
- **One logical change per commit.** For example, a new token, the docs that describe it, and a skill tweak are three commits.
- **Type** from the change (git-conventions table): `feat`, `fix`, `docs`, `refactor`, `chore`; `feat!` + `BREAKING CHANGE:` for anything renamed or removed.
- **Split by review:** if both `prds/` and DS files changed, propose two branches, so feature work isn't held up by a DS review.
- **Branch:** on `main`, name a new one: `<type>/<short-kebab>`, or `prd/<feature>` for feature work. Already on a feature branch? Stay on it.

Show the plan in plain words and wait for the OK:

```
Branch: feat/skill-share-changes (new)
1. feat(scripts): add share-check for pre-commit guardrails   → scripts/share-check.py
2. feat(skills): add /share-changes skill                      → .claude/skills/share-changes/SKILL.md
Review: DS owner (both files are DS files). Nothing blocked.
```

## 3 · Commit
1. On `main`: `git switch -c <branch>` (uncommitted changes come along).
2. For each planned commit: `git add <its paths>`, check `git diff --cached --stat` lists only them, then:

```bash
git commit -F - <<'EOF'
<type>(<scope>): <summary, imperative, lower case, ≤ 72 chars>

<what changed and why, in plain words, wrapped at 72>

Figma-Version: "<named version saved before the Figma change>"   ← only if Figma changed
Co-Authored-By: <the agent's attribution line>
EOF
```
3. `git log --oneline main..HEAD` to confirm the list.

## 4 · Bring in the latest main (remote only)
If `origin/main` has moved since the branch started (`git log HEAD..origin/main`), run `git merge origin/main`. Don't rebase.
On a conflict, stop and explain it in plain words:
- `tokens/*.json` or an AUTO block: never hand-merge. Take `origin/main`'s version, then re-run the generator (`/ds-sync`, `render-docs.py`, `write-component-docs.py`).
- Anything else: show both versions and ask which to keep.

## 5 · Push and open the pull request (remote only)
1. `git push -u origin <branch>`.
2. `gh pr list --head <branch> --state open`. If a PR exists, the push updated it: add a comment summarising the new commits, and don't open another.
3. Otherwise: `gh pr create --base main --head <branch> --title "<type>(<scope>): <summary>" --body-file <file>`, with this body:

```markdown
## Summary
<2–4 plain sentences: what changed and why>

## Changes
- <commit summary> (<files>)

## Figma
<links and named versions, or "No Figma changes">

## Review
<"DS owner review needed (CODEOWNERS)" or "prds only: no DS review needed">. <Checks: share-check clean / what was confirmed>

🤖 Generated with [Claude Code](https://claude.com/claude-code)
```
PR titles follow the commit format. The PR is squash-merged into `main` (governance), so its title becomes the commit on `main`.

## 6 · No remote yet
Commit on the branch (step 3), then explain the options in plain words:
- **Keep the branch** until the GitHub repo exists. Nothing else changes.
- **Squash-merge into `main` locally.** Only a DS owner can choose this, and only when they ask (git-conventions: "until the GitHub remote exists"):
  `git switch main`, `git merge --squash <branch>`, `git commit -F -` (PR-title message + summary + attribution), then `git branch -D <branch>`.
  Check `git diff <branch> main` is empty before deleting.

## 7 · Report
In plain words: the branch, each commit (`hash summary`), the PR link (or "saved locally, not shared yet"), who must review (DS owner or nobody), and anything left: blocked files left out, an `ASK` the person deferred, a `WARN` they accepted.
