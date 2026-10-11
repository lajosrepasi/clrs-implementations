"""
Dynamic programming algorithms for matrix-chain multiplication.

Computes the optimal parenthesization of a matrix chain and the
minimum number of scalar multiplications required.
"""


def number_of_parenthesization(n: int) -> int:
    """
    Return the number of valid parenthesizations for n matrices.
    """
    if n == 1:
        return 1

    s = 0

    for k in range(1, n):
        s += number_of_parenthesization(k) * number_of_parenthesization(n - k)

    return s


def get_matrices_list(p: list) -> list:
    """
    Convert a dimension array into a list of matrix descriptions.
    """
    matrices = []
    for i in range(0, len(p) - 1):
        num_of_rows = str(p[i])
        num_of_cols = str(p[i + 1])
        matrices.append("{0}x{1}".format(num_of_rows, num_of_cols))

    return matrices


def matrix_chain_order(p, n) -> tuple[list[list], int | float]:
    """
    Compute the optimal matrix-chain multiplication order.
    """
    m: list[list] = [[None for _ in range(n)] for _ in range(n)]
    s: list[list] = [[None for _ in range(n)] for _ in range(n)]

    for i in range(n):
        m[i][i] = 0

    for l in range(2, n + 1):
        for i in range(0, n - l + 1):
            j = i + l - 1
            if j > i:
                m[i][j] = float("inf")
                for k in range(i, j):
                    sol = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j]
                    if sol < m[i][j]:
                        m[i][j] = sol
                        s[i][j] = k

    return (s, m[1][n - 1])


def get_solution(matrices: list[list], s: list[list], i: int, j: int) -> str | list:
    """
    Reconstruct the optimal parenthesization from the split table.
    """
    if i == j:
        return matrices[i - 1]
    else:
        return "({0})*({1})".format(
            get_solution(matrices, s, i, s[i][j]),
            get_solution(matrices, s, s[i][j] + 1, j),
        )


def main():
    p = [5, 10, 3, 12, 5, 50, 6]
    n = len(p)

    print(get_matrices_list(p))
    sol = matrix_chain_order(p, n)
    print(sol[1])
    print(get_solution(get_matrices_list(p), sol[0], 1, n - 1))


if __name__ == "__main__":
    main()
