"""
Selection-based algorithms for finding minimum and maximum values.
"""

import random
from time import time
from typing import TypeVar

from clrs.utils.comparable import Comparable

T = TypeVar("T", bound=Comparable)


def min_sel(array: list[T]) -> T:
    """
    Return the minimum element using a linear scan.
    """
    current_min = array[0]

    for i in range(1, len(array)):
        if current_min > array[i]:
            current_min = array[i]

    return current_min


def max_sel(array: list[T]) -> T:
    """
    Return the maximum element using a linear scan.
    """
    current_max = array[0]

    for i in range(1, len(array)):
        if current_max < array[i]:
            current_max = array[i]

    return current_max


def min_max(array: list[T]) -> tuple[T, T]:
    """
    Return the minimum and maximum using pairwise comparisons.
    """
    array_len = len(array)

    if array_len % 2 == 0:
        current_min = None
        current_max = None

        if array[0] > array[1]:
            current_max = array[0]
            current_min = array[1]
        else:
            current_max = array[1]
            current_min = array[0]

        for i in range(2, array_len, 2):
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

        return current_min, current_max

    else:

        current_min = array[0]
        current_max = array[0]

        for i in range(1, array_len, 2):
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

        return current_min, current_max


def main():
    array: list[int] = [int(123123423432 * random.random()) for _ in range(1000000)]

    print("min max with sort")
    start = time()
    sorted_array = sorted(array)
    print(sorted_array[0])
    print(sorted_array[-1])
    print("time: {0}\n".format(time() - start))

    print("min max with two selection")
    start = time()
    print(min_sel(array))
    print(max_sel(array))
    print("time: {0}\n".format(time() - start))

    print("min max with combined, two step algorithm")
    start = time()
    print(min_max(array))
    print("time: {0}\n".format(time() - start))


if __name__ == "__main__":
    main()
