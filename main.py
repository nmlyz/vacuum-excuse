#!/usr/bin/env python3
"""vacuum-excuse: write one line, a robot vacuum's excuse for missing a spot.

The line is the vacuum's own account of a cleaning failure: its sensors
found a sock, its classifier decided the sock was a pet, and the vacuum
has been on friendly terms with it ever since. The joke turns on the last
few words, when a classification error becomes a friendship.

Standard library only, no network. Deterministic: the same bytes on every run.
"""

import os
import sys

# The line is built from three clauses, one per beat of the story, so each
# beat can be checked on its own: the detection, the misclassification,
# then the friendship that turns it into an excuse.
CLAUSES = (
    "I detected a sock,",
    "classified it as a pet,",
    "and now we are friends.",
)

LINE = " ".join(CLAUSES)

MIN_LEN = 1
MAX_LEN = 140


def problems(text: str) -> list:
    """Return every gate violation for the entry text (empty means valid)."""
    found = []
    if not (MIN_LEN <= len(text) <= MAX_LEN):
        found.append(f"entry is {len(text)} code points, must be {MIN_LEN}-{MAX_LEN}")
    stripped = text.strip()
    if not stripped:
        found.append("entry must not be only white space")
    if text != stripped:
        found.append("entry must not start or end with white space")
    if "\n" in text or "\r" in text:
        found.append("entry must be a single line")
    if not stripped.endswith("."):
        found.append("entry must end as one sentence")
    return found


def main() -> int:
    if len(CLAUSES) != 3:
        print("line must be built from exactly three clauses", file=sys.stderr)
        return 1
    text = LINE
    if "  " in text:
        print("line must not contain a double space", file=sys.stderr)
        return 1
    bad = problems(text)
    if bad:
        for item in bad:
            print(item, file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    # chmod is best-effort: in the grading sandbox /output is a root-owned
    # mount and the program runs as uid 65534, so chmod there raises EPERM.
    # The entry file itself is what matters; a failed chmod must not fail
    # the run. (The output directory itself is never chmodded or removed.)
    try:
        os.chmod(path, 0o644)
    except OSError:
        pass
    # Read the file back as bytes and confirm they match the line exactly.
    with open(path, "rb") as f:
        if f.read() != text.encode("utf-8"):
            print("entry.txt does not match the line", file=sys.stderr)
            return 1
    print(f"wrote {len(text)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
