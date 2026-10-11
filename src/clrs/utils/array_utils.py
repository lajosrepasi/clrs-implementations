"""
Array utility functions.
"""

import random


def gen_rand_array(max_num: int, length: int) -> list[int]:
    """
    Generate a list of random integers.

    The list contains `length` integers in the range [0, max_num].
    """
    return [int(random.random() * max_num) for _ in range(length)]


def swap(i: int, j: int, array: list):
    """
    Swap the elements at indices i and j in the array.
    """
    array[i], array[j] = array[j], array[i]
