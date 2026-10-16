"""Regenerate the AUTO blocks in docs/foundations/*.md from tokens/*.json.

Usage: python3 scripts/render-docs.py
Only text between <!-- AUTO:START ... --> and <!-- AUTO:END --> is replaced; everything else is hand-written.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOK = ROOT / "tokens"


def load(name):
    return json.loads((TOK / name).read_text())


def flatten(tree, prefix=()):
    """Yield (path, token) for every token in a DTCG tree."""
    for key, node in tree.items():
        if key.startswith("$") and key != "$root":
            continue
        path = prefix if key == "$root" else prefix + (key,)
        if isinstance(node, dict) and "$value" in node:
            yield "/".join(path), node
        elif isinstance(node, dict):
            yield from flatten(node, path)


PRIMS = {}
for f in ["primitives.color.json", "primitives.typography.json", "primitives.spacing-radius.json"]:
    PRIMS.update({p: t["$value"] for p, t in flatten(load(f))})
SEM_COLOR = dict(flatten(load("semantic.color.json")))
SEM_TYPE = dict(flatten(load("semantic.typography.json")))


def ref_name(v):
    return v[1:-1].replace(".", "/") if isinstance(v, str) and v.startswith("{") else None


def resolve(v, mode="Light"):
    """Resolve a value or {reference} to a literal, following semantic tokens in the given mode."""
    seen = 0
    while (name := ref_name(v)) and seen < 10:
        seen += 1
        if name in PRIMS:
            v = PRIMS[name]
        elif name in SEM_COLOR:
            t = SEM_COLOR[name]
            v = t.get("$extensions", {}).get("modes", {}).get(mode, t["$value"]) if mode != "Light" else t["$value"]
        elif name in SEM_TYPE:
            t = SEM_TYPE[name]
            v = t.get("$extensions", {}).get("modes", {}).get(mode, t["$value"]) if mode != "Mobile" else t["$value"]
        else:
            return v
    return v


def short(v):
    return "`" + ref_name(v) + "`" if ref_name(v) else "`" + str(v) + "`"


def colors_md():
    groups = {}
    for path, t in SEM_COLOR.items():
        if t["$type"] != "color":
            continue
        groups.setdefault(path.split("/")[0], []).append((path, t))
    out = []
    for g, items in groups.items():
        if g == "elevation":
            continue  # documented in elevation.md
        out += [f"### {g}/*", "", "| Token | Light | Dark |", "|---|---|---|"]
        for path, t in items:
            dark = t.get("$extensions", {}).get("modes", {}).get("Dark", t["$value"])
            out.append(f"| `{path}` | {short(t['$value'])} {resolve(t['$value'])} | {short(dark)} {resolve(dark)} |")
        out.append("")
    return "\n".join(out)


def typography_md():
    styles = load("styles.text.json")
    out = ["| Role | Mobile | Tablet | Desktop | Family | Weights | Tracking | Case |", "|---|---|---|---|---|---|---|---|"]
    for role, weights in styles.items():
        if role.startswith("$"):
            continue
        first = next(iter(weights.values()))
        v = first["$value"]
        size, lh = ref_name(v["fontSize"]), ref_name(v["lineHeight"])
        cells = []
        for mode in ["Mobile", "Tablet", "Desktop"]:
            s = resolve(SEM_TYPE[size]["$value"] if mode == "Mobile" else SEM_TYPE[size]["$extensions"]["modes"][mode]) if size in SEM_TYPE else v["fontSize"]
            l = resolve(SEM_TYPE[lh]["$value"] if mode == "Mobile" else SEM_TYPE[lh]["$extensions"]["modes"][mode]) if lh in SEM_TYPE else v["lineHeight"]
            cells.append(f"{str(s).replace('px', '')}/{str(l).replace('px', '')}")
        fam = resolve(v["fontFamily"])
        case = first["$extensions"]["figma"].get("textCase", "ORIGINAL").lower().replace("original", "as typed")
        out.append(f"| `{role}` | {cells[0]} | {cells[1]} | {cells[2]} | {fam} | {', '.join(weights)} | {v['letterSpacing']} | {case} |")
    return "\n".join(out)


def spacing_md():
    space = [(p, v) for p, v in PRIMS.items() if p.startswith("space/")]
    radius = [(p, v) for p, v in PRIMS.items() if p.startswith("radius/")]
    out = ["| Space token | Value |", "|---|---|"] + [f"| `{p}` | {v} |" for p, v in space]
    out += ["", "| Radius token | Value |", "|---|---|"] + [f"| `{p}` | {v} |" for p, v in radius]
    return "\n".join(out)


def elevation_md():
    fx = load("styles.effect.json")["elevation"]
    out = ["| Style | Light layers | Dark layers |", "|---|---|---|"]
    for name, t in fx.items():
        cols = []
        for mode in ["Light", "Dark"]:
            parts = []
            for layer in t["$value"]:
                if layer["type"] == "background-blur":
                    b = resolve(layer["blur"], mode)
                    if b not in ("0px", 0):
                        parts.append(f"blur {b}")
                    continue
                c = resolve(layer["color"], mode)
                if c.endswith("00") and len(c) == 9:
                    continue  # fully transparent in this mode
                kind = "inset " if layer["type"] == "inner-shadow" else ""
                parts.append(f"{kind}{layer['offsetX']} {layer['offsetY']} {layer['blur']} {c}")
            cols.append("<br>".join(parts) or "none")
        out.append(f"| `elevation/{name}` | {cols[0]} | {cols[1]} |")
    return "\n".join(out)


BLOCKS = {
    "foundations/colors.md": colors_md,
    "foundations/typography.md": typography_md,
    "foundations/spacing-radius.md": spacing_md,
    "foundations/elevation.md": elevation_md,
}

AUTO = re.compile(r"(<!-- AUTO:START[^>]*-->\n).*?(<!-- AUTO:END -->)", re.S)

for rel, fn in BLOCKS.items():
    path = ROOT / "docs" / rel
    text = path.read_text()
    if not AUTO.search(text):
        raise SystemExit(f"{rel}: no AUTO markers")
    path.write_text(AUTO.sub(lambda m: m.group(1) + fn() + "\n" + m.group(2), text, count=1))
    print("updated", rel)
