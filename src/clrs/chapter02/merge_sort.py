"""
Merge sort implementation.
"""

from typing import TypeVar

from clrs.utils import array_utils
from clrs.utils.comparable import Comparable
from clrs.utils.timer_utils import Timer

T = TypeVar("T", bound=Comparable)


def merge(array1: list[T], array2: list[T], orig_array: list[T]) -> list[T]:
    length1 = len(array1)
    length2 = len(array2)

    i1 = 0
    i2 = 0
    i = 0

    while i1 < length1 and i2 < length2:
        if array1[i1] <= array2[i2]:
            orig_array[i] = array1[i1]
            i1 += 1
            i += 1
        else:
            orig_array[i] = array2[i2]
            i2 += 1
            i += 1

    while i1 < length1:
        orig_array[i] = array1[i1]
        i1 += 1
        i += 1

    while i2 < length2:
        orig_array[i] = array2[i2]
        i2 += 1
        i += 1

    return orig_array


def merge_sort(array: list[T]) -> list[T]:
    """
    Sort an array in ascending order using the merge sort algorithm.
    """
    length = len(array)

    if length <= 1:
        return array

    half_size = length // 2

    array1 = array[:half_size]
    array2 = array[half_size:]

    array1_sorted = merge_sort(array1)
    array2_sorted = merge_sort(array2)

    array = merge(array1_sorted, array2_sorted, array)

    return array


def main():
    array: list[int] = array_utils.gen_rand_array(1000, 200000)
    timer = Timer("merge sort random array")
    sorted_array = merge_sort(array)
    timer.stop()

    timer = Timer("merge sort sorted array")
    sorted_array_2 = merge_sort(sorted_array)
    timer.stop()

    sorted_array_2.reverse()
    timer = Timer("merge sort reversed sorted array")
    sorted_array_3 = merge_sort(sorted_array_2)
    # print(sorted_array_3)
    timer.stop()


if __name__ == "__main__":
    main()
