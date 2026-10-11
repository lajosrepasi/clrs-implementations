"""
Adjacency-list graph implementation.

Supports directed and undirected edges, vertex lookup, and graph traversal.
"""

from __future__ import annotations

from collections.abc import Iterator
from typing import Any

from clrs.chapter11.hash_table_chaining import HashTableChaining as HashTable


class EdgeIterator:
    """
    Iterate over all edges in a graph.
    """

    def __init__(self, g: Graph) -> None:
        self.vertices_it = iter(g)
        self.current_vertex = None
        self.current_edge = -1

        try:
            self.current_vertex = next(self.vertices_it)
        except StopIteration:
            self.current_vertex = None

    def __iter__(self) -> EdgeIterator:
        return self

    def __next__(self) -> tuple[Vertex, Vertex | None]:
        while self.current_vertex is not None:
            # Advance to next neighbor of current vertex if available
            if self.current_edge + 1 < len(self.current_vertex.neighbours):
                self.current_edge += 1
                return (
                    self.current_vertex,
                    self.current_vertex.neighbours[self.current_edge],
                )

            # Move to next vertex when current vertex's neighbors are exhausted
            try:
                self.current_vertex = next(self.vertices_it)
                self.current_edge = -1
            except StopIteration:
                self.current_vertex = None

        raise StopIteration


class Vertex:
    """
    A graph vertex with an adjacency list.
    """

    def __init__(self, label: int, graph: Graph) -> None:
        self.label: int = label
        self.graph: Graph = graph
        self.neighbours: list[Any] = []

    def add_neighbour(self, vertex: Vertex) -> None:
        """
        Add an outgoing edge to another vertex.
        """
        if vertex not in self.neighbours:
            self.neighbours.append(vertex)

    def add_neighbour_undirected(self, vertex: Vertex) -> None:
        """
        Add an undirected edge between two vertices.
        """
        self.add_neighbour(vertex)
        vertex.add_neighbour(self)

    def __str__(self) -> str:
        return "({0})".format(self.label)

    def __repr__(self) -> str:
        return str(self)


class Graph:
    """
    Graph represented using adjacency lists.
    """

    def __init__(self) -> None:
        self.vertices = HashTable()

    def add_vertex(self, label: int) -> Vertex:
        """
        Add and return a new vertex.
        """
        v = Vertex(label, self)
        self.vertices[label] = v

        return v

    def add_directed_edge(self, v1: Vertex, v2: Vertex) -> None:
        """
        Add a directed edge from v1 to v2.
        """
        self.check_contains(v1, v2)

        v1.add_neighbour(v2)

    def add_undirected_edge(self, v1: Vertex, v2: Vertex) -> None:
        """
        Add an undirected edge between two vertices.
        """
        self.check_contains(v1, v2)

        v1.add_neighbour_undirected(v2)

    def check_contains(self, *vertices_to_check: Vertex) -> None:
        """
        Verify that all vertices belong to this graph.
        """
        for v in vertices_to_check:
            if v not in self:
                raise Exception("{0} not in the graph.".format(v))

    def get_vertex(self, label: int) -> Vertex:
        """
        Return the vertex with the given label.
        """
        return self.vertices[label]

    def __len__(self) -> int:
        return len(self.vertices)

    def __getitem__(self, label: int) -> Vertex:
        return self.get_vertex(label)

    def __contains__(self, item: Vertex | int) -> bool:
        if type(item) == int:
            label = item
            return label in self.vertices
        elif isinstance(item, Vertex):
            vertex = item
            return vertex.label in self.vertices and self.vertices[vertex.label] is item
        else:
            raise Exception("Not right type: use vertex or vertex label")

    def __init__(self) -> None:
        self.vertices = HashTable()

    def __iter__(self) -> Iterator[Vertex]:
        """
        Return a fresh generator iterator over Vertex objects.
        """
        for label in self.vertices:
            yield self.vertices[label]


def main():
    g = Graph()

    v1 = g.add_vertex(1)
    v2 = g.add_vertex(2)

    g.add_undirected_edge(v1, v2)

    print("v1:", g[1])
    print("v1 neighbours:", g[1].neighbours)
    print("v2 neighbours:", g[2].neighbours)

    print("\nIterate over vertices:")
    for v in g:
        print(v)

    print("\ncontains check")
    print("Is 1 in the graph?", 1 in g)
    print("Is v1 in the graph?", v1 in g)
    print("Is 34 in the graph?", 34 in g)

    g = Graph()

    v1 = g.add_vertex(1)
    v2 = g.add_vertex(2)

    it = EdgeIterator(g)
    next(it)


if __name__ == "__main__":
    main()
