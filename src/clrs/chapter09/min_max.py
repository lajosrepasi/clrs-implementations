"""
Algorithms for finding minimum and maximum values in an array.

Includes both the naive approach and the pairwise method from CLRS
that reduces the number of comparisons.
"""

from typing import TypeVar

from clrs.utils.array_utils import gen_rand_array
from clrs.utils.comparable import Comparable
from clrs.utils.timer_utils import Timer

T = TypeVar("T", bound=Comparable)


def minimum(A: list[T]) -> T:
    """
    Return the smallest element in the array.
    """

    m = A[0]

    l = len(A)

    for i in range(1, l):
        if A[i] < m:
            m = A[i]

    return m


def min_max_naive(A: list[T]) -> tuple[T, T]:
    """
    Return the minimum and maximum elements using a naive scan.
    """
    curr_min = A[0]
    curr_max = A[0]

    l = len(A)

    for i in range(l):
        if A[i] < curr_min:
            curr_min = A[i]

        if A[i] > curr_max:
            curr_max = A[i]

    return (curr_min, curr_max)


def min_max_effective(array: list[T]) -> tuple[T, T]:
    """
    Return the minimum and maximum elements using pairwise comparisons.
    """
    l = len(array)

    start = 1
    current_min = array[0]
    current_max = array[0]

    if l % 2 == 0:
        start = 2

        if array[0] > array[1]:
            current_max = array[0]
            current_min = array[1]
        else:
            current_max = array[1]
            current_min = array[0]

    for i in range(start, l, 2):
        array_i = array[i]
        array_ip1 = array[i + 1]

        if array_i > array_ip1:
            if array_i > current_max:
                current_max = array_i

            if array_ip1 < current_min:
                current_min = array_ip1

        else:
            if array_ip1 > current_max:
                current_max = array_ip1

            if array_i < current_min:
                current_min = array_i

    return (current_min, current_max)


def main():
    array: list[int] = gen_rand_array(10000000, 100000)

    min = minimum(array)
    print("minimum:", min)

    t = Timer()
    min_max = min_max_naive(array)
    print("min,max naive:", min_max)
    t.stop()

    t = Timer()
    min_max = min_max_effective(array)
    print("min,max effective:", min_max)
    t.stop()


if __name__ == "__main__":
    main()
