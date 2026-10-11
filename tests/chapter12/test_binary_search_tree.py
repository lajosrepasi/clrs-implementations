from clrs.chapter12.binary_search_tree import BinarySearchTree, Node


def test_node_creation():
    node = Node(10, "value")

    assert node.key == 10
    assert node.data == "value"
    assert node.left is None
    assert node.right is None
    assert node.p is None


def test_insert():
    tree = BinarySearchTree()

    tree.insert(5, "five")
    tree.insert(2, "two")
    tree.insert(8, "eight")

    assert tree.root is not None
    assert tree.root.key == 5
    assert tree.root.left is not None
    assert tree.root.right is not None
    assert tree.root.left.key == 2
    assert tree.root.right.key == 8


def test_insert_sets_parent():
    tree = BinarySearchTree()

    tree.insert(5, "five")
    tree.insert(2, "two")
    tree.insert(8, "eight")

    assert tree.root is not None
    assert tree.root.left is not None
    assert tree.root.right is not None

    assert tree.root.left.p is tree.root
    assert tree.root.right.p is tree.root


def test_insert_duplicate_goes_left():
    tree = BinarySearchTree()

    tree.insert(5, "first")
    tree.insert(5, "second")

    assert tree.root is not None
    assert tree.root.left is not None
    assert tree.root.left.key == 5
    assert tree.root.left.data == "second"


def test_search():
    tree = BinarySearchTree()

    tree.insert(5, "five")
    tree.insert(2, "two")
    tree.insert(8, "eight")

    node = tree.search(8)

    assert node is not None
    assert node.key == 8
    assert node.data == "eight"


def test_search_missing_key():
    tree = BinarySearchTree()

    tree.insert(5, "five")

    assert tree.search(10) is None


def test_search_empty_tree():
    tree = BinarySearchTree()

    assert tree.search(10) is None


def test_search_iter_matches_recursive_search():
    tree = BinarySearchTree()

    for key in [5, 2, 8, 1, 3, 7, 9]:
        tree.insert(key, str(key))

    for key in [1, 2, 3, 5, 7, 8, 9, 10]:
        recursive = tree.search(key)
        iterative = tree.search_iter(key)

        if recursive is None:
            assert iterative is None
        else:
            assert iterative is not None
            assert iterative.key == recursive.key


def test_minimum():
    tree = BinarySearchTree()

    for key in [5, 2, 8, 1, 3]:
        tree.insert(key, str(key))

    minimum = tree.minimum()

    assert minimum is not None
    assert minimum.key == 1


def test_maximum():
    tree = BinarySearchTree()

    for key in [5, 2, 8, 1, 3, 10]:
        tree.insert(key, str(key))

    maximum = tree.maximum()

    assert maximum is not None
    assert maximum.key == 10


def test_recursive_minimum_and_maximum():
    tree = BinarySearchTree()

    for key in [5, 2, 8, 1, 3, 10]:
        tree.insert(key, str(key))

    assert tree.root is not None
    assert tree.root.minimum_recursive().key == 1
    assert tree.root.maximum_recursive().key == 10


def test_successor():
    tree = BinarySearchTree()

    for key in [5, 2, 8, 1, 3, 7, 9]:
        tree.insert(key, str(key))

    successor = tree.successor(5)

    assert successor is not None
    assert successor.key == 7


def test_successor_with_no_right_child():
    tree = BinarySearchTree()

    for key in [5, 2, 8, 7]:
        tree.insert(key, str(key))

    successor = tree.successor(5)

    assert successor is not None
    assert successor.key == 7
    assert successor.right is None


def test_successor_of_maximum_is_none():
    tree = BinarySearchTree()

    for key in [5, 2, 8, 1, 3, 7, 9]:
        tree.insert(key, str(key))

    assert tree.successor(9) is None


def test_predecessor():
    tree = BinarySearchTree()

    for key in [5, 2, 8, 1, 3, 7, 9]:
        tree.insert(key, str(key))

    predecessor = tree.predecessor(5)

    assert predecessor is not None
    assert predecessor.key == 3


def test_predecessor_of_minimum_is_none():
    tree = BinarySearchTree()

    for key in [5, 2, 8, 1, 3, 7, 9]:
        tree.insert(key, str(key))

    assert tree.predecessor(1) is None


def test_inorder_traversal(capsys):
    tree = BinarySearchTree()

    for key in [5, 2, 8, 1, 3, 7, 9]:
        tree.insert(key, str(key))

    tree.walk_inorder()

    captured = capsys.readouterr()

    assert captured.out.splitlines() == [
        "[1: 1]",
        "[2: 2]",
        "[3: 3]",
        "[5: 5]",
        "[7: 7]",
        "[8: 8]",
        "[9: 9]",
    ]


def test_preorder_traversal(capsys):
    tree = BinarySearchTree()

    for key in [5, 2, 8, 1, 3, 7, 9]:
        tree.insert(key, str(key))

    tree.walk_preorder()

    captured = capsys.readouterr()

    assert captured.out.splitlines() == [
        "[5: 5]",
        "[2: 2]",
        "[1: 1]",
        "[3: 3]",
        "[8: 8]",
        "[7: 7]",
        "[9: 9]",
    ]


def test_postorder_traversal(capsys):
    tree = BinarySearchTree()

    for key in [5, 2, 8, 1, 3, 7, 9]:
        tree.insert(key, str(key))

    tree.walk_postorder()

    captured = capsys.readouterr()

    assert captured.out.splitlines() == [
        "[1: 1]",
        "[3: 3]",
        "[2: 2]",
        "[7: 7]",
        "[9: 9]",
        "[8: 8]",
        "[5: 5]",
    ]


def test_delete_leaf():
    tree = BinarySearchTree()

    for key in [5, 2, 8]:
        tree.insert(key, str(key))

    deleted = tree.delete(2)

    assert deleted is not None
    assert deleted.key == 2
    assert tree.search(2) is None

    assert tree.root is not None
    assert tree.root.left is None


def test_delete_only_node():
    tree = BinarySearchTree()
    tree.insert(5, "five")

    deleted = tree.delete(5)

    assert deleted is not None
    assert deleted.key == 5
    assert tree.root is None


def test_delete_node_with_one_child():
    tree = BinarySearchTree()

    for key in [5, 2, 8, 1]:
        tree.insert(key, str(key))

    tree.delete(2)

    assert tree.search(2) is None
    assert tree.root is not None
    assert tree.root.left is not None
    assert tree.root.left.key == 1
    assert tree.root.left.p is tree.root


def test_delete_root_with_one_child():
    tree = BinarySearchTree()

    tree.insert(5, "five")
    tree.insert(8, "eight")

    tree.delete(5)

    assert tree.root is not None
    assert tree.root.key == 8
    assert tree.root.p is None


def test_delete_root_with_two_children():
    tree = BinarySearchTree()

    for key in [5, 2, 8, 1, 3, 7, 9]:
        tree.insert(key, str(key))

    tree.delete(5)

    assert tree.root is not None
    assert tree.root.key == 7
    assert tree.root.p is None
    assert tree.root.left is not None
    assert tree.root.left.key == 2
    assert tree.root.right is not None
    assert tree.root.right.key == 8


def test_delete_two_children_successor_has_no_right_child():
    tree = BinarySearchTree()

    for key in [5, 2, 8, 7]:
        tree.insert(key, str(key))

    tree.delete(5)

    assert tree.root is not None
    assert tree.root.key == 7
    assert tree.root.p is None
    assert tree.root.left is not None
    assert tree.root.left.key == 2
    assert tree.root.right is not None
    assert tree.root.right.key == 8


def test_delete_two_children_successor_is_right_child():
    tree = BinarySearchTree()

    for key in [5, 2, 8]:
        tree.insert(key, str(key))

    tree.delete(5)

    assert tree.root is not None
    assert tree.root.key == 8
    assert tree.root.left is not None
    assert tree.root.left.key == 2
    assert tree.root.right is None
    assert tree.root.p is None


def test_delete_non_root_with_two_children():
    tree = BinarySearchTree()

    for key in [10, 5, 15, 2, 7, 12, 20, 6, 8]:
        tree.insert(key, str(key))

    tree.delete(5)

    assert tree.search(5) is None
    assert tree.root is not None
    assert tree.root.left is not None
    assert tree.root.left.key == 6
    assert tree.root.left.p is tree.root
    assert tree.root.left.left is not None
    assert tree.root.left.left.key == 2
    assert tree.root.left.right is not None
    assert tree.root.left.right.key == 7


def test_delete_missing_key():
    tree = BinarySearchTree()

    for key in [5, 2, 8]:
        tree.insert(key, str(key))

    assert tree.delete(100) is None

    assert tree.root is not None
    assert tree.root.key == 5


def test_delete_all_nodes():
    tree = BinarySearchTree()

    for key in [5, 2, 8, 1, 3, 7, 9]:
        tree.insert(key, str(key))

    for key in [1, 2, 3, 5, 7, 8, 9]:
        tree.delete(key)

    assert tree.root is None
    assert tree.minimum() is None
    assert tree.maximum() is None


def test_deleted_node_is_detached():
    tree = BinarySearchTree()

    for key in [5, 2, 8]:
        tree.insert(key, str(key))

    deleted = tree.delete(2)

    assert deleted is not None
    assert deleted.p is None
    assert deleted.left is None
    assert deleted.right is None


def test_deleted_one_child_node_is_detached():
    tree = BinarySearchTree()

    for key in [5, 2, 1, 8]:
        tree.insert(key, str(key))

    deleted = tree.delete(2)

    assert deleted is not None
    assert deleted.p is None


def test_delete_preserves_inorder_order():
    tree = BinarySearchTree()

    keys = [10, 5, 15, 2, 7, 12, 20, 6, 8]
    for key in keys:
        tree.insert(key, str(key))

    tree.delete(5)
    tree.delete(15)
    tree.delete(10)

    remaining_keys = []

    def collect(node: Node | None) -> None:
        if node is None:
            return
        collect(node.left)
        remaining_keys.append(node.key)
        collect(node.right)

    collect(tree.root)

    assert remaining_keys == [2, 6, 7, 8, 12, 20]
