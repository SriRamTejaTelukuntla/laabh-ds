"""Turn /ds-audit results into a plain-language report.

Usage: python3 scripts/audit-report.py <result.json> [<result.json> ...] [--out <report.md>]
Each <result.json> is one run of scripts/figma/audit.js, saved with scripts/figma-result.py (several when the audit ran in
batches). The script merges them, checks the text/effect styles and variable collections they used against tokens/,
names known gaps from docs/index.md, compares Light and Dark copies, and writes markdown (default scratch/ds-audit/report.md).
It prints the summary block and the path of the report.
"""
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SEV_ORDER = ["S1", "S2", "S3", "S4"]
SEV_NAME = {"S1": "Blocker", "S2": "Major", "S3": "Minor", "S4": "Polish"}

# Plain-language name and the rule each check comes from.
CHECKS = {
    "contrast": ("Text contrast too low", "accessibility.md · WCAG 1.4.3"),
    "contrast-ui": ("Border or icon contrast too low", "accessibility.md · WCAG 1.4.11"),
    "hit-target": ("Tap target too small", "accessibility.md · WCAG 2.5.8 / house 44 pt"),
    "hit-target-android": ("Android 48 dp hit area not annotated", "decisions.md D-04"),
    "wrong-mode": ("Frame shows the wrong mode", "light-dark.md"),
    "missing-dark": ("No Dark copy", "light-dark.md"),
    "missing-light": ("No Light copy", "light-dark.md"),
    "light-dark-drift": ("Light and Dark copies differ", "light-dark.md"),
    "dark-placement": ("Dark copy not to the right", "light-dark.md"),
    "missing-variable": ("Bound to a deleted variable", "tokens.md"),
    "raw-color": ("Colour not from a token", "tokens.md"),
    "primitive-color": ("Colour bound to a primitive", "tokens.md"),
    "foreign-variable": ("Token from another library", "tokens.md"),
    "raw-radius": ("Radius not from a token", "tokens.md"),
    "raw-space": ("Padding or gap not from a token", "tokens.md"),
    "raw-effect": ("Shadow or blur not an elevation style", "tokens.md"),
    "unstyled-text": ("Text without a text style", "typography.md"),
    "foreign-style": ("Style not from the DS", "typography.md"),
    "doc-style": ("Docs-only style in a screen", "typography.md"),
    "detached": ("Detached component", "components.md"),
    "lookalike": ("Drawn copy of a DS component", "components.md"),
    "missing-main": ("Instance of a missing component", "components.md"),
    "sandbox-component": ("Component from the Sandbox page", "components.md"),
    "local-component": ("Local component, not from the library", "components.md"),
    "structure": ("Screen chrome missing or out of order", "components.md · layout.md"),
    "canvas": ("Frame size off the 390×844 canvas", "layout.md"),
    "frame-fill": ("Frame fill is not surface/page", "layout.md"),
    "screen-name": ("Screen name format", "naming.md"),
    "section-name": ("Section name format", "naming.md"),
    "duplicate-name": ("Two screens with the same name", "naming.md"),
    "stray-node": ("Loose layer outside any screen", "figma-safety.md"),
    "not-found": ("Target not found", ""),
}
PAGE_CHECKS = {"stray-node", "section-name", "duplicate-name", "missing-dark", "missing-light", "dark-placement", "screen-name", "wrong-mode", "not-found"}
# Lookalike layer names that are a known DS gap (docs/index.md "Known gaps"), not a copy of an existing component.
KNOWN_GAP_NAMES = {"tab bar": "Navigation Bar", "navigation bar": "Navigation Bar", "nav bar": "Navigation Bar"}


def load(paths):
    runs = [json.loads(Path(p).read_text()) for p in paths]
    if not runs:
        sys.exit(__doc__)
    return runs


def ds_style_keys():
    keys = {}
    for f in ["styles.text.json", "styles.effect.json"]:
        def walk(o, path):
            if isinstance(o, dict):
                ext = o.get("$extensions", {}).get("figma", {})
                if "key" in ext:
                    keys[ext["key"]] = "/".join(path)
                for k, v in o.items():
                    if not k.startswith("$"):
                        walk(v, path + [k])
        walk(json.loads((ROOT / "tokens" / f).read_text()), [])
    return keys


def known_gaps():
    text = (ROOT / "docs/index.md").read_text()
    m = re.search(r"## Known gaps.*?\n((?:\|.*\n)+)", text)
    return {row.split("|")[1].strip().split(" (")[0] for row in (m.group(1).splitlines()[2:] if m else [])}


def key_in_docs(key):
    for p in list((ROOT / "docs").rglob("*.md")):
        t = p.read_text()
        i = t.find(key)
        if i >= 0:
            line = t[: i].rsplit("\n", 1)[-1]
            return f"{p.relative_to(ROOT)} ({line.strip('| `').split('|')[0].strip()})"
    return None


def merge(runs):
    screens, findings, ds, pairs = {}, [], {}, {}
    page_seen, exempt, not_measured, styles, foreign = set(), defaultdict(int), [], {}, {}
    for r in runs:
        for s in r["screens"]:
            sid = s[0]
            if sid not in screens or (s[6] and not screens[sid][6]):
                screens[sid] = s
        for f in r["findings"]:
            if f["check"] in PAGE_CHECKS:
                k = (f["check"], f["node"])
                if k in page_seen:
                    continue
                page_seen.add(k)
                findings.append(f)
            elif f.get("scope") == "ds":
                k = (f["check"], f.get("component"), f["detail"])
                if k in ds:
                    ds[k]["count"] += f["count"]
                    ds[k]["screens"] = (ds[k]["screens"] + [x for x in f["screens"] if x not in ds[k]["screens"]])
                else:
                    ds[k] = dict(f)
            else:
                findings.append(f)
        for c in r["contrast"]:
            k = tuple(c[:4])
            if k in pairs:
                p = pairs[k]
                if c[4] < p[4]:
                    p[4], p[7] = c[4], c[7]
                p[5] += c[5]
            else:
                pairs[k] = list(c)
        for k, v in r.get("exempt", {}).items():
            exempt[k] += v
        not_measured += r.get("notMeasured", [])
        for s in r.get("styles", []):
            st = styles.setdefault(s[1], list(s))
            if st is not s:
                st[4] += s[4]
        for v in r.get("foreignVariables", []):
            fv = foreign.setdefault((v[0], v[2]), list(v))
            if fv is not v:
                fv[3] += v[3]
    return screens, findings, list(ds.values()), list(pairs.values()), exempt, not_measured, styles, foreign


def repo_checks(screens, findings, styles, foreign, is_ds_file):
    """Findings that need the repo: style keys, foreign variables, known gaps, detached keys, Light/Dark drift."""
    keys = ds_style_keys()
    for key, s in styles.items():
        name, _, remote, kind, count, nodes = s
        if key not in keys and not (is_ds_file and not remote and name.startswith("mono/")):
            findings.append({"check": "foreign-style", "sev": "S3", "screen": None, "node": ", ".join(nodes), "name": name, "count": count,
                             "detail": f"{kind} style `{name}` (key {key[:10]}…) is not in tokens/styles.{kind}.json"})
    for (name, ckey), v in foreign.items():
        findings.append({"check": "foreign-variable", "sev": "S3", "screen": None, "node": ", ".join(v[4]), "name": name, "count": v[3],
                         "detail": f"`{name}` comes from collection \"{v[1]}\" (key {ckey[:10]}…), not the DS library"})
    gaps = known_gaps()
    for f in findings:
        if f["check"] == "lookalike":
            gap = KNOWN_GAP_NAMES.get(f["name"].strip().lower())
            if gap and gap in gaps:
                f["check"], f["sev"] = "lookalike", "S4"
                f["detail"] = f"local copy of the {gap}, a known DS gap (docs/index.md); swap it in when the component exists"
        key = f.get("key") or (re.search(r"\(([0-9a-f]{40})\)", f["detail"]) or [None, None])[1]
        if f["check"] == "detached" and key and "local component" not in f["detail"] and "DS component" not in f["detail"]:
            f["key"] = key
            where = key_in_docs(key)
            f["detail"] = (f"detached from {where}" if where else
                           f"detached from a library component that isn't in the DS docs (key {f['key'][:10]}…)")
    base = lambda n: re.sub(r"\s+—\s+(Light|Dark)$", "", n)
    by_base = defaultdict(dict)
    for s in screens.values():
        m = re.search(r"—\s+(Light|Dark)$", s[1])
        if m and s[6]:
            by_base[(base(s[1]), s[4].replace("Dark", "").replace("Light", ""))][m.group(1)] = s
    for (_, _), pair in by_base.items():
        if "Light" in pair and "Dark" in pair and pair["Light"][6] != pair["Dark"][6]:
            d = pair["Dark"]
            findings.append({"check": "light-dark-drift", "sev": "S3", "screen": d[0], "node": f"{pair['Light'][0]}, {d[0]}", "name": d[1], "count": 1,
                             "detail": f"Light has {pair['Light'][6]} layers, Dark has {d[6]}: the Dark copy is no longer a straight duplicate"})


def fmt_nodes(f):
    nodes = f.get("nodes") or [f["node"]]
    more = f.get("count", 1) - len(nodes)
    return ", ".join(f"`{n}`" for n in nodes) + (f" +{more} more" if more > 0 else "")


def line(f):
    label = CHECKS.get(f["check"], (f["check"], ""))[0]
    text = f' "{f["text"]}"' if f.get("text") else ""
    inst = f" (in {f['inInstance']})" if f.get("inInstance") else ""
    times = f" ×{f['count']}" if f.get("count", 1) > 1 else ""
    return f"- **[{f['sev']}] {label}**{times} · {f['name']}{inst}{text}: {f['detail']} · {fmt_nodes(f)}"


def report(runs, out):
    screens, findings, ds, pairs, exempt, not_measured, styles, foreign = merge(runs)
    is_ds_file = runs[0].get("isDsFile")
    repo_checks(screens, findings, styles, foreign, is_ds_file)
    sname = {s[0]: s[1] for s in screens.values()}
    deep = [s for s in screens.values() if s[6]]
    incomplete = [r for r in runs if r.get("next") is not None]
    done_from = {r["from"] for r in runs}
    missing_batch = [r["next"] for r in incomplete if r["next"] not in done_from]

    # systemic = same check and detail on 3+ screens
    by_issue = defaultdict(list)
    for f in findings:
        if f.get("screen") and f["check"] not in PAGE_CHECKS:
            by_issue[(f["check"], f["detail"])].append(f)
    systemic = {k: v for k, v in by_issue.items() if len({f["screen"] for f in v}) >= 3}
    in_systemic = {id(f) for v in systemic.values() for f in v}
    # an illustration or chart drawn with raw colours: one line for all its colours, not one per colour
    merged = defaultdict(list)
    for (check, detail), fs in systemic.items():
        if check == "raw-color":
            merged[(frozenset(f["screen"] for f in fs), fs[0]["name"])].append((detail, fs))
    for (_, name), items in merged.items():
        if len(items) > 2:
            colours = [re.sub(r"^(fill|stroke) (gradient \w+ stop )?| is not a token$", "", d) for d, _ in items]
            for d, _ in items:
                del systemic[("raw-color", d)]
            fs = [f for _, x in items for f in x]
            systemic[("raw-color", f"{len(items)} raw colours on layers named `{name}` (an illustration or chart?): " + ", ".join(colours[:8]) + (" …" if len(colours) > 8 else ""))] = fs

    all_items = findings + ds
    sev_count = defaultdict(int)
    for f in all_items:
        sev_count[f["sev"]] += 1
    fails = sorted([p for p in pairs if p[4] < p[6]], key=lambda p: p[4])

    md = [f"# /ds-audit report", "",
          f"**File:** {runs[0]['file']} · **Target:** {', '.join(f'`{t}`' for t in runs[0]['target'])} · **Run:** {runs[-1]['exportedAt'][:16].replace('T', ' ')} UTC",
          f"**Screens:** {len(screens)} found, {len(deep)} checked in depth. Read-only: nothing in Figma was changed.", ""]
    if missing_batch:
        md += [f"> ⚠️ Incomplete: the audit stopped at screen {missing_batch[0]} of {len(screens)}. Run the next batch (FROM = {missing_batch[0]}) before trusting the counts.", ""]
    md += ["## Summary", "", "| Severity | Findings | Meaning |", "|---|---|---|"]
    for s in SEV_ORDER:
        md.append(f"| {s} {SEV_NAME[s]} | {sev_count.get(s, 0)} | " + {"S1": "fix before handoff", "S2": "fix before release, or waive with a reason",
                                                                     "S3": "fix when the screen is next touched", "S4": "optional tidy-up"}[s] + " |")
    md += ["", "_A finding can cover several layers (×n). `/design-review` may raise a severity (order or first-run flow, repeated on 3+ screens)._", "",
           "| Check | Findings | Rule |", "|---|---|---|"]
    per_check = defaultdict(lambda: [0, 0])
    for f in all_items:
        per_check[f["check"]][0] += 1
        per_check[f["check"]][1] += f.get("count", 1)
    for c, (n, total) in sorted(per_check.items(), key=lambda x: -x[1][0]):
        label, rule = CHECKS.get(c, (c, ""))
        md.append(f"| {label} | {n}" + (f" ({total} layers)" if total != n else "") + f" | {rule} |")
    md.append("")

    if fails:
        md += ["## Contrast failures (measured)", "", "| Text or part | On | Mode | Kind | Ratio | Needs | Seen | Example |", "|---|---|---|---|---|---|---|---|"]
        for p in fails:
            md.append(f"| `{p[0]}` | {p[1]} | {p[2]} | {p[3]} | {p[4]}:1 | {p[6]}:1 | {p[5]}× | `{p[7]}` |")
        md += ["", "Fix by choosing a different semantic token (`docs/foundations/colors.md`), never by editing values.", ""]

    if ds:
        md += ["## Inside DS components (fix in the library, not the screen)", "",
               "These come from a component's own design. Report them to a DS owner (`/new-component` to change a component).", ""]
        for f in sorted(ds, key=lambda f: (SEV_ORDER.index(f["sev"]), f.get("component") or "")):
            uniq = sorted({sname.get(x, x) for x in f["screens"]})
            scr = ", ".join(uniq[:3]) + (" …" if len(uniq) > 3 else "")
            md.append(f"- **[{f['sev']}] {CHECKS[f['check']][0]}** · {f['component']} › {f['name']}: {f['detail']} · seen {f['count']}× (e.g. {scr}) · `{f['nodes'][0]}`")
        md.append("")

    if systemic:
        md += ["## Systemic (same problem on 3+ screens)", ""]
        for (check, detail), fs in sorted(systemic.items(), key=lambda x: (SEV_ORDER.index(x[1][0]["sev"]), -len(x[1]))):
            scr = {f["screen"] for f in fs}
            uniq = sorted({sname.get(x, x) for x in scr})
            names = ", ".join(uniq[:4]) + (f" and {len(uniq) - 4} more" if len(uniq) > 4 else "")
            md.append(f"- **[{fs[0]['sev']}] {CHECKS.get(check, (check,))[0]}** on {len(scr)} screens: {detail}. Layer `{fs[0]['name']}` · e.g. {names} · `{fs[0]['nodes'][0] if fs[0].get('nodes') else fs[0]['node']}`")
        md.append("")

    page = [f for f in findings if f["check"] in PAGE_CHECKS or not f.get("screen")]
    if page:
        md += ["## Page and file", ""]
        for f in sorted(page, key=lambda f: (SEV_ORDER.index(f["sev"]), f["check"])):
            md.append(line(f))
        md.append("")

    md += ["## By screen", ""]
    by_screen = defaultdict(list)
    for f in findings:
        if f.get("screen") and f["check"] not in PAGE_CHECKS and id(f) not in in_systemic:
            by_screen[f["screen"]].append(f)
    clean = []
    for s in sorted(deep, key=lambda s: (s[4], s[1])):
        fs = by_screen.get(s[0], [])
        if not fs:
            clean.append(s[1])
            continue
        md += [f"### {s[1]} · `{s[0]}`" + (f" · {s[4]}" if s[4] else ""), ""]
        md += [line(f) for f in sorted(fs, key=lambda f: (SEV_ORDER.index(f["sev"]), f["check"]))]
        md.append("")
    if clean:
        md += [f"**No screen-specific findings:** {', '.join(clean)}", ""]

    md += ["## Contrast pairs measured", "",
           "Colours resolved per mode and composited over everything behind them (glass and alpha included; Screen Atmosphere and background blur left out).", "",
           "| Text or part | On | Mode | Kind | Lowest | Needs | Seen |", "|---|---|---|---|---|---|---|"]
    for p in sorted(pairs, key=lambda p: (p[4] >= p[6], p[3], p[4])):
        md.append(f"| `{p[0]}` | {p[1]} | {p[2]} | {p[3]} | {p[4]}:1{' ❌' if p[4] < p[6] else ''} | {p[6]}:1 | {p[5]}× |")
    md.append("")
    md += ["## Not checked or exempt", ""]
    for k, v in sorted(exempt.items()):
        why = {"Status Bar Time": "unstyled by design (system-components.md)", "disabled text": "disabled controls are exempt (WCAG 1.4.3)",
               "text/disabled token": "disabled text is exempt", "text covered by an overlay": "under a scrim or sheet, not readable by design"}.get(k, "")
        md.append(f"- {k}: {v}× — {why}")
    for n in not_measured[:20]:
        md.append(f"- To measure by hand: `{n['node']}` {n['name']} on {sname.get(n['screen'], n['screen'])} ({n['why']})")
    md += ["- Hit areas are measured on component bounds; a larger tappable parent frame, or spacing between small targets, is not seen. Check those by eye.",
           "- Not covered here (judged in `/design-review`): copy, flows, states, focus order, annotations.", ""]

    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(md))
    summary = [f"{len(screens)} screens ({len(deep)} in depth) · " + " · ".join(f"{s}: {sev_count.get(s, 0)}" for s in SEV_ORDER),
               f"contrast pairs: {len(pairs)} measured, {len(fails)} failing · DS-component findings: {len(ds)} · systemic: {len(systemic)}"]
    if missing_batch:
        summary.append(f"INCOMPLETE: run the next batch with FROM = {missing_batch[0]}")
    print("\n".join(summary))
    print(f"wrote {out.relative_to(ROOT) if out.is_relative_to(ROOT) else out}")


def main(args):
    out = ROOT / "scratch/ds-audit/report.md"
    if "--out" in args:
        i = args.index("--out")
        out = Path(args[i + 1]).resolve()
        args = args[:i] + args[i + 2:]
    report(load(args), out)


if __name__ == "__main__":
    main(sys.argv[1:])
