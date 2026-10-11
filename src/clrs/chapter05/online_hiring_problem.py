"""
Online hiring problem implementation using the 1/e stopping rule.
"""

import math
from random import randint


def get_online_maximum(candidates: list[int]) -> tuple[int, int]:
    """
    Select a candidate using the online maximum algorithm.

    Observes the first n/e candidates without selecting them, then
    returns the first candidate better than all previously observed
    candidates. Returns the last candidate if no such candidate exists.
    """
    n = len(candidates)
    k = round(n / math.e)

    best_so_far = -1

    for i in range(k):
        if candidates[i] > best_so_far:
            best_so_far = candidates[i]

    for i in range(k + 1, n):
        if candidates[i] > best_so_far:
            return (candidates[i], i)

    return (candidates[-1], n - 1)


def main():
    rand_array = [randint(0, 1000) for _ in range(100)]

    print("random array:", rand_array)
    max_item = max(rand_array)
    print("max:", max(rand_array), "index of max:", rand_array.index(max_item))

    max_online, index_max_online = get_online_maximum(rand_array)
    print("max online:", max_online, "index of max online:", index_max_online)


if __name__ == "__main__":
    main()
