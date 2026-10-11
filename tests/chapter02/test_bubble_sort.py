from clrs.chapter02.bubble_sort import bubble_sort
from clrs.utils.sorting_test_utils import (
    assert_sort_correct,
    assert_sort_in_place,
    assert_sort_random_array,
)


def test_bubble_sort():
    assert_sort_correct(bubble_sort)


def test_bubble_sort_in_place():
    assert_sort_in_place(bubble_sort)


def test_bubble_sort_random_array():
    assert_sort_random_array(bubble_sort)
