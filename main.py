#!/usr/bin/env python3
"""Two-sentence horror entry for u-suroto-two-sentence-horror-acea9253.

Writes one 120-character, two-sentence story to $MAKEFUN_OUTPUT_DIR/entry.txt.
"""

import os
from pathlib import Path

FIRST = "An album called You, Asleep appeared in my gallery last night."
SECOND = "I live alone, and the photo was taken eleven minutes ago."
STORY = FIRST + " " + SECOND


def main():
    target_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "")
    if not target_dir.strip():
        raise SystemExit("MAKEFUN_OUTPUT_DIR is not set")
    if not FIRST.endswith(".") or not SECOND.endswith("."):
        raise SystemExit("each sentence must end with a full stop")
    parts = [piece for piece in STORY.split(".") if piece.strip()]
    if len(parts) != 2:
        raise SystemExit(f"expected exactly 2 sentences, got {len(parts)}")
    if len(STORY) != 120:
        raise SystemExit(f"expected 120 characters, got {len(STORY)}")
    out = Path(target_dir)
    out.mkdir(parents=True, exist_ok=True)
    entry = out / "entry.txt"
    entry.write_text(STORY + "\n", encoding="utf-8")
    if entry.read_text(encoding="utf-8") != STORY + "\n":
        raise SystemExit("entry.txt mismatch after write")
    print(f"wrote {entry} ({len(STORY)} chars, 2 sentences)")


if __name__ == "__main__":
    main()
