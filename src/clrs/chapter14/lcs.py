"""
Dynamic programming solution for the Longest Common Subsequence problem.

Computes both the LCS length table and the direction table used
to reconstruct an optimal subsequence.
"""

from typing import Any

UP = "U"
LEFT = "L"
LEFT_UP = "LU"


def lcs(x: list[Any], y: list[Any]) -> tuple[list[list], list[list]]:
    """
    Compute the longest common subsequence tables for two sequences.
    """
    m = len(x) + 1
    n = len(y) + 1

    c: list[list] = [[None for _ in range(n)] for _ in range(m)]
    b: list[list] = [[None for _ in range(n)] for _ in range(m)]

    for i in range(m):
        c[i][0] = 0

    for j in range(n):
        c[0][j] = 0

    for i in range(1, m):
        for j in range(1, n):
            if x[i - 1] == y[j - 1]:
                c[i][j] = c[i - 1][j - 1] + 1
                b[i][j] = LEFT_UP
            elif c[i - 1][j] >= c[i][j - 1]:
                c[i][j] = c[i - 1][j]
                b[i][j] = UP
            else:
                c[i][j] = c[i][j - 1]
                b[i][j] = LEFT

    return (c, b)


def get_lcs(b: list[list], x: list, i: int, j: int) -> str:
    """
    Reconstruct the longest common subsequence as a string.
    """
    s = ""
    if i == 0 or j == 0:
        return s
    else:
        if b[i][j] == LEFT_UP:
            s += get_lcs(b, x, i - 1, j - 1) + str(x[i - 1])
        elif b[i][j] == UP:
            s += get_lcs(b, x, i - 1, j)
        elif b[i][j] == LEFT:
            s += get_lcs(b, x, i, j - 1)

    return s


def get_lcs_list(b: list[list], x, i: int, j: int) -> list:
    """
    Reconstruct the longest common subsequence as a list.
    """
    s = []
    if i == 0 or j == 0:
        return s
    else:
        if b[i][j] == LEFT_UP:
            s += get_lcs_list(b, x, i - 1, j - 1) + [x[i - 1]]
        elif b[i][j] == UP:
            s += get_lcs_list(b, x, i - 1, j)
        elif b[i][j] == LEFT:
            s += get_lcs_list(b, x, i, j - 1)

    return s


def main():
    x = [1, 0, 0, 1, 0, 1, 0, 1]
    y = [0, 1, 0, 1, 1, 0, 1, 1, 0]

    # x = ['A', 'B', 'C', 'B', 'D', 'A', 'B']
    # y = ['B', 'D', 'C', 'A', 'B', 'A']

    sol = lcs(x, y)
    print(sol[0][-1][-1])
    print(get_lcs(sol[1], x, len(x), len(y)))


if __name__ == "__main__":
    main()
