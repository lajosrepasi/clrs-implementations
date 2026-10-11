from clrs.chapter04.basic_matrix_multiply import multiply_matrix_basic


def test_multiply_2x2_matrices():
    m1 = [
        [1, 2],
        [3, 4],
    ]

    m2 = [
        [5, 6],
        [7, 8],
    ]

    assert multiply_matrix_basic(m1, m2) == [
        [19, 22],
        [43, 50],
    ]


def test_multiply_by_identity_matrix():
    matrix = [
        [1, 2],
        [3, 4],
    ]

    identity = [
        [1, 0],
        [0, 1],
    ]

    assert multiply_matrix_basic(matrix, identity) == matrix


def test_identity_matrix_multiplication():
    matrix = [
        [1, 2],
        [3, 4],
    ]

    identity = [
        [1, 0],
        [0, 1],
    ]

    assert multiply_matrix_basic(identity, matrix) == matrix


def test_multiply_by_zero_matrix():
    matrix = [
        [1, 2],
        [3, 4],
    ]

    zero = [
        [0, 0],
        [0, 0],
    ]

    assert multiply_matrix_basic(matrix, zero) == zero


def test_multiply_negative_numbers():
    m1 = [
        [1, -2],
        [-3, 4],
    ]

    m2 = [
        [-5, 6],
        [7, -8],
    ]

    assert multiply_matrix_basic(m1, m2) == [
        [-19, 22],
        [43, -50],
    ]


def test_multiply_3x3_matrices():
    m1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]

    m2 = [
        [9, 8, 7],
        [6, 5, 4],
        [3, 2, 1],
    ]

    assert multiply_matrix_basic(m1, m2) == [
        [30, 24, 18],
        [84, 69, 54],
        [138, 114, 90],
    ]


def test_multiply_1x1_matrices():
    assert multiply_matrix_basic([[5]], [[7]]) == [[35]]
