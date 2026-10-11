from clrs.chapter04.basic_matrix_multiply import multiply_matrix_basic
from clrs.chapter04.recursive_matrix_multiply import multiply_matrix_recursive
from clrs.utils.matrix_utils import Matrix


def test_multiply_1x1_matrices():
    m1 = Matrix([[5]])
    m2 = Matrix([[7]])

    result = multiply_matrix_recursive(m1, m2)

    assert result.m == [[35]]


def test_multiply_2x2_matrices():
    m1 = Matrix(
        [
            [1, 2],
            [3, 4],
        ]
    )

    m2 = Matrix(
        [
            [5, 6],
            [7, 8],
        ]
    )

    result = multiply_matrix_recursive(m1, m2)

    assert result.m == [
        [19, 22],
        [43, 50],
    ]


def test_multiply_by_identity_matrix():
    matrix = Matrix(
        [
            [1, 2],
            [3, 4],
        ]
    )

    identity = Matrix(
        [
            [1, 0],
            [0, 1],
        ]
    )

    result = multiply_matrix_recursive(matrix, identity)

    assert result.m == matrix.m


def test_multiply_by_zero_matrix():
    matrix = Matrix(
        [
            [1, 2],
            [3, 4],
        ]
    )

    zero = Matrix(
        [
            [0, 0],
            [0, 0],
        ]
    )

    result = multiply_matrix_recursive(matrix, zero)

    assert result.m == zero.m


def test_multiply_4x4_matrices():
    m1 = Matrix(
        [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16],
        ]
    )

    m2 = Matrix(
        [
            [16, 15, 14, 13],
            [12, 11, 10, 9],
            [8, 7, 6, 5],
            [4, 3, 2, 1],
        ]
    )

    recursive_result = multiply_matrix_recursive(m1, m2)
    basic_result = multiply_matrix_basic(m1.m, m2.m)

    assert recursive_result.m == basic_result


def test_recursive_matches_basic_multiplication():
    m1 = Matrix(
        [
            [2, 4, 1, 3],
            [5, 2, 6, 1],
            [7, 3, 4, 2],
            [1, 6, 2, 5],
        ]
    )

    m2 = Matrix(
        [
            [3, 1, 4, 2],
            [2, 5, 1, 3],
            [6, 2, 3, 1],
            [4, 3, 2, 5],
        ]
    )

    recursive_result = multiply_matrix_recursive(m1, m2)
    basic_result = multiply_matrix_basic(m1.m, m2.m)

    assert recursive_result.m == basic_result
