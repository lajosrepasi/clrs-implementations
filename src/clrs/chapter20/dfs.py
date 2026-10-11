"""
Depth-first search (DFS) implementations.

Provides both recursive and explicit-stack versions of DFS,
including discovery times, finish times, parent tracking,
and edge processing callbacks.
"""

from __future__ import annotations

from collections.abc import Callable

from clrs.chapter10.stack import Stack
from clrs.chapter20.graph import Graph, Vertex


class DFS:
    """
    Depth-first search traversal.

    Tracks discovery times, finish times,
    colors, and parent relationships.
    """

    WHITE = 1
    GRAY = 2
    BLACK = 3

    def __init__(
        self,
        graph: Graph,
        start_vertex: Vertex,
        vertex_proc_func: Callable[[Vertex, DFS], None],
        edge_proc_func: Callable[[Vertex, Vertex, DFS], None] | None = None,
    ) -> None:
        self.graph: Graph = graph
        self.start_vertex: Vertex = start_vertex
        self.vertex_proc_func: Callable[[Vertex, DFS], None] = vertex_proc_func
        self.edge_proc_func: Callable[[Vertex, Vertex, DFS], None] | None = (
            edge_proc_func
        )
        self.time: int = 0

        # State stored cleanly mapping Vertex -> state
        self.colors: dict[Vertex, int] = {}
        self.discovery_times: dict[Vertex, int] = {}
        self.finish_times: dict[Vertex, int] = {}
        self.parents: dict[Vertex, Vertex | None] = {}

    def do(self) -> None:
        """
        Execute depth-first search over the graph.
        """
        self.init_dfs()

        self.visit(self.start_vertex)

        for v in self.graph:
            if self.is_white(v):
                self.visit(v)

    def visit(self, v: Vertex) -> None:
        """
        Recursively visit a vertex and its descendants.
        """
        self.time += 1
        self.set_discovery_time(v, self.time)
        self.set_gray(v)

        for neighbour in v.neighbours:
            if self.edge_proc_func is not None:
                self.edge_proc_func(v, neighbour, self)

            if self.is_white(neighbour):
                self.set_parent(neighbour, v)
                self.visit(neighbour)

        self.time += 1
        self.set_black(v)
        self.set_finish_time(v, self.time)

        self.vertex_proc_func(v, self)

    def init_dfs(self) -> None:
        """
        Initialize DFS state before traversal.
        """
        self.time = 0

        for v in self.graph:
            self.set_white(v)
            self.set_discovery_time(v, 0)
            self.set_finish_time(v, 0)
            self.set_parent(v, None)

    def set_white(self, v: Vertex) -> None:
        """
        Mark a vertex as undiscovered.
        """
        self.colors[v] = DFS.WHITE

    def set_gray(self, v: Vertex) -> None:
        """
        Mark a vertex as discovered but not fully processed.
        """
        self.colors[v] = DFS.GRAY

    def set_black(self, v: Vertex) -> None:
        """
        Mark a vertex as fully processed.
        """
        self.colors[v] = DFS.BLACK

    def set_discovery_time(self, v: Vertex, d: int) -> None:
        """
        Store a vertex discovery time.
        """
        self.discovery_times[v] = d

    def get_discovery_time(self, v: Vertex) -> int:
        """
        Return the discovery time of a vertex.
        """
        return self.discovery_times[v]

    def set_finish_time(self, v: Vertex, fin: int) -> None:
        """
        Store a vertex finish time.
        """
        self.finish_times[v] = fin

    def get_finish_time(self, v: Vertex) -> int | None:
        """
        Return a vertex finish time.
        """
        return self.finish_times[v]

    def get_color(self, v: Vertex) -> int | None:
        """
        Return the current color of a vertex.
        """
        return self.colors[v]

    def is_white(self, v: Vertex) -> bool:
        """
        Return True if the vertex has not been discovered.
        """
        return self.colors[v] == DFS.WHITE

    def set_parent(self, v: Vertex, p: Vertex | None) -> None:
        """
        Record a parent in the DFS forest.
        """
        self.parents[v] = p


class DFSWithStack(DFS):
    """
    Iterative depth-first search using an explicit stack.

    Produces the same DFS forest and timestamps as
    the recursive implementation.
    """

    def __init__(
        self,
        graph: Graph,
        start_vertex: Vertex,
        vertex_proc_func: Callable[[Vertex, DFS], None],
    ) -> None:
        super().__init__(graph, start_vertex, vertex_proc_func)
        self.stack: Stack = Stack()

    def init_dfs(self) -> None:
        super().init_dfs()
        self.stack.reset()

    def visit(self, v: Vertex) -> None:
        self.stack.push(v)
        self.time += 1
        self.set_discovery_time(v, self.time)
        self.set_gray(v)

        while not self.stack.empty():
            n = self.stack.get_top()

            for neighbour in n.neighbours:
                if self.is_white(neighbour):
                    self.set_parent(neighbour, n)
                    self.time += 1
                    self.set_discovery_time(neighbour, self.time)
                    self.set_gray(neighbour)
                    self.stack.push(neighbour)
                    break

            if n == self.stack.get_top():
                n = self.stack.pop()
                self.time += 1
                self.set_black(n)
                self.set_finish_time(n, self.time)
                self.vertex_proc_func(n, self)


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

    print("Do DFS recursive:")

    def process_vertex(v, dfs):
        print(
            "vertex: {0}, dist: {1}, finish: {2}".format(
                v, dfs.get_discovery_time(v), dfs.get_finish_time(v)
            )
        )

    def process_edge(u, v, dfs):
        if dfs.get_color(v) == DFS.GRAY:
            print("{0}--{1} is back edge".format(u, v))
        elif dfs.get_color(v) == DFS.WHITE:
            print("{0}--{1} is tree edge".format(u, v))

    dfs = DFS(g, v1, process_vertex, process_edge)
    dfs.do()

    print("\nDo DFS with stack ds:")
    dfs_with_stack = DFSWithStack(g, v1, process_vertex)
    dfs_with_stack.do()


if __name__ == "__main__":
    main()
