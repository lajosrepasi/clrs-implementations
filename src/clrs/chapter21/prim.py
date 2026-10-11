"""
Prim's algorithm for computing a minimum spanning tree.

The algorithm grows the tree from a chosen start vertex,
repeatedly selecting the lightest edge connecting the
current tree to an unexplored vertex.

This implementation uses a min-priority queue and returns
the edges of the minimum spanning tree.
"""

from clrs.chapter06.priority_queue import MinPriorityQueue
from clrs.chapter07.quick_sort import quick_sort
from clrs.chapter20.weighted_graph import Edge, Vertex, WeightedGraph
from clrs.chapter21.kruskal import create_graph


def prim(start_vertex: Vertex, g: WeightedGraph) -> list[Edge]:
    """
    Compute a minimum spanning tree using Prim's algorithm.
    """
    mst = []

    min_prio_queue: MinPriorityQueue[float, Vertex] = MinPriorityQueue()

    parents: dict[Vertex, Vertex | None] = {}
    known_mins: dict[Vertex, float] = {}

    for v in g:
        if v != start_vertex:
            assert isinstance(v, Vertex)
            known_mins[v] = float("inf")
            parents[v] = None
            min_prio_queue.insert(known_mins[v], v)

    parents[start_vertex] = None
    known_mins[start_vertex] = 0
    min_prio_queue.insert(known_mins[start_vertex], start_vertex)

    while not min_prio_queue.empty():
        w_u = min_prio_queue.extract_minimum()

        if w_u is not None:
            w, u = w_u
            assert u is not None
            p = parents[u]
            if p is not None:
                mst.append(Edge(p, u, w))

            for neighbour in u.neighbours:
                v = neighbour.v
                if v in min_prio_queue and neighbour.w < known_mins[v]:
                    n_w = neighbour.w
                    min_prio_queue.decrease_key(n_w, known_mins[v], v)

                    known_mins[v] = n_w
                    parents[v] = u

    return mst


def main():
    v1, g = create_graph()

    mst = prim(v1, g)
    print(mst)
    print(quick_sort(mst))


if __name__ == "__main__":
    main()
