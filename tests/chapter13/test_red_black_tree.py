from clrs.chapter13.red_black_tree import Color, Node, RBTree


def test_node_creation():
    node = Node(10, "value")

    assert node.key == 10
    assert node.data == "value"
    assert node.left is None
    assert node.right is None
    assert node.p is None
    assert node.color == Node.RED


def test_node_with_explicit_color():
    node = Node(10, "value", color=Node.BLACK)

    assert node.color == Node.BLACK
    assert node.is_black()
    assert not node.is_red()


def test_color_enum():
    assert Color.RED.value == "RED"
    assert Color.BLACK.value == "BLACK"


def test_nil_node():
    tree = RBTree()

    nil = tree.create_nil_node_with_parent()

    assert nil.is_nil()
    assert nil.is_not_nil() is False
    assert nil.color == Node.BLACK
    assert nil.key is None
    assert nil.data == RBTree.NIL
    assert nil.p is None


def test_nil_node_has_parent():
    tree = RBTree()
    parent = Node(10)

    nil = tree.create_nil_node_with_parent(parent)

    assert nil.is_nil()
    assert nil.p is parent
    assert nil.is_black()


def test_insert_first_node():
    tree = RBTree()

    tree.insert(10, "ten")

    assert tree.root is not None
    assert tree.root.key == 10
    assert tree.root.data == "ten"
    assert tree.root.p is None
    assert tree.root.is_black()


def test_insert_creates_nil_children():
    tree = RBTree()

    tree.insert(10, "ten")

    assert tree.root is not None
    assert tree.root.left is not None
    assert tree.root.right is not None

    assert tree.root.left.is_nil()
    assert tree.root.right.is_nil()

    assert tree.root.left.is_black()
    assert tree.root.right.is_black()

    assert tree.root.left.p is tree.root
    assert tree.root.right.p is tree.root


def test_insert_left_child():
    tree = RBTree()

    tree.insert(10, "ten")
    tree.insert(5, "five")

    assert tree.root is not None
    assert tree.root.left is not None

    assert tree.root.left.key == 5
    assert tree.root.left.data == "five"
    assert tree.root.left.p is tree.root


def test_insert_right_child():
    tree = RBTree()

    tree.insert(10, "ten")
    tree.insert(15, "fifteen")

    assert tree.root is not None
    assert tree.root.right is not None

    assert tree.root.right.key == 15
    assert tree.root.right.data == "fifteen"
    assert tree.root.right.p is tree.root


def test_insert_duplicate_goes_left():
    tree = RBTree()

    tree.insert(10, "first")
    tree.insert(10, "second")

    assert tree.root is not None
    assert tree.root.left is not None

    assert tree.root.left.key == 10
    assert tree.root.left.data == "second"


def test_search():
    tree = RBTree()

    for key in [5, 2, 8]:
        tree.insert(key, str(key))

    node = tree.search(8)

    assert node is not None
    assert node.key == 8
    assert node.data == "8"


def test_search_missing_key():
    tree = RBTree()

    for key in [5, 2, 8]:
        tree.insert(key, str(key))

    assert tree.search(10) is None


def test_search_empty_tree():
    tree = RBTree()

    assert tree.search(10) is None


def test_search_does_not_return_nil_node():
    tree = RBTree()

    tree.insert(5, "five")

    result = tree.search(10)

    assert result is None


def test_is_root():
    tree = RBTree()

    tree.insert(10, "ten")

    assert tree.root is not None
    assert tree.root.is_root()


def test_is_left_child():
    tree = RBTree()

    tree.insert(10, "ten")
    tree.insert(5, "five")

    assert tree.root is not None
    assert tree.root.left is not None

    assert tree.root.left.is_left_child()
    assert not tree.root.left.is_right_child()


def test_is_right_child():
    tree = RBTree()

    tree.insert(10, "ten")
    tree.insert(15, "fifteen")

    assert tree.root is not None
    assert tree.root.right is not None

    assert tree.root.right.is_right_child()
    assert not tree.root.right.is_left_child()


def test_root_is_neither_left_nor_right_child():
    tree = RBTree()

    tree.insert(10, "ten")

    assert tree.root is not None
    assert tree.root.is_root()
    assert not tree.root.is_left_child()
    assert not tree.root.is_right_child()


def test_left_rotate():
    tree = RBTree()

    tree.insert(10, "ten")
    tree.insert(20, "twenty")

    tree.left_rotate(10)

    assert tree.root is not None
    assert tree.root.key == 20
    assert tree.root.p is None

    assert tree.root.left is not None
    assert tree.root.left.key == 10
    assert tree.root.left.p is tree.root


def test_left_rotate_preserves_nil_child():
    tree = RBTree()

    tree.insert(10, "ten")
    tree.insert(20, "twenty")

    tree.left_rotate(10)

    assert tree.root is not None
    assert tree.root.left is not None
    assert tree.root.left.key == 10

    assert tree.root.left.right is not None
    assert tree.root.left.right.is_nil()
    assert tree.root.left.right.p is tree.root.left


def test_right_rotate():
    tree = RBTree()

    tree.insert(20, "twenty")
    tree.insert(10, "ten")

    tree.right_rotate(20)

    assert tree.root is not None
    assert tree.root.key == 10
    assert tree.root.p is None

    assert tree.root.right is not None
    assert tree.root.right.key == 20
    assert tree.root.right.p is tree.root


def assert_red_black_properties(tree: RBTree) -> None:
    assert tree.root is not None
    assert tree.root.is_black()

    def check(node: Node) -> int:
        assert node.is_red() or node.is_black()

        if node.is_nil():
            assert node.is_black()
            return 1

        assert node.left is not None
        assert node.right is not None

        if node.is_red():
            assert (
                node.left.is_black()
            ), f"Red node {node.key} has red left child {node.left.key}"
            assert (
                node.right.is_black()
            ), f"Red node {node.key} has red right child {node.right.key}"

        left_black_height = check(node.left)
        right_black_height = check(node.right)

        assert left_black_height == right_black_height, (
            f"Black-height mismatch at node {node.key}: "
            f"{left_black_height} != {right_black_height}"
        )

        return left_black_height + int(node.is_black())

    check(tree.root)


def test_insert_preserves_red_black_properties():
    tree = RBTree()

    for key in [5, 2, 8, 1, 3, 7, 9, 19, 21, 25]:
        tree.insert(key, str(key))
        assert_red_black_properties(tree)


def test_insert_causes_left_rotation():
    tree = RBTree()

    tree.insert(10, "10")
    tree.insert(20, "20")
    tree.insert(30, "30")

    assert tree.root is not None
    assert tree.root.key == 20

    assert tree.root.left is not None
    assert tree.root.left.key == 10

    assert tree.root.right is not None
    assert tree.root.right.key == 30

    assert_red_black_properties(tree)


def test_insert_causes_right_rotation():
    tree = RBTree()

    tree.insert(30, "30")
    tree.insert(20, "20")
    tree.insert(10, "10")

    assert tree.root is not None
    assert tree.root.key == 20

    assert tree.root.left is not None
    assert tree.root.left.key == 10

    assert tree.root.right is not None
    assert tree.root.right.key == 30

    assert_red_black_properties(tree)


def test_insert_causes_recoloring():
    tree = RBTree()

    for key in [10, 5, 15, 1]:
        tree.insert(key, str(key))

    assert tree.root is not None
    assert tree.root.key == 10
    assert tree.root.is_black()

    assert tree.root.left is not None
    assert tree.root.right is not None

    assert tree.root.left.is_black()
    assert tree.root.right.is_black()

    assert_red_black_properties(tree)
