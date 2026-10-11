"""
Bellman-Ford single-source shortest-path algorithm.
"""

from clrs.chapter20.graph import EdgeIterator
from clrs.chapter20.weighted_graph import Edge, Vertex, WeightedGraph


class BellmanFord:
    """
    Compute shortest paths from a source using Bellman-Ford.
    """

    def __init__(self, g: WeightedGraph, s: Vertex) -> None:
        self.distances: dict[Vertex, float] = {}
        self.parents: dict[Vertex, Vertex | None] = {}
        self.g: WeightedGraph = g
        self.s: Vertex = s

        self.initialise_single_source(g, s)

    def initialise_single_source(self, g: WeightedGraph, s: Vertex):
        """
        Initialize distances and parents for single-source shortest paths.
        """
        for v in g:
            assert isinstance(v, Vertex)
            self.distances[v] = float("inf")
            self.parents[v] = None

        self.distances[s] = 0

    def relax(self, u: Vertex, v: Vertex, w: float) -> None:
        """
        Relax the weighted edge from u to v.
        """
        if self.distances[v] > self.distances[u] + w:
            self.distances[v] = self.distances[u] + w
            self.parents[v] = u

    def do(self) -> bool:
        """
        Compute shortest paths and detect reachable negative-weight cycles.
        """
        max_edges_in_sp = len(self.g)

        for _ in range(max_edges_in_sp):
            for _, e in EdgeIterator(self.g):

                if e is None:
                    continue

                assert isinstance(e, Edge)

                self.relax(e.u, e.v, e.w)

        for _, e in EdgeIterator(self.g):
            if e is None:
                continue

            assert isinstance(e, Edge)

            if self.distances[e.v] > self.distances[e.u] + e.w:
                return False

        return True


def create_graph() -> tuple[Vertex, WeightedGraph]:
    """
    Create an example directed weighted graph.
    """
    g = WeightedGraph()

    v1 = g.add_vertex(1)
    v2 = g.add_vertex(2)
    v3 = g.add_vertex(3)
    v4 = g.add_vertex(4)
    v5 = g.add_vertex(5)

    g.add_directed_edge(v1, v2, 3)
    g.add_directed_edge(v1, v4, 5)
    g.add_directed_edge(v2, v4, 2)
    g.add_directed_edge(v2, v3, 6)
    g.add_directed_edge(v3, v5, 2)
    g.add_directed_edge(v4, v2, 1)
    g.add_directed_edge(v4, v3, 4)
    g.add_directed_edge(v4, v5, 1)
    g.add_directed_edge(v5, v3, 7)
    g.add_directed_edge(v5, v1, 3)

    return v1, g


def print_path(v: Vertex, bf: BellmanFord):
    """
    Print the shortest-path length and parent chain to a vertex.
    """
    assert isinstance(v, Vertex)
    print("length: ", bf.distances[v])
    vv: Vertex | None = v

    while vv is not None:
        print(vv)
        assert isinstance(vv, Vertex)
        vv = bf.parents[vv]


def main():
    v1, g = create_graph()
    bf = BellmanFord(g, v1)
    _ = bf.do()

    print_path(g[5], bf)


if __name__ == "__main__":
    main()
