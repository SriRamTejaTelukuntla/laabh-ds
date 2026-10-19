"""Print the library keys a product-file build needs, as one JavaScript line to paste at the top of a use_figma script.

Usage: python3 scripts/build-kit.py [component name ...]     (no names: every documented component)
Reads the keys from the repo, never from node IDs (which only work in the DS file):
  components     docs/components/*.md AUTO blocks: name → { key, set } (set = a component set with variants)
  textStyles     tokens/styles.text.json: "<role>/<Weight>" → key
  effectStyles   tokens/styles.effect.json: "elevation/<level>" → key
  collections    tokens/_meta.variables.json: collection name → key (variables are looked up by name in it)
In the product file: figma.importComponentSetByKeyAsync / importComponentByKeyAsync, figma.importStyleByKeyAsync,
and figma.teamLibrary.getVariablesInLibraryCollectionAsync(collectionKey) → find by name → figma.variables.importVariableByKeyAsync.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
AUTO = re.compile(r"<!-- AUTO:START[^\n]*-->\n(.*?)<!-- AUTO:END -->", re.S)
BLOCK = re.compile(r"^### (.+?)\n(.*?)(?=^### |\Z)", re.M | re.S)


def components():
    out = {}
    for doc in sorted((ROOT / "docs" / "components").glob("*.md")):
        m = AUTO.search(doc.read_text())
        for name, body in BLOCK.findall(m.group(1) if m else ""):
            key = re.search(r"^\| Key \| `([0-9a-f]{40})`", body, re.M)
            if key:
                out[name.strip()] = {"key": key.group(1), "set": bool(re.search(r"^\| [^|]+ \| variant \|", body, re.M))}
    return out


def styles(path, prefix=""):
    out = {}

    def walk(node, parts):
        for k, v in node.items():
            if k.startswith("$"):
                continue
            if isinstance(v, dict) and "$value" in v:
                key = v.get("$extensions", {}).get("figma", {}).get("key")
                if key:
                    out[prefix + "/".join(parts + [k])] = key
            elif isinstance(v, dict):
                walk(v, parts + [k])

    walk(json.loads(path.read_text()), [])
    return out


def main(names):
    comps = components()
    missing = [n for n in names if n not in comps]
    if missing:
        sys.exit(f"Not documented with a key: {', '.join(missing)}. Known: {', '.join(comps)}")
    meta = json.loads((ROOT / "tokens" / "_meta.variables.json").read_text())
    kit = {
        "components": {n: comps[n] for n in names} if names else comps,
        "textStyles": styles(ROOT / "tokens" / "styles.text.json"),
        "effectStyles": styles(ROOT / "tokens" / "styles.effect.json"),
        "collections": {c["name"]: c["key"] for c in meta["collections"]},
    }
    print("const KIT = " + json.dumps(kit, ensure_ascii=False, separators=(",", ":")) + ";")


if __name__ == "__main__":
    main(sys.argv[1:])
