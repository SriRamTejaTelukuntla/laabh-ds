"""Check changes before /share-changes commits them: who must review, and anything that must not be shared.

Usage: python3 scripts/share-check.py [--base main] [path ...]
Looks at everything on this branch since it left <base> (default main): commits not yet on <base>, plus
uncommitted and untracked files. Pass paths to check only those (the files you are about to share).

Prints each file with its review rule (from .github/CODEOWNERS), then the checks:
  BLOCK  must be fixed before sharing (secret, local or scratch file, file over 5 MB)
  ASK    confirm with the person (tokens/*.json changed, CHANGELOG entry, prds plan.md)
  WARN   look before sharing (an edit inside an AUTO:START/END block)
Exits 1 if anything is BLOCK, otherwise 0.
"""
import fnmatch
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MAX_BYTES = 5 * 1024 * 1024
SECRETS = [
    (r"figd_[A-Za-z0-9_-]{20,}", "Figma token"),
    (r"gh[pousr]_[A-Za-z0-9]{20,}", "GitHub token"),
    (r"sk-[A-Za-z0-9_-]{20,}", "API key (sk-)"),
    (r"AKIA[0-9A-Z]{16}", "AWS key"),
    (r"-----BEGIN [A-Z ]*PRIVATE KEY-----", "private key"),
    (r"(?i)(api[_-]?key|secret|password|access[_-]?token)\s*[:=]\s*['\"][^'\"\s]{12,}['\"]", "credential"),
]
NEVER = ["*.local.json", "scratch/*", ".env", ".env.*", "*.fig"]
AUTO = re.compile(r"<!-- AUTO:START.*?<!-- AUTO:END[^\n]*-->", re.S)


def git(*args):
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True, check=True).stdout


def owners():
    """CODEOWNERS rules as (pattern, owned) in file order; the last match wins."""
    rules = []
    for line in (ROOT / ".github" / "CODEOWNERS").read_text().splitlines():
        parts = line.split("#", 1)[0].split()
        if parts:
            rules.append((parts[0], len(parts) > 1))
    return rules


def review(path, rules):
    owned = None
    for pattern, has_owner in rules:
        p = pattern.lstrip("/")
        if (p.endswith("/") and path.startswith(p)) or path == p or fnmatch.fnmatch(path, p):
            owned = has_owner
    if owned is None:
        return "no rule"
    return "DS-owner review" if owned else "no DS review"


def changed(base, only):
    """{path: state} for files changed since the branch left base, plus uncommitted and untracked ones."""
    files = {}
    mb = git("merge-base", base, "HEAD").strip()
    for line in git("diff", "--name-status", mb, "HEAD").splitlines():
        status, *paths = line.split("\t")
        files[paths[-1]] = "committed" if not status.startswith("D") else "committed (deleted)"
    out = git("status", "--porcelain=v1", "-z", "--untracked-files=all").split("\0")
    i = 0
    while i < len(out):
        entry = out[i]
        i += 1
        if not entry:
            continue
        xy, path = entry[:2], entry[3:]
        if xy[0] in "RC":
            i += 1  # skip the old name
        files[path] = "untracked" if xy == "??" else ("uncommitted (deleted)" if "D" in xy else "uncommitted")
    if only:
        files = {p: s for p, s in files.items() if any(p == o.rstrip("/") or p.startswith(o.rstrip("/") + "/") for o in only)}
    return mb, files


def added_lines(mb, path, state):
    """Lines this change adds to path, as (line number in the new file, text)."""
    if state == "untracked":
        try:
            return list(enumerate((ROOT / path).read_text().splitlines(), 1))
        except (UnicodeDecodeError, OSError):
            return []
    lines, n = [], 0
    for line in git("diff", "-U0", mb, "--", path).splitlines():
        m = re.match(r"@@ -\S+ \+(\d+)", line)
        if m:
            n = int(m.group(1))
        elif line.startswith("+") and not line.startswith("+++"):
            lines.append((n, line[1:]))
            n += 1
    return lines


def main(args):
    base = "main"
    if "--base" in args:
        i = args.index("--base")
        base = args[i + 1]
        args = args[:i] + args[i + 2:]
    mb, files = changed(base, args)
    if not files:
        print("Nothing to share: no changes since the branch left " + base + ".")
        return
    rules = owners()
    print(f"Files ({len(files)}), compared with {base}:")
    for path in sorted(files):
        print(f"  {review(path, rules):16} {files[path]:22} {path}")

    block, ask, warn = [], [], []
    for path, state in sorted(files.items()):
        if "deleted" in state:
            continue
        full = ROOT / path
        if any(fnmatch.fnmatch(path, g) or fnmatch.fnmatch(Path(path).name, g) for g in NEVER):
            block.append(f"{path}: local or scratch file; never share it")
        if full.is_file() and full.stat().st_size > MAX_BYTES:
            block.append(f"{path}: {full.stat().st_size // (1024 * 1024)} MB, over the 5 MB limit")
            continue
        lines = added_lines(mb, path, state)
        for pattern, label in SECRETS:
            hit = next((n for n, text in lines if re.search(pattern, text)), None)
            if hit:
                block.append(f"{path}:{hit}: looks like a {label}; remove it")
        if path.endswith(".md") and state != "untracked" and lines:
            spans = []
            text = full.read_text()
            for m in AUTO.finditer(text):
                spans.append((text.count("\n", 0, m.start()) + 1, text.count("\n", 0, m.end()) + 1))
            inside = sorted({n for n, _ in lines for a, b in spans if a < n < b})
            if inside:
                warn.append(f"{path}: edits inside an AUTO block (lines {inside[0]}–{inside[-1]}); they must come from a script (/ds-sync, render-docs.py)")

    paths = set(files)
    if any(p.startswith("tokens/") and p.endswith(".json") for p in paths):
        ask.append("tokens/*.json changed: confirm it came from /ds-sync (never hand-edited)")
    ds = [p for p in paths if review(p, rules) == "DS-owner review"]
    if ds and "CHANGELOG.md" not in paths:
        ask.append(f"{len(ds)} DS file(s) changed but CHANGELOG.md didn't: ask whether to add an entry (entries may be paused)")
    for feature in sorted({p.split("/")[1] for p in paths if p.startswith("prds/") and p.count("/") >= 2}):
        if f"prds/{feature}/plan.md" not in paths:
            ask.append(f"prds/{feature}/ changed but its plan.md didn't: update it (status, Figma links, next steps)")

    print()
    for label, items in [("BLOCK", block), ("ASK", ask), ("WARN", warn)]:
        for item in items:
            print(f"{label:6} {item}")
    if not (block or ask or warn):
        print("No problems found.")
    sys.exit(1 if block else 0)


if __name__ == "__main__":
    main(sys.argv[1:])
