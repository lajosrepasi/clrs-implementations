from clrs.chapter17.order_statistic_tree import Node, OrderStatisticTree


def create_tree() -> OrderStatisticTree:
    tree = OrderStatisticTree()

    for key in [5, 2, 9, 19, 21, 1, 3, 25]:
        tree.insert(key, str(key))

    return tree


def test_root_size():
    tree = create_tree()

    assert tree.root is not None
    assert isinstance(tree.root, Node)
    assert tree.root.size == 8


def test_get_ith_element():
    tree = create_tree()

    expected = [1, 2, 3, 5, 9, 19, 21, 25]

    for i, expected_key in enumerate(expected, start=1):
        node = tree.get_ith_element(i)

        assert node is not None
        assert node.key == expected_key


def test_get_ith_element_iterative():
    tree = create_tree()

    for i, expected in enumerate(
        [1, 2, 3, 5, 9, 19, 21, 25],
        start=1,
    ):
        node = tree.get_ith_element_it(i)
        assert node is not None
        assert node.key == expected


def test_get_ith_element_out_of_range():
    tree = create_tree()

    assert tree.get_ith_element(9) is None
    assert tree.get_ith_element_it(9) is None


def test_rank_queries():
    tree = create_tree()

    assert tree.get_rank(1) == 1
    assert tree.get_rank(2) == 2
    assert tree.get_rank(3) == 3
    assert tree.get_rank(5) == 4
    assert tree.get_rank(9) == 5
    assert tree.get_rank(19) == 6
    assert tree.get_rank(21) == 7
    assert tree.get_rank(25) == 8


def test_iterative_rank():
    tree = create_tree()

    node1 = tree.search(1)
    assert node1 is not None
    assert isinstance(node1, Node)
    assert node1.get_node_rank_it() == 1

    node5 = tree.search(5)
    assert node5 is not None
    assert isinstance(node5, Node)
    assert node5.get_node_rank_it() == 4

    node19 = tree.search(19)
    assert node19 is not None
    assert isinstance(node19, Node)
    assert node19.get_node_rank_it() == 6

    node25 = tree.search(25)
    assert node25 is not None
    assert isinstance(node25, Node)
    assert node25.get_node_rank_it() == 8


def test_recursive_and_iterative_select_match():
    tree = create_tree()

    for i in range(1, 9):
        assert tree.get_ith_element(i).key == tree.get_ith_element_it(i).key
