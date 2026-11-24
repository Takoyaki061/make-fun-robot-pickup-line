#!/usr/bin/env python3
"""The Robot Pickup Line Championship — writes one pickup line to /output/entry.txt.

The line: a robot that ran ten thousand simulations of meeting someone,
and froze in every single one. The joke grows out of being a machine —
simulations as preparation, "froze" as both stage fright and a system
hang — and the twist is that all that compute changed nothing.

Stdlib only, deterministic, no network.
"""

import os

LINE = "I ran 10,000 simulations of us meeting and in every single one I still froze."


def main():
    # Gate: /output/entry.txt must be UTF-8 text of 1-200 characters,
    # not only whitespace, and a single line / single sentence, or the
    # entry scores 0 and never reaches the judge.
    if not 1 <= len(LINE) <= 200:
        raise ValueError(f"line is {len(LINE)} characters, must be 1-200")
    if not LINE.strip():
        raise ValueError("line must not be only whitespace")
    if LINE != LINE.strip():
        raise ValueError("line must not carry leading or trailing whitespace")
    if "\n" in LINE:
        raise ValueError("line must be a single line")
    if LINE.count(".") != 1 or not LINE.endswith("."):
        raise ValueError("line must be exactly one sentence")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    # Read back and verify: the grader reads this file, so confirm the
    # bytes on disk are exactly the line that passed the gate above.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    if written != LINE:
        raise ValueError("entry.txt on disk differs from the line")
    print(LINE)


if __name__ == "__main__":
    main()
