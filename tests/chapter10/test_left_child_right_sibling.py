from clrs.chapter10.left_child_right_sibling import Node


def test_node_creation():
    node = Node("A")

    assert node.key == "A"
    assert node.parent is None
    assert node.left_child is None
    assert node.right_sibling is None


def test_add_first_child():
    parent = Node("A")
    child = Node("B")

    returned = parent.add_child(child)

    assert returned is child
    assert parent.left_child is child
    assert child.parent is parent
    assert child.right_sibling is None


def test_add_multiple_children():
    parent = Node("A")

    child_b = parent.add_child_with_key("B")
    child_c = parent.add_child_with_key("C")
    child_d = parent.add_child_with_key("D")

    assert parent.left_child is child_b
    assert child_b.right_sibling is child_c
    assert child_c.right_sibling is child_d
    assert child_d.right_sibling is None


def test_add_children_sets_parent():
    parent = Node("A")

    child_b = parent.add_child_with_key("B")
    child_c = parent.add_child_with_key("C")
    child_d = parent.add_child_with_key("D")

    assert child_b.parent is parent
    assert child_c.parent is parent
    assert child_d.parent is parent


def test_add_child_with_key():
    parent = Node("A")

    child = parent.add_child_with_key("B")

    assert child.key == "B"
    assert child.parent is parent
    assert parent.left_child is child


def test_add_grandchildren():
    root = Node("A")

    child_b = root.add_child_with_key("B")
    child_c = root.add_child_with_key("C")

    grandchild_2 = child_b.add_child_with_key("2")
    grandchild_3 = child_c.add_child_with_key("3")

    assert grandchild_2.parent is child_b
    assert grandchild_3.parent is child_c

    assert child_b.left_child is grandchild_2
    assert child_c.left_child is grandchild_3


def test_sibling_chain_is_preserved():
    root = Node("A")

    child_b = root.add_child_with_key("B")
    child_c = root.add_child_with_key("C")
    child_d = root.add_child_with_key("D")

    assert root.left_child is child_b
    assert child_b.right_sibling is child_c
    assert child_c.right_sibling is child_d
    assert child_d.right_sibling is None


def test_walk_dfs(capsys):
    root = Node("A")

    child_b = root.add_child_with_key("B")
    child_c = root.add_child_with_key("C")

    child_b.add_child_with_key("2")
    child_c.add_child_with_key("3")
    child_c.add_child_with_key("4")

    root.walk_dfs()

    captured = capsys.readouterr()

    assert captured.out.splitlines() == [
        "A",
        "C",
        "4",
        "3",
        "B",
        "2",
    ]
