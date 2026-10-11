"""
Problem 2-1
"""

from typing import TypeVar

from clrs.chapter02.insertion_sort import insertion_sort
from clrs.chapter02.merge_sort import merge, merge_sort
from clrs.utils import array_utils
from clrs.utils.comparable import Comparable
from clrs.utils.timer_utils import Timer

T = TypeVar("T", bound=Comparable)


def merge_ins_sort(array: list[T], k: int) -> list[T]:
    length = len(array)

    if length <= 1:
        return array

    half_size = round(length / 2)

    array1 = array[:half_size]
    array2 = array[half_size:]

    array1_sorted = None
    array2_sorted = None

    if length < k:
        array1_sorted = insertion_sort(array1)
        array2_sorted = insertion_sort(array2)
    else:
        array1_sorted = merge_ins_sort(array1, k)
        array2_sorted = merge_ins_sort(array2, k)

    array_sorted = merge(array1_sorted, array2_sorted, array)

    return array_sorted


def main():
    array_1: list[int] = array_utils.gen_rand_array(max_num=10000, length=30000)
    array_2 = array_1[:]

    timer = Timer("Merge sort random array")
    sorted_array = merge_sort(array_1)
    timer.stop()

    timer = Timer("Merge/insertion sort sort random array")
    sorted_array = merge_ins_sort(array_2, 100)
    timer.stop()


if __name__ == "__main__":
    main()
