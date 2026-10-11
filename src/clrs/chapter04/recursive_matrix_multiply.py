"""
Recursive matrix multiplication implementation.
"""

from clrs.chapter04.basic_matrix_multiply import multiply_matrix_basic
from clrs.utils.matrix_utils import Matrix, gen_rand_matrix, join_4_matrixes
from clrs.utils.timer_utils import Timer


def multiply_matrix_recursive(m1: Matrix, m2: Matrix) -> Matrix:
    """
    Multiply two square matrices recursively by dividing them into submatrices.
    The matrix dimensions must be powers of two.
    """

    (columns, rows) = m1.dimensions()

    if columns == 1:
        return Matrix([[m1.m[0][0] * m2.m[0][0]]])

    sub_matrix_dimension = columns // 2

    m1_11 = m1.sub_matrix(0, 0, sub_matrix_dimension, sub_matrix_dimension)
    m1_12 = m1.sub_matrix(
        sub_matrix_dimension, 0, sub_matrix_dimension, sub_matrix_dimension
    )
    m1_21 = m1.sub_matrix(
        0, sub_matrix_dimension, sub_matrix_dimension, sub_matrix_dimension
    )
    m1_22 = m1.sub_matrix(
        sub_matrix_dimension,
        sub_matrix_dimension,
        sub_matrix_dimension,
        sub_matrix_dimension,
    )

    m2_11 = m2.sub_matrix(0, 0, sub_matrix_dimension, sub_matrix_dimension)
    m2_12 = m2.sub_matrix(
        sub_matrix_dimension, 0, sub_matrix_dimension, sub_matrix_dimension
    )
    m2_21 = m2.sub_matrix(
        0, sub_matrix_dimension, sub_matrix_dimension, sub_matrix_dimension
    )
    m2_22 = m2.sub_matrix(
        sub_matrix_dimension,
        sub_matrix_dimension,
        sub_matrix_dimension,
        sub_matrix_dimension,
    )

    c11 = multiply_matrix_recursive(m1_11, m2_11) + multiply_matrix_recursive(
        m1_12, m2_21
    )
    c12 = multiply_matrix_recursive(m1_11, m2_12) + multiply_matrix_recursive(
        m1_12, m2_22
    )
    c21 = multiply_matrix_recursive(m1_21, m2_11) + multiply_matrix_recursive(
        m1_22, m2_21
    )
    c22 = multiply_matrix_recursive(m1_21, m2_12) + multiply_matrix_recursive(
        m1_22, m2_22
    )

    c = join_4_matrixes(c11, c12, c21, c22)

    return c


def main():
    columns = 8
    rows = 8
    max_num = 50

    print("Random matrixes:")
    m1 = Matrix(gen_rand_matrix(columns, rows, max_num))
    print(m1)
    print()
    m2 = Matrix(gen_rand_matrix(columns, rows, max_num))
    print(m2)
    print()

    print("Basic multiplication result:")
    timer = Timer("execution time")
    multiplied_matrix = Matrix(multiply_matrix_basic(m1.m, m2.m))
    timer.stop()
    print(multiplied_matrix)

    print()
    print("Recursive multiplication result:")
    timer = Timer("execution time")
    multiplied_matrix_rec = multiply_matrix_recursive(m1, m2)
    timer.stop()
    print(multiplied_matrix_rec)


if __name__ == "__main__":
    main()
