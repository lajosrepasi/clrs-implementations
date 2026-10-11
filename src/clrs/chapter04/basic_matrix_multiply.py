"""
Basic matrix multiplication implementation.
"""

from clrs.utils.matrix_utils import (
    gen_empty_matrix,
    gen_rand_matrix,
    get_matrix_dimensions,
    print_matrix,
)


def multiply_matrix_basic(m1: list[list[int]], m2: list[list[int]]) -> list[list[int]]:
    """
    Multiply two square matrices using the basic matrix multiplication algorithm.
    """
    (columns, rows) = get_matrix_dimensions(m1)
    multiplied_matrix = gen_empty_matrix(columns, rows)

    for i in range(rows):
        for j in range(columns):
            c_i_j = 0

            for k in range(columns):
                c_i_j += m1[i][k] * m2[k][j]

            multiplied_matrix[i][j] = c_i_j

    return multiplied_matrix


def main():
    columns = 3
    rows = 3
    max_num = 50

    m1 = gen_rand_matrix(columns, rows, max_num)
    print_matrix(m1)
    print()
    m2 = gen_rand_matrix(columns, rows, max_num)
    print_matrix(m2)
    print()

    multiplied_matrix = multiply_matrix_basic(m1, m2)
    print_matrix(multiplied_matrix)


if __name__ == "__main__":
    main()
