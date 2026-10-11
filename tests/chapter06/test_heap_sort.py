from clrs.chapter06.heap_sort import heap_sort
from clrs.utils.sorting_test_utils import assert_sort_correct, assert_sort_random_array


def test_heap_sort():
    assert_sort_correct(heap_sort)


def test_heap_sort_random_array():
    assert_sort_random_array(heap_sort)


def test_heap_sort_does_not_modify_input():
    array = [5, 3, 1, 4, 2]
    original = array.copy()

    result = heap_sort(array)

    assert array == original
    assert result == [1, 2, 3, 4, 5]
    assert result is not array
