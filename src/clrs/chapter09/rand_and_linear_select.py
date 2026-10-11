"""
Selection algorithms based on randomized partitioning and median-of-medians.
"""

from math import floor
from random import randint
from typing import TypeVar

from clrs.chapter02.insertion_sort import insertion_sort
from clrs.chapter07.quick_sort import partition
from clrs.utils.array_utils import gen_rand_array, swap
from clrs.utils.comparable import Comparable
from clrs.utils.timer_utils import Timer

T = TypeVar("T", bound=Comparable)


def randomised_select(array: list[T], p: int, r: int, i: int) -> T | None:
    """
    Return the ith order statistic using randomized quickselect.
    """

    if p > r:
        return

    k = partition(array, p, r)

    if k == i:
        return array[i]

    if k < i:
        return randomised_select(array, k + 1, r, i)
    else:
        return randomised_select(array, p, k - 1, i)


def partition_around_pivot(array: list[T], p: int, r: int, pivot: T) -> int:
    """
    Partition a subarray around the given pivot value.
    """
    pivot_index = p

    for j in range(p, r):
        if array[j] == pivot:
            pivot_index = j
            pivot = array[j]
            break

    swap(r, pivot_index, array)

    i = p

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


def linear_select(array: list[T], p: int, r: int, i: int) -> T:
    """
    Return the ith order statistic using median-of-medians.
    """
    n = r - p + 1

    while n % 5 != 0:
        for j in range(p + 1, r):
            if array[j] < array[p]:
                swap(j, p, array)

        if i == 0:
            return array[p]

        p = p + 1
        i = i - 1

        n = r - p + 1

    g = int(n / 5)

    for j in range(p, p + g):
        indexes = [(j + gi) for gi in range(0, 4 * g + 1, g)]
        group = [array[j + gi] for gi in range(0, 4 * g + 1, g)]
        insertion_sort(group)

        for ii in range(5):
            array[indexes[ii]] = group[ii]

    x = linear_select(array, p + 2 * g, p + 3 * g - 1, floor(g / 2))

    k = partition_around_pivot(array, p, r, x)

    if k == p + i:
        return array[k]

    if k < p + i:
        return linear_select(array, k + 1, r, i - (k - p + 1))

    return linear_select(array, p, k - 1, i)


def main():
    length = 20000
    max_num = 1000

    array: list[int] = gen_rand_array(max_num, length)
    array_for_sorted_select: list[int] = array.copy()
    array_for_rand_select: list[int] = array.copy()
    array_for_linear_select: list[int] = array.copy()

    i = randint(1, length)

    print("Find %ith element with sort." % i)
    t = Timer()
    sorted_array = sorted(array_for_sorted_select)
    ith_with_sort = sorted_array[i - 1]
    print("%ith element is: %i" % (i, ith_with_sort))
    t.stop()

    print()

    print("Find %ith element with randomised quick select." % i)
    t = Timer()
    ith_with_rqs = randomised_select(array_for_rand_select, 0, length - 1, i - 1)
    print("%ith element is: %i" % (i, ith_with_rqs))
    t.stop()

    print()

    print("Find %ith element with linear select." % i)
    t = Timer()
    ith_with_ls = linear_select(array_for_linear_select, 0, length - 1, i - 1)
    print("%ith element is: %i" % (i, ith_with_ls))
    t.stop()


if __name__ == "__main__":
    main()
