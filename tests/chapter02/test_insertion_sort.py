from clrs.chapter02.insertion_sort import insertion_sort, insertion_sort_recursive
from clrs.utils.sorting_test_utils import (
    assert_sort_correct,
    assert_sort_in_place,
    assert_sort_random_array,
)


def test_insertion_sort():
    assert_sort_correct(insertion_sort)


def test_insertion_sort_in_place():
    assert_sort_in_place(insertion_sort)


def test_insertion_sort_random_array():
    assert_sort_random_array(insertion_sort)


def test_insertion_sort_recursive():
    assert_sort_correct(insertion_sort_recursive)


def test_insertion_sort_recursive_random_array():
    assert_sort_random_array(insertion_sort_recursive)
