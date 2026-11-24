#!/usr/bin/env python3
"""Funniest Time Machine Warning Label.

Writes a single warning label for a time machine, 120 characters or
fewer, to /output/entry.txt and prints it.

The label is a straight-faced safety notice: it turns a real hazard of
time travel (the grandfather paradox - preventing your own birth) into
the joke by treating it as a refund-policy matter, and it saves the
surprise for the last few words.
"""

import os

LABEL = (
    "WARNING: This time machine offers no refunds for births "
    "you prevent. Please vanish responsibly."
)

MAX_CHARS = 120


def main() -> None:
    label = LABEL.strip()
    assert label, "label must not be empty"
    assert "\n" not in label, "label must be a single line"
    assert len(label) <= MAX_CHARS, f"label is {len(label)} chars, over {MAX_CHARS}"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(label)
    with open("/output/entry.txt", "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != label:
        raise SystemExit(
            f"verification failed: /output/entry.txt content {written!r} "
            f"does not match label {label!r}"
        )
    print(label)


if __name__ == "__main__":
    main()
