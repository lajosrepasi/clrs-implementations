"""
Red-black tree implementation.
"""

from __future__ import annotations

from enum import Enum
from typing import Any


class Color(Enum):
    """
    Colors used by red-black tree nodes.
    """

    RED = "RED"
    BLACK = "BLACK"


class Node:
    """
    A node in a red-black tree.
    """

    RED: Color = Color.RED
    BLACK: Color = Color.BLACK

    def __init__(
        self,
        key: Any = None,
        data: Any = None,
        color: Color | None = None,
        tree: RBTree | None = None,
    ) -> None:
        """
        Create a red-black tree node.
        """
        self.key: Any = key
        self.data: Any = data

        self.left: Node | None = None
        self.right: Node | None = None
        self.p: Node | None = None

        if color == None:
            self.color = Node.RED
        else:
            self.color = color

        self.tree: RBTree | None = tree

    def __str__(self) -> str:
        """
        Return a string representation of the node.
        """
        return "[Node] {0}: {1}".format(self.key, self.data)

    def is_nil(self) -> bool:
        """
        Return whether the node is a NIL node.
        """
        return self.data == RBTree.NIL

    def is_not_nil(self) -> bool:
        """
        Return whether the node is not a NIL node.
        """
        return not self.is_nil()

    def search(self, key: Any) -> Node | None:
        """
        Search for a key in the subtree.
        """
        n = self

        while n is not None and n.is_not_nil() and n.key != key:
            if n.key >= key:
                n = n.left
            elif n.key < key:
                n = n.right

        if n is not None and n.is_nil():
            return None

        return n

    def set_left_child(self, node: Node | None) -> None:
        """
        Set the left child of this node.
        """
        self.left = node

        if node is not None:
            node.p = self

    def set_right_child(self, node: Node | None) -> None:
        """
        Set the right child of this node.
        """
        self.right = node

        if node is not None:
            node.p = self

    def replace_child(self, n: Node, new_n: Node) -> None:
        """
        Replace a child of this node.
        """
        if self.right == n:
            self.right = new_n

        if self.left == n:
            self.left = new_n

        if new_n is not None:
            new_n.p = self

    def add_node(self, node: Node) -> None:
        """
        Insert a node into the appropriate subtree.
        """
        curr = self
        prev = None

        while curr is not None and curr.is_not_nil():
            prev = curr
            if curr.key >= node.key:
                curr = curr.left
            else:
                curr = curr.right

        assert prev is not None

        if prev.key >= node.key:
            prev.left = node
        else:
            prev.right = node

        node.p = prev

        assert self.tree is not None

        node.right = self.tree.create_nil_node_with_parent(node)
        node.left = self.tree.create_nil_node_with_parent(node)

        node.color = Node.RED

    def walk_inorder(self) -> None:
        """
        Traverse the subtree in inorder.
        """
        if self.left is not None and self.left.is_not_nil():
            self.left.walk_inorder()

        print(self)

        if self.right is not None and self.right.is_not_nil():
            self.right.walk_inorder()

    def is_root(self) -> bool:
        """
        Return whether this node is the root.
        """
        return self.p is None

    def is_right_child(self) -> bool:
        """
        Return whether this node is the right child of its parent.
        """
        if self.is_root():
            return False

        return self.p is not None and self.p.right == self

    def is_left_child(self) -> bool:
        """
        Return whether this node is the left child of its parent.
        """
        if self.is_root():
            return False

        return self.p is not None and self.p.left == self

    def minimum(self) -> Node:
        """
        Return the minimum node in the subtree.
        """
        if self.left is None or self.left.is_nil():
            return self

        return self.left.minimum()

    def is_red(self) -> bool:
        """
        Return whether this node is red.
        """
        return self.color == Node.RED

    def is_black(self) -> bool:
        """
        Return whether this node is black.
        """
        return self.color == Node.BLACK

    def successor(self) -> Node | None:
        """
        Return the successor of this node.
        """
        if self.right is not None and self.right.is_not_nil():
            return self.right.minimum()
        else:
            p = self.p
            n = self

            while p is not None and n == p.right:
                n, p = p, p.p

            return p


class RBTree:
    """
    A self-balancing binary search tree using red-black properties.
    """

    NIL = "NIL"

    def __init__(self, root: Node | None = None) -> None:
        """
        Create a red-black tree.
        """
        self.root = root

    def walk_inorder(self) -> None:
        """
        Traverse the tree in inorder.
        """
        if self.root is not None:
            self.root.walk_inorder()

    def left_rotate(self, key: Any) -> None:
        """
        Rotate the node with the given key to the left.
        """
        node = self.search(key)

        if node is not None:
            self.left_rotate_node(node)

    def right_rotate(self, key: Any) -> None:
        """
        Rotate the node with the given key to the right.
        """
        node = self.search(key)

        if node is not None:
            self.right_rotate_node(node)

    def right_rotate_node(self, node: Node) -> None:
        """
        Rotate a node to the right.
        """
        left_child = node.left

        if left_child is not None:
            node.set_left_child(left_child.right)

            if node.is_root():
                self.root = left_child
                left_child.p = None
            elif node.p is not None:
                node.p.replace_child(node, left_child)

            left_child.set_right_child(node)

    def left_rotate_node(self, node: Node) -> None:
        """
        Rotate a node to the left.
        """
        right_child = node.right

        if right_child is not None:
            node.set_right_child(right_child.left)

            if node.is_root():
                self.root = right_child
                right_child.p = None
            elif node.p is not None:
                node.p.replace_child(node, right_child)

            right_child.set_left_child(node)

    def create_node(
        self, key: Any, data: Any, tree: RBTree, color: Color | None = Color.BLACK
    ) -> Node:
        new_node = Node(key=key, data=data, tree=tree, color=color)
        return new_node

    def insert(self, key: Any, data: Any) -> None:
        """
        Insert a key-value pair into the tree.
        """
        new_node = self.create_node(key=key, data=data, tree=self)

        if self.root is None:
            self.root = new_node
            self.root.right = self.create_nil_node_with_parent(self.root)
            self.root.left = self.create_nil_node_with_parent(self.root)
        else:
            self.root.add_node(new_node)

        self.rb_insert_fixup(new_node)

    def rb_insert_fixup(self, new_node: Node) -> None:
        """
        Restore red-black properties after insertion.
        """
        current_node = new_node

        while (
            current_node is not None
            and current_node.p is not None
            and current_node.p.is_red()
        ):
            parent = current_node.p
            grand_parent = parent.p
            assert grand_parent is not None

            if parent == grand_parent.left:
                uncle = grand_parent.right

                if uncle is not None and uncle.is_red():
                    parent.color = Node.BLACK
                    uncle.color = Node.BLACK
                    grand_parent.color = Node.RED
                    current_node = grand_parent
                else:
                    if current_node == parent.right:
                        current_node = parent
                        self.left_rotate_node(current_node)
                        parent = current_node.p

                    assert parent is not None
                    assert grand_parent is not None
                    parent.color = Node.BLACK
                    grand_parent.color = Node.RED

                    self.right_rotate_node(grand_parent)

            else:
                uncle = grand_parent.left

                if uncle is not None and uncle.is_red():
                    parent.color = Node.BLACK
                    uncle.color = Node.BLACK
                    grand_parent.color = Node.RED
                    current_node = grand_parent
                else:
                    if current_node == parent.left:
                        current_node = parent
                        self.right_rotate_node(current_node)
                        parent = current_node.p

                    assert parent is not None
                    parent.color = Node.BLACK
                    grand_parent.color = (
                        Node.RED
                    )  # after rotate it is parent right child

                    self.left_rotate_node(grand_parent)

        assert self.root is not None
        self.root.color = Node.BLACK

    def rb_transplant(self, node_to_replace: Node, node_to_insert: Node) -> None:
        """
        Replace one subtree with another.
        """
        if node_to_replace.is_root():
            self.root = node_to_insert
        elif (
            node_to_replace is not None
            and node_to_replace.p is not None
            and node_to_replace.is_left_child()
        ):
            node_to_replace.p.left = node_to_insert
        elif node_to_replace.p is not None:
            node_to_replace.p.right = node_to_insert

        node_to_insert.p = node_to_replace.p

    def search(self, key: Any) -> Node | None:
        """
        Search for a key in the tree.
        """
        if self.root is not None:
            return self.root.search(key)

        return None

    def create_nil_node_with_parent(self, parent: Node | None = None) -> Node:
        """
        Create a black NIL node with the given parent.
        """
        nil_node = self.create_node(
            key=None, data=RBTree.NIL, color=Node.BLACK, tree=self
        )
        nil_node.p = parent

        return nil_node


def main():
    rb_tree = RBTree()

    rb_tree.insert(5, "thing")
    rb_tree.insert(2, "another")
    rb_tree.insert(9, "value")
    rb_tree.insert(19, "value 2")
    rb_tree.insert(21, "value 3")
    rb_tree.insert(1, "another thing")
    rb_tree.insert(3, "another another thing")
    rb_tree.insert(25, "thing thing")

    rb_tree.walk_inorder()

    to_search = 25
    print("\nsearch {0}:".format(to_search))
    print(rb_tree.search(to_search))


if __name__ == "__main__":
    main()
