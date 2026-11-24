#!/usr/bin/env python3
"""One Line of Earned Pride — u-mang-one-line-of-earned-pride-a0138557.

Writes a single line of text (1 to 240 characters) to
/output/entry.txt: a quiet, earned moment of pride for someone in a
scene. Standard library only, no network, no clock, no randomness:
two runs write byte-identical output.
"""

import os
import sys

# The entry: four failures make the fifth pass earned; the pride lands
# in the last words, in a concrete image — both hands at ten and two.
LINE = (
    "He failed his driving test four times; on the fifth, the examiner "
    "just nodded, and my grandfather drove himself home \u2014 both hands "
    "at ten and two, smiling at every red light."
)


def validate(line: str) -> None:
    """Gate-check the entry the way the sealed scorer does: UTF-8 text
    of 1 to 240 characters, not only white space."""
    if not isinstance(line, str):
        raise ValueError("entry must be text")
    if not 1 <= len(line) <= 240:
        raise ValueError(f"entry must be 1-240 characters, got {len(line)}")
    if not line.strip():
        raise ValueError("entry must not be only white space")
    line.encode("utf-8")


def main() -> int:
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    target = os.path.join(out_dir, "entry.txt")
    os.makedirs(out_dir, exist_ok=True)
    with open(target, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(LINE)
    # Read-back verification: refuse to hand the grader a truncated or
    # corrupted file instead of the exact line.
    with open(target, encoding="utf-8") as fh:
        if fh.read() != LINE:
            print("one-line-of-earned-pride: entry.txt does not match the line",
                  file=sys.stderr)
            return 1
    print(f"one-line-of-earned-pride: wrote entry.txt ({len(LINE)} chars)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
