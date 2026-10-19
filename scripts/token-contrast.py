"""Contrast of a colour token over a stack of background tokens, in Light and Dark, from tokens/*.json (no Figma needed).

Usage: python3 scripts/token-contrast.py <foreground> <background> [<background below it> ...] [--ui]
  Backgrounds go top-down. Alpha fills are composited over the next one; the stack always ends on surface/page.
  --ui  judge as a UI part or large text (3:1) instead of body text (4.5:1).
Example: python3 scripts/token-contrast.py text/brand surface/brand-subtle glass/nav
Exits 1 if any mode fails.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SEM = json.loads((ROOT / "tokens" / "semantic.color.json").read_text())
PRIM = json.loads((ROOT / "tokens" / "primitives.color.json").read_text())
MODES = ["Light", "Dark"]


def node(tree, keys):
    for k in keys:
        tree = tree[k]
    return tree


def resolve(name, mode):
    """Hex value of a semantic token (slash path) in a mode, following aliases."""
    try:
        n = node(SEM, name.split("/"))
    except KeyError:
        sys.exit(f"No colour token '{name}' in tokens/semantic.color.json.")
    v = n.get("$extensions", {}).get("modes", {}).get(mode, n["$value"])
    while isinstance(v, str) and v.startswith("{"):
        ref = v.strip("{}").split(".")
        try:
            v = node(PRIM, ref)["$value"]
        except KeyError:
            v = resolve("/".join(ref), mode)
    return v


def rgba(h):
    h = h.lstrip("#")
    return [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)], (int(h[6:8], 16) / 255 if len(h) == 8 else 1.0)


def over(top, below):
    c, a = rgba(top)
    return [c[i] * a + below[i] * (1 - a) for i in range(3)]


def lum(c):
    f = lambda x: x / 12.92 if x <= 0.03928 else ((x + 0.055) / 1.055) ** 2.4
    r, g, b = map(f, c)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def ratio(a, b):
    hi, lo = sorted([lum(a), lum(b)], reverse=True)
    return (hi + 0.05) / (lo + 0.05)


def main(args):
    ui = "--ui" in args
    names = [a for a in args if a != "--ui"]
    if len(names) < 2:
        sys.exit(__doc__)
    fg, stack = names[0], names[1:]
    if stack[-1] != "surface/page":
        stack.append("surface/page")
    need = 3.0 if ui else 4.5
    failed = False
    print(f"{fg} on {' over '.join(stack)} (needs {need}:1, {'UI part / large text' if ui else 'body text'})")
    for mode in MODES:
        bg = rgba(resolve(stack[-1], mode))[0]
        for b in reversed(stack[:-1]):
            bg = over(resolve(b, mode), bg)
        r = ratio(over(resolve(fg, mode), bg), bg)
        ok = r >= need
        failed |= not ok
        print(f"  {mode:5} {r:5.2f}:1  {'pass' if ok else 'FAIL'}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
