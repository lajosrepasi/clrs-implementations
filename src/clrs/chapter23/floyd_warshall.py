"""
Floyd-Warshall all-pairs shortest-path algorithm.
"""

from copy import deepcopy
from typing import cast

from clrs.chapter23.apsp_improved_matrix_mult import print_path
from clrs.utils.matrix_utils import print_matrix

INF = float("inf")


def create_parent_matrix(g: list[list[int | float]]) -> list[list[int | float]]:
    """
    Create the initial predecessor matrix from a graph.
    """
    n = len(g)

    M: list[list[int | float]] = []

    for i in range(n):
        M.append([0] * n)

    for i in range(n):
        for j in range(n):
            if g[i][j] != INF and i != j:
                M[i][j] = i

    return M


def create_graph() -> list[list[float]]:
    """
    Create the graph from the CLRS example.
    """
    g = [
        [0, 3, 8, INF, -4],
        [INF, 0, INF, 1, 7],
        [INF, 4, 0, INF, INF],
        [2, INF, -5, 0, INF],
        [INF, INF, INF, 6, 0],
    ]

    return g


def create_empty_matrix(g: list[list[int | float]]) -> list[list[int | float]]:
    """
    Create an empty matrix with the same dimensions as the graph.
    """
    n = len(g)
    m = []

    for _ in range(n):
        m.append([0] * n)

    return m


def set_parents(
    i: int,
    j: int,
    k: int | None,
    parent_matrix: list[list[int | None]],
    prev_parent_matrix: list[list[int | None]],
):
    l = i
    m = j
    n = k

    while n != m:
        assert n is not None
        parent_matrix[l][m] = prev_parent_matrix[n][m]
        m = prev_parent_matrix[n][m]

        if m == None:
            break

    while i != k:
        assert k is not None
        parent_matrix[i][k] = prev_parent_matrix[i][k]
        k = prev_parent_matrix[i][k]

        if k == None:
            break


def floyd_warshall(
    g: list[list[int | float]], p_m: list[list[int | float]]
) -> tuple[list[list[int | float]] | None, list[list[int | float]] | None]:
    """
    Compute all-pairs shortest paths using Floyd-Warshall.
    """

    m_prev = deepcopy(g)
    m_nxt = None

    pm_prev = deepcopy(p_m)
    pm_nxt = None

    n = len(g)
    for k in range(n):
        m_nxt = create_empty_matrix(g)
        pm_nxt = create_empty_matrix(g)
        for i in range(n):
            for j in range(n):
                if m_prev[i][j] > m_prev[i][k] + m_prev[k][j]:
                    m_nxt[i][j] = m_prev[i][k] + m_prev[k][j]
                    pm_nxt[i][j] = pm_prev[k][j]
                else:
                    m_nxt[i][j] = m_prev[i][j]
                    pm_nxt[i][j] = pm_prev[i][j]

        m_prev = m_nxt
        pm_prev = pm_nxt

    return (m_nxt, pm_nxt)


def main():
    g = create_graph()
    pm = create_parent_matrix(g)

    M, parent_matrix = floyd_warshall(g, pm)

    assert M is not None
    assert parent_matrix is not None
    print_matrix(M)

    print("\nparent matrix:")
    print_matrix(parent_matrix)
    print("\nprint path:")
    print("length:", M[4][1])
    print_path(4, 1, cast(list[list[int]], parent_matrix))


if __name__ == "__main__":
    main()
