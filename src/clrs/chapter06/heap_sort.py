"""
Heap sort implementation.
"""

from typing import TypeVar

from clrs.chapter06.heap import Heap
from clrs.utils import array_utils
from clrs.utils.timer_utils import Timer

T = TypeVar("T")


def heap_sort(array: list[T]) -> list[T]:
    """
    Sort an array in ascending order using the heap sort algorithm.
    """
    sorted_array: list[T] = []

    h = Heap(array)
    n = len(h)

    for i in range(n - 1, -1, -1):
        sorted_array.insert(0, h.get_max())
        h.swap(0, i)
        h.remove_last_item()
        h.max_heapify(0)

    return sorted_array


def main():
    array: list[int] = array_utils.gen_rand_array(1000, 100)
    print(array)
    timer = Timer("Heap sort random array")
    sorted_array: list[int] = heap_sort(array)
    timer.stop()
    print(sorted_array)


if __name__ == "__main__":
    main()
