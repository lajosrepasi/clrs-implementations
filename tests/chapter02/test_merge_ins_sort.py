from clrs.chapter02.problems.problem_2_1 import merge_ins_sort
from clrs.utils.sorting_test_utils import (
    assert_sort_correct,
    assert_sort_in_place,
    assert_sort_random_array,
)


def test_merge_ins_sort():
    assert_sort_correct(lambda array: merge_ins_sort(array, k=3))


def test_merge_ins_sort_in_place():
    assert_sort_in_place(lambda array: merge_ins_sort(array, k=3))


def test_merge_ins_sort_random_array():
    assert_sort_random_array(lambda array: merge_ins_sort(array, k=3))
