"""
Radix sort implementation.
"""

from math import ceil, floor, log10, pow

from clrs.utils.array_utils import gen_rand_array


def get_digit(n: int, d: int):
    """Return the digit at position d, starting from the least significant digit."""
    return floor((n % pow(10, d + 1)) / pow(10, d))


def counting_sort_by_digit(array: list[int], digit: int):
    """Sort an array by the digit at position d using counting sort."""
    n = len(array)

    counting_array = [0] * 10
    sorted_array = [0] * n

    for i in range(n):
        counting_array[get_digit(array[i], digit)] += 1

    for j in range(1, 10):
        counting_array[j] += counting_array[j - 1]

    for i in range(n - 1, -1, -1):
        num = array[i]
        d = get_digit(num, digit)
        count_less_or_equals = counting_array[d]
        index_in_sorted_array = count_less_or_equals - 1
        sorted_array[index_in_sorted_array] = num

        # for duplicates we have to decrement counter
        counting_array[d] -= 1

    return sorted_array


def radix_sort(array: list[int], k: int):
    """Sort non-negative integers using radix sort."""

    if not array:
        return []

    if k < 0:
        raise ValueError("k must be non-negative")

    if any(num < 0 or num > k for num in array):
        raise ValueError("array values must be between 0 and k")

    max_digit = ceil(log10(k)) + 1

    sorted_array = array
    for digit in range(max_digit):
        sorted_array = counting_sort_by_digit(sorted_array, digit)

    return sorted_array


def main():
    array = gen_rand_array(1000, 100)
    print(array)

    sorted_array = radix_sort(array, 999)
    print(sorted_array)


if __name__ == "__main__":

    main()
