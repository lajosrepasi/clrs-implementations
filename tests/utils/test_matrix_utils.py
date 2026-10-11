from clrs.utils.matrix_utils import (
    Matrix,
    add_matrixes,
    gen_empty_matrix,
    gen_rand_matrix,
    get_matrix_dimensions,
    get_sub_matrix,
    join_4_matrixes,
    sub_matrixes,
)


def test_gen_empty_matrix():
    assert gen_empty_matrix(3, 2) == [
        [0, 0, 0],
        [0, 0, 0],
    ]


def test_gen_rand_matrix():
    matrix = gen_rand_matrix(3, 2, 10)

    assert len(matrix) == 2
    assert all(len(row) == 3 for row in matrix)
    assert all(0 <= value <= 10 for row in matrix for value in row)


def test_get_matrix_dimensions():
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
    ]

    assert get_matrix_dimensions(matrix) == (3, 2)


def test_get_sub_matrix():
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16],
    ]

    assert get_sub_matrix(1, 1, 2, 2, matrix) == [
        [6, 7],
        [10, 11],
    ]


def test_add_matrixes():
    m1 = [
        [1, 2],
        [3, 4],
    ]

    m2 = [
        [5, 6],
        [7, 8],
    ]

    assert add_matrixes(m1, m2) == [
        [6, 8],
        [10, 12],
    ]


def test_sub_matrixes():
    m1 = [
        [5, 6],
        [7, 8],
    ]

    m2 = [
        [1, 2],
        [3, 4],
    ]

    assert sub_matrixes(m1, m2) == [
        [4, 4],
        [4, 4],
    ]


def test_matrix_addition():
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

    result = m1 + m2

    assert result.m == [
        [6, 8],
        [10, 12],
    ]


def test_matrix_subtraction():
    m1 = Matrix(
        [
            [5, 6],
            [7, 8],
        ]
    )

    m2 = Matrix(
        [
            [1, 2],
            [3, 4],
        ]
    )

    result = m1 - m2

    assert result.m == [
        [4, 4],
        [4, 4],
    ]


def test_matrix_dimensions():
    matrix = Matrix(
        [
            [1, 2, 3],
            [4, 5, 6],
        ]
    )

    assert matrix.dimensions() == (3, 2)


def test_matrix_sub_matrix():
    matrix = Matrix(
        [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ]
    )

    result = matrix.sub_matrix(1, 1, 2, 2)

    assert result.m == [
        [5, 6],
        [8, 9],
    ]


def test_matrix_str():
    matrix = Matrix(
        [
            [1, 2],
            [3, 4],
        ]
    )

    assert str(matrix) == "[1, 2]\n[3, 4]\n"


def test_join_4_matrixes():
    m1 = Matrix([[1, 2], [3, 4]])
    m2 = Matrix([[5, 6], [7, 8]])
    m3 = Matrix([[9, 10], [11, 12]])
    m4 = Matrix([[13, 14], [15, 16]])

    result = join_4_matrixes(m1, m2, m3, m4)

    assert result.m == [
        [1, 2, 5, 6],
        [3, 4, 7, 8],
        [9, 10, 13, 14],
        [11, 12, 15, 16],
    ]
