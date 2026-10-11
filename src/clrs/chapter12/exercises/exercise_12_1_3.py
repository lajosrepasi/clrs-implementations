"""
Exercise 12.1-3
"""

from clrs.chapter10.stack import Stack
from clrs.chapter12.binary_search_tree import BinarySearchTree


def walk_inorder_iter(binary_search_tree: BinarySearchTree) -> None:
    stack = Stack(100)

    n = binary_search_tree.root

    while n != None or not stack.empty():
        while n != None:
            stack.push(n)
            n = n.left

        n = stack.pop()
        print(n)
        n = n.right


def main():
    binary_search_tree = BinarySearchTree()

    binary_search_tree.insert(5, "thing")
    binary_search_tree.insert(2, "value")
    binary_search_tree.insert(29, "another thing")
    binary_search_tree.insert(9, "another")
    binary_search_tree.insert(19, "value2")

    walk_inorder_iter(binary_search_tree)


if __name__ == "__main__":
    main()
