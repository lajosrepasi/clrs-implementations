"""
String matching using a rolling hash.
"""

import re

from clrs.chapter32.naive_string_matching import find_naive
from clrs.chapter32.text import TEXT
from clrs.utils.timer_utils import Timer


def hash(s: str) -> int:
    """
    Return a simple additive hash of a string.
    """
    h = 0

    for c in s:
        h += ord(c)

    return h


def find_hash(to_find: str, text: str) -> list[int]:
    """
    Find all occurrences of a pattern using a rolling hash.
    """
    indexes = []

    len_text = len(text)
    len_to_find = len(to_find)
    if len_to_find == 0 or len_to_find > len_text:
        return indexes

    hash_to_find = hash(to_find)

    i = 0
    current_hash = 0
    while i < len_text:

        current_hash = (
            current_hash
            - (ord(text[i - len_to_find]) if (i - len_to_find >= 0) else 0)
            + ord(text[i])
        )

        if current_hash == hash_to_find:
            is_match = True
            for j in range(len_to_find):
                if to_find[j] != text[i - len_to_find + 1 + j]:
                    is_match = False
                    break

            if is_match:
                indexes.append(i - len_to_find + 1)

        i += 1

    return indexes


def main():
    to_find = "referee"
    text = TEXT

    timer = Timer("Naive impl")
    find_naive(to_find, text)
    timer.stop()

    timer = Timer("Hash impl")
    found_indexes = find_hash(to_find, text)
    timer.stop()

    timer = Timer("\nRe tool")
    found_indexes_with_re = [m.start() for m in re.finditer(to_find, text)]
    timer.stop()

    print("\nIs OK?", found_indexes == found_indexes_with_re)


if __name__ == "__main__":
    main()
