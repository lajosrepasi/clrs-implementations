import sys

from clrs.chapter23.apsp_basic_matrix_mult import (
    apsp_basic_matrix_mult,
    create_graph,
)


def test_clrs_example():
    g = create_graph()

    result = apsp_basic_matrix_mult(g)

    expected = [
        [0, 1, -3, 2, -4],
        [3, 0, -4, 1, -1],
        [7, 4, 0, 5, 3],
        [2, -1, -5, 0, -2],
        [8, 5, 1, 6, 0],
    ]

    assert result == expected


def test_single_vertex():
    g = [[0]]

    assert apsp_basic_matrix_mult(g) == [[0]]


def test_two_vertices():
    inf = sys.maxsize

    g = [
        [0, 5],
        [inf, 0],
    ]

    assert apsp_basic_matrix_mult(g) == g


def test_indirect_path():
    inf = sys.maxsize

    g = [
        [0, 10, 3],
        [inf, 0, inf],
        [inf, 2, 0],
    ]

    result = apsp_basic_matrix_mult(g)

    assert result[0][1] == 5


def test_unreachable_vertex():
    inf = sys.maxsize

    g = [
        [0, 5, inf],
        [inf, 0, inf],
        [inf, inf, 0],
    ]

    result = apsp_basic_matrix_mult(g)

    assert result[0][2] == inf
    assert result[1][2] == inf


def test_diagonal_is_zero():
    result = apsp_basic_matrix_mult(create_graph())

    for i in range(len(result)):
        assert result[i][i] == 0
