"""
Exercise 10.3-3
"""

from clrs.chapter10.binary_tree import Node, create_binary_tree
from clrs.chapter10.stack import Stack


def traverse_iterative(root: Node):
    stack = Stack(100)

    stack.push(root)

    while not stack.empty():
        node = stack.pop()
        print(node.value)

        if node.right != None:
            stack.push(node.right)

        if node.left != None:
            stack.push(node.left)


def main():
    root = create_binary_tree()

    traverse_iterative(root)


if __name__ == "__main__":
    main()
