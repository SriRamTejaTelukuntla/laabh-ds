"""Check a feature's plan.md against docs/process/plan-template.md and say where the work stands.

Usage: python3 scripts/plan-check.py prds/<feature>/plan.md
Prints the status counts, the next screen to work on, open questions, open gaps and waivers, then:
  FAIL  a missing section · a screen ID that isn't <letter><2 digits>[a-z] or is used twice · an unknown status
        · a screen with no components, states or rules that apply
  WARN  screen IDs with more than one letter · a built screen without a Figma link · no Log entry
Exits 1 if anything FAILs. Used by /prd-to-screens after each update and by /get-latest to say where someone left off.
"""
import re
import sys
from pathlib import Path

SECTIONS = ["Review context", "Flows", "Screens", "Open questions", "Gaps", "Decisions & waivers", "Log"]
STATUSES = ["planned", "built", "approved", "dark", "annotated", "reviewed", "blocked"]
ID = re.compile(r"^[A-Z]\d{2}[a-z]?$")


def section(text, name):
    m = re.search(rf"^## {re.escape(name)}\s*$(.*?)(?=^## |\Z)", text, re.M | re.S)
    return m.group(1) if m else None


def table(body):
    rows = [r.strip() for r in (body or "").splitlines() if r.strip().startswith("|")]
    if len(rows) < 2:
        return [], []
    cells = lambda r: [c.strip() for c in r.strip("|").split("|")]
    head = cells(rows[0])
    return head, [dict(zip(head, cells(r))) for r in rows[2:]]


def empty(v):
    return not v or v.strip("—- ") == ""


def main(path):
    text = Path(path).read_text()
    fails, warns = [], []
    for s in SECTIONS:
        if section(text, s) is None:
            fails.append(f"no '## {s}' section (docs/process/plan-template.md)")

    head, screens = table(section(text, "Screens"))
    for col in ["ID", "Screen", "Components", "States", "Rules that apply", "Status", "Figma"]:
        if screens and col not in head:
            fails.append(f"Screens table has no '{col}' column")
    seen = {}
    for r in screens:
        sid, status = r.get("ID", ""), r.get("Status", "").lower()
        if not ID.match(sid):
            fails.append(f"screen ID '{sid}' should be one letter + 2 digits, plus a letter for a state frame (K03b)")
        if sid in seen:
            fails.append(f"screen ID {sid} is used twice")
        seen[sid] = r
        if status.split(" ")[0] not in STATUSES:
            fails.append(f"{sid}: status '{r.get('Status', '')}' isn't one of {', '.join(STATUSES)}")
        for col in ["Components", "States", "Rules that apply"]:
            if col in head and empty(r.get(col)):
                fails.append(f"{sid}: '{col}' is empty")
        if status in STATUSES[1:6] and empty(r.get("Figma")):
            warns.append(f"{sid}: status '{status}' but no Figma link")
    letters = {s[0] for s in seen if s}
    if len(letters) > 1:
        warns.append(f"screen IDs use several letters ({', '.join(sorted(letters))}); one feature uses one letter")

    _, questions = table(section(text, "Open questions"))
    open_q = [q for q in questions if not empty(q.get("Question")) and empty(q.get("Answer"))]
    _, gaps = table(section(text, "Gaps"))
    open_g = [g for g in gaps if not empty(g.get("Need")) and "done" not in g.get("Status", "").lower()]
    _, waivers = table(section(text, "Decisions & waivers"))
    waivers = [w for w in waivers if not empty(w.get("Decision or waived finding"))]
    log = [l for l in (section(text, "Log") or "").splitlines() if l.strip().startswith("-")]
    if not log:
        warns.append("the Log has no entries: add what was done and what's next")

    status = re.search(r"\*\*Status:\*\*\s*([^·\n]+)", text)
    print(f"{Path(path).parent.name}: {status.group(1).strip() if status else 'no status line'} · {len(screens)} screens")
    counts = {s: sum(1 for r in screens if r.get("Status", "").lower().split(" ")[0] == s) for s in STATUSES}
    print("  " + " · ".join(f"{s} {n}" for s, n in counts.items() if n))
    st = lambda r: r.get("Status", "").lower().split(" ")[0]
    active = [r for r in screens if st(r) in STATUSES[:5]]
    if active:  # the least advanced screen, in plan order: Light screens are built one by one, Dark/annotations/review follow
        nxt = min(active, key=lambda r: STATUSES.index(st(r)))
        print(f"  next: {nxt.get('ID')} {nxt.get('Screen')} ({nxt.get('Status')})")
    waiting = [r.get("ID") for r in screens if st(r) == "built"]
    if waiting:
        print(f"  waiting for an OK: {', '.join(waiting)}")
    blocked = [r.get("ID") for r in screens if st(r) == "blocked"]
    if blocked:
        print(f"  blocked: {', '.join(blocked)} (see the Log)")
    print(f"  open questions {len(open_q)} · open gaps {len(open_g)} · decisions & waivers {len(waivers)}")
    if log:
        print(f"  last log: {log[-1].strip()[2:][:120]}")
    for f in fails:
        print(f"  FAIL  {f}")
    for w in warns:
        print(f"  WARN  {w}")
    return 1 if fails else 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    sys.exit(main(sys.argv[1]))
