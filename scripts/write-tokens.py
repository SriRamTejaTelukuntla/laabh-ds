"""Write the result of scripts/figma/export-*.js into the repo and check nothing was dropped.

Usage: python3 scripts/write-tokens.py <result.json>
<result.json> is the exact object the Figma script returned: {"meta": {...}, "files": {...}}.
Exits non-zero if any collection's token count in the files differs from Figma's count.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def count_tokens(node):
    if not isinstance(node, dict):
        return 0
    if "$value" in node:
        return 1
    return sum(count_tokens(v) for k, v in node.items() if not k.startswith("$") or k == "$root")


def main(path):
    result = json.loads(Path(path).read_text())
    meta, files = result["meta"], result["files"]
    for rel, tree in files.items():
        out = ROOT / rel
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(tree, indent=2, ensure_ascii=False) + "\n")

    problems = []
    for c in meta.get("collections", []):
        rel = c.get("file")
        if not rel:
            continue
        got = count_tokens(files[rel])
        status = "ok" if got == c["count"] else "MISMATCH"
        if got != c["count"]:
            problems.append(rel)
        print(f"{status:9} {rel}: {got} written / {c['count']} in Figma")

    meta_path = ROOT / "tokens" / ("_meta." + meta.get("kind", "variables") + ".json")
    meta_path.write_text(json.dumps(meta, indent=2, ensure_ascii=False) + "\n")
    print(f"wrote {len(files)} files + {meta_path.relative_to(ROOT)}")
    if problems:
        sys.exit(f"Token count mismatch in: {', '.join(problems)}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
