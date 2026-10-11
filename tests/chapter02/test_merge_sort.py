from clrs.chapter02.merge_sort import merge, merge_sort
from clrs.utils.sorting_test_utils import (
    assert_sort_correct,
    assert_sort_in_place,
    assert_sort_random_array,
)


def test_merge_sort():
    assert_sort_correct(merge_sort)


def test_merge_sort_in_place():
    assert_sort_in_place(merge_sort)


def test_merge_sort_random_array():
    assert_sort_random_array(merge_sort)


def test_merge():
    array1: list = [1, 3, 5]
    array2: list = [2, 4, 6]
    array: list = [0] * 6

    result = merge(array1, array2, array)

    assert result == [1, 2, 3, 4, 5, 6]
    assert result is array


def test_merge_with_empty_array():
    array1: list = []
    array2: list = [1, 2, 3]
    array: list = [0] * 3

    assert merge(array1, array2, array) == [1, 2, 3]


def test_merge_with_duplicates():
    array1: list = [1, 2, 2]
    array2: list = [2, 3, 3]
    array: list = [0] * 6

    assert merge(array1, array2, array) == [1, 2, 2, 2, 3, 3]
