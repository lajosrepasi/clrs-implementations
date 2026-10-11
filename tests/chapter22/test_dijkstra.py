from clrs.chapter20.weighted_graph import Vertex, WeightedGraph
from clrs.chapter22.bellman_ford import create_graph
from clrs.chapter22.dijkstra import Dijkstra


def test_initialisation():
    start, g = create_graph()

    dijkstra = Dijkstra(g, start)

    assert dijkstra.distances[start] == 0
    assert dijkstra.parents[start] is None

    for v in g:
        if v is not start:
            assert isinstance(v, Vertex)
            assert dijkstra.distances[v] == float("inf")
            assert dijkstra.parents[v] is None


def test_relax():
    g = WeightedGraph()

    v1 = g.add_vertex(1)
    v2 = g.add_vertex(2)

    dijkstra = Dijkstra(g, v1)

    changed = dijkstra.relax(v1, v2, 5)

    assert changed
    assert dijkstra.distances[v2] == 5
    assert dijkstra.parents[v2] is v1


def test_relax_does_not_replace_shorter_path():
    g = WeightedGraph()

    v1 = g.add_vertex(1)
    v2 = g.add_vertex(2)

    dijkstra = Dijkstra(g, v1)

    assert dijkstra.relax(v1, v2, 5)
    assert not dijkstra.relax(v1, v2, 10)

    assert dijkstra.distances[v2] == 5
    assert dijkstra.parents[v2] is v1


def test_example_graph():
    start, g = create_graph()

    dijkstra = Dijkstra(g, start)
    dijkstra.do()

    assert dijkstra.distances[g[1]] == 0
    assert dijkstra.distances[g[2]] == 3
    assert dijkstra.distances[g[3]] == 9
    assert dijkstra.distances[g[4]] == 5
    assert dijkstra.distances[g[5]] == 6


def test_example_graph_parents():
    start, g = create_graph()

    dijkstra = Dijkstra(g, start)
    dijkstra.do()

    assert dijkstra.parents[g[1]] is None
    assert dijkstra.parents[g[2]] is g[1]
    assert dijkstra.parents[g[4]] is g[1]
    assert dijkstra.parents[g[5]] is g[4]


def test_shorter_indirect_path():
    g = WeightedGraph()

    v1 = g.add_vertex(1)
    v2 = g.add_vertex(2)
    v3 = g.add_vertex(3)

    g.add_directed_edge(v1, v3, 10)
    g.add_directed_edge(v1, v2, 3)
    g.add_directed_edge(v2, v3, 4)

    dijkstra = Dijkstra(g, v1)
    dijkstra.do()

    assert dijkstra.distances[v1] == 0
    assert dijkstra.distances[v2] == 3
    assert dijkstra.distances[v3] == 7

    assert dijkstra.parents[v2] is v1
    assert dijkstra.parents[v3] is v2


def test_multiple_relaxations():
    g = WeightedGraph()

    v1 = g.add_vertex(1)
    v2 = g.add_vertex(2)
    v3 = g.add_vertex(3)
    v4 = g.add_vertex(4)

    g.add_directed_edge(v1, v4, 20)
    g.add_directed_edge(v1, v2, 5)
    g.add_directed_edge(v2, v3, 3)
    g.add_directed_edge(v3, v4, 2)

    dijkstra = Dijkstra(g, v1)
    dijkstra.do()

    assert dijkstra.distances[v4] == 10
    assert dijkstra.parents[v4] is v3


def test_unreachable_vertex():
    g = WeightedGraph()

    v1 = g.add_vertex(1)
    v2 = g.add_vertex(2)
    v3 = g.add_vertex(3)

    g.add_directed_edge(v1, v2, 4)

    dijkstra = Dijkstra(g, v1)
    dijkstra.do()

    assert dijkstra.distances[v1] == 0
    assert dijkstra.distances[v2] == 4
    assert dijkstra.distances[v3] == float("inf")

    assert dijkstra.parents[v3] is None


def test_dijkstra_matches_bellman_ford():
    from clrs.chapter22.bellman_ford import BellmanFord

    start, g = create_graph()

    dijkstra = Dijkstra(g, start)
    dijkstra.do()

    bellman_ford = BellmanFord(g, start)
    assert bellman_ford.do()

    for v in g:
        assert isinstance(v, Vertex)
        assert dijkstra.distances[v] == bellman_ford.distances[v]
