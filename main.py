#!/usr/bin/env python3
"""One Line, Zero Use — burn entry.

Emits one original line about a hilariously useless superpower to
/output/entry.txt. The brief: a single line, at most 200 characters,
judged pairwise on how funny it is, how fresh the idea feels, and how
neatly the words are put together. The power here is real, just pointed
at the one place it can never help: instant sleep, everywhere except
the bed it was made for.
"""
import os
import sys

POWER = "I can fall asleep anywhere in under a minute, except in my own bed."

TARGET = "/output/entry.txt"
LIMIT = 200


def check(text):
    if not text or text.isspace():
        return "entry is empty"
    if not text.isascii():
        return "entry must be ASCII"
    if len(text) > LIMIT:
        return f"entry is {len(text)} chars, over the {LIMIT} limit"
    if "\n" in text or "\r" in text:
        return "entry must stay on one line"
    return None


def run():
    problem = check(POWER)
    if problem:
        print(f"bad entry: {problem}", file=sys.stderr)
        raise SystemExit(1)
    os.makedirs(os.path.dirname(TARGET), exist_ok=True)
    with open(TARGET, "w", encoding="utf-8") as handle:
        handle.write(POWER)
    with open(TARGET, "r", encoding="utf-8") as handle:
        written = handle.read()
    if written != POWER:
        print("bad entry: file content does not match the entry", file=sys.stderr)
        raise SystemExit(1)
    print(f"wrote {len(POWER)} chars to {TARGET}")


if __name__ == "__main__":
    run()
