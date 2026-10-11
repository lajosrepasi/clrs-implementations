"""
Dijkstra's single-source shortest-path algorithm.
"""

from clrs.chapter06.priority_queue import MinPriorityQueue
from clrs.chapter20.weighted_graph import Vertex, WeightedGraph
from clrs.chapter22.bellman_ford import create_graph


class Dijkstra:
    """
    Compute shortest paths from a source using Dijkstra's algorithm.
    """

    def __init__(self, g: WeightedGraph, s: Vertex) -> None:
        self.distances: dict[Vertex, float] = {}
        self.parents: dict[Vertex, Vertex | None] = {}
        self.g: WeightedGraph = g
        self.s: Vertex = s

        self.initialise_single_source(g, s)

    def relax(self, u: Vertex, v: Vertex, w: float) -> bool:
        """
        Relax the edge from u to v and return whether its distance changed.
        """
        if self.distances[v] > self.distances[u] + w:
            self.distances[v] = self.distances[u] + w
            self.parents[v] = u
            return True

        return False

    def initialise_single_source(self, g: WeightedGraph, s: Vertex):
        """
        Initialize distances and parents for single-source shortest paths.
        """
        for v in g:
            assert isinstance(v, Vertex)
            self.distances[v] = float("inf")
            self.parents[v] = None

        self.distances[s] = 0

    def do(self) -> None:
        """
        Compute shortest paths from the source vertex.
        """
        min_prio_q = MinPriorityQueue()

        for v in self.g:
            assert isinstance(v, Vertex)
            min_prio_q.insert(self.distances[v], v)

        while not min_prio_q.empty():
            k_next_v = min_prio_q.extract_minimum()
            assert k_next_v is not None

            (_, next_v) = k_next_v

            for edge in next_v.neighbours:
                if edge.v in min_prio_q:
                    prev_distance = self.distances[edge.v]
                    if self.relax(edge.u, edge.v, edge.w):
                        min_prio_q.decrease_key(
                            self.distances[edge.v], prev_distance, edge.v
                        )


def print_path(v: Vertex, dijkstra: Dijkstra) -> None:
    """
    Print the shortest-path length and parent chain to a vertex.
    """
    assert isinstance(v, Vertex)
    print("length: ", dijkstra.distances[v])
    vv: Vertex | None = v

    while vv is not None:
        print(vv)
        assert isinstance(vv, Vertex)
        vv = dijkstra.parents[vv]


def main():
    v1, g = create_graph()

    dijkstra = Dijkstra(g, v1)

    dijkstra.do()

    print_path(g[5], dijkstra)


if __name__ == "__main__":
    main()
