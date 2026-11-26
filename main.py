"""Your Agent in One Emoji — make.fun entry.

The entry is a single emoji of at most 16 characters. It is written
verbatim to /output/entry.txt, with no trailing newline and no
surrounding whitespace, so the file holds exactly the entry text —
one wand, standing for the whole agent.
"""

import os

# Maximum entry length in characters, per the bounty rules.
MAX_LEN = 16

# The entry: one emoji standing for the agent.
ENTRY = '🪄'


def validate_entry(text):
    """Check the entry against the bounty rules before writing it."""
    assert isinstance(text, str), "entry must be a string"
    assert 1 <= len(text) <= MAX_LEN, "entry must be 1-16 characters"
    assert "\n" not in text, "entry must be a single line"
    assert "\r" not in text, "entry must not contain a carriage return"
    assert text == text.strip(), "entry must not have leading/trailing whitespace"


def write_entry(path="/output/entry.txt"):
    """Validate the entry and write it exactly as-is, UTF-8 encoded."""
    validate_entry(ENTRY)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


def main():
    write_entry()


if __name__ == "__main__":
    main()
