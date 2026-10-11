import pytest

from clrs.chapter08.radix_sort import radix_sort


def test_radix_sort():
    array = [329, 457, 657, 839, 436, 720, 355]

    assert radix_sort(array, 999) == [
        329,
        355,
        436,
        457,
        657,
        720,
        839,
    ]


@pytest.mark.parametrize(
    ("array", "k", "expected"),
    [
        ([], 1, []),
        ([0], 1, [0]),
        ([5], 5, [5]),
        ([5, 3, 1, 4, 2], 5, [1, 2, 3, 4, 5]),
        ([5, 4, 3, 2, 1], 5, [1, 2, 3, 4, 5]),
        ([3, 1, 3, 2, 1], 3, [1, 1, 2, 3, 3]),
        ([100, 1, 10, 1000, 10], 1000, [1, 10, 10, 100, 1000]),
    ],
)
def test_radix_sort_edge_cases(array, k, expected):
    assert radix_sort(array, k) == expected


def test_radix_sort_random_array():
    import random

    random.seed(42)
    array = [random.randint(0, 9999) for _ in range(500)]

    assert radix_sort(array, 9999) == sorted(array)
