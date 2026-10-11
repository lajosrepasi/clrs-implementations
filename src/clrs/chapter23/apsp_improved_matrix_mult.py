import sys
from copy import deepcopy

from clrs.utils.matrix_utils import print_matrix
from clrs.utils.timer_utils import Timer

INF = sys.maxsize


def create_initial_matrix(n: int) -> list[list[int]]:
    return [[INF] * n for _ in range(n)]


def create_parent_matrix(g: list[list[int]]) -> list[list[int]]:
    """
    Create the predecessor matrix used for path reconstruction.
    """
    n = len(g)

    M: list[list[int]] = []

    for i in range(n):
        M.append([-1] * n)

    for i in range(n):
        for j in range(n):
            if g[i][j] != INF and i != j:
                M[i][j] = i

    return M


def create_graph() -> list[list[int]]:
    """
    Return the example graph as an adjacency matrix.
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
    g: list[list[int]],
    Lr_1: list[list[int]],
    Lr: list[list[int]],
    parent_matrix: list[list[int]],
):
    """
    Extend shortest paths by one matrix multiplication step.

    Updates both the distance matrix and predecessor matrix.
    """
    n = len(g)

    for i in range(n):
        for j in range(n):
            for k in range(n):
                if Lr[i][j] > Lr_1[i][k] + g[k][j]:
                    Lr[i][j] = Lr_1[i][k] + g[k][j]
                    parent_matrix[i][j] = k


def apsp_basic_matrix_mult(g: list[list[int]], parent_matrix: list[list[int]]):
    """
    Compute all-pairs shortest-path distances.

    Uses repeated min-plus matrix multiplication.
    """
    l = deepcopy(g)

    n = len(g)
    r = 1

    while r < n:
        next_L = create_initial_matrix(len(g))

        extends_shortest_path(g, l, next_L, parent_matrix)
        l = next_L
        r = r * 2

    return l


def print_path(
    i: int,
    j: int | None,
    parent_matrix: list[list[int]],
):
    """
    Print the path from vertex i to vertex j using the
    predecessor matrix.
    """
    path = []

    while j != i:
        if j == -1:
            print("no path")
            return

        assert j is not None
        j = parent_matrix[i][j]

        path.append(j)

    path.append(j)

    print(list(reversed(path)))


def main():
    g = create_graph()
    parent_matrix = create_parent_matrix(g)

    t = Timer()
    M = apsp_basic_matrix_mult(g, parent_matrix)
    t.stop()

    print_matrix(M)
    print("\nparent matrix:")
    print_matrix(parent_matrix)

    print("\nprint path:")
    print("length:", M[4][1])
    print_path(4, 1, parent_matrix)


if __name__ == "__main__":
    main()
