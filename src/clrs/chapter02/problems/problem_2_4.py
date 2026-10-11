"""
Problem 2-4
"""

from clrs.utils.timer_utils import Timer


def merge(array1: list[int], array2: list[int]):
    merged = []
    length1 = len(array1)
    length2 = len(array2)

    i1 = 0
    i2 = 0

    inversions = 0
    while i1 < length1 and i2 < length2:
        if array1[i1] < array2[i2]:
            merged.append(array1[i1])
            i1 += 1
        elif array1[i1] >= array2[i2]:
            merged.append(array2[i2])
            i2 += 1
            inversions += i2

    while i1 < length1:
        merged.append(array1[i1])
        inversions += length2
        i1 += 1

    while i2 < length2:
        merged.append(array2[i2])
        i2 += 1

    return (merged, inversions)


def merge_sort(array: list[int]) -> tuple[list[int], int]:
    length = len(array)

    if length <= 1:
        return (array, 0)

    half_size = round(length / 2)

    array1 = array[:half_size]
    array2 = array[half_size:]

    (array1_sorted, inversions_1) = merge_sort(array1)
    (array2_sorted, inversions_2) = merge_sort(array2)

    (array_sorted, inversions) = merge(array1_sorted, array2_sorted)

    inversions_sum = inversions_1 + inversions_2 + inversions

    return (array_sorted, inversions_sum)


def main():
    timer = Timer("merge sort random array")
    (sorted_array, inversions) = merge_sort([2, 3, 8, 6, 1])
    timer.stop()

    print(inversions)
    print(sorted_array)


if __name__ == "__main__":
    main()
