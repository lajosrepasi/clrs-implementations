"""
Binary search tree implementation.
"""

from __future__ import annotations

from typing import Any


class Node:
    """
    A node in a binary search tree.
    """

    def __init__(
        self,
        key: Any = None,
        data: Any = None,
        left: Node | None = None,
        right: Node | None = None,
        p: Node | None = None,
    ) -> None:
        """
        Create a binary search tree node.
        """

        self.left: Node | None = left
        self.right: Node | None = right
        self.p: Node | None = p

        self.key: Any = key
        self.data: Any = data

    def add_node(self, node: Node) -> None:
        """
        Insert a node into the appropriate subtree.
        """

        if node.key <= self.key:
            self.add_node_to_left_subtree(node)
        else:
            self.add_node_to_right_subtree(node)

    def add_node_to_left_subtree(self, node: Node) -> None:
        """
        Insert a node into the left subtree.
        """

        if self.left is None:
            self.set_left_node(node)
        else:
            self.left.add_node(node)

    def add_node_to_right_subtree(self, node: Node) -> None:
        """
        Insert a node into the right subtree.
        """

        if self.right is None:
            self.set_right_node(node)
        else:
            self.right.add_node(node)

    def set_left_node(self, node: Node) -> None:
        """
        Set the left child of this node.
        """

        self.left = node
        node.p = self

    def set_right_node(self, node: Node) -> None:
        """
        Set the right child of this node.
        """

        self.right = node
        node.p = self

    def walk_inorder(self) -> None:
        """
        Traverse the subtree in inorder.
        """

        if self.left is not None:
            self.left.walk_inorder()

        print("[{0}: {1}]".format(self.key, self.data))

        if self.right is not None:
            self.right.walk_inorder()

    def walk_preorder(self) -> None:
        """
        Traverse the subtree in preorder.
        """

        print("[{0}: {1}]".format(self.key, self.data))

        if self.left is not None:
            self.left.walk_preorder()

        if self.right is not None:
            self.right.walk_preorder()

    def walk_postorder(self) -> None:
        """
        Traverse the subtree in postorder.
        """

        if self.left is not None:
            self.left.walk_postorder()

        if self.right is not None:
            self.right.walk_postorder()

        print(str(self))

    def search(self, key: Any) -> Node | None:
        """
        Recursively search for a key in the subtree.
        """

        if key == self.key:
            return self
        elif key <= self.key and self.left is not None:
            return self.left.search(key)
        elif key > self.key and self.right is not None:
            return self.right.search(key)

        return None

    def minimum_recursive(self) -> Node:
        """
        Return the minimum node in the subtree.
        """

        if self.left is None:
            return self

        return self.left.minimum_recursive()

    def maximum_recursive(self) -> Node:
        """
        Return the maximum node in the subtree.
        """

        if self.right is None:
            return self

        return self.right.maximum_recursive()

    def successor(self) -> Node | None:
        """
        Return the successor of this node.
        """

        if self.right is not None:
            return self.right.minimum_recursive()
        else:
            p = self.p
            n = self

            while p is not None and n == p.right:
                n, p = p, p.p

            return p

    def predecessor(self) -> Node | None:
        """
        Return the predecessor of this node.
        """

        if self.left is not None:
            return self.left.maximum_recursive()
        else:
            p = self.p
            n = self

            while p is not None and n == p.left:
                n, p = p, p.p

            return p

    def delete_child(self, n: Node) -> None:
        """
        Remove a child from this node.
        """

        if self.right is n:
            self.right = None

        if self.left is n:
            self.left = None

    def replace_child(self, n: Node, new_n: Node | None) -> None:
        """
        Replace a child of this node.
        """

        if self.right is n:
            self.right = new_n

        if self.left is n:
            self.left = new_n

        if new_n is not None:
            new_n.p = self
        n.p = None

    def __str__(self) -> str:
        """
        Return a string representation of the node.
        """

        return "[{0}: {1}]".format(self.key, self.data)


class BinarySearchTree:
    """
    A binary search tree.
    """

    def __init__(self, root: Node | None = None) -> None:
        """
        Create a binary search tree.
        """

        self.root = root

    def insert(self, key: Any, data: Any) -> None:
        """
        Insert a key-value pair into the tree.
        """

        new_node = Node(key=key, data=data)

        if self.root is None:
            self.root = new_node
        else:
            self.root.add_node(new_node)

    def walk_inorder(self) -> None:
        """
        Traverse the tree in inorder.
        """

        if self.root is not None:
            self.root.walk_inorder()

    def walk_preorder(self) -> None:
        """
        Traverse the tree in preorder.
        """

        if self.root is not None:
            self.root.walk_preorder()

    def walk_postorder(self) -> None:
        """
        Traverse the tree in postorder.
        """

        if self.root is not None:
            self.root.walk_postorder()

    def search(self, key: Any) -> Node | None:
        """
        Recursively search for a key.
        """

        if self.root is not None:
            return self.root.search(key)

        return None

    def delete(self, key: Any) -> Node | None:
        """
        Delete a node with no children.
        """

        n = self.search(key)

        if n is None:
            return

        no_children = n.right is None and n.left is None
        if no_children:
            return self.delete_without_child(n)

        one_child = (int(n.right is not None) + int(n.left is not None)) == 1
        if one_child:
            return self.delete_with_one_child(n)

        return self.delete_with_two_children(n)

    def delete_without_child(self, n: Node) -> Node:
        """
        Delete a node with no children.
        """

        p = n.p

        if p is None:
            self.root = None
        else:
            n.p = None
            p.delete_child(n)

        return n

    def delete_with_one_child(self, n: Node) -> Node:
        """
        Delete a node with one child.
        """

        child = n.left if n.left is not None else n.right

        if n.p is None:
            self.root = child
            if child is not None:
                child.p = None
        elif child is not None:
            n.p.replace_child(n, child)

        return n

    def delete_with_two_children(self, n: Node) -> Node:
        """
        Delete a node with two children.
        """

        p = n.p
        successor = n.successor()

        assert successor is not None
        p_successor = successor.p
        successor_right = successor.right

        assert p_successor is not None

        if n == self.root:
            self.root = successor
            successor.p = None

            if successor != n.right:
                p_successor.replace_child(successor, successor_right)
                successor.right = n.right
                if successor.right is not None:
                    successor.right.p = successor

            successor.left = n.left
            assert successor.left is not None
            successor.left.p = successor
        else:
            if successor != n.right:
                p_successor.replace_child(successor, successor_right)
                successor.right = n.right
                if successor.right is not None:
                    successor.right.p = successor

            assert p is not None
            p.replace_child(n, successor)

            successor.left = n.left
            if successor.left is not None:
                successor.left.p = successor

        return n

    def successor(self, key: Any) -> Node | None:
        """
        Return the successor of a key.
        """

        n = self.search(key)

        if n is not None:
            return n.successor()

    def predecessor(self, key: Any) -> Node | None:
        """
        Return the predecessor of a key.
        """

        n = self.search(key)

        if n is not None:
            return n.predecessor()

    def search_iter(self, key: Any) -> Node | None:
        """
        Iteratively search for a key.
        """

        n = self.root

        while n is not None and n.key != key:
            if n.key >= key:
                n = n.left
            elif n.key < key:
                n = n.right

        return n

    def minimum(self) -> Node | None:
        """
        Return the minimum node in the tree.
        """

        l = self.root

        while l is not None and l.left is not None:
            l = l.left

        return l

    def maximum(self) -> Node | None:
        """
        Return the maximum node in the tree.
        """

        r = self.root

        while r is not None and r.right is not None:
            r = r.right

        return r


def main():
    binary_search_tree = BinarySearchTree()

    binary_search_tree.insert(5, "thing")
    binary_search_tree.insert(2, "bthing")
    binary_search_tree.insert(9, "another")
    binary_search_tree.insert(19, "1 another")
    binary_search_tree.insert(21, "1 max another")
    binary_search_tree.insert(1, "1 min another")
    binary_search_tree.insert(3, "foo")
    binary_search_tree.insert(25, "1 max another to delete")

    to_delete = 25
    print("\nsearch {0}".format(to_delete))
    print(binary_search_tree.search(to_delete))
    print("delete {0}".format(to_delete))
    binary_search_tree.delete(to_delete)
    print("search {0}".format(to_delete))
    print(binary_search_tree.search(to_delete))

    to_delete = 19
    print("\nsearch {0}".format(to_delete))
    print(binary_search_tree.search(to_delete))
    print("delete {0}".format(to_delete))
    binary_search_tree.delete(to_delete)
    print("search {0}".format(to_delete))
    print(binary_search_tree.search(to_delete))

    to_delete = 5
    print("\nsearch {0}".format(to_delete))
    print(binary_search_tree.search(to_delete))
    print("delete {0}".format(to_delete))
    binary_search_tree.delete(to_delete)
    print("search {0}".format(to_delete))
    print(binary_search_tree.search(to_delete))

    s = 9
    print("\nsuccessor of {0}".format(s))
    print(binary_search_tree.successor(s))

    p = 9
    print("\npredecessor of {0}".format(p))
    print(binary_search_tree.predecessor(p))

    print("\nin roder:")
    binary_search_tree.walk_inorder()
    print("\npre roder:")
    binary_search_tree.walk_preorder()
    print("\npost order:")
    binary_search_tree.walk_postorder()

    print("\nsearch 19:")
    print(binary_search_tree.search(19))

    print("\nsearch 19 iter:")
    print(binary_search_tree.search_iter(19))

    print("\nsearch 1900:")
    print(binary_search_tree.search(1900))

    print("\nminimum:")
    print(binary_search_tree.minimum())

    print("\nminimum recursive:")
    assert binary_search_tree.root is not None
    print(binary_search_tree.root.minimum_recursive())

    print("\nmaximum:")
    print(binary_search_tree.maximum())

    print("\nmaximum recursive:")
    print(binary_search_tree.root.maximum_recursive())


if __name__ == "__main__":
    main()
