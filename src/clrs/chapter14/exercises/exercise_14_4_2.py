"""
Exercise 14.4-2
"""

from typing import Any

from clrs.chapter14.lcs import lcs


def get_lcs(c: list[list[Any]], X: list[Any], Y: list[Any], i: int, j: int) -> str:

    s = ""

    if i == 0 or j == 0:
        return s
    else:
        if X[i - 1] == Y[j - 1]:
            return get_lcs(c, X, Y, i - 1, j - 1) + str(X[i - 1])
        else:
            if c[i - 1][j] >= c[i][j - 1]:
                return get_lcs(c, X, Y, i - 1, j)
            else:
                return get_lcs(c, X, Y, i, j - 1)


def main():
    X = [1, 0, 0, 1, 0, 1, 0, 1]
    Y = [0, 1, 0, 1, 1, 0, 1, 1, 0]

    X = ["A", "B", "C", "B", "D", "A", "B"]
    Y = ["B", "D", "C", "A", "B", "A"]

    sol = lcs(X, Y)
    print(sol[0][-1][-1])

    print(get_lcs(sol[0], X, Y, len(X), len(Y)))


if __name__ == "__main__":
    main()
