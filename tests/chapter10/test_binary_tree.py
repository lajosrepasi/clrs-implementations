from clrs.chapter10.binary_tree import Node, create_binary_tree


def test_node_creation():
    node = Node(10)

    assert node.value == 10
    assert node.parent is None
    assert node.left is None
    assert node.right is None


def test_set_left():
    parent = Node(10)
    child = Node(5)

    parent.set_left(child)

    assert parent.left == child
    assert child.parent == parent


def test_set_right():
    parent = Node(10)
    child = Node(20)

    parent.set_right(child)

    assert parent.right == child
    assert child.parent == parent


def test_parent_chain():
    root = Node(1)
    left = Node(2)
    grandchild = Node(3)

    root.set_left(left)
    left.set_left(grandchild)

    assert grandchild.parent == left
    if grandchild.parent is not None:
        assert grandchild.parent.parent == root


def test_create_binary_tree_root():
    root = create_binary_tree()

    assert root.value == 15


def test_create_binary_tree_children():
    root = create_binary_tree()

    assert root.left is not None
    assert root.right is not None

    assert root.left.value == 17
    assert root.right.value == 20


def test_create_binary_tree_parent_links():
    root = create_binary_tree()

    assert root.left is not None
    assert root.right is not None

    assert root.left.parent == root
    assert root.right.parent == root


def test_create_binary_tree_deep_node():
    root = create_binary_tree()

    assert root.left is not None
    assert root.left.right is not None
    assert root.left.right.left is not None

    assert root.left.right.left.value == 12


def test_leaf_nodes_have_no_children():
    root = create_binary_tree()

    assert root.left is not None
    assert root.left.right is not None
    leaf = root.left.right.left

    assert leaf is not None
    assert leaf.left is None
    assert leaf.right is None


def test_inorder_traversal(capsys):
    root = Node(2)

    root.set_left(Node(1))
    root.set_right(Node(3))

    root.walk_inorder()

    captured = capsys.readouterr()

    assert captured.out.splitlines() == ["1", "2", "3"]
