"""
Naive string matching algorithm.
"""

import re

from clrs.chapter32.text import TEXT
from clrs.utils.timer_utils import Timer


def find_naive(to_find: str, text: str) -> list[int]:
    """
    Find all occurrences of a pattern in a text.
    """

    indexes = []

    len_text = len(text)
    len_to_find = len(to_find)

    i = 0
    while i < len_text - len_to_find + 1:
        is_match = True
        for j in range(len_to_find):
            if to_find[j] != text[i + j]:
                is_match = False
                break

        if is_match:
            indexes.append(i)

        i += 1

    return indexes


def main():
    """
    Compare the naive implementation with Python's regex search.
    """
    to_find = "match"

    timer = Timer("Naive impl")
    found_indexes = find_naive(to_find, TEXT)
    timer.stop()

    timer = Timer("\nRe tool")
    found_indexes_with_re = [m.start() for m in re.finditer(to_find, TEXT)]
    timer.stop()

    print("\nIs OK?", found_indexes == found_indexes_with_re)


if __name__ == "__main__":
    main()
