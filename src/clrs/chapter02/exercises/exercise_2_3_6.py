"""
Exercise 2.3-6
"""

from random import randint

from clrs.chapter02.binary_search import binary_search
from clrs.chapter02.merge_sort import merge_sort
from clrs.utils import array_utils
from clrs.utils.timer_utils import Timer


def main():
    limit = 10000

    array: list[int] = array_utils.gen_rand_array(limit, 1000)
    timer = Timer("merge sort random array")
    sorted_array = merge_sort(array)
    timer.stop()

    to_find = randint(0, limit)
    print("Find %i" % to_find)

    print("\n")
    try:
        timer = Timer("Find with index method timer")
        i_with_index = sorted_array.index(to_find)
        print("Index found with index method: " + str(i_with_index))
        timer.stop()
    except ValueError as e:
        print(e)
        timer.stop()

    print("\n")
    timer = Timer("Find with index binary search timer")
    i_with_binary_search = binary_search(
        sorted_array, to_find, 0, len(sorted_array) - 1
    )
    print("Index found with binary search: " + str(i_with_binary_search))
    timer.stop()


if __name__ == "__main__":
    main()
