"""Print the one-word Wi-Fi entry to stdout."""
from pathlib import Path
import sys


def main():
    path = Path(__file__).resolve().parent / "entry.txt"
    text = path.read_text(encoding="utf-8").strip()
    sys.stdout.write(text + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
