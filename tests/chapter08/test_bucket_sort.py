import pytest

from clrs.chapter08.bucket_sort import bucket_sort


@pytest.mark.parametrize(
    ("array", "max_item", "expected"),
    [
        ([], 100, []),
        ([5], 5, [5]),
        ([5, 3, 1, 4, 2], 5, [1, 2, 3, 4, 5]),
        ([5, 4, 3, 2, 1], 5, [1, 2, 3, 4, 5]),
        ([3, 1, 3, 2, 1], 3, [1, 1, 2, 3, 3]),
        ([3, 3, 3, 3], 3, [3, 3, 3, 3]),
        ([0, 0, 0], 10, [0, 0, 0]),
        ([0, 5, 0, 5, 2], 5, [0, 0, 2, 5, 5]),
        ([5, 1, 4, 2, 3], 100, [1, 2, 3, 4, 5]),
    ],
)
def test_bucket_sort(array, max_item, expected):
    assert bucket_sort(array, max_item) == expected


def test_bucket_sort_random_array():
    import random

    random.seed(42)
    array = [random.randint(0, 1000) for _ in range(500)]

    assert bucket_sort(array, 1000) == sorted(array)
