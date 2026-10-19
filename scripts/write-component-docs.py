"""Write the AUTO blocks of docs/components/<name>.md from the result of scripts/figma/inspect-components.js.

Usage:
  python3 scripts/write-component-docs.py --groups [name ...]   print the GROUPS line for inspect-components.js
  python3 scripts/write-component-docs.py --groups <name>=<id>[,<id>]   same, for a new doc whose AUTO block is still empty
  python3 scripts/write-component-docs.py <result.json>         replace the AUTO block of each doc in the result

--groups reads the node IDs from the existing AUTO blocks. A new doc (copied from _template.md) has an empty
block, so give its IDs with name=id (e.g. navigation-bar=180:12); the first write fills the block, and later
runs find the IDs there. Only text between AUTO:START and AUTO:END changes.
After writing, it prints each doc's count of unbound paints / unstyled text (`raw`), which should be 0
unless the doc's "Figma doc drift" section explains it.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs" / "components"
AUTO = re.compile(r"(<!-- AUTO:START[^\n]*-->\n)(.*?)(<!-- AUTO:END -->)", re.S)


def groups(args):
    out, names = {}, []
    for a in args:
        if "=" not in a:
            names.append(a)
            continue
        name, ids = a.split("=", 1)
        ids = [i.strip() for i in ids.split(",") if i.strip()]
        if not (DOCS / f"{name}.md").exists():
            sys.exit(f"No docs/components/{name}.md: copy _template.md to it first.")
        if not ids or not all(re.fullmatch(r"\d+:\d+", i) for i in ids):
            sys.exit(f"{a}: node IDs look like 180:12 (comma-separated for several).")
        out[name] = ids
    only = bool(names or out)  # names given: just those; nothing given: every documented component
    for doc in sorted(DOCS.glob("*.md")):
        if doc.name.startswith("_") or doc.stem in out or (only and doc.stem not in names):
            continue
        m = AUTO.search(doc.read_text())
        if m:
            ids = re.findall(r"^\| Node ID \| `([0-9:]+)`", m.group(2), re.M)
            if ids:
                out[doc.stem] = ids
    print("const GROUPS = " + json.dumps(out) + ";")


def write(path):
    result = json.loads(Path(path).read_text())
    for name, r in result.items():
        if name.startswith("$"):
            continue
        doc = DOCS / f"{name}.md"
        if not doc.exists():
            print(f"SKIP     {name}: no docs/components/{name}.md")
            continue
        text = doc.read_text()
        if not AUTO.search(text):
            print(f"SKIP     {name}: no AUTO block")
            continue
        new = AUTO.sub(lambda m: m.group(1) + r["md"] + m.group(3), text, count=1)
        status = "updated" if new != text else "same"
        doc.write_text(new)
        print(f"{status:8} {name} (raw {r.get('raw', '?')})")


if __name__ == "__main__":
    if len(sys.argv) >= 2 and sys.argv[1] == "--groups":
        groups(sys.argv[2:])
    elif len(sys.argv) == 2:
        write(sys.argv[1])
    else:
        sys.exit(__doc__)
