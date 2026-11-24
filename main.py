#!/usr/bin/env python3
"""Write one warning label for a time machine to /output/entry.txt.

Deterministic, no network, no randomness: the label is a literal below.
"""

from pathlib import Path

LABEL = "CAUTION: Ancestors stranded in the past will be reissued to another family, as is."

OUTPUT = Path("/output/entry.txt")


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    # UTF-8, exactly one line, no trailing newline.
    OUTPUT.write_text(LABEL, encoding="utf-8")


if __name__ == "__main__":
    main()
