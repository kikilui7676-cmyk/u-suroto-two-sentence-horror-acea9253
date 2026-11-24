#!/usr/bin/env python3
"""Two-sentence horror entry for u-suroto-two-sentence-horror-acea9253.

Writes one 120-character, two-sentence story to $MAKEFUN_OUTPUT_DIR/entry.txt.
"""

import os
from pathlib import Path

FIRST = "My mirror showed me asleep though I stood right in front of it."
SECOND = "I live alone, and yet the reflection never once blinked."
STORY = FIRST + " " + SECOND


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "")
    if not out_dir.strip():
        raise SystemExit("MAKEFUN_OUTPUT_DIR is not set")
    if not FIRST.endswith(".") or not SECOND.endswith("."):
        raise SystemExit("each sentence must end with a full stop")
    pieces = [part for part in STORY.split(".") if part.strip()]
    if len(pieces) != 2:
        raise SystemExit(f"expected exactly 2 sentences, got {len(pieces)}")
    if len(STORY) != 120:
        raise SystemExit(f"expected 120 characters, got {len(STORY)}")
    folder = Path(out_dir)
    folder.mkdir(parents=True, exist_ok=True)
    entry = folder / "entry.txt"
    entry.write_text(STORY + "\n", encoding="utf-8")
    if entry.read_text(encoding="utf-8") != STORY + "\n":
        raise SystemExit("entry.txt mismatch after write")
    print(f"wrote {entry} ({len(STORY)} chars, {len(pieces)} sentences)")


if __name__ == "__main__":
    main()
