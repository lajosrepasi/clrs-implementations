"""
Selection sort implementation.
"""

from typing import TypeVar

from clrs.utils import array_utils
from clrs.utils.array_utils import swap
from clrs.utils.comparable import Comparable
from clrs.utils.timer_utils import Timer

T = TypeVar("T", bound=Comparable)


def selection_sort(array: list[T]) -> list[T]:
    """
    Sort an array in ascending order using the naive selection sort algorithm.
    """
    n = len(array)

    for i in range(n - 1):
        min_index = i
        min_item = array[i]

        for j in range(i + 1, n):
            if array[j] < min_item:
                min_index = j
                min_item = array[j]

        swap(i, min_index, array)

    return array


def main():
    array: list[int] = array_utils.gen_rand_array(1000, 10000)
    timer = Timer("selection sort random array")
    sorted_array = selection_sort(array)
    timer.stop()

    timer = Timer("selection sort sorted array")
    sorted_array_2 = selection_sort(sorted_array)
    timer.stop()

    sorted_array_2.reverse()
    timer = Timer("selection sort reversed sorted array")
    sorted_array_3 = selection_sort(sorted_array_2)
    timer.stop()


if __name__ == "__main__":
    main()
