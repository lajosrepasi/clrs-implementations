import pytest

from clrs.chapter08.counting_sort import counting_sort, counting_sort_forward_iterate


@pytest.mark.parametrize(
    ("array", "k", "expected"),
    [
        ([], 1, []),
        ([0], 1, [0]),
        ([5, 3, 1, 4, 2], 6, [1, 2, 3, 4, 5]),
        ([1, 2, 3, 4, 5], 6, [1, 2, 3, 4, 5]),
        ([5, 4, 3, 2, 1], 6, [1, 2, 3, 4, 5]),
        ([3, 1, 3, 2, 1], 4, [1, 1, 2, 3, 3]),
        ([3, 3, 3, 3], 4, [3, 3, 3, 3]),
        ([0, 0, 0], 1, [0, 0, 0]),
        ([0, 4, 2, 1, 3], 5, [0, 1, 2, 3, 4]),
    ],
)
def test_counting_sort(array, k, expected):
    assert counting_sort(array, k) == expected
    assert counting_sort_forward_iterate(array, k) == expected


def test_counting_sort_random_array():
    import random

    random.seed(42)
    array = [random.randint(0, 999) for _ in range(500)]

    assert counting_sort(array, 1000) == sorted(array)


def test_counting_sort_does_not_modify_input():
    array = [4, 1, 3, 2, 1]
    original = array.copy()

    counting_sort(array, 5)

    assert array == original
