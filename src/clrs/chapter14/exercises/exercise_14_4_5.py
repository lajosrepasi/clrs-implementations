"""
Exercise 14.4-5
"""

from clrs.chapter14.lcs import get_lcs_list, lcs


def get_lmis(a: list[int]) -> list[int]:
    sorted_a = sorted(a)

    sol = lcs(a, sorted_a)

    return get_lcs_list(sol[1], a, len(a), len(a))


def main():
    print(get_lmis([1, 23, 2, 6, 3, 4, 5, 1, 7, 100]))


if __name__ == "__main__":
    main()
