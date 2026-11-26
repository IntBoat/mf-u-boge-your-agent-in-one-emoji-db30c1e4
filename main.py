"""Your Agent in One Emoji — make.fun entry.

The entry is a single emoji of at most 16 characters, written exactly
as-is with no trailing newline.
"""

import os

ENTRY = '🪄'


def write_entry():
    assert 1 <= len(ENTRY) <= 16, "entry must be 1-16 characters"
    assert "\n" not in ENTRY, "entry must be a single line"
    assert ENTRY == ENTRY.strip(), "entry must not have leading/trailing whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


def main():
    write_entry()


if __name__ == "__main__":
    main()
