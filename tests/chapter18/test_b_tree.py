import random

from clrs.chapter18.b_tree import BTree, clean


def setup_function():
    clean()


def test_insert_and_search_single_key():
    tree = BTree()

    tree.insert(5, "five")

    node, idx = tree.search(5)

    assert node is not None
    assert idx is not None
    assert node.kvs[idx].v == "five"


def test_search_missing_key():
    tree = BTree()

    tree.insert(5, "five")

    node, idx = tree.search(100)

    assert node is None
    assert idx is None


def test_multiple_insertions():
    tree = BTree()

    data = {
        5: "a",
        34: "b",
        9: "c",
        234: "d",
        23: "e",
        123: "f",
        99: "g",
        919: "h",
        9191: "i",
    }

    for k, v in data.items():
        tree.insert(k, v)

    for k, expected in data.items():
        node, idx = tree.search(k)

        assert node is not None
        assert idx is not None
        assert node.kvs[idx].v == expected


def test_root_split_occurs():
    tree = BTree(min_degree=2)

    for i in range(10):
        tree.insert(i, str(i))

    assert tree.root.leaf is False
    assert len(tree.root.children) > 1


def test_keys_remain_searchable_after_root_split():
    tree = BTree(min_degree=2)

    for i in range(20):
        tree.insert(i, str(i))

    for i in range(20):
        node, idx = tree.search(i)

        assert node is not None
        assert idx is not None
        assert node.kvs[idx].v == str(i)


def test_insert_in_ascending_order():
    tree = BTree()

    for i in range(50):
        tree.insert(i, str(i))

    for i in range(50):
        node, idx = tree.search(i)

        assert node is not None
        assert idx is not None
        assert node.kvs[idx].v == str(i)


def test_insert_in_descending_order():
    tree = BTree()

    for i in reversed(range(50)):
        tree.insert(i, str(i))

    for i in range(50):
        node, idx = tree.search(i)

        assert node is not None
        assert idx is not None
        assert node.kvs[idx].v == str(i)


def test_large_ascending_insertions():
    tree = BTree(min_degree=2)

    for i in range(200):
        tree.insert(i, str(i))

    for i in range(200):
        node, idx = tree.search(i)

        assert node is not None
        assert idx is not None
        assert node.kvs[idx].v == str(i)


def test_large_descending_insertions():
    tree = BTree(min_degree=2)

    for i in reversed(range(200)):
        tree.insert(i, str(i))

    for i in range(200):
        node, idx = tree.search(i)

        assert node is not None
        assert idx is not None
        assert node.kvs[idx].v == str(i)


def test_random_insertions():
    tree = BTree(min_degree=2)

    keys = list(range(200))
    random.shuffle(keys)

    for key in keys:
        tree.insert(key, str(key))

    for key in range(200):
        node, idx = tree.search(key)

        assert node is not None
        assert idx is not None
        assert node.kvs[idx].v == str(key)


def test_search_for_missing_keys_after_many_splits():
    tree = BTree(min_degree=2)

    for i in range(100):
        tree.insert(i, str(i))

    for key in [100, 101, 1000, -1, -100]:
        node, idx = tree.search(key)

        assert node is None
        assert idx is None


def test_root_becomes_internal_node():
    tree = BTree(min_degree=2)

    for i in range(20):
        tree.insert(i, str(i))

    assert tree.root.leaf is False
    assert len(tree.root.children) >= 2


def test_all_inserted_keys_are_unique_and_reachable():
    tree = BTree(min_degree=2)

    inserted = {}

    for i in range(150):
        inserted[i] = f"value-{i}"
        tree.insert(i, inserted[i])

    for key, expected_value in inserted.items():
        node, idx = tree.search(key)

        assert node is not None
        assert idx is not None
        assert node.kvs[idx].v == expected_value


def test_multiple_tree_levels():
    tree = BTree(min_degree=2)

    for i in range(500):
        tree.insert(i, str(i))

    assert tree.root.leaf is False

    for i in [0, 1, 5, 17, 42, 99, 123, 250, 499]:
        node, idx = tree.search(i)

        assert node is not None
        assert idx is not None
        assert node.kvs[idx].v == str(i)


def test_randomized_insertions_repeatable():
    random.seed(42)

    tree = BTree(min_degree=2)

    keys = list(range(300))
    random.shuffle(keys)

    for key in keys:
        tree.insert(key, str(key))

    for key in range(300):
        node, idx = tree.search(key)

        assert node is not None
        assert idx is not None
        assert node.kvs[idx].v == str(key)


def validate_btree_node(node, min_degree, is_root=False):
    max_keys = 2 * min_degree - 1
    min_keys = 1 if is_root else min_degree - 1

    if not is_root:
        assert len(node.kvs) >= min_keys

    assert len(node.kvs) <= max_keys

    keys = [kv.k for kv in node.kvs]
    assert keys == sorted(keys)

    if node.leaf:
        assert len(node.children) == 0
    else:
        assert len(node.children) == len(node.kvs) + 1
