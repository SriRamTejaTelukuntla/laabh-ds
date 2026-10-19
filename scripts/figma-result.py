"""Save the result of a Figma script (figma_execute / use_figma) to a JSON file without retyping it.

Usage: python3 scripts/figma-result.py <marker> <out.json> [--transcript <session.jsonl>]
<marker> is a unique string from the result, normally its exportedAt value (e.g. 2026-10-16T13:44:06.843Z).
The script searches the most recently changed Claude Code session transcripts (~/.claude/projects/*/*.jsonl)
for the last tool result containing the marker, unwraps figma-console's {"_mcp": ..., "result": ...} envelope,
and writes the bare result. A result too large to show inline is saved by Claude Code to a tool-results file
(~/.claude/projects/*/<session>/tool-results/*.txt); those are searched too. Exits non-zero if nothing is found.
"""
import json
import sys
from pathlib import Path


def candidates(obj, marker):
    """Yield every JSON string inside obj that contains the marker and parses as a JSON object."""
    if isinstance(obj, str):
        s = obj.lstrip()
        if marker in s and s.startswith("{"):
            try:
                parsed = json.loads(s)
            except ValueError:
                return
            if isinstance(parsed, dict):
                yield parsed
    elif isinstance(obj, dict):
        for v in obj.values():
            yield from candidates(v, marker)
    elif isinstance(obj, list):
        for v in obj:
            yield from candidates(v, marker)


def unwrap(found):
    if "_mcp" in found and "result" in found:
        return found["result"]
    if "result" in found and isinstance(found["result"], dict) and len(found) <= 3:
        return found["result"]
    return found


def search(path, marker):
    """Prefer the last figma-console envelope; otherwise the largest matching object (use_figma output)."""
    envelope, largest, size = None, None, 0
    escaped = json.dumps(marker)[1:-1]  # how a marker with quotes looks inside a JSON string in the transcript
    with open(path, encoding="utf-8") as f:
        for line in f:
            if marker not in line and escaped not in line:
                continue
            try:
                entry = json.loads(line)
            except ValueError:
                continue
            if isinstance(entry, dict) and "_mcp" in entry and "result" in entry:
                envelope = entry  # a saved tool-results file holds the bare envelope
                continue
            for c in candidates(entry, marker):
                if "_mcp" in c:
                    envelope = c
                n = len(json.dumps(c))
                if n >= size:
                    largest, size = c, n
    return envelope or largest


def main(args):
    if len(args) < 2:
        sys.exit(__doc__)
    marker, out = args[0], Path(args[1])
    if "--transcript" in args:
        files = [Path(args[args.index("--transcript") + 1])]
    else:
        recent = lambda pattern, n: sorted(Path.home().glob(pattern), key=lambda p: p.stat().st_mtime, reverse=True)[:n]
        files = recent(".claude/projects/*/*/tool-results/*", 10) + recent(".claude/projects/*/*.jsonl", 5)
    for path in files:
        found = search(path, marker)
        if found is not None:
            result = unwrap(found)
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(json.dumps(result, ensure_ascii=False))
            print(f"wrote {out} ({out.stat().st_size // 1024} KB) from {path.name}")
            return
    sys.exit(f"No tool result containing {marker!r} in {len(files)} recent transcript(s). Pass --transcript, or save the result by hand.")


if __name__ == "__main__":
    main(sys.argv[1:])
