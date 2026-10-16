# Governance (DS owners)

## Roles
| Role | Can |
|---|---|
| Designer | Build product screens, propose components, edit `prds/` freely, open PRs for docs |
| DS owner (1–2 people, listed in `.github/CODEOWNERS`) | Approve changes to `docs/`, `.claude/`, `tokens/`, `scripts/`, `CLAUDE.md`; edit the DS Figma file; publish the library |

## Git flow (Claude does the git part)
- `main` is protected: changes arrive by Pull Request with one DS-owner approval.
- Designers run `/share-changes`: Claude creates a branch, commits, pushes and opens the PR with a plain-language summary.
- Branch names, commit messages and PR titles follow [git conventions](git-conventions.md). PRs are squash-merged.
- `prds/` changes don't need DS-owner review, but still go through `/share-changes` so others get them.

## Versioning
- Semver in `CHANGELOG.md`, tags `vX.Y.Z` on `main`. Figma library publish notes use the same version.
- **Major:** renamed/removed component, variant, property, token or style. **Minor:** new component/variant/token. **Patch:** fixes, docs.

## Keeping repo and Figma in sync
1. Change Figma (DS file) → publish the library.
2. Run `/ds-sync`: re-exports tokens (with count checks), regenerates AUTO blocks in docs, lists drift.
3. Review the diff, update CHANGELOG, `/share-changes`.
Run `/ds-sync` at least before each release, and whenever someone reports "the docs say X but Figma shows Y".

## Cadence
- Weekly: review open PRs and proposals.
- Each release: `/ds-audit` on the product file's active pages; update component statuses.

## Known debt
See "Known issues" in `CHANGELOG.md` and "Figma doc drift" sections in component docs.
