"""
Bucket sort implementation.
"""

import itertools
from math import floor

from clrs.chapter02.insertion_sort import insertion_sort
from clrs.utils.array_utils import gen_rand_array


def bucket_sort(A: list[int], max_item: int) -> list[int]:
    """
    Sort a list of non-negative integers using bucket sort.
    """
    if not A:
        return []

    if max_item <= 0:
        raise ValueError("max_item must be positive")

    if any(item < 0 or item > max_item for item in A):
        raise ValueError("array items must be between 0 and max_item")

    n = len(A)
    max_index = n - 1

    buckets: list[list[int]] = [[] for _ in range(n)]

    for item in A:

        item_dist = item / max_item
        bucket_index = floor(item_dist * max_index)

        buckets[bucket_index].append(item)

    for bucket in buckets:
        insertion_sort(bucket)

    sorted_array = list(itertools.chain.from_iterable(buckets))

    return sorted_array


def main():
    array = gen_rand_array(1000, 100)
    print(array)

    sorted_array = bucket_sort(array, 999)
    print(sorted_array)


if __name__ == "__main__":
    main()
