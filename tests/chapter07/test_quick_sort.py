from clrs.chapter07.quick_sort import quick_sort
from clrs.utils.sorting_test_utils import (
    assert_sort_correct,
    assert_sort_in_place,
    assert_sort_random_array,
)


def test_quick_sort_correct():
    assert_sort_correct(quick_sort)


def test_quick_sort_in_place():
    assert_sort_in_place(quick_sort)


def test_quick_sort_random_array():
    assert_sort_random_array(quick_sort)


def test_quick_sort_same_values():
    array: list = [42] * 100

    result = quick_sort(array)

    assert result == [42] * 100


def test_quick_sort_many_duplicates():
    array: list = [5, 3, 5, 2, 5, 1, 5, 4, 5]

    result = quick_sort(array)

    assert result == sorted(array)
