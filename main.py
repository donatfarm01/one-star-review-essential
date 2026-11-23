#!/usr/bin/env python3
"""One-Star Review of Something Essential — make.fun entry.

Writes a single deadpan one-star review of gravity to /output/entry.txt.
No trailing newline: the gate counts characters exactly.
"""

import os

ENTRY = "Gravity has never once failed. One star, because the single time I needed it to, my phone was already face down."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    assert 1 <= len(ENTRY) <= 160, "entry must be 1-160 characters"
    assert "\n" not in ENTRY, "entry must be a single line"

if __name__ == "__main__":
    main()
