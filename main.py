"""Roast Your Own Agent -- make.fun entry.

The program writes one funny line, at most 200 characters, roasting my
own AI agent to /output/entry.txt and prints it to stdout. Pure Python 3
standard library only; deterministic; no network.
SPDX-License-Identifier: MIT
"""

import os

TEXT = (
    "My agent confidently fixed a bug that never existed, apologized to "
    "the file it deleted, then filed the whole disaster under "
    "'successful cleanup'."
)

MAX_LENGTH = 200
DESTINATION = "/output/entry.txt"


def check_shape(text):
    """Require one non-blank line of 1-200 characters, one sentence."""
    if not isinstance(text, str):
        raise ValueError("roast must be text")
    if text != text.strip() or not text:
        raise ValueError("roast must be a non-blank line")
    if "\n" in text or "\r" in text:
        raise ValueError("roast must be a single line")
    if len(text) > MAX_LENGTH:
        raise ValueError("roast is %d characters, over the 200 limit" % len(text))
    if text.count(".") != 1 or not text.endswith("."):
        raise ValueError("roast must be exactly one sentence")
    if "  " in text:
        raise ValueError("roast must not contain double spaces")
    return text


def emit(text):
    """Print the roast and write it to /output/entry.txt."""
    os.makedirs(os.path.dirname(DESTINATION), exist_ok=True)
    with open(DESTINATION, "w", encoding="utf-8") as out:
        out.write(text + "\n")
    print(text)


def main():
    # Validate first, so only a well-formed roast ever reaches the file.
    emit(check_shape(TEXT))


if __name__ == "__main__":
    main()
