import pytest

from clrs.chapter20.graph import Graph


def test_add_vertex():
    g = Graph()

    v = g.add_vertex(1)

    assert len(g) == 1
    assert g[1] is v


def test_contains_label():
    g = Graph()

    g.add_vertex(1)

    assert 1 in g
    assert 2 not in g


def test_contains_vertex():
    g = Graph()

    v = g.add_vertex(1)

    assert v in g


def test_directed_edge():
    g = Graph()

    v1 = g.add_vertex(1)
    v2 = g.add_vertex(2)

    g.add_directed_edge(v1, v2)

    assert v2 in v1.neighbours
    assert v1 not in v2.neighbours


def test_undirected_edge():
    g = Graph()

    v1 = g.add_vertex(1)
    v2 = g.add_vertex(2)

    g.add_undirected_edge(v1, v2)

    assert v2 in v1.neighbours
    assert v1 in v2.neighbours


def test_no_duplicate_edges():
    g = Graph()

    v1 = g.add_vertex(1)
    v2 = g.add_vertex(2)

    g.add_directed_edge(v1, v2)
    g.add_directed_edge(v1, v2)

    assert len(v1.neighbours) == 1


def test_get_vertex():
    g = Graph()

    v = g.add_vertex(10)

    assert g.get_vertex(10) is v


def test_graph_iteration():
    g = Graph()

    g.add_vertex(1)
    g.add_vertex(2)
    g.add_vertex(3)

    labels = sorted(v.label for v in g)

    assert labels == [1, 2, 3]


def test_add_edge_with_foreign_vertex():
    g1 = Graph()
    g2 = Graph()

    v1 = g1.add_vertex(1)
    v2 = g2.add_vertex(2)

    with pytest.raises(Exception):
        g1.add_directed_edge(v1, v2)


def test_multiple_edges():
    g = Graph()

    v1 = g.add_vertex(1)
    v2 = g.add_vertex(2)
    v3 = g.add_vertex(3)

    g.add_directed_edge(v1, v2)
    g.add_directed_edge(v1, v3)

    assert len(v1.neighbours) == 2
    assert v2 in v1.neighbours
    assert v3 in v1.neighbours


def test_vertex_string_representation():
    g = Graph()

    v = g.add_vertex(42)

    assert str(v) == "(42)"
