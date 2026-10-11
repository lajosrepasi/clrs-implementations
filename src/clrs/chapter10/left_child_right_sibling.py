"""
Left-child, right-sibling representation of a general tree.
"""

from __future__ import annotations

from typing import Any

from clrs.chapter10.stack import Stack


class Node:
    """
    A node in a general tree using left-child, right-sibling links.
    """

    def __init__(self, key: Any) -> None:
        """
        Create a tree node with the given key.
        """
        self.key = key
        self.parent: Node | None = None
        self.left_child: Node | None = None
        self.right_sibling: Node | None = None

    def add_child(self, child_node: Node) -> Node:
        """
        Add a node as the last child of this node.
        """
        child_node.parent = self

        if self.left_child is None:
            self.left_child = child_node
        else:
            rightmost_child = self.left_child

            while rightmost_child.right_sibling is not None:
                rightmost_child = rightmost_child.right_sibling

            rightmost_child.right_sibling = child_node

        return child_node

    def add_child_with_key(self, key: Any) -> Node:
        """
        Create and add a child node with the given key.
        """
        return self.add_child(Node(key))

    def walk_dfs(self) -> None:
        """
        Print all keys using a depth-first traversal.
        """
        stack = Stack(1000)

        stack.push(self)

        while not stack.empty():
            n = stack.pop()

            print(n.key)

            child = n.left_child

            while child is not None:
                stack.push(child)
                child = child.right_sibling


def main():
    """
    Create and print a sample general tree.
    """
    t = Node("A")

    # Save the returned nodes to variables
    node_b = t.add_child_with_key("B")
    node_c = t.add_child_with_key("C")
    node_d = t.add_child_with_key("D")

    # Add children directly to those variables!
    node_b.add_child_with_key("2")

    node_c.add_child_with_key("3")
    node_c.add_child_with_key("4")
    node_c.add_child_with_key("5")

    node_d.add_child_with_key("6")

    t.walk_dfs()


if __name__ == "__main__":
    main()
