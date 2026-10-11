from clrs.chapter09.rand_and_linear_select import (
    linear_select,
    randomised_select,
)


def test_randomised_select_small():
    array: list = [5, 1, 9, 3, 7]

    assert randomised_select(array.copy(), 0, 4, 0) == 1
    assert randomised_select(array.copy(), 0, 4, 2) == 5
    assert randomised_select(array.copy(), 0, 4, 4) == 9


def test_randomised_select_duplicates():
    array: list = [3, 1, 3, 2, 1]

    assert randomised_select(array.copy(), 0, 4, 0) == 1
    assert randomised_select(array.copy(), 0, 4, 1) == 1
    assert randomised_select(array.copy(), 0, 4, 4) == 3


def test_linear_select_small():
    array: list = [5, 1, 9, 3, 7]

    assert linear_select(array.copy(), 0, 4, 0) == 1
    assert linear_select(array.copy(), 0, 4, 2) == 5
    assert linear_select(array.copy(), 0, 4, 4) == 9


def test_linear_select_duplicates():
    array: list = [3, 1, 3, 2, 1]

    assert linear_select(array.copy(), 0, 4, 0) == 1
    assert linear_select(array.copy(), 0, 4, 1) == 1
    assert linear_select(array.copy(), 0, 4, 4) == 3


def test_randomised_and_linear_match_sorted():
    array: list = [8, 2, 7, 1, 9, 4, 6, 3, 5]

    expected = sorted(array)

    for i in range(len(array)):
        assert randomised_select(array.copy(), 0, len(array) - 1, i) == expected[i]

        assert linear_select(array.copy(), 0, len(array) - 1, i) == expected[i]
