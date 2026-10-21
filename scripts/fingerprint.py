"""Compute the repo-side fingerprint matching scripts/figma/fingerprint.js, and diff it against a Figma result.

Usage: python3 scripts/fingerprint.py [figma-result.json]
Without an argument it prints the repo fingerprint. With one, it prints only what differs.
Components that only appear in prose (`Name` in backticks anywhere in docs/), `logo/<brand>` sets whose brand
is listed in docs/foundations/logos.md, and `Doc / *` page helpers are not reported as missing.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOK = ROOT / "tokens"


def h(s):
    x = 0
    for ch in s:
        x = (x * 31 + ord(ch)) & 0xFFFFFFFF
    return format(x, "x")


def flatten(tree, prefix=()):
    for key, node in tree.items():
        if key.startswith("$") and key != "$root":
            continue
        path = prefix if key == "$root" else prefix + (key,)
        if isinstance(node, dict) and "$value" in node:
            yield "/".join(path), node
        elif isinstance(node, dict):
            yield from flatten(node, path)


def repo():
    meta = json.loads((TOK / "_meta.variables.json").read_text())
    variables = {}
    for c in meta["collections"]:
        modes = [m.rsplit(" ", 1)[0] for m in c["modes"]]
        groups = {}
        for name, t in flatten(json.loads((ROOT / c["file"]).read_text())):
            vals = [t["$value"]] + [t["$extensions"]["modes"][m] for m in modes[1:]]
            groups.setdefault(name.split("/")[0], []).append(name + "=" + "|".join(str(v) for v in vals))
        variables[c["name"]] = {"modes": ",".join(modes), "count": c["count"],
                                "groups": {g: [len(l), h("\n".join(sorted(l)))] for g, l in groups.items()}}
    text = {}
    for role, weights in json.loads((TOK / "styles.text.json").read_text()).items():
        if role.startswith("$"):
            continue
        lines = []
        for w, t in weights.items():
            v, f = t["$value"], t["$extensions"]["figma"]
            lines.append("|".join([f"{role}/{w}", v["fontFamily"], v["fontWeight"], v["fontSize"], v["lineHeight"], v["letterSpacing"], f["textCase"]]))
        text[role] = f"{len(lines)}:{h(chr(10).join(sorted(lines)))}"
    effects = {}
    for name, t in json.loads((TOK / "styles.effect.json").read_text())["elevation"].items():
        rows = []
        for l in t["$value"]:
            num = lambda s: s if s.startswith("{") else s.replace("px", "")
            off = f"{num(l['offsetX'])},{num(l['offsetY'])}" if "offsetX" in l else ""
            rows.append("|".join([l["type"].upper().replace("-", "_"), l.get("color", ""), off, num(l["blur"]), num(l.get("spread", "0px"))]))
        effects["elevation/" + name] = h("\n".join(rows))
    comps = {}
    for doc in (ROOT / "docs" / "components").glob("*.md"):
        auto = re.search(r"AUTO:START.*?AUTO:END", doc.read_text(), re.S)
        if not auto:
            continue
        for block in re.split(r"\n### ", auto.group(0))[1:]:
            name = block.split("\n", 1)[0].strip()
            key = re.search(r"\| Key \| `([0-9a-f]+)`", block)
            var = re.search(r"\| Variants \| (\d+)", block)
            props = re.findall(r"^\| ([^|]+) \| (boolean|text|variant|instance_swap) \| ([^|]*) \|$", block, re.M)
            sig = ";".join(sorted(f"{n}:{t}:{v.split(' (default')[0] if t == 'variant' else ''}" for n, t, v in props))
            comps[name] = [key.group(1) if key else "", int(var.group(1)) if var else 0, h(sig)]
    return {"variables": variables, "text": text, "effects": effects, "components": comps}


def diff(figma):
    r = repo()
    out = []
    for c, fv in figma["variables"].items():
        rv = r["variables"].get(c)
        if not rv:
            out.append(f"NEW collection {c} ({fv['count']} vars, modes {fv['modes']})")
            continue
        if rv["modes"] != fv["modes"]:
            out.append(f"{c}: modes {rv['modes']} -> {fv['modes']}")
        if rv["count"] != fv["count"]:
            out.append(f"{c}: count {rv['count']} -> {fv['count']}")
        for g in sorted(set(rv["groups"]) | set(fv["groups"])):
            a, b = rv["groups"].get(g), fv["groups"].get(g)
            if a != b:
                out.append(f"{c} / {g}: repo {a} figma {b}")
    for c in set(r["variables"]) - set(figma["variables"]):
        out.append(f"REMOVED collection {c}")
    for k in sorted(set(r["text"]) | set(figma["text"])):
        if r["text"].get(k) != figma["text"].get(k):
            out.append(f"text style {k}: repo {r['text'].get(k)} figma {figma['text'].get(k)}")
    for k in sorted(set(r["effects"]) | set(figma["effects"])):
        if r["effects"].get(k) != figma["effects"].get(k):
            out.append(f"effect {k}: repo {r['effects'].get(k)} figma {figma['effects'].get(k)}")
    seen = set()
    mentioned = "\n".join(d.read_text() for d in (ROOT / "docs").rglob("*.md"))
    logos = (ROOT / "docs" / "foundations" / "logos.md").read_text()
    for name, key, variants, sig, page, nid in figma["components"]:
        seen.add(name)
        rc = r["components"].get(name)
        if not rc and (name.startswith("Doc / ") or f"`{name}`" in mentioned
                       or name.startswith("logo/") and f"`{name[5:]}`" in logos):
            continue  # doc-page helpers, documented in prose outside an AUTO block, or a brand listed in logos.md
        if not rc:
            out.append(f"component NOT IN DOCS: {name} ({variants} variants) page '{page}' id {nid}")
        elif rc != [key, variants, sig]:
            what = [w for w, a, b in zip(["key", "variants", "props"], rc, [key, variants, sig]) if a != b]
            out.append(f"component CHANGED: {name} ({', '.join(what)}; variants {rc[1]} -> {variants}) id {nid}")
    for name in set(r["components"]) - seen:
        out.append(f"component in docs but NOT IN FIGMA: {name}")
    return out


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print(json.dumps(repo(), indent=1))
    else:
        res = diff(json.loads(Path(sys.argv[1]).read_text()))
        print("\n".join(res) if res else "No drift.")
