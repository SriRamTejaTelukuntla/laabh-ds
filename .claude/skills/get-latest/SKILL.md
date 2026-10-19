---
name: get-latest
description: Start the day with the newest rules, docs and skills. Safely updates `main` from GitHub (fast-forward only, never touches the person's unsaved work), says in plain words what's new since they last checked (new skills, rules, tokens, components, breaking changes), and optionally checks the setup (Figma sign-in, DS file, product file key) and where a feature was left off. Works without a GitHub remote too. Use when someone says "get latest", "update", "pull", "start my day", "what's new", "am I up to date", "check my setup", or "continue the <feature> screens".
argument-hint: "[setup] [feature]"
---

# /get-latest

Bring this computer up to date with the team, then tell the person what changed and where they left off.
The person never needs to know git. Explain each step in plain words ("Main has 4 new changes; I'll bring them in. Your own work isn't touched.").

`/get-latest` updates and summarises. `/get-latest setup` also runs the "Check my setup" checks (step 4).
`/get-latest <feature>` (or `setup <feature>`) also reads `prds/<feature>/plan.md` (step 5).

## Rules
- **Never stash, reset, discard, rebase or force anything.** The person's uncommitted work stays exactly where it is. (`reset --hard` and force-push are blocked in `.claude/settings.json`.)
- Update `main` by **fast-forward only**. If that isn't possible, stop and explain. Never "fix" it by rewriting history.
- Bring `main` into a feature branch **only when the person asks**, and only with a clean tree. Stop on any conflict.
- Switch branches only with the person's OK, and only when the tree is clean.
- Don't commit, push, create the GitHub repo or add a remote here. Saving work is `/share-changes`.

## 0 · Preflight
1. `git status --short` and `git branch --show-current`. Note: the branch, and whether there is uncommitted work (list the files).
2. `git remote -v`. No remote → step 2. Otherwise `gh auth status` (needed later for `/share-changes`; if signed out, say so, but carry on: fetching may still work through GitHub Desktop).
3. On a feature branch, also note how far it is from `main`: `git log --oneline main..HEAD` (its own commits) and `git log --oneline HEAD..main` (what it's missing).

## 1 · With a remote: update `main`
1. `git fetch origin --prune`. If it fails with an auth error: ask them to sign in to GitHub Desktop (or `gh auth login`), then stop.
2. `git log --oneline main..origin/main`. Empty → `main` is already up to date; go to step 3.
3. Fast-forward `main`:

| Where they are | Do this | If it fails |
|---|---|---|
| On `main` | `git pull --ff-only` | See below |
| On a feature branch (clean or not) | `git fetch origin main:main`. It moves `main` without touching the branch or its files | See below |

**When the fast-forward fails**, stop and explain. Never stash or reset to make it work.

| Git says | Plain words | Options to offer |
|---|---|---|
| "local changes … would be overwritten" | You have unsaved edits on `main` in files the update also changes | Save them first with `/share-changes` (it moves them onto their own branch), then run `/get-latest` again. Or skip the update for today |
| "Not possible to fast-forward" / "non-fast-forward" / "rejected" | This computer's `main` has changes GitHub doesn't (e.g. from a local squash-merge before the remote existed) | Ask a DS owner. Show both lists: `git log --oneline origin/main..main` and `main..origin/main` |

4. **On a feature branch:** if `git log --oneline HEAD..main` isn't empty, say "Your branch `<name>` is missing N changes from main", and ask whether to bring them in. Only if they say yes:
   - The tree must be clean. If not: "Save your work first with `/share-changes`, then I'll bring main in."
   - `git merge main` (never rebase). Conflicts → stop. Run `git diff --name-only --diff-filter=U`, explain each file in plain words, and offer:
     - `tokens/*.json` or an AUTO block: take `main`'s version (`git checkout --theirs <file>`), then re-run the generator (`/ds-sync`, `render-docs.py`, `write-component-docs.py`).
     - Anything else: show both versions and ask which to keep.
     - Or undo the merge: `git merge --abort` puts everything back as it was before the merge.

Then go to step 3.

## 2 · No remote yet
Say: "This repo isn't on GitHub yet, so there's nothing to pull. Here's where this computer stands." Report:
- branch, uncommitted files, and (on a feature branch) its own commits and what it's missing from `main`;
- local branches: `git branch --format='%(refname:short) %(committerdate:relative)'`.
Then go to step 3: it still shows what landed on `main` since they last checked (local merges by other sessions or a DS owner).

## 3 · What's new
1. `python3 scripts/whats-new.py --mark`. It prints `main`'s new commits since this computer last checked, grouped by area, breaking changes first,
   then the skill and rule files that were added, changed or removed. `--mark` saves the new last-seen point (`.git/laabh-ds-last-seen`, never shared).
   The first run on a computer shows the last 10 changes.
2. Tell the person in plain words, most important first:

| They see | Tell them |
|---|---|
| BREAKING | What was renamed or removed and what to use instead. If they have screens in progress, suggest `/ds-audit` on them |
| Skill added | The new `/command`, what it's for (from its `description`), and when they'd use it |
| Skill changed | What it does differently now (run the `git diff` the heading shows, for that `SKILL.md`) |
| Rule added or changed | The rule in one line, and whether it affects work in progress |
| Tokens, components | New or changed tokens and components they can use now |
| Feature work | Other designers' features that moved (no action needed) |
| Nothing new | "You're up to date." |

3. If a new skill doesn't show up in the `/` menu, say: start a new Claude session in this folder.

## 4 · Check my setup (`setup`, or when asked)
Report each check as ✅ or ❌ with the fix, in plain words:

| Check | How | If it fails |
|---|---|---|
| Figma plugin signed in | `whoami` (Figma plugin) | "Type `/mcp`, choose **figma**, and sign in" (README step 4) |
| DS file reachable | `get_screenshot` of node `1:12` (Buttons page) in fileKey `mmAhXn4vJKlmuThcAMgGss` | Ask a DS owner for access to "Laabh — Design System" |
| Product file key set | `docs/figma-map.md`, "Laabh — Product" row: a real key, not `_TBD: …_` | Tell a DS owner. `/prd-to-screens` can't build until it's set |
| Repo up to date | Steps 1–2 above | Whatever step 1 reported |

## 5 · Where you left off (`<feature>`)
1. Read `prds/<feature>/plan.md` and run `python3 scripts/plan-check.py prds/<feature>/plan.md` (status counts, next screen, open questions, last Log line). Not there? List the folders in `prds/` and ask which one they meant.
2. Say, in a few lines: screens done / in progress / not started, the next screen, screens waiting for an OK, open questions and gaps still open, and the Figma links.
3. Branch: feature work lives on `prd/<feature>`. If they're on another branch and `prd/<feature>` exists (`git branch --list prd/<feature>`), offer to switch (`git switch prd/<feature>`, clean tree only).
   Check it isn't missing changes from `main` (step 1.4).
4. Offer the next step: "Continue with `<next screen>`?" (`/prd-to-screens` picks up from `plan.md`).

## 6 · Report
Keep it short:
```
Up to date: main has 3 new changes (fast-forwarded) · or: no GitHub remote yet, nothing to pull
You're on: prd/kyc, 2 unsaved files (left as they are), missing 3 changes from main
What's new: new /get-latest skill; tokens rule changed (space/3 removed: use space/4)
Setup: ✅ Figma · ✅ DS file · ❌ product file key not set (ask a DS owner)
Where you left off (kyc): K01–K03 done, K04 next, 1 open question
```
End with the one thing to do next (save work, bring main in, continue a screen), if any.
