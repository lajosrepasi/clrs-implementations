import pytest

from clrs.chapter20.weighted_graph import Edge, Vertex, WeightedGraph


def test_add_vertex():
    g = WeightedGraph()

    v = g.add_vertex(1)

    assert v.label == 1
    assert g[1] is v


def test_directed_edge():
    g = WeightedGraph()

    v1 = g.add_vertex(1)
    v2 = g.add_vertex(2)

    g.add_directed_edge(v1, v2, 5.0)

    assert len(v1.neighbours) == 1
    assert len(v2.neighbours) == 0

    edge = v1.neighbours[0]

    assert edge.u is v1
    assert edge.v is v2
    assert edge.w == 5.0


def test_undirected_edge():
    g = WeightedGraph()

    v1 = g.add_vertex(1)
    v2 = g.add_vertex(2)

    g.add_undirected_edge(v1, v2, 7.5)

    assert len(v1.neighbours) == 1
    assert len(v2.neighbours) == 1

    assert v1.neighbours[0].v is v2
    assert v2.neighbours[0].v is v1

    assert v1.neighbours[0].w == 7.5
    assert v2.neighbours[0].w == 7.5


def test_edge_comparison():
    g = WeightedGraph()

    v1 = g.add_vertex(1)
    v2 = g.add_vertex(2)

    e1 = Edge(v1, v2, 3)
    e2 = Edge(v1, v2, 7)

    assert e1 < e2
    assert e2 > e1
    assert e1 <= e2
    assert e2 >= e1


def test_multiple_edges():
    g = WeightedGraph()

    v1 = g.add_vertex(1)
    v2 = g.add_vertex(2)
    v3 = g.add_vertex(3)

    g.add_directed_edge(v1, v2, 5)
    g.add_directed_edge(v1, v3, 8)

    assert len(v1.neighbours) == 2

    destinations = {edge.v.label for edge in v1.neighbours}

    assert destinations == {2, 3}


def test_contains_vertex():
    g = WeightedGraph()

    v = g.add_vertex(1)

    assert v in g
    assert 1 in g
    assert 99 not in g


def test_foreign_vertex_rejected():
    g1 = WeightedGraph()
    g2 = WeightedGraph()

    v1 = g1.add_vertex(1)
    v2 = g2.add_vertex(2)

    with pytest.raises(Exception):
        g1.add_directed_edge(v1, v2, 1.0)


def test_edge_string():
    g = WeightedGraph()

    v1 = g.add_vertex(1)
    v2 = g.add_vertex(2)

    edge = Edge(v1, v2, 5)

    assert str(edge) == "((1)--5--(2))"


def test_vertex_string():
    g = WeightedGraph()

    v = g.add_vertex(42)

    assert str(v) == "(42)"


def test_add_vertex_returns_weighted_vertex():
    g = WeightedGraph()

    v = g.add_vertex(1)

    assert isinstance(v, Vertex)
