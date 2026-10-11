"""
All-pairs shortest paths using repeated min-plus matrix multiplication.

This is the O(V^4) dynamic-programming algorithm that computes
shortest-path distances between every pair of vertices.
"""

import sys

from clrs.utils.matrix_utils import print_matrix
from clrs.utils.timer_utils import Timer

max_int = sys.maxsize

INF = sys.maxsize


def create_L0(n: int) -> list[list[int]]:
    """
    Create L^(0), where each vertex has distance 0 to itself
    and infinity to all other vertices.
    """
    return [[0 if r == c else INF for c in range(n)] for r in range(n)]


def create_initial_L(n: int) -> list[list[int]]:
    """
    Create a matrix initialized to infinity.
    """
    return [[INF] * n for _ in range(n)]


def create_graph() -> list[list[int]]:
    """
    Return an example graph as an adjacency matrix.
    """
    g = [
        [0, 3, 8, INF, -4],
        [INF, 0, INF, 1, 7],
        [INF, 4, 0, INF, INF],
        [2, INF, -5, 0, INF],
        [INF, INF, INF, 6, 0],
    ]

    return g


def extends_shortest_path(
    g: list[list[int]], Lr_1: list[list[int]], Lr: list[list[int]]
) -> None:
    """
    Compute L^(r) from L^(r-1).

    For each vertex pair (i, j), compute the shortest path
    using at most r edges.
    """
    n = len(g)

    for i in range(n):
        for j in range(n):
            for k in range(n):
                if Lr[i][j] > Lr_1[i][k] + g[k][j]:
                    Lr[i][j] = Lr_1[i][k] + g[k][j]


def apsp_basic_matrix_mult(g: list[list[int]]) -> list[list[int]]:
    """
    Compute all-pairs shortest paths using repeated
    min-plus matrix multiplication.

    Runs in O(V^4) time.
    """
    n = len(g)
    Lr_1 = create_L0(n)

    for _ in range(n):
        L = create_initial_L(n)

        extends_shortest_path(g, Lr_1, L)

        Lr_1 = L

    return Lr_1


def main():
    g = create_graph()

    t = Timer()
    M = apsp_basic_matrix_mult(g)
    t.stop()

    print_matrix(M)


if __name__ == "__main__":
    main()
