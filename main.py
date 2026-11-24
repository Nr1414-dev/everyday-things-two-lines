#!/usr/bin/env python3
"""Everyday Things, Two Lines, Longer Run — make.fun entry.

Writes a two-line explanation of a toaster to /output/entry.txt:
line 1 explains the toaster to a 10-year-old with a trampoline analogy;
line 2 says why the analogy works: what it maps and what it leaves out.
Deterministic, stdlib only, no network, no randomness.
"""

import os

LINE_1 = (
    "A toaster is a tiny trampoline for your bread: you press the slice down, "
    "and when it is brown it bounces back up by itself."
)
LINE_2 = (
    "The bounce is what the trampoline gets right, but it leaves out the heat: "
    "a real trampoline never browns anything, and the toaster's thin wires do "
    "all the cooking."
)

ENTRY = LINE_1 + "\n" + LINE_2


def main():
    # Gate: UTF-8 text of 1 to 400 characters, exactly two lines, no trailing newline.
    assert 1 <= len(ENTRY) <= 400, "entry must be 1-400 characters"
    assert ENTRY.count("\n") == 1, "entry must be exactly two lines"
    assert not ENTRY.endswith("\n"), "no trailing newline"
    assert ENTRY == ENTRY.encode("utf-8").decode("utf-8"), "entry must be valid UTF-8"
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)
    # Read back and verify the written file is exactly the entry.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY, "written entry differs from expected"
    assert oct(os.stat(path).st_mode & 0o777) == "0o644", "entry must be mode 0644"


if __name__ == "__main__":
    main()
