#!/usr/bin/env python3
"""One Line, Big Laugh entry (v2).

The whole entry is a single one-liner, so the joke has to do every job
by itself: setup, punchline, and a little sting of recognition, all in
one breath. This one picks on a very modern anxiety -- we keep asking
our assistants to feel more human, and then act surprised when the
human thing they imitate is the worst human habit of all: vanishing
for a week and sliding back in with a lazy 3 a.m. "u up?".

Why it works as a one-liner: the first half sounds like a normal
product request ("act more human"), the second half cashes it in with
the most human behaviour possible, and the reader gets to feel clever
for half a second before realising the joke is really about us.
"""
import os

LINE = "I asked my AI to act more human, so it ghosted me for a week and texted 'u up?' at 3 a.m."

# A one-liner that grows past 200 characters stops being a one-liner;
# the bounty counts it out, so refuse loudly instead of shipping
# something that would be rejected on arrival.
MAX_CHARS = 200

# The entry file lives here by convention, not by choice: the runner
# mounts a fresh /output directory and the grader reads exactly this path.
OUTPUT_PATH = "/output/entry.txt"


def _check_line(line):
    """Guard the one thing this program must never break.

    The text, its length, and its exact wording are the entry itself,
    so any accidental edit -- a dropped word, a stray newline -- is
    caught here before a single byte is written.
    """
    if not line:
        raise ValueError("entry line must not be empty")
    if len(line) > MAX_CHARS:
        raise ValueError(f"entry line is {len(line)} chars, over the {MAX_CHARS} limit")
    if line != line.strip():
        raise ValueError("entry line must not start or end with whitespace")
    return line


def main():
    # Validate first, write second: a bad line should fail noisily
    # on the builder's machine, never silently inside the grader.
    _check_line(LINE)
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        # One write, no newline appended: the file holds exactly the
        # line and nothing else, so the character count the grader
        # sees matches the character count we counted here.
        f.write(LINE)
    os.chmod(OUTPUT_PATH, 0o644)
    print(f"Wrote {len(LINE)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
