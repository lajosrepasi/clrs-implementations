from clrs.chapter20.graph import EdgeIterator
from clrs.chapter20.weighted_graph import Edge, Vertex, WeightedGraph
from clrs.chapter22.bellman_ford import BellmanFord as BF
from clrs.chapter22.bellman_ford import print_path


class BellmanFord(BF):
    def __init__(self, g: WeightedGraph, s: Vertex) -> None:
        self.path_lengths: dict[Vertex, float] = {}
        super().__init__(g, s)

    def initialise_single_source(self, g: WeightedGraph, s: Vertex):
        super().initialise_single_source(g, s)

        for v in g:
            assert isinstance(v, Vertex)
            self.path_lengths[v] = float("inf")

        self.path_lengths[s] = 0

    def do(self) -> bool:
        max_path_length = 0
        i = 0

        while i <= max_path_length and i < len(self.g) - 1:
            prev_path_lengths = self.path_lengths.copy()

            for _, e in EdgeIterator(self.g):
                assert isinstance(e, Edge)

                if self.distances[e.v] > self.distances[e.u] + e.w:
                    self.distances[e.v] = self.distances[e.u] + e.w
                    self.parents[e.v] = e.u

                    self.path_lengths[e.v] = prev_path_lengths[e.u] + 1

                    if self.path_lengths[e.v] > max_path_length:
                        max_path_length = self.path_lengths[e.v]

            i += 1

        for _, e in EdgeIterator(self.g):
            assert isinstance(e, Edge)
            if self.distances[e.v] > self.distances[e.u] + e.w:
                return False

        return True


def create_graph():
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


def main():
    v1, g = create_graph()

    bf = BellmanFord(g, v1)
    bf.do()

    print_path(g[5], bf)


if __name__ == "__main__":
    main()
