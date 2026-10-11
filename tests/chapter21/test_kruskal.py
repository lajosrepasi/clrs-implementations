from clrs.chapter20.weighted_graph import WeightedGraph
from clrs.chapter21.kruskal import create_graph, kruskal


def mst_weight(edges):
    return sum(e.w for e in edges)


def test_clrs_example_mst_weight():
    _, g = create_graph()

    mst = kruskal(g)

    assert len(mst) == len(g) - 1
    assert mst_weight(mst) == 37


def test_single_vertex_graph():
    g = WeightedGraph()
    g.add_vertex(1)

    mst = kruskal(g)

    assert mst == []


def test_two_vertices_one_edge():
    g = WeightedGraph()

    v1 = g.add_vertex(1)
    v2 = g.add_vertex(2)

    g.add_undirected_edge(v1, v2, 5)

    mst = kruskal(g)

    assert len(mst) == 1
    assert mst[0].w == 5


def test_triangle_graph():
    g = WeightedGraph()

    v1 = g.add_vertex(1)
    v2 = g.add_vertex(2)
    v3 = g.add_vertex(3)

    g.add_undirected_edge(v1, v2, 1)
    g.add_undirected_edge(v2, v3, 2)
    g.add_undirected_edge(v1, v3, 10)

    mst = kruskal(g)

    assert len(mst) == 2
    assert mst_weight(mst) == 3


def test_no_cycles_in_mst():
    _, g = create_graph()

    mst = kruskal(g)

    assert len(mst) == len(g) - 1
