#!/usr/bin/env python3
"""The Worst App Idea Ever Pitched entry.

One sentence pitching the worst, most useless app imaginable, written to
/output/entry.txt. Pure standard library, no network, same bytes each run.
"""

import sys
from pathlib import Path

PITCH = (
    "Fernder is the dating app for houseplants, matching your fern with "
    "compatible ferns nearby through proprietary chlorophyll-compatibility "
    "scoring, because love, like photosynthesis, should never be rushed."
)


def write_entry(target: Path) -> int:
    target.parent.mkdir(parents=True, exist_ok=True)
    return target.write_text(PITCH, encoding="utf-8")


if __name__ == "__main__":
    sys.exit(0 if write_entry(Path("/output/entry.txt")) else 1)
