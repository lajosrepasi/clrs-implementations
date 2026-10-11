"""
Random array permutation using the Fisher–Yates shuffle algorithm.
"""

from random import randrange

from clrs.utils.array_utils import swap


def randomly_permute(array: list[int]) -> list[int]:
    """
    Randomly permute the elements of an array in place.
    """
    l = len(array)

    for i in range(l - 1):
        index_to_swap = randrange(i, l)
        swap(i, index_to_swap, array)

    return array


def main():
    inc_array = [i for i in range(100)]

    shuffled_array = randomly_permute(inc_array)

    print(shuffled_array)


if __name__ == "__main__":
    main()
