"""
Order-statistic tree implementation based on a red-black tree.

Supports selecting the i-th smallest element and determining
the rank of a node in O(log n) time.
"""

from __future__ import annotations

from typing import Any, cast

from clrs.chapter13.red_black_tree import Color
from clrs.chapter13.red_black_tree import Node as RBTreeNode
from clrs.chapter13.red_black_tree import RBTree


class Node(RBTreeNode):
    def __init__(
        self,
        key: Any = None,
        data: Any = None,
        color: Color | None = None,
        tree: OrderStatisticTree | None = None,
    ) -> None:
        super().__init__(key, data, color, tree)
        self.size: int = 1

    def __str__(self) -> str:
        return "[Node] {0}: {1}, size: {2}".format(self.key, self.data, self.size)

    def get_ith_element(self, i: int) -> Node:
        """
        Return the i-th smallest node in the subtree.
        """
        my_rank = self.get_my_rank()

        if my_rank == i:
            return self

        if i < my_rank:
            assert isinstance(self.left, Node)
            return self.left.get_ith_element(i)

        assert isinstance(self.right, Node)
        return self.right.get_ith_element(i - my_rank)

    def get_ith_element_it(self, i: int) -> Node:
        """
        Return the i-th smallest node using iteration.
        """
        n = self

        while n is not None and n.is_not_nil():
            assert isinstance(n, Node)
            my_rank = n.get_my_rank()
            if my_rank == i:
                return n

            if i < my_rank:
                n = n.left
            else:
                n = n.right
                i -= my_rank

        assert isinstance(n, Node)
        return n

    def get_my_rank(self) -> int:
        """
        Return this node's rank within its own subtree.
        """
        my_rank = 0

        assert isinstance(self.left, Node)
        if self.left.is_nil():
            my_rank = 1
        else:
            my_rank = self.left.size + 1

        return my_rank

    def get_node_rank(self, node: Node, rank_adjust: int) -> int:
        """
        Return the rank of a node within this subtree.
        """
        my_rank = self.get_my_rank()

        if node == self:
            return rank_adjust + my_rank

        if self.key > node.key:
            assert isinstance(self.left, Node)
            return self.left.get_node_rank(node, rank_adjust)

        assert isinstance(self.right, Node)
        return self.right.get_node_rank(node, rank_adjust + my_rank)

    def get_node_rank_it(self) -> int:
        my_rank = self.get_my_rank()
        n = self

        assert isinstance(n, Node)
        while n is not None and not n.is_root():
            if n.is_right_child():
                assert n.p is not None
                assert isinstance(n.p.left, Node)
                my_rank += n.p.left.size + 1
            n = n.p

        return my_rank


class OrderStatisticTree(RBTree):

    def __init__(self, root: Node | None = None) -> None:
        super().__init__(root)

    def create_node(
        self, key: Any, data: Any, tree: RBTree, color: Color | None = Color.BLACK
    ) -> Node:
        assert isinstance(tree, OrderStatisticTree)
        new_node = Node(key=key, data=data, tree=tree)
        return new_node

    def create_nil_node_with_parent(self, parent=None) -> Node:
        """
        Create a black NIL node with the given parent.
        """
        nil_node = self.create_node(
            key=None, data=RBTree.NIL, color=Node.BLACK, tree=self
        )
        nil_node.p = parent
        nil_node.size = 0

        return nil_node

    def rb_insert_fixup(self, new_node) -> None:
        p = new_node.p

        while p is not None:
            assert isinstance(p, Node)
            p.size += 1
            p = p.p

        super().rb_insert_fixup(new_node)

    def right_rotate_node(self, node) -> None:
        super().right_rotate_node(node)

        assert isinstance(node, Node)

        if node.p is not None:
            assert isinstance(node.p, Node)
            node.p.size = node.size

        node.size = 1

        assert isinstance(node.right, Node)
        if node.right.is_not_nil():
            node.size += node.right.size

        assert isinstance(node.left, Node)
        if node.left.is_not_nil():
            node.size += node.left.size

    def left_rotate_node(self, node) -> None:
        super().left_rotate_node(node)

        assert isinstance(node, Node)
        if node.p is not None:

            assert isinstance(node.p, Node)
            node.p.size = node.size

        node.size = 1

        assert isinstance(node.right, Node)
        if node.right.is_not_nil():
            node.size += node.right.size

        assert isinstance(node.left, Node)
        if node.left.is_not_nil():
            node.size += node.left.size

    def get_ith_element(self, i: int) -> Node | None:
        """
        Return the i-th smallest node in the tree.
        """

        if self.root is not None:
            assert isinstance(self.root, Node)
            if i > self.root.size:
                return None

            return self.root.get_ith_element(i)

        return None

    def get_ith_element_it(self, i: int) -> Node | None:

        if self.root is not None:
            assert isinstance(self.root, Node)
            if i > self.root.size:
                return None

            return self.root.get_ith_element_it(i)

        return None

    def get_rank(self, key: Any) -> int | None:
        """
        Return the rank of the node with the given key.
        """
        node = self.search(key)

        assert isinstance(node, Node)
        if node is not None:
            return self.get_node_rank(node)

        return None

    def get_node_rank(self, node: Node) -> int:
        """
        Return the rank of this node in the tree.
        """
        assert isinstance(self.root, Node)
        return self.root.get_node_rank(node, 0)


def main():
    ost = OrderStatisticTree()

    ost.insert(5, "thing")
    ost.insert(2, "bthing")
    ost.insert(9, "another")
    ost.insert(19, "another 2")
    ost.insert(21, "max another")
    ost.insert(1, "min another")
    ost.insert(3, "something")
    ost.insert(25, "tu max another to delete")

    ost.walk_inorder()

    print("\nOrder statistics:")
    print("1st: ", ost.get_ith_element(1))
    print("4th: ", ost.get_ith_element(4))
    print("7th: ", ost.get_ith_element(7))
    print("8th: ", ost.get_ith_element(8))

    print("\nOrder statistics iterative:")
    print("1st: ", ost.get_ith_element_it(1))
    print("4th: ", ost.get_ith_element_it(4))
    print("7th: ", ost.get_ith_element_it(7))
    print("8th: ", ost.get_ith_element_it(8))

    print("\nGet rank of node:")
    print("Rank of node with key 19: ", ost.get_rank(19))
    print("Rank of node with key 5: ", ost.get_rank(5))
    print("Rank of node with key 3: ", ost.get_rank(3))

    print("\nGet rank of node iterative:")
    print(
        "Rank of node with key 19: ",
        cast(Node, ost.search(19)).get_node_rank_it(),
    )
    print("Rank of node with key 5: ", cast(Node, ost.search(5)).get_node_rank_it())
    print("Rank of node with key 3: ", cast(Node, ost.search(3)).get_node_rank_it())


if __name__ == "__main__":
    main()
