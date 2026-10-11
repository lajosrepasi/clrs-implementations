"""
Insertion sort implementation.
"""

from typing import TypeVar

from clrs.utils import array_utils
from clrs.utils.comparable import Comparable
from clrs.utils.timer_utils import Timer

T = TypeVar("T", bound=Comparable)


def insertion_sort(array: list[T]) -> list[T]:
    """
    Sort an array in ascending order using the insertion sort algorithm.
    """
    l: int = len(array)

    for i in range(1, l):
        key = array[i]
        j = i - 1

        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = key

    return array


def insertion_sort_recursive(array: list[T]) -> list[T]:
    """
    Sort an array in ascending order using the recursive insertion sort algorithm.
    """
    l: int = len(array)

    if l <= 1:
        return array

    sub_array: list = array[: l - 1]
    item_to_insert: T = array[-1]
    sorted_sub_array: list[T] = insertion_sort_recursive(sub_array)

    i: int = 0
    while i < len(sorted_sub_array) and sorted_sub_array[i] <= item_to_insert:
        i += 1

    sorted_sub_array.insert(i, item_to_insert)

    return sorted_sub_array


def main():
    array: list[int] = array_utils.gen_rand_array(5000, 100)
    timer = Timer("insertion sort random array")
    sorted_array: list[int] = insertion_sort(array)
    timer.stop()

    timer = Timer("insertion sort sorted array")
    sorted_array_2: list[int] = insertion_sort(sorted_array)
    timer.stop()

    sorted_array_2.reverse()
    timer = Timer("insertion sort reversed sorted array")
    sorted_array_3: list[int] = insertion_sort(sorted_array_2)
    timer.stop()


if __name__ == "__main__":
    main()
