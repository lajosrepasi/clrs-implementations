from clrs.chapter20.weighted_graph import WeightedGraph
from clrs.chapter21.kruskal import create_graph, kruskal
from clrs.chapter21.prim import prim


def mst_weight(edges):
    return sum(edge.w for edge in edges)


def test_single_vertex_graph():
    g = WeightedGraph()

    v1 = g.add_vertex(1)

    mst = prim(v1, g)

    assert mst == []


def test_two_vertices():
    g = WeightedGraph()

    v1 = g.add_vertex(1)
    v2 = g.add_vertex(2)

    g.add_undirected_edge(v1, v2, 5)

    mst = prim(v1, g)

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

    mst = prim(v1, g)

    assert len(mst) == 2
    assert mst_weight(mst) == 3


def test_square_graph():
    g = WeightedGraph()

    v1 = g.add_vertex(1)
    v2 = g.add_vertex(2)
    v3 = g.add_vertex(3)
    v4 = g.add_vertex(4)

    g.add_undirected_edge(v1, v2, 1)
    g.add_undirected_edge(v2, v3, 2)
    g.add_undirected_edge(v3, v4, 3)
    g.add_undirected_edge(v4, v1, 4)
    g.add_undirected_edge(v1, v3, 10)

    mst = prim(v1, g)

    assert len(mst) == 3
    assert mst_weight(mst) == 6


def test_clrs_example_weight():
    start_vertex, g = create_graph()

    mst = prim(start_vertex, g)

    assert len(mst) == len(g) - 1
    assert mst_weight(mst) == 37


def test_prim_matches_kruskal():
    start_vertex, g = create_graph()

    prim_mst = prim(start_vertex, g)
    kruskal_mst = kruskal(g)

    assert mst_weight(prim_mst) == mst_weight(kruskal_mst)


def test_disconnected_graph():
    g = WeightedGraph()

    v1 = g.add_vertex(1)
    v2 = g.add_vertex(2)
    v3 = g.add_vertex(3)
    v4 = g.add_vertex(4)

    g.add_undirected_edge(v1, v2, 5)
    g.add_undirected_edge(v3, v4, 1)

    mst = prim(v1, g)

    assert len(mst) == 2
    assert mst_weight(mst) == 6
