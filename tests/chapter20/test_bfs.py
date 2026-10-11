from sys import maxsize as Infinity

from clrs.chapter20.bfs import BFS, Graph, create_graph


def noop(v, bfs):
    pass


def test_bfs_start_distance():
    start, g = create_graph()

    bfs = BFS(g, start, noop)
    bfs.do()

    assert bfs.get_dist(start) == 0


def test_bfs_distance_to_neighbours():
    start, g = create_graph()

    bfs = BFS(g, start, noop)
    bfs.do()

    assert bfs.get_dist(g[2]) == 1
    assert bfs.get_dist(g[3]) == 1
    assert bfs.get_dist(g[4]) == 1


def test_bfs_distance_to_vertex_6():
    start, g = create_graph()

    bfs = BFS(g, start, noop)
    bfs.do()

    assert bfs.get_dist(g[6]) == 3


def test_bfs_distance_to_vertex_11():
    start, g = create_graph()

    bfs = BFS(g, start, noop)
    bfs.do()

    assert bfs.get_dist(g[11]) == 4


def test_bfs_parent_relationships():
    start, g = create_graph()

    bfs = BFS(g, start, noop)
    bfs.do()

    assert bfs.get_parent(g[2]) == g[1]
    assert bfs.get_parent(g[3]) == g[1]
    assert bfs.get_parent(g[4]) == g[1]


def test_all_vertices_visited():
    start, g = create_graph()

    bfs = BFS(g, start, noop)
    bfs.do()

    for v in g:
        assert not bfs.is_white(v)


def test_callback_called_for_every_vertex():
    start, g = create_graph()

    visited = []

    def process(v, bfs):
        visited.append(v.label)

    bfs = BFS(g, start, process)
    bfs.do()

    assert len(visited) == len(g)
    assert set(visited) == set(range(1, 12))


def test_shortest_path_to_11():
    start, g = create_graph()

    bfs = BFS(g, start, noop)
    bfs.do()

    path = []

    current = g[11]

    while current is not None:
        path.append(current.label)
        current = bfs.get_parent(current)

    path.reverse()

    assert path[0] == 1
    assert path[-1] == 11
    assert len(path) == 5


def test_start_vertex_has_no_parent():
    start, g = create_graph()

    bfs = BFS(g, start, noop)
    bfs.do()

    assert bfs.get_parent(start) is None


def test_vertex_colors_after_bfs():
    start, g = create_graph()

    bfs = BFS(g, start, noop)
    bfs.do()

    for v in g:
        assert bfs.colors[v] == BFS.BLACK


def test_unreachable_vertex():
    g = Graph()

    v1 = g.add_vertex(1)
    v2 = g.add_vertex(2)
    v3 = g.add_vertex(3)

    g.add_undirected_edge(v1, v2)
    # v3 is disconnected

    bfs = BFS(g, v1, lambda v, bfs: None)
    bfs.do()

    assert bfs.get_dist(v1) == 0
    assert bfs.get_dist(v2) == 1
    assert bfs.get_dist(v3) == Infinity

    assert bfs.get_parent(v3) is None
    assert bfs.colors[v3] == BFS.WHITE
