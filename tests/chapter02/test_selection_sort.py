from clrs.chapter02.selection_sort import selection_sort
from clrs.utils.sorting_test_utils import (
    assert_sort_correct,
    assert_sort_in_place,
    assert_sort_random_array,
)


def test_selection_sort():
    assert_sort_correct(selection_sort)


def test_selection_sort_in_place():
    assert_sort_in_place(selection_sort)


def test_selection_sort_random_array():
    assert_sort_random_array(selection_sort)
