from clrs.chapter23.floyd_warshall import (
    INF,
    create_graph,
    create_parent_matrix,
    floyd_warshall,
)


def test_create_parent_matrix():
    graph = create_graph()

    parent_matrix = create_parent_matrix(graph)

    assert parent_matrix == [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1],
        [0, 2, 0, 0, 0],
        [3, 0, 3, 0, 0],
        [0, 0, 0, 4, 0],
    ]


def test_floyd_warshall_clrs_example():
    graph = create_graph()
    parent_matrix = create_parent_matrix(graph)

    distances, parents = floyd_warshall(graph, parent_matrix)

    assert distances == [
        [0, 1, -3, 2, -4],
        [3, 0, -4, 1, -1],
        [7, 4, 0, 5, 3],
        [2, -1, -5, 0, -2],
        [8, 5, 1, 6, 0],
    ]

    # Verify some predecessor relationships.
    assert parents is not None
    assert parents[0][1] == 2
    assert parents[0][2] == 3
    assert parents[0][3] == 4
    assert parents[0][4] == 0


def test_floyd_warshall_preserves_unreachable_vertices():
    graph = [
        [0, 2, INF, INF],
        [INF, 0, 3, INF],
        [INF, INF, 0, INF],
        [INF, INF, INF, 0],
    ]

    parent_matrix = create_parent_matrix(graph)

    distances, parents = floyd_warshall(graph, parent_matrix)

    assert distances == [
        [0, 2, 5, INF],
        [INF, 0, 3, INF],
        [INF, INF, 0, INF],
        [INF, INF, INF, 0],
    ]

    assert parents == [
        [0, 0, 1, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ]


def test_floyd_warshall_handles_negative_edges():
    graph = [
        [0, 4, 5, INF],
        [INF, 0, -2, 6],
        [INF, INF, 0, 3],
        [INF, INF, INF, 0],
    ]

    parent_matrix = create_parent_matrix(graph)

    distances, _ = floyd_warshall(graph, parent_matrix)

    assert distances == [
        [0, 4, 2, 5],
        [INF, 0, -2, 1],
        [INF, INF, 0, 3],
        [INF, INF, INF, 0],
    ]


def test_floyd_warshall_does_not_treat_inf_plus_negative_as_a_path():
    """An unreachable path must remain INF even when negative edges exist."""
    graph = [
        [0, INF, INF],
        [INF, 0, -10],
        [INF, INF, 0],
    ]

    parent_matrix = create_parent_matrix(graph)

    distances, _ = floyd_warshall(graph, parent_matrix)
    assert distances is not None

    assert distances[0][2] == INF
    assert distances[2][0] == INF
    assert distances[0][1] == INF


def test_floyd_warshall_finds_shortest_directed_path():
    graph = [
        [0, 10, 3, INF],
        [INF, 0, INF, 7],
        [INF, 2, 0, 5],
        [INF, INF, INF, 0],
    ]

    parent_matrix = create_parent_matrix(graph)

    distances, _ = floyd_warshall(graph, parent_matrix)
    assert distances is not None

    # 0 -> 2 -> 1: 3 + 2 = 5
    assert distances[0][1] == 5

    # 0 -> 2 -> 1 -> 3: 3 + 2 + 7 = 12
    # versus 0 -> 2 -> 3 = 3 + 5 = 8
    assert distances[0][3] == 8


def test_floyd_warshall_handles_single_vertex_graph():
    graph: list[list[int | float]] = [[0]]

    parent_matrix = create_parent_matrix(graph)

    distances, parents = floyd_warshall(graph, parent_matrix)

    assert distances == [[0]]
    assert parents == [[0]]


def test_floyd_warshall_handles_empty_graph():
    graph: list[list[int | float]] = []
    parent_matrix: list[list[int | float]] = []

    distances, parents = floyd_warshall(graph, parent_matrix)

    assert distances == None
    assert parents == None
