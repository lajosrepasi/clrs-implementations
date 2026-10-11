"""
Benchmark sorting algorithm implementations.
"""

from clrs.chapter02.bubble_sort import bubble_sort
from clrs.chapter02.insertion_sort import insertion_sort
from clrs.chapter02.merge_sort import merge_sort
from clrs.chapter02.selection_sort import selection_sort
from clrs.chapter06.heap_sort import heap_sort
from clrs.chapter07.quick_sort import quick_sort
from clrs.utils import array_utils
from clrs.utils.timer_utils import Timer


def main():
    array: list = array_utils.gen_rand_array(1000, 8000)
    array_for_bubble_sort: list = array.copy()
    array_for_selection_sort: list = array.copy()
    array_for_insertion_sort: list = array.copy()
    array_for_heap_sort: list = array.copy()
    array_for_merge_sort: list = array.copy()
    array_for_quick_sort: list = array.copy()

    timer = Timer("Bubble sort")
    sorted_array = bubble_sort(array_for_bubble_sort)
    timer.stop()

    timer = Timer("Selection sort")
    sorted_array = selection_sort(array_for_selection_sort)
    timer.stop()

    timer = Timer("Insertion sort")
    sorted_array = insertion_sort(array_for_insertion_sort)
    timer.stop()

    timer = Timer("Heap sort")
    sorted_array = heap_sort(array_for_heap_sort)
    timer.stop()

    timer = Timer("Merge sort")
    sorted_array = merge_sort(array_for_merge_sort)
    timer.stop()

    timer = Timer("Quick sort")
    sorted_array = quick_sort(array_for_quick_sort)
    timer.stop()


if __name__ == "__main__":
    main()
