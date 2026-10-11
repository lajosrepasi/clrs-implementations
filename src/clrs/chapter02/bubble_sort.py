"""
Bubble sort implementation.
"""

from typing import TypeVar

from clrs.utils import array_utils
from clrs.utils.comparable import Comparable
from clrs.utils.timer_utils import Timer

T = TypeVar("T", bound=Comparable)


def bubble_sort(array: list[T]) -> list[T]:
    """
    Sort an array in ascending order using the bubble sort algorithm.
    """
    l: int = len(array)

    for i in range(l):
        for j in range(l - 2, i - 1, -1):
            if array[j] > array[j + 1]:
                array_utils.swap(j, j + 1, array)

    return array


def main():
    array_1: list[int] = array_utils.gen_rand_array(max_num=10000, length=10000)
    timer = Timer("bubble sort random array")
    sorted_array = bubble_sort(array_1)
    timer.stop()


if __name__ == "__main__":
    main()
