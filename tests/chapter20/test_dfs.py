from clrs.chapter20.dfs import DFS, DFSWithStack, create_graph


def noop_vertex(v, dfs):
    pass


def test_recursive_visits_all_vertices():
    start, g = create_graph()

    dfs = DFS(g, start, noop_vertex)
    dfs.do()

    for v in g:
        assert dfs.get_color(v) == DFS.BLACK


def test_stack_visits_all_vertices():
    start, g = create_graph()

    dfs = DFSWithStack(g, start, noop_vertex)
    dfs.do()

    for v in g:
        assert dfs.get_color(v) == DFS.BLACK


def test_discovery_and_finish_times_recursive():
    start, g = create_graph()

    dfs = DFS(g, start, noop_vertex)
    dfs.do()

    for v in g:
        assert dfs.get_discovery_time(v) > 0
        ft = dfs.get_finish_time(v)
        assert ft is not None
        assert ft > dfs.get_discovery_time(v)


def test_discovery_and_finish_times_stack():
    start, g = create_graph()

    dfs = DFSWithStack(g, start, noop_vertex)
    dfs.do()

    for v in g:
        assert dfs.get_discovery_time(v) > 0
        ft = dfs.get_finish_time(v)
        assert ft is not None
        assert ft > dfs.get_discovery_time(v)


def test_start_vertex_discovered_first():
    start, g = create_graph()

    dfs = DFS(g, start, noop_vertex)
    dfs.do()

    assert dfs.get_discovery_time(start) == 1


def test_parent_relationships():
    start, g = create_graph()

    dfs = DFS(g, start, noop_vertex)
    dfs.do()

    parent_count = 0

    for v in g:
        if dfs.parents[v] is not None:
            parent_count += 1

    assert parent_count == len(g) - 1


def test_finish_times_are_unique():
    start, g = create_graph()

    dfs = DFS(g, start, noop_vertex)
    dfs.do()

    finishes = [dfs.get_finish_time(v) for v in g]

    assert len(finishes) == len(set(finishes))


def test_discovery_times_are_unique():
    start, g = create_graph()

    dfs = DFS(g, start, noop_vertex)
    dfs.do()

    discoveries = [dfs.get_discovery_time(v) for v in g]

    assert len(discoveries) == len(set(discoveries))


def test_recursive_and_stack_visit_same_vertices():
    start, g = create_graph()

    recursive_seen = []
    stack_seen = []

    DFS(
        g,
        start,
        lambda v, dfs: recursive_seen.append(v.label),
    ).do()

    DFSWithStack(
        g,
        start,
        lambda v, dfs: stack_seen.append(v.label),
    ).do()

    assert set(recursive_seen) == set(stack_seen)
    assert len(recursive_seen) == len(g)
    assert len(stack_seen) == len(g)


def test_edge_callback_is_called():
    start, g = create_graph()

    edges = []

    def edge_proc(u, v, dfs):
        edges.append((u.label, v.label))

    dfs = DFS(
        g,
        start,
        noop_vertex,
        edge_proc,
    )

    dfs.do()

    assert len(edges) > 0
