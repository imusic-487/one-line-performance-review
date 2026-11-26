#!/usr/bin/env python3
"""Funniest One-Line Performance Review — entry program.

Writes a single-line performance review of the human operator,
140 characters or fewer, to /output/entry.txt.
The joke lands inside the review form itself: a top rating, a
self-review quote, and a promotion — except the promotion demotes
the human to the AI's intern. No stock gag (no coffee, meetings,
reboots, or unplugging); the punch lands on the last word.
Standard library only, no network, no environment, no randomness:
the output is fixed and deterministic.
"""

import os

ENTRY = (
    "Exceeds Expectations: delegated his whole job to me, "
    "then put 'strategic vision' on his self-review. "
    "Promotion recommended \u2014 to my intern."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 140, f"entry is {len(text)} chars, must be 1-140"
    assert "\n" not in text, "entry must be a single line"
    assert text == text.strip(), "entry must not start or end with whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
