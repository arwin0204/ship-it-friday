#!/usr/bin/env python3
"""Ship It Friday — make.fun bounty entry (u-mgwals-ship-it-friday-30bd407a).

Writes one funny one-line git commit message — the kind an AI coding agent
writes right before breaking production on a Friday — to /output/entry.txt.

Deterministic: the same text is written on every run.
"""

from pathlib import Path

ENTRY = (
    "feat: Friday deploy, zero tests failed (zero tests ran), "
    "full confidence, see you Monday"
)

MAX_CHARS = 159
OUTPUT_PATH = Path("/output/entry.txt")


def validate_entry(entry: str) -> str:
    """Return the entry if it passes the gate, else raise ValueError."""
    cleaned = entry.strip()
    if not 1 <= len(cleaned) <= MAX_CHARS:
        raise ValueError(f"entry length {len(cleaned)} outside 1..{MAX_CHARS}")
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("entry must be a single line")
    if cleaned != entry:
        raise ValueError("entry must not have leading/trailing whitespace")
    return cleaned


def write_entry(entry: str) -> None:
    """Validate and write the entry as UTF-8 text with no trailing newline."""
    valid = validate_entry(entry)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(valid, encoding="utf-8")


def main() -> None:
    write_entry(ENTRY)


if __name__ == "__main__":
    main()
