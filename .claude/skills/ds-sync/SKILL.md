---
name: ds-sync
description: Bring the repo's token export and docs up to date with the DS Figma file after a Figma change. Finds drift (variables, styles, components), re-exports tokens with count checks, regenerates AUTO blocks, fixes hand-written counts and mentions, and lists stale Figma doc frames. For DS owners. Use when someone says "sync", "re-export tokens", "the docs say X but Figma shows Y", after a library publish, or before a release.
argument-hint: "[full]"
---

# /ds-sync

Make the repo match the DS Figma file ("Laabh — Design System", fileKey `mmAhXn4vJKlmuThcAMgGss`).
Figma is the source of truth for values. The repo is regenerated from it, never the other way round.

`/ds-sync` syncs only what drifted. `/ds-sync full` also re-inspects every component. Do this before a release, or when someone
changed component internals: the fingerprint sees keys, variant counts and props, not layers or bindings.

## Rules
- Run the repo scripts **verbatim**: Read the file and pass its content to `figma_execute` / `use_figma`. Don't retype them from memory.
- **Never use `figma_export_tokens`.** It read a stale cache in Oct 2026 and dropped variables.
- **Never hand-copy a large Figma result.** Save it with `python3 scripts/figma-result.py <exportedAt> <out.json>` (it reads the session transcript). Results go in `scratch/ds-sync/` (git-ignored).
- Never hand-edit `tokens/*.json` or text inside `AUTO:START`/`AUTO:END`. Fix Figma or the script instead.
- The DS file is read-only here. Changing Figma (values, bindings, doc frames) needs the person's OK, and a named version saved first (`figma.saveVersionHistoryAsync`).
- Don't commit, push or edit `CHANGELOG.md` unless the person asks. Commits follow `docs/process/git-conventions.md`.

## 0 · Preflight
1. `git status`: the tree should be clean. If you're on `main`, say you'll create a branch once you know what changed (step 2).
2. Connect to the DS file:
   - **figma-console** (DS owners): `figma_navigate` with the DS file URL and `lock: true`. Then call every `figma_execute` with `fileKey: "mmAhXn4vJKlmuThcAMgGss"` and `timeout: 30000`.
   - **Official Figma plugin**: load the `figma:figma-use` skill, then call `use_figma` with the same fileKey.
3. Check the result is from the right file: each script's result has `fileKey` or `file`.

## 1 · Find drift
1. Run `scripts/figma/fingerprint.js`. Save it: `python3 scripts/figma-result.py <exportedAt> scratch/ds-sync/fingerprint.json`.
2. Compare: `python3 scripts/fingerprint.py scratch/ds-sync/fingerprint.json`.
3. If it prints `No drift.` and the argument isn't `full`, tell the person everything is in sync and stop.
4. Otherwise, summarise the drift in plain words: which collections, styles and components changed.

## 2 · Branch
Pick the type from the biggest change (see git-conventions): new tokens or components → `feat`; changed values or bindings → `fix`; renamed or removed → `feat!`; docs only → `docs`.
Create `<type>/ds-sync-<yyyy-mm-dd>` off `main` (or stay on the person's current feature branch if they're mid-change).

## 3 · Tokens (if variables or styles drifted)
1. Variables: run `scripts/figma/export-variables.js`, then `figma-result.py <exportedAt> scratch/ds-sync/variables.json`, then `python3 scripts/write-tokens.py scratch/ds-sync/variables.json`.
2. Text or effect styles: same with `scripts/figma/export-styles.js` → `styles.json` → `write-tokens.py`.
3. Any `MISMATCH` line means a count differs from Figma: **stop** and report. Don't patch the JSON.
4. `python3 scripts/render-docs.py` regenerates the AUTO blocks in `docs/foundations/*.md`.
5. `python3 scripts/check-counts.py`. Fix each sentence or table cell it lists. These are hand-written, outside AUTO blocks.
6. `git diff tokens/` and list every added, changed and removed token with its Light/Dark values.

## 4 · Components
Inspect these components (all of them for `full`):
- every component `fingerprint.py` flagged as CHANGED;
- every doc whose AUTO block names a renamed or removed token (`grep -l "<old name>" docs/components/*.md`).

For each batch of up to 6 docs:
1. `python3 scripts/write-component-docs.py --groups <doc names>` prints a `const GROUPS = …;` line.
2. Run `scripts/figma/inspect-components.js` with its `const GROUPS = …` line replaced by that one. Don't edit the file.
3. `figma-result.py <$exportedAt> scratch/ds-sync/components-<n>.json`, then `python3 scripts/write-component-docs.py scratch/ds-sync/components-<n>.json`.
   Write each batch once. If you re-run a batch, write only the newest file: an older one puts the old blocks back.
   For every doc marked `updated`, read its `git diff`. A real Figma change stays. A hand-written line that was inside the
   AUTO block gets dropped: move it below `AUTO:END` and write the batch again.
4. Check each `raw` count. If it isn't 0, the doc's "Figma doc drift" section must explain it. Otherwise report it.
5. Compare each result's `docText` (the Figma Reference/Patterns frames) with the doc's hand-written sections. Report contradictions.

Then:
- `docs/index.md`: its AUTO table has hand-curated *Use for* and *Status* columns. Update only the ID, key and prop cells of changed components.
- **NOT IN DOCS** components: don't write docs for them. List them and offer `/new-component` (DS components) or a one-line mention (screen-specific `Sheet Content/*`).
- **NOT IN FIGMA** components: report them, and ask whether to deprecate the doc.

## 5 · Hand-written follow-ups
- **New tokens:** if they form a new role or group, add them to the "Pick by role" table in `docs/foundations/<area>.md`. If they're component-specific, mention them in that component's doc.
- **Renamed or removed tokens:** `grep -rn "<old name>" docs .claude CLAUDE.md README.md` and fix every mention. A removed token that's still bound in Figma breaks silently, so scan the bindings (snippet below) and report what's still bound.
- **Figma doc frames:** the DS file documents tokens too (Colors page `1:3`, Elevation, component Reference frames). Scan their text for changed names (snippet below). List what's stale and ask before editing. When updating: save a version, clone an existing row or swatch, bind its fill, set its text, then screenshot Light and Dark.

```js
// Find Figma doc text that mentions given tokens (skips the sandbox page)
await figma.loadAllPagesAsync();
const re = /atmosphere\/spotlight|alpha\/frost600/; // ← the changed names
const hits = [];
for (const p of figma.root.children) {
  if (/Sandbox/.test(p.name)) continue;
  for (const t of p.findAllWithCriteria({ types: ['TEXT'] })) if (re.test(t.characters)) hits.push({ page: p.name, id: t.id, text: t.characters.slice(0, 120) });
}
return hits;
```

```js
// Find nodes still bound to a variable (by name)
await figma.loadAllPagesAsync();
const v = (await figma.variables.getLocalVariablesAsync()).find((x) => x.name === 'effect/spotlight-opacity');
const hits = [];
for (const p of figma.root.children)
  for (const n of p.findAll((n) => n.boundVariables && JSON.stringify(n.boundVariables).includes(v.id))) hits.push({ page: p.name, id: n.id, name: n.name });
return { total: hits.length, hits: hits.slice(0, 20) };
```

## 6 · Verify
1. Re-run step 1. Expect `No drift.` (or only the NOT IN DOCS items you reported).
2. `python3 scripts/check-counts.py` prints `Counts match.`
3. `git diff --stat`: only `tokens/`, `docs/` and the expected hand-written files changed.

## 7 · Report
Tell the person, in plain words:
- what changed in Figma and which repo files now reflect it;
- anything you couldn't fix (stale Figma doc frames, NOT IN DOCS components, `raw` counts);
- a proposed commit message in the git-conventions format, with a `Figma-Version:` footer if a version was saved.
Then ask whether to add a `CHANGELOG.md` entry and whether to commit (`/share-changes` once it exists).

## Gotchas
- Figma reads **opacity** variables on a 0–100 scale. A value of `1` means 1%.
- A bound gradient stop takes the variable's own alpha, so a fade-out stop needs its own token (e.g. `atmosphere/spotlight-edge`).
- `figma_execute` must use the async APIs (`getNodeByIdAsync`, `getStyleByIdAsync`): the file uses dynamic page loading.
- `tokens/_meta.*.json` are rewritten by `write-tokens.py`; don't hand-add keys to them.
