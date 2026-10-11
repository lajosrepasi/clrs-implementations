"""
Exercise 5.1-2
"""

from math import ceil, log2
from random import random


def get_random_0_1() -> float:
    return round(random())


def get_random_bin(a: int, b: int) -> int:
    rand_bin_str = ""
    diff = b - a
    bin_length = ceil(log2(diff))

    for _ in range(bin_length):
        rand_bin_str += str(get_random_0_1())

    rand_int = int(rand_bin_str, 2)

    if rand_int > diff:
        return get_random_bin(a, b)

    return a + rand_int


def main():
    arr = [0] * 101
    for _ in range(1000):
        n = get_random_bin(0, 100)
        arr[n] += 1

    print(arr)


if __name__ == "__main__":
    main()
