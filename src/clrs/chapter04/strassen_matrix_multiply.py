"""
Strassen's matrix multiplication implementation.
"""

from clrs.chapter04.basic_matrix_multiply import multiply_matrix_basic
from clrs.chapter04.recursive_matrix_multiply import multiply_matrix_recursive
from clrs.utils.matrix_utils import (
    Matrix,
    gen_rand_matrix,
    join_4_matrixes,
    print_matrix,
)
from clrs.utils.timer_utils import Timer


def multiply_matrix_strassen(m1: Matrix, m2: Matrix) -> Matrix:
    """
    Multiply two square matrices using Strassen's algorithm.
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

    s1 = m2_12 - m2_22
    s2 = m1_11 + m1_12
    s3 = m1_21 + m1_22
    s4 = m2_21 - m2_11
    s5 = m1_11 + m1_22
    s6 = m2_11 + m2_22
    s7 = m1_12 - m1_22
    s8 = m2_21 + m2_22
    s9 = m1_11 - m1_21
    s10 = m2_11 + m2_12

    p1 = multiply_matrix_strassen(m1_11, s1)
    p2 = multiply_matrix_strassen(s2, m2_22)
    p3 = multiply_matrix_strassen(s3, m2_11)
    p4 = multiply_matrix_strassen(m1_22, s4)
    p5 = multiply_matrix_strassen(s5, s6)
    p6 = multiply_matrix_strassen(s7, s8)
    p7 = multiply_matrix_strassen(s9, s10)

    c11 = p5 + p4 - p2 + p6
    c12 = p1 + p2
    c21 = p3 + p4
    c22 = p5 + p1 - p3 - p7

    c = join_4_matrixes(c11, c12, c21, c22)

    return c


def main():
    columns = 8
    rows = 8
    max_num = 50

    print("Random matrixes:")
    m1 = gen_rand_matrix(columns, rows, max_num)
    print_matrix(m1)
    print()
    m2 = gen_rand_matrix(columns, rows, max_num)
    print_matrix(m2)
    print()

    print("Basic multiplication result:")
    timer = Timer("execution time")
    multiplied_matrix = multiply_matrix_basic(m1, m2)
    print_matrix(multiplied_matrix)
    timer.stop()

    print()
    print("Recursive multiplication result:")
    timer = Timer("execution time")
    multiplied_matrix_dq = multiply_matrix_recursive(Matrix(m1), Matrix(m2))
    print(multiplied_matrix_dq)
    timer.stop()

    print()
    print("Strassen multiplication result:")
    timer = Timer("execution time")
    multiplied_matrix_strassen = multiply_matrix_strassen(Matrix(m1), Matrix(m2))
    print(multiplied_matrix_strassen)
    timer.stop()


if __name__ == "__main__":
    main()
