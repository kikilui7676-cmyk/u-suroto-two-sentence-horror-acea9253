import os
from pathlib import Path

LINE = "A new album appeared in my photos called 'You, Asleep.' I live alone, and the latest photo was taken eleven minutes ago."


def main() -> None:
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
