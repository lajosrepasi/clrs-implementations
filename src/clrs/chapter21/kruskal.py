"""
Kruskal's minimum spanning tree algorithm.

The algorithm sorts all edges by weight and repeatedly adds the
lightest edge that connects two different connected components.

Connected components are maintained using a disjoint-set data
structure.

Running time: O(E log E).
"""

from clrs.chapter07.quick_sort import quick_sort
from clrs.chapter19.disjoint_sets_with_ll import DisjointSetsLL as Sets
from clrs.chapter19.disjoint_sets_with_ll import Item
from clrs.chapter20.weighted_graph import Edge, Vertex, WeightedGraph


def create_graph() -> tuple[Vertex, WeightedGraph]:
    """
    Create the weighted graph from the CLRS minimum-spanning-tree
    example.
    """
    g = WeightedGraph()

    v1 = g.add_vertex(1)
    v2 = g.add_vertex(2)
    v3 = g.add_vertex(3)
    v4 = g.add_vertex(4)
    v5 = g.add_vertex(5)
    v6 = g.add_vertex(6)
    v7 = g.add_vertex(7)
    v8 = g.add_vertex(8)
    v9 = g.add_vertex(9)

    g.add_undirected_edge(v1, v2, 4)
    g.add_undirected_edge(v1, v8, 8)
    g.add_undirected_edge(v2, v3, 8)
    g.add_undirected_edge(v2, v8, 11)
    g.add_undirected_edge(v3, v4, 7)
    g.add_undirected_edge(v3, v9, 2)
    g.add_undirected_edge(v3, v6, 4)
    g.add_undirected_edge(v4, v5, 9)
    g.add_undirected_edge(v4, v6, 14)
    g.add_undirected_edge(v5, v6, 10)
    g.add_undirected_edge(v6, v7, 2)
    g.add_undirected_edge(v7, v9, 6)
    g.add_undirected_edge(v7, v8, 1)
    g.add_undirected_edge(v8, v9, 7)

    return (v1, g)


def kruskal(g: WeightedGraph) -> list[Edge]:
    """
    Compute a minimum spanning tree using Kruskal's algorithm.

    The algorithm sorts all edges by weight and repeatedly adds
    the lightest edge that does not create a cycle.
    """
    mst = []

    sets = Sets()

    edges = []

    set_items: dict[Vertex, Item] = {}

    for v in g:
        assert isinstance(v, Vertex)
        set_item = Item(v, v)
        sets.make_set(set_item)
        set_items[v] = set_item

        edges += v.neighbours

    quick_sort(edges)

    for e in edges:
        set_u = sets.find_set(set_items[e.u])
        set_v = sets.find_set(set_items[e.v])

        if set_u != set_v and set_u is not None and set_v is not None:
            mst.append(e)
            sets.union(set_u.set, set_v.set)

    return mst


def main():
    v1, g = create_graph()

    mst = kruskal(g)
    print(quick_sort(mst))


if __name__ == "__main__":
    main()
