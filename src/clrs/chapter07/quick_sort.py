"""
Randomized quicksort implementation.
"""

from math import floor
from random import randint
from typing import TypeVar

from clrs.utils import array_utils
from clrs.utils.array_utils import swap
from clrs.utils.comparable import Comparable
from clrs.utils.timer_utils import Timer

T = TypeVar("T", bound=Comparable)


def partition(array: list[T], p: int, r: int) -> int:
    """
    Partition a subarray and return the pivot index.
    """
    random_index = randint(p, r)
    swap(r, random_index, array)

    i = p
    pivot = array[r]

    are_same_values = True
    for j in range(p, r):

        if array[j] != pivot:
            are_same_values = False

        if array[j] <= pivot:
            swap(i, j, array)
            i += 1

    if are_same_values:
        return floor((p + r) / 2)

    swap(i, r, array)

    return i


def quick_sort_with_indexes(array: list[T], p: int, r: int) -> list[T]:
    """
    Sort a subarray using quicksort.
    """
    if p < r:
        pivot_index = partition(array, p, r)
        quick_sort_with_indexes(array, p, pivot_index - 1)
        quick_sort_with_indexes(array, pivot_index + 1, r)

    return array


def quick_sort(array: list[T]) -> list[T]:
    """
    Sort an array in ascending order using quicksort.
    """
    return quick_sort_with_indexes(array, 0, len(array) - 1)


def main():
    array: list[int] = array_utils.gen_rand_array(1000, 100)
    print(array)
    timer = Timer("Quick sort random array")
    sorted_array = quick_sort(array)
    timer.stop()
    print(sorted_array)

    array_same_element: list[int] = [100] * 100
    print(array_same_element)
    timer = Timer("Quick sort array with same elements")
    sorted_array = quick_sort(array_same_element)
    timer.stop()
