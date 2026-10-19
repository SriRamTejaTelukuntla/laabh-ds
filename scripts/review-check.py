"""Check a /design-review report against the rule book's self-check (docs/ux/ux-governance.md §7–§9) before it's shown.

Usage: python3 scripts/review-check.py <review.md> [--all]
Checks the newest review in the file (the first "# Design review:" block), or every one with --all.
Reads the plain-language format (§9: "**Result:**", "## At a glance", "### DR-01 · <title> · 🔴 Must fix (S1)") and the older
"## Verdict:" / "### [S1] <title> · DR-01" format.
  FAIL  a cited ID that isn't defined in docs/ux/ or .claude/rules/ · a MYTH-* cited as a rule · more than one primary
        + one supporting ID (GOV-03) · a finding missing Where / What's wrong / Why it matters / Fix / Rule / How sure (GOV-02)
        · the problem counts don't match the open findings · the result doesn't follow the counts (§3)
        · a finding's colour word doesn't match its S-level
  WARN  a web-only rule cited (D-04) · S1 with "Needs research" · a contrast ratio not marked measured or sent to /ds-audit
        · DR numbers out of order · a finding missing from the "At a glance" table
Exits 1 if anything FAILs.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ID = re.compile(r"\b(?:GOV-\d{2}|[MWX]-\d{2}|TR-[A-Z]+-\d{2}|D-\d{2}|L-[A-Z][A-Z-]*[A-Z]|V-[A-Z][A-Z-]*[A-Z]|DN-[A-Z][A-Z-]*[A-Z]"
                r"|NH-\d+|SR-\d+|A11Y-[A-Z]{3}-\d{2}|AN-\d{2}|MYTH-\d+|WCAG \d\.\d\.\d+)\b")
RANGE = re.compile(r"\b([A-Z0-9]+(?:-[A-Z]+)*-)(\d{2})…(\d{2})\b")
SC = re.compile(r"\|\s*(\d\.\d\.\d+)\s*\|")
WEB_ONLY = {"A11Y-TXT-03", "A11Y-LAY-05", "A11Y-LAY-06"}
# Report labels (§9) and the older ones they replace.
FIELDS = {"Where": ["Where"], "What's wrong": ["Problem"], "Why it matters": ["Impact"], "Fix": ["Recommendation"],
          "Rule": ["Principle"], "How sure": ["Confidence"]}
SEVERITY = {"S1": ("🔴", "Must fix"), "S2": ("🟠", "Should fix"), "S3": ("🟡", "Small fix"), "S4": ("⚪", "Polish")}
RESULT = {"Changes required": "Not ready for handoff", "Pass with fixes": "Ready after fixes", "Pass": "Ready for handoff"}
FINDING = re.compile(r"^### (DR-\d{2}) · (.+?) · (🔴|🟠|🟡|⚪) ([^(\n]+?) \((S[1-4])\)\s*$", re.M)
LEGACY = re.compile(r"^### \[(S[1-4])\] (.+?) · (DR-\d{2})\s*$", re.M)


def known_ids():
    ids, scs = set(), set()
    for f in [*(ROOT / "docs" / "ux").glob("*.md"), *(ROOT / ".claude" / "rules").glob("*.md")]:
        text = f.read_text()
        ids |= set(ID.findall(text))
        for prefix, a, b in RANGE.findall(text):
            ids |= {f"{prefix}{n:02d}" for n in range(int(a), int(b) + 1)}
        scs |= set(SC.findall(text))
    ids |= {f"WCAG {s}" for s in scs}
    return ids


def check(block, known):
    fails, warns = [], []
    title = block.splitlines()[0].removeprefix("# Design review:").strip()
    findings = []
    legacy = not FINDING.search(block) and bool(LEGACY.search(block))
    heads = list((LEGACY if legacy else FINDING).finditer(block))
    for i, m in enumerate(heads):
        end = heads[i + 1].start() if i + 1 < len(heads) else len(block)
        nxt = re.search(r"^## ", block[m.end():end], re.M)
        body = block[m.end(): m.end() + nxt.start()] if nxt else block[m.end():end]
        raw = {k.rstrip(":").strip(): v for k, v in re.findall(r"^- \*\*(.+?)\*\*:?\s*(.*)$", body, re.M)}
        fields = {new: raw.get(new) or next((raw[o] for o in old if raw.get(o)), "") for new, old in FIELDS.items()}
        if legacy:
            sev, name, dr = m.group(1), m.group(2), m.group(3)
        else:
            dr, name, dot, word, sev = m.groups()
            if (dot, word.strip()) != SEVERITY[sev]:
                fails.append(f"{dr}: '{dot} {word.strip()}' doesn't match {sev}; use '{' '.join(SEVERITY[sev])} ({sev})'")
        fixed = raw.get("Status", "").strip().lower().startswith(("fixed", "✅"))
        findings.append((sev, name, dr, fields, body, fixed))

    open_ = [f for f in findings if not f[5]]
    counts = {s: sum(1 for f in open_ if f[0] == s) for s in SEVERITY}
    if legacy:
        line = re.search(r"S1:\s*(\d+)\s*·\s*S2:\s*(\d+)\s*·\s*S3:\s*(\d+)\s*·\s*S4:\s*(\d+)", block)
        counts = {s: sum(1 for f in findings if f[0] == s) for s in SEVERITY}  # the old format had no Status
        label = "'S1: n · S2: n · S3: n · S4: n' line"
    else:
        line = re.search(r"Must fix:\s*(\d+)\s*·\s*🟠 Should fix:\s*(\d+)\s*·\s*🟡 Small fix:\s*(\d+)\s*·\s*⚪ Polish:\s*(\d+)", block)
        label = "'**Open problems:** 🔴 Must fix: n · 🟠 Should fix: n · 🟡 Small fix: n · ⚪ Polish: n' line"
    if not line:
        fails.append(f"no {label}")
    elif [int(x) for x in line.groups()] != list(counts.values()):
        fails.append(f"counts say {'/'.join(line.groups())} but the open findings are {'/'.join(map(str, counts.values()))} (S1/S2/S3/S4)")
    want = "Changes required" if counts["S1"] else ("Pass with fixes" if counts["S2"] else "Pass")
    if legacy:
        verdict = re.search(r"^## Verdict:\s*(.+?)\s*$", block, re.M)
        got = verdict.group(1) if verdict else None
    else:
        verdict = re.search(r"^\*\*Result:\*\*\s*\S+\s+(Not ready for handoff|Ready after fixes|Ready for handoff)\b", block, re.M)
        got = next((k for k, v in RESULT.items() if verdict and v == verdict.group(1)), None)
    if not verdict:
        fails.append("no '## Verdict:' line" if legacy else "no '**Result:** <❌|⚠️|✅> <Not ready for handoff|Ready after fixes|Ready for handoff>' line")
    elif got != want and not (want == "Pass with fixes" and got == "Changes required"):
        fails.append(f"result '{RESULT.get(got, got)}' doesn't follow the open findings: expected '{RESULT[want]}' (§3)")

    glance = re.search(r"^## At a glance\s*$(.*?)(?=^## |\Z)", block, re.M | re.S)
    for sev, name, dr, fields, body, fixed in findings:
        where = f"{dr} [{sev}] {name}"
        missing = [k for k in FIELDS if not fields.get(k, "").strip()]
        if missing:
            fails.append(f"{where}: missing {', '.join(missing)} (GOV-02: no concrete Where / What's wrong / Why it matters, no finding)")
        rule = fields.get("Rule", "")
        cited = [x for x in ID.findall(rule) if not x.startswith("WCAG") or "A11Y-" not in rule]
        if len(set(cited)) > 2:
            fails.append(f"{where}: {len(set(cited))} rule IDs ({', '.join(dict.fromkeys(cited))}); one primary + at most one supporting (GOV-03)")
        if any(x.startswith("MYTH-") for x in cited):
            fails.append(f"{where}: cites a MYTH-* as its rule (misapplication, ux-laws.md §8)")
        if any(x.startswith("W-") or x in WEB_ONLY for x in ID.findall(body)):
            warns.append(f"{where}: cites a web-only rule; web isn't in scope yet (D-04)")
        if sev == "S1" and "research" in fields.get("How sure", "").lower():
            warns.append(f"{where}: S1 with 'Needs research' is allowed only when the possible harm is financial (§3)")
        if re.search(r"\d+(\.\d+)?\s?:\s?1\b", body) and not re.search(r"measured|/ds-audit|to verify|token-contrast", body, re.I):
            warns.append(f"{where}: quotes a contrast ratio without saying it was measured (send it to /ds-audit)")
        if not legacy and not (glance and re.search(rf"^\|\s*{dr}\s*\|", glance.group(1), re.M)):
            warns.append(f"{where}: not in the 'At a glance' table")

    for x in sorted(set(ID.findall(block)) - known):
        fails.append(f"'{x}' isn't defined in docs/ux/ or .claude/rules/ (typo, or an ID that doesn't exist)")
    nums = [int(f[2][3:]) for f in findings]
    if nums != list(range(1, len(nums) + 1)):
        warns.append(f"DR numbers aren't DR-01, DR-02, … in order: {', '.join(f[2] for f in findings)}")
    return title, counts, fails, warns


def main(args):
    if not args:
        sys.exit(__doc__)
    text = Path(args[0]).read_text()
    blocks = ["# Design review:" + b for b in re.split(r"^# Design review:", text, flags=re.M)[1:]]
    if not blocks:
        sys.exit("No '# Design review:' heading found.")
    known = known_ids()
    bad = False
    for block in blocks if "--all" in args else blocks[:1]:
        title, counts, fails, warns = check(block, known)
        print(f"{title}: open S1 {counts['S1']} · S2 {counts['S2']} · S3 {counts['S3']} · S4 {counts['S4']}")
        for f in fails:
            print(f"  FAIL  {f}")
        for w in warns:
            print(f"  WARN  {w}")
        if not fails and not warns:
            print("  OK    self-check passed")
        bad |= bool(fails)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
