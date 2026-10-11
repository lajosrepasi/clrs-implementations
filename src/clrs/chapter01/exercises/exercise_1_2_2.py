"""
Exercise 1.2-2
"""

from math import log2

n: int = 2

while True:
    insertion_sort_time: int = 8 * n * n
    merge_sort_time: float = 64 * n * log2(n)

    if insertion_sort_time > merge_sort_time:
        break

    n += 1

print(n)
