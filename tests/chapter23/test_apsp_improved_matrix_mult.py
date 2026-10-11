from clrs.chapter23.apsp_improved_matrix_mult import (
    INF,
    apsp_basic_matrix_mult,
    create_graph,
    create_parent_matrix,
)


def test_clrs_example_distances():
    g = create_graph()
    parent = create_parent_matrix(g)

    result = apsp_basic_matrix_mult(g, parent)

    expected = [
        [0, 1, -3, 2, -4],
        [3, 0, -4, 1, -1],
        [7, 4, 0, 5, 3],
        [2, -1, -5, 0, -2],
        [8, 5, 1, 6, 0],
    ]

    assert result == expected


def test_parent_matrix_created():
    g = create_graph()

    parent = create_parent_matrix(g)

    assert parent[0][1] == 0
    assert parent[0][4] == 0
    assert parent[0][3] == -1


def test_single_vertex():
    g = [[0]]

    parent = create_parent_matrix(g)

    result = apsp_basic_matrix_mult(g, parent)

    assert result == [[0]]


def test_two_vertices():
    g = [
        [0, 5],
        [INF, 0],
    ]

    parent = create_parent_matrix(g)

    result = apsp_basic_matrix_mult(g, parent)

    assert result == g


def test_indirect_shortest_path():
    g = [
        [0, 10, 3],
        [INF, 0, INF],
        [INF, 2, 0],
    ]

    parent = create_parent_matrix(g)

    result = apsp_basic_matrix_mult(g, parent)

    assert result[0][1] == 5


def test_unreachable_vertex():
    g = [
        [0, 5, INF],
        [INF, 0, INF],
        [INF, INF, 0],
    ]

    parent = create_parent_matrix(g)

    result = apsp_basic_matrix_mult(g, parent)

    assert result[0][2] == INF
    assert result[1][2] == INF


def test_diagonal_remains_zero():
    g = create_graph()

    parent = create_parent_matrix(g)

    result = apsp_basic_matrix_mult(g, parent)

    for i in range(len(result)):
        assert result[i][i] == 0


def test_negative_edges():
    g = [
        [0, 4, INF],
        [INF, 0, -2],
        [INF, INF, 0],
    ]

    parent = create_parent_matrix(g)

    result = apsp_basic_matrix_mult(g, parent)

    assert result[0][2] == 2
