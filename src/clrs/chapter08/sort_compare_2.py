"""
Benchmark sorting algorithm implementations.
"""

from clrs.chapter02.bubble_sort import bubble_sort
from clrs.chapter02.insertion_sort import insertion_sort
from clrs.chapter02.merge_sort import merge_sort
from clrs.chapter02.selection_sort import selection_sort
from clrs.chapter06.heap_sort import heap_sort
from clrs.chapter07.quick_sort import quick_sort
from clrs.chapter08.bucket_sort import bucket_sort
from clrs.chapter08.counting_sort import counting_sort
from clrs.chapter08.radix_sort import radix_sort
from clrs.utils import array_utils
from clrs.utils.timer_utils import Timer


def main():
    n = 10000
    max_item = 999

    array: list[int] = array_utils.gen_rand_array(max_item + 1, n)
    array_for_bubble_sort: list[int] = array.copy()
    array_for_selection_sort: list[int] = array.copy()
    array_for_insertion_sort: list[int] = array.copy()
    array_for_heap_sort: list[int] = array.copy()
    array_for_merge_sort: list[int] = array.copy()
    array_for_quick_sort: list[int] = array.copy()
    array_for_counting_sort: list[int] = array.copy()
    array_for_radix_sort: list[int] = array.copy()
    array_for_bucket_sort: list[int] = array.copy()

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

    timer = Timer("Counting sort")
    sorted_array = counting_sort(array_for_counting_sort, max_item + 1)
    timer.stop()

    timer = Timer("Radix sort")
    sorted_array = radix_sort(array_for_radix_sort, max_item)
    timer.stop()

    timer = Timer("Bucket sort")
    sorted_array = bucket_sort(array_for_bucket_sort, max_item)
    timer.stop()


if __name__ == "__main__":
    main()
