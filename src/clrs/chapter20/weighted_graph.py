"""
Weighted graph implementation using adjacency lists.

Vertices store outgoing edges, and each edge
contains a destination vertex and a weight.
"""

from __future__ import annotations

from clrs.chapter20.graph import Graph
from clrs.chapter20.graph import Vertex as GraphVertex


class Vertex(GraphVertex):
    """
    Vertex in a weighted graph.
    """

    def __init__(self, label: int, graph: WeightedGraph) -> None:
        super().__init__(label, graph)

    def add_neighbour_undirected(
        self, vertex: GraphVertex, weight: float = 1.0
    ) -> None:
        """
        Add an undirected weighted edge.
        """
        assert isinstance(vertex, Vertex)
        self.neighbours.append(Edge(self, vertex, weight))
        vertex.neighbours.append(Edge(vertex, self, weight))

    def add_neighbour(self, vertex: GraphVertex, weight: float = 1.0) -> None:
        assert isinstance(vertex, Vertex)
        self.neighbours.append(Edge(self, vertex, weight))

    def __str__(self) -> str:
        return "({0})".format(self.label)


class Edge:
    """
    Weighted edge between two vertices.
    """

    def __init__(self, u: Vertex, v: Vertex, weight: float):
        self.u: Vertex = u
        self.v: Vertex = v
        self.w: float = weight

    def __str__(self) -> str:
        return "({0}--{1}--{2})".format(self.u, self.w, self.v)

    def __repr__(self) -> str:
        return str(self)

    def __lt__(self, other: Edge) -> bool:
        return self.w < other.w

    def __le__(self, other: Edge) -> bool:
        return self.w <= other.w

    def __ge__(self, other: Edge) -> bool:
        return self.w >= other.w

    def __gt__(self, other: Edge) -> bool:
        return self.w > other.w


class WeightedGraph(Graph):
    """
    Graph whose edges carry weights.
    """

    def __init__(self) -> None:
        super().__init__()

    def add_vertex(self, label: int) -> Vertex:
        """
        Add and return a new vertex.
        """
        v = Vertex(label, self)
        self.vertices[label] = v

        return v

    def add_directed_edge(
        self, v1: GraphVertex, v2: GraphVertex, w: float = 1.0
    ) -> None:
        """
        Add a directed weighted edge.
        """
        assert isinstance(v1, Vertex)
        assert isinstance(v2, Vertex)
        self.check_contains(v1, v2)

        v1.add_neighbour(v2, w)

    def add_undirected_edge(self, v1: GraphVertex, v2: GraphVertex, w: float = 1.0):
        """
        Add an undirected weighted edge.
        """
        assert isinstance(v1, Vertex)
        assert isinstance(v2, Vertex)
        self.check_contains(v1, v2)

        v1.add_neighbour_undirected(v2, w)

    def __getitem__(self, label: int) -> Vertex:
        v = self.get_vertex(label)
        assert isinstance(v, Vertex)
        return v


def main():
    g = WeightedGraph()

    v1 = g.add_vertex(1)
    v2 = g.add_vertex(2)

    v1.add_neighbour(v2, 5)

    print(g[1])
    print(g[1].neighbours)


if __name__ == "__main__":
    main()
