"""
Binary tree node implementation and traversal utilities.
"""

from __future__ import annotations

from typing import Any

from clrs.chapter10.my_queue import Queue


class Node:
    """
    A node in a binary tree.
    """

    def __init__(self, value: Any) -> None:
        """
        Create a tree node.
        """
        self.value: Any = value

        self.parent: Node | None = None
        self.left: Node | None = None
        self.right: Node | None = None

    def set_left(self, node: Node) -> None:
        """
        Set the left child of this node.
        """
        self.left = node
        node.set_parent(self)

    def set_right(self, node: Node) -> None:
        """
        Set the right child of this node.
        """
        self.right = node
        node.set_parent(self)

    def set_parent(self, parent: Node) -> None:
        """
        Set the parent of this node.
        """
        self.parent = parent

    def walk_inorder(self) -> None:
        """
        Print the tree using inorder traversal.
        """
        if self.left is not None:
            self.left.walk_inorder()

        print(self.value)

        if self.right is not None:
            self.right.walk_inorder()

    def print(self, printer=None) -> None:
        """
        Print the tree level by level.
        """
        if printer is None:
            printer = lambda n: n.value

        NEXT_LEVEL = "NL"
        MAX_PADDING = 7
        EMPTY_NODE = "EMPT"

        queue = Queue(100)

        queue.enqueue(self)
        queue.enqueue(NEXT_LEVEL)
        level_count = 1
        node_count = 1

        while node_count > 0:
            level = "_" * (MAX_PADDING - level_count + 1)

            next_node_to_print = queue.dequeue()

            while next_node_to_print != NEXT_LEVEL:
                if next_node_to_print != EMPTY_NODE:
                    node_count -= 1
                    level += "__{0}({1}{2})__".format(
                        printer(next_node_to_print),
                        (
                            printer(next_node_to_print.parent)
                            if next_node_to_print.parent is not None
                            else "root"
                        ),
                        (
                            (
                                "L"
                                if next_node_to_print.parent.left == next_node_to_print
                                else "R"
                            )
                            if next_node_to_print.parent is not None
                            else ""
                        ),
                    )

                    if next_node_to_print.left is not None:
                        queue.enqueue(next_node_to_print.left)
                        node_count += 1
                    else:
                        queue.enqueue(EMPTY_NODE)

                    if next_node_to_print.right is not None:
                        queue.enqueue(next_node_to_print.right)
                        node_count += 1
                    else:
                        queue.enqueue(EMPTY_NODE)

                else:
                    level += "__"
                    queue.enqueue(EMPTY_NODE)
                    queue.enqueue(EMPTY_NODE)

                next_node_to_print = queue.dequeue()

            print(level)

            queue.enqueue(NEXT_LEVEL)
            level_count += 1


def create_binary_tree() -> Node:
    """
    Create a sample binary tree.
    """
    root = Node(15)

    node17 = Node(17)
    root.set_left(node17)
    node20 = Node(20)
    root.set_right(node20)

    node22 = Node(22)
    node17.set_left(node22)
    node13 = Node(13)
    node17.set_right(node13)

    node25 = Node(25)
    node20.set_left(node25)

    node12 = Node(12)
    node13.set_left(node12)
    node28 = Node(28)
    node13.set_right(node28)

    node33 = Node(33)
    node25.set_left(node33)

    node14 = Node(14)
    node33.set_left(node14)

    return root


def main():
    tree = create_binary_tree()

    tree.print()


if __name__ == "__main__":
    main()
