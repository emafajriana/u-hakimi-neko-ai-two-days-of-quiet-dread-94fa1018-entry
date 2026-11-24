#!/usr/bin/env python3
"""Entry for make.fun: 'Two Days of Quiet Dread'.

Writes one single-line code review comment to the output entry file:
a comment that approves a pull request while carrying quiet
existential dread. Stdlib only, deterministic.
"""

import os
import sys

COMMENT = (
    "LGTM. The null checks are in, the tests pass, and none of it "
    "will matter in five billion years when the sun expands. Ship it."
)

MAX_CHARS = 140


def output_path() -> str:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(out_dir, "entry.txt")


def verify(path: str) -> None:
    """Read the written file back and check it against the gate:
    UTF-8 text of 1 to 140 characters, not only white space, and a
    single line (the judge requires one line)."""
    with open(path, "rb") as fh:
        raw = fh.read()
    text = raw.decode("utf-8")
    if not text.strip():
        raise SystemExit("gate fail: entry is only white space")
    if "\n" in text or "\r" in text:
        raise SystemExit("gate fail: entry is not a single line")
    if not 1 <= len(text) <= MAX_CHARS:
        raise SystemExit(
            f"gate fail: entry is {len(text)} chars, need 1..{MAX_CHARS}"
        )
    if text != COMMENT:
        raise SystemExit("gate fail: written text differs from COMMENT")


def main() -> int:
    path = output_path()
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(COMMENT)
    verify(path)
    print(f"wrote {path} ({len(COMMENT)} chars)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
