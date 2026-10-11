"""
Sorting test utils.
"""

import random
from collections.abc import Callable
from typing import TypeVar

from clrs.utils.comparable import Comparable

T = TypeVar("T", bound=Comparable)


def assert_sort_correct(
    sort_function: Callable[[list[T]], list[T]],
) -> None:
    """Verify that a sorting algorithm produces the expected result."""
    test_cases = [
        # General case
        ([5, 3, 1, 4, 2], [1, 2, 3, 4, 5]),
        # Already sorted
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        # Reverse sorted
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        # Duplicates
        ([3, 1, 3, 2, 1], [1, 1, 2, 3, 3]),
        # Single element
        ([5], [5]),
        # Empty
        ([], []),
        # Two elements
        ([2, 1], [1, 2]),
        # All elements equal
        ([3, 3, 3, 3], [3, 3, 3, 3]),
        # Negative numbers
        ([3, -1, 5, -7, 0], [-7, -1, 0, 3, 5]),
    ]

    for array, expected in test_cases:
        assert sort_function(array) == expected


def assert_sort_in_place(
    sort_function: Callable[[list[T]], list[T]],
) -> None:
    """Verify that the sorting algorithm modifies the input list in place."""
    array: list = [5, 3, 1, 4, 2]

    result = sort_function(array)

    assert result is array
    assert array == [1, 2, 3, 4, 5]


def assert_sort_random_array(
    sort_function: Callable[[list[T]], list[T]],
) -> None:
    """Verify that a sorting algorithm correctly sorts a random array."""
    random.seed(42)
    array: list = [random.randint(-1000, 1000) for _ in range(500)]

    expected = sorted(array)

    assert sort_function(array) == expected
