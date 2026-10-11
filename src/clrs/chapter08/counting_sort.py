"""
Counting sort implementation.
"""

from clrs.utils.array_utils import gen_rand_array


def counting_sort(array: list[int], k: int) -> list[int]:
    """Sort an array of integers in the range 0 to k - 1."""
    n = len(array)

    counting_array = [0] * k
    sorted_array = [0] * n

    for i in range(n):
        counting_array[array[i]] += 1

    for j in range(1, k):
        counting_array[j] += counting_array[j - 1]

    for i in range(n - 1, -1, -1):
        num = array[i]
        count_less_or_equals = counting_array[num]
        index_in_sorted_array = count_less_or_equals - 1
        sorted_array[index_in_sorted_array] = num

        # for duplicates we have to decrement counter
        counting_array[num] -= 1

    return sorted_array


def counting_sort_forward_iterate(array: list[int], k: int) -> list[int]:
    """Sort an array using counting sort while iterating forward."""
    n = len(array)

    counting_array = [0] * k
    counting_array_without_sum = [0] * k
    sorted_array = [0] * n

    for i in range(n):
        counting_array[array[i]] += 1
        counting_array_without_sum[array[i]] += 1

    for j in range(1, k):
        counting_array[j] += counting_array[j - 1]

    for i in range(0, n):
        num = array[i]

        count_less = counting_array[num] - counting_array_without_sum[num]

        index_in_sorted_array = count_less
        sorted_array[index_in_sorted_array] = num

        # for duplicates we have to decrement counter
        counting_array_without_sum[num] -= 1

    return sorted_array


def main():
    array = gen_rand_array(1000, 100)
    print(array)

    sorted_array = counting_sort(array, 1000)
    print("Countin sort 1:", sorted_array)

    sorted_array = counting_sort_forward_iterate(array, 1000)
    print("Counting sort 2:", sorted_array)


if __name__ == "__main__":
    main()
