"""
Binary search implementation.
"""

from typing import Any


def binary_search(
    array: list[int], item: Any, start_i: int, end_i: int
) -> int | list[int]:
    """
    Find an item in a sorted array using binary search.

    Returns the index of the first occurrence if found; otherwise returns
    [-1, insertion_index].
    """

    if start_i == end_i:
        if array[start_i] == item:
            return start_i
        return [-1, start_i]

    half_index = start_i + (end_i - start_i) // 2

    if array[half_index] == item:
        first_i = half_index

        while first_i > 0 and array[first_i - 1] == item:
            first_i -= 1
        return first_i

    if array[half_index] < item:
        return binary_search(array, item, half_index + 1, end_i)

    return binary_search(array, item, start_i, half_index)
