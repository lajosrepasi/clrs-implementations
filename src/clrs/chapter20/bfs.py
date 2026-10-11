"""
Breadth-first search (BFS) implementation.

Computes shortest-path distances in an unweighted graph
and records parent relationships for path reconstruction.
"""

from __future__ import annotations

from collections.abc import Callable
from sys import maxsize as Infinity

from clrs.chapter10.my_queue import Queue
from clrs.chapter20.graph import Graph, Vertex


class BFS:
    """
    Breadth-first search traversal.

    Tracks vertex colors, distances from the source,
    and parent relationships.
    """

    WHITE = 1
    GRAY = 2
    BLACK = 3

    def __init__(
        self,
        graph: Graph,
        start_vertex: Vertex,
        vertex_proc_func: Callable[[Vertex, BFS], None],
    ) -> None:
        self.graph: Graph = graph
        self.start_vertex: Vertex = start_vertex
        self.vertex_proc_func: Callable[[Vertex, BFS], None] = vertex_proc_func
        self.queue: Queue = Queue()

        # State stored cleanly mapping Vertex -> state
        self.colors: dict[Vertex, int] = {}
        self.distances: dict[Vertex, int] = {}
        self.parents: dict[Vertex, Vertex | None] = {}

    def do(self) -> None:
        """
        Execute breadth-first search from the start vertex.
        """
        self.init_bfs()

        while not self.queue.empty():
            v: Vertex = self.queue.dequeue()

            self.vertex_proc_func(v, self)

            # can be removed
            self.set_black(v)

            for neighbour in v.neighbours:
                # can be used parent or dist value to check whether it has been visited already.
                if self.is_white(neighbour):
                    self.set_gray(neighbour)
                    self.set_parent(neighbour, v)
                    self.set_dist(neighbour, self.get_dist(v) + 1)
                    self.queue.enqueue(neighbour)

    def init_bfs(self) -> None:
        """
        Initialize BFS state and enqueue the start vertex.
        """
        self.queue.reset()

        for v in self.graph:
            self.set_white(v)
            self.set_dist(v, Infinity)
            self.set_parent(v, None)

        self.set_gray(self.start_vertex)
        self.set_dist(self.start_vertex, 0)

        self.queue.enqueue(self.start_vertex)

    def set_white(self, v: Vertex) -> None:
        """
        Mark a vertex as undiscovered.
        """
        self.colors[v] = BFS.WHITE

    def set_gray(self, v: Vertex) -> None:
        """
        Mark a vertex as discovered but not fully processed.
        """
        self.colors[v] = BFS.GRAY

    def set_black(self, v: Vertex) -> None:
        """
        Mark a vertex as fully processed.
        """
        self.colors[v] = BFS.BLACK

    def set_dist(self, v: Vertex, d: int) -> None:
        """
        Store the distance from the source vertex.
        """
        self.distances[v] = d

    def get_dist(self, v: Vertex) -> int:
        """
        Return the distance from the source vertex.
        """
        return self.distances[v]

    def set_parent(self, v: Vertex, p: Vertex | None) -> None:
        """
        Record a predecessor in the BFS tree.
        """
        self.parents[v] = p

    def get_parent(self, v: Vertex | None) -> Vertex | None:
        """
        Return the predecessor of a vertex.
        """
        if v is not None:
            return self.parents[v]
        return None

    def is_white(self, v: Vertex) -> bool:
        """
        Return True if the vertex has not been discovered.
        """
        return self.colors[v] == BFS.WHITE

    def print_path(self, v: Vertex) -> None:
        """
        Print the shortest path from the source to a vertex.
        """
        path = []
        next_v: Vertex | None = v

        path.append(next_v)

        while next_v is not None:
            path.append(self.get_parent(next_v))
            next_v = self.get_parent(next_v)

        print([v for v in reversed(path)])


def create_graph() -> tuple[Vertex, Graph]:
    g = Graph()

    v1 = g.add_vertex(1)
    v2 = g.add_vertex(2)
    v3 = g.add_vertex(3)
    v4 = g.add_vertex(4)
    v5 = g.add_vertex(5)
    v6 = g.add_vertex(6)
    v7 = g.add_vertex(7)
    v8 = g.add_vertex(8)
    v9 = g.add_vertex(9)
    v10 = g.add_vertex(10)
    v11 = g.add_vertex(11)

    g.add_undirected_edge(v1, v2)
    g.add_undirected_edge(v1, v3)
    g.add_undirected_edge(v1, v4)
    g.add_undirected_edge(v2, v3)
    g.add_undirected_edge(v2, v8)
    g.add_undirected_edge(v3, v5)
    g.add_undirected_edge(v4, v5)
    g.add_undirected_edge(v5, v6)
    g.add_undirected_edge(v6, v7)
    g.add_undirected_edge(v7, v8)
    g.add_undirected_edge(v8, v9)
    g.add_undirected_edge(v8, v10)
    g.add_undirected_edge(v9, v11)

    return (v1, g)


def main():
    (v1, g) = create_graph()

    print("Do BFS:")

    def process_vertex(v: Vertex, bfs: BFS):
        print(
            "vertex: {0}, parent: {1}, distance: {2}".format(
                v, bfs.get_parent(v), bfs.get_dist(v)
            )
        )

    bfs = BFS(g, v1, process_vertex)
    bfs.do()

    print("\nShortest paths:")
    print("to 6:")
    bfs.print_path(g[6])
    print("to 11:")
    bfs.print_path(g[11])


if __name__ == "__main__":
    main()
