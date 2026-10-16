"""Check the hand-written counts in docs against tokens/_meta.*.json.

Usage: python3 scripts/check-counts.py
Counts outside AUTO blocks (intro sentences, the figma-map table, tokens/README.md) are not regenerated,
so /ds-sync runs this after write-tokens.py. Prints each mismatch with the line to fix; exits non-zero if any.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOK = ROOT / "tokens"


def counts():
    c = {}
    for kind in ["variables", "styles"]:
        for col in json.loads((TOK / f"_meta.{kind}.json").read_text())["collections"]:
            c[col["name"]] = col["count"]
    return c


# (file, regex with one number group, collection name)
CHECKS = [
    ("docs/foundations/colors.md", r"\*\*Color Primitives\*\* \((\d+) raw values", "Color Primitives"),
    ("docs/foundations/colors.md", r"\((\d+) semantic tokens", "Color Tokens"),
    ("docs/foundations/elevation.md", r"^(\d+) effect styles", "Effect styles"),
    ("docs/figma-map.md", r"^Styles: (\d+) text styles", "Text styles"),
    ("docs/figma-map.md", r"^Styles: .*?, (\d+) effect styles", "Effect styles"),
    ("tokens/README.md", r"\| (\d+) raw colours", "Color Primitives"),
    ("tokens/README.md", r"\| (\d+) semantic colours", "Color Tokens"),
    ("tokens/README.md", r"\| (\d+) text styles", "Text styles"),
    ("tokens/README.md", r"\| (\d+) `elevation/\*` effect styles", "Effect styles"),
]


def main():
    want = counts()
    problems = []
    for rel, pattern, name in CHECKS:
        text = (ROOT / rel).read_text()
        m = re.search(pattern, text, re.M)
        if not m:
            problems.append(f"{rel}: pattern for {name} not found (sentence reworded? update scripts/check-counts.py)")
        elif int(m.group(1)) != want[name]:
            problems.append(f"{rel}: {name} says {m.group(1)}, Figma has {want[name]}")
    # figma-map.md collection table: | <name> | ... | <count> |
    fmap = (ROOT / "docs/figma-map.md").read_text()
    for name, n in want.items():
        m = re.search(r"^\| " + re.escape(name) + r" \|.*\| (\d+) \|$", fmap, re.M)
        if m and int(m.group(1)) != n:
            problems.append(f"docs/figma-map.md: {name} row says {m.group(1)}, Figma has {n}")
    print("\n".join(problems) if problems else "Counts match.")
    if problems:
        sys.exit(1)


if __name__ == "__main__":
    main()
