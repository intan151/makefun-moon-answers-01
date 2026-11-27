#!/usr/bin/env python3
"""The Moon Finally Answers Back — one line, in the voice of the Moon.

The Moon replies at last to the wishes, howls and late-night promises
of everyone staring up at it. Gate: /output/entry.txt must be UTF-8
text of 1 to 240 characters, not only white space.
"""

import os

ENTRY = (
    "Four billion years of wishes, howls, and 3 a.m. promises — "
    "and the best you've got is 'please let him text back'? "
    "Fine. He's typing. He's been typing since 2019."
)


def main() -> None:
    # Gate self-check (mirrors the sealed scorer): 1-240 chars, not only
    # whitespace. The written text itself is unchanged by this check.
    assert 1 <= len(ENTRY) <= 240, "entry outside 1-240 characters"
    assert ENTRY.strip(), "entry is only white space"
    assert "\n" not in ENTRY.strip(), "entry must be one line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
