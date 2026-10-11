"""
Exercise 10.3-2
"""

from clrs.chapter10.binary_tree import Node, create_binary_tree


def traverse_recursive(root: Node):

    print(root.value)

    if root.left != None:
        traverse_recursive(root.left)

    if root.right != None:
        traverse_recursive(root.right)


def main():
    root = create_binary_tree()

    traverse_recursive(root)


if __name__ == "__main__":
    main()
