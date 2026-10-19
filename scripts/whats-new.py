"""Say what's new on main since this person last looked, for /get-latest.

Usage: python3 scripts/whats-new.py [--since <ref>] [--to <ref>] [--mark]
  --since  start point (default: the last-seen marker saved by --mark; first run: the last 10 commits)
  --to     end point (default: main)
  --mark   after printing, save <to> as this computer's last-seen point (.git/laabh-ds-last-seen, never shared)

Prints the new commits grouped by area (skills, rules, tokens, components, patterns and process, features,
other), breaking changes first, then the skill and rule files that were added, changed or removed.
"""
import argparse
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FIRST_RUN = 10
EMPTY_TREE = "4b825dc642cb6eb9a060e54bf8d69288fbee4904"  # git's empty tree: "since the very start"
SUBJECT = re.compile(r"^(?P<type>\w+)(?:\((?P<scope>[^)]+)\))?(?P<bang>!)?: (?P<summary>.+)$")
VERB = {"feat": "New", "fix": "Fix", "docs": "Docs", "refactor": "Tidy", "chore": "Housekeeping"}
# (area, scopes, path prefixes). The first area whose scope or files match wins.
AREAS = [
    ("Skills (the /commands)", {"skills"}, (".claude/skills/",)),
    ("Rules", {"rules"}, (".claude/rules/", "docs/ux/", "CLAUDE.md")),
    ("Tokens and foundations", {"tokens", "foundations"}, ("tokens/", "docs/foundations/")),
    ("Components", {"components"}, ("docs/components/", "docs/index.md")),
    ("Patterns and process", {"patterns", "process"}, ("docs/patterns/", "docs/process/", "docs/references/")),
    ("Feature work", set(), ("prds/",)),
    ("Other", set(), ()),
]
WATCH = [(".claude/skills/", "Skill"), (".claude/rules/", "Rule"), ("docs/ux/", "Rule"), ("CLAUDE.md", "Rule")]
STATUS = {"A": "added", "M": "changed", "D": "removed", "R": "renamed"}


def git(*args, check=True):
    r = subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True)
    if check and r.returncode:
        sys.exit(f"git {' '.join(args)} failed: {r.stderr.strip()}")
    return r


def marker():
    return ROOT / git("rev-parse", "--git-path", "laabh-ds-last-seen").stdout.strip()


def area(scope, files):
    scope = (scope or "").lower()
    if scope.startswith("prd/"):
        return "Feature work"
    for name, scopes, _ in AREAS:
        if scope in scopes:
            return name
    for name, _, prefixes in AREAS:
        if any(f.startswith(prefixes) for f in files):
            return name
    return "Other"


def commits(since, to):
    rng = f"{since}..{to}" if since else to
    extra = [] if since else [f"-{FIRST_RUN}"]
    out = git("log", "--reverse", "--format=%x1e%h%x1f%ad%x1f%s%x1f%b%x1f", "--date=format:%d %b",
              "--name-only", *extra, rng).stdout
    for chunk in out.split("\x1e")[1:]:
        h, date, subject, body, files = chunk.split("\x1f")
        yield h, date, subject, body, [f for f in files.split("\n") if f]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--since")
    ap.add_argument("--to", default="main")
    ap.add_argument("--mark", action="store_true")
    a = ap.parse_args()

    to = git("rev-parse", "--verify", "--quiet", a.to + "^{commit}", check=False).stdout.strip()
    if not to:
        sys.exit(f"Can't find '{a.to}'.")
    since, note = a.since, ""
    if not since and marker().exists():
        since = marker().read_text().strip()
        note = f"since you last checked ({datetime.fromtimestamp(marker().stat().st_mtime):%d %b %Y})"
    if since and git("merge-base", "--is-ancestor", since, to, check=False).returncode:
        print(f"Last-seen point {since[:7]} is not part of {a.to} any more (history was rewritten). Showing the last {FIRST_RUN} changes.")
        since, note = None, ""
    if not since:
        note = note or f"(first run on this computer: the last {FIRST_RUN} changes)"
    elif not note:
        note = f"since {a.since}"

    groups, breaking, n = {}, [], 0
    for h, date, subject, body, files in commits(since, to):
        n += 1
        m = SUBJECT.match(subject)
        if m:
            feature = f" ({m['scope'][4:]})" if (m["scope"] or "").startswith("prd/") else ""
            label = f"{VERB.get(m['type'], m['type'].title())}{feature}: {m['summary']}"
            where = area(m["scope"], files)
            if m["bang"] or "BREAKING CHANGE:" in body:
                why = re.search(r"BREAKING CHANGE: (.+)", body)
                breaking.append(f"{m['summary']} ({h}){': ' + why[1] if why else ''}")
        else:
            label, where = subject, area(None, files)
        groups.setdefault(where, []).append(f"{label} ({h}, {date})")

    if not n:
        print(f"Nothing new on {a.to} {note}.")
    else:
        print(f"What's new on {a.to} {note}: {n} change{'s' if n != 1 else ''}.")
    if breaking:
        print("\nBREAKING (something was renamed or removed; check your screens):")
        for b in breaking:
            print(f"  - {b}")
    for name, _, _ in AREAS:
        if name in groups:
            print(f"\n{name}")
            for line in groups[name]:
                print(f"  - {line}")

    base = since or git("rev-list", "--max-count=1", f"--skip={FIRST_RUN}", to).stdout.strip() or EMPTY_TREE
    diff = git("diff", "--name-status", base, to).stdout
    watched = []
    for line in diff.splitlines():
        status, *paths = line.split("\t")
        path = paths[-1]
        shown = " → ".join(paths)
        for prefix, kind in WATCH:
            if path.startswith(prefix) and (kind == "Rule" or path.endswith("SKILL.md")):
                watched.append(f"  - {kind} {STATUS.get(status[0], status)}: {shown}")
                break
    if watched:
        print(f"\nSkills and rules to know about (to see a change: git diff {base[:7]}..{to[:7]} -- <file>)")
        print("\n".join(watched))

    if a.mark:
        marker().write_text(to + "\n")
        print(f"\nSaved {to[:7]} as this computer's last-seen point.")


if __name__ == "__main__":
    main()
