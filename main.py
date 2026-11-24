#!/usr/bin/env python3
"""Fortune Cookie Wisdom for Developers -- make.fun entry.

Writes one original fortune-cookie line (1-120 characters) for a software
developer to /output/entry.txt.

Pure Python standard library: no third-party dependencies, no network,
no files read from outside this repository.
"""

import os

FORTUNE = (
    "The legacy code you curse today was written by someone "
    "who once felt as clever as you do now."
)


def main() -> None:
    line = FORTUNE.strip()
    if not 1 <= len(line) <= 120:
        raise ValueError(f"fortune must be 1-120 chars, got {len(line)}")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
