from clrs.chapter20.weighted_graph import Vertex, WeightedGraph
from clrs.chapter22.bellman_ford import BellmanFord, create_graph


def test_initialisation():
    start, g = create_graph()

    bf = BellmanFord(g, start)

    assert bf.distances[start] == 0
    assert bf.parents[start] is None

    for v in g:
        if v is not start:
            assert isinstance(v, Vertex)
            assert bf.distances[v] == float("inf")
            assert bf.parents[v] is None


def test_relax():
    g = WeightedGraph()

    v1 = g.add_vertex(1)
    v2 = g.add_vertex(2)

    bf = BellmanFord(g, v1)

    bf.relax(v1, v2, 5)

    assert bf.distances[v2] == 5
    assert bf.parents[v2] is v1


def test_relax_does_not_replace_shorter_path():
    g = WeightedGraph()

    v1 = g.add_vertex(1)
    v2 = g.add_vertex(2)

    bf = BellmanFord(g, v1)

    bf.relax(v1, v2, 5)
    bf.relax(v1, v2, 10)

    assert bf.distances[v2] == 5
    assert bf.parents[v2] is v1


def test_example_graph():
    start, g = create_graph()

    bf = BellmanFord(g, start)

    assert bf.do()

    assert bf.distances[g[1]] == 0
    assert bf.distances[g[2]] == 3
    assert bf.distances[g[3]] == 9
    assert bf.distances[g[4]] == 5
    assert bf.distances[g[5]] == 6


def test_example_graph_parents():
    start, g = create_graph()

    bf = BellmanFord(g, start)
    bf.do()

    assert bf.parents[g[1]] is None
    assert bf.parents[g[2]] is g[1]
    assert bf.parents[g[4]] is g[1]
    assert bf.parents[g[5]] is g[4]


def test_graph_with_negative_edge():
    g = WeightedGraph()

    v1 = g.add_vertex(1)
    v2 = g.add_vertex(2)
    v3 = g.add_vertex(3)

    g.add_directed_edge(v1, v2, 5)
    g.add_directed_edge(v1, v3, 10)
    g.add_directed_edge(v2, v3, -3)

    bf = BellmanFord(g, v1)

    assert bf.do()

    assert bf.distances[v1] == 0
    assert bf.distances[v2] == 5
    assert bf.distances[v3] == 2

    assert bf.parents[v2] is v1
    assert bf.parents[v3] is v2


def test_negative_weight_cycle():
    g = WeightedGraph()

    v1 = g.add_vertex(1)
    v2 = g.add_vertex(2)
    v3 = g.add_vertex(3)

    g.add_directed_edge(v1, v2, 1)
    g.add_directed_edge(v2, v3, -2)
    g.add_directed_edge(v3, v1, -2)

    bf = BellmanFord(g, v1)

    assert not bf.do()


def test_positive_cycle():
    g = WeightedGraph()

    v1 = g.add_vertex(1)
    v2 = g.add_vertex(2)
    v3 = g.add_vertex(3)

    g.add_directed_edge(v1, v2, 1)
    g.add_directed_edge(v2, v3, 2)
    g.add_directed_edge(v3, v1, 3)

    bf = BellmanFord(g, v1)

    assert bf.do()

    assert bf.distances[v1] == 0
    assert bf.distances[v2] == 1
    assert bf.distances[v3] == 3


def test_shorter_path_found_after_multiple_relaxations():
    g = WeightedGraph()

    v1 = g.add_vertex(1)
    v2 = g.add_vertex(2)
    v3 = g.add_vertex(3)
    v4 = g.add_vertex(4)

    g.add_directed_edge(v1, v4, 20)
    g.add_directed_edge(v1, v2, 5)
    g.add_directed_edge(v2, v3, 3)
    g.add_directed_edge(v3, v4, 2)

    bf = BellmanFord(g, v1)

    assert bf.do()

    assert bf.distances[v4] == 10
    assert bf.parents[v4] is v3


def test_unreachable_vertex():
    g = WeightedGraph()

    v1 = g.add_vertex(1)
    v2 = g.add_vertex(2)
    v3 = g.add_vertex(3)

    g.add_directed_edge(v1, v2, 4)

    bf = BellmanFord(g, v1)

    assert bf.do()

    assert bf.distances[v1] == 0
    assert bf.distances[v2] == 4
    assert bf.distances[v3] == float("inf")

    assert bf.parents[v3] is None
