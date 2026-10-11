"""
Exercise 10.2-2

Stack implementation using a doubly linked list.
"""

from typing import Any

from clrs.chapter10.linked_list import Item, LinkedList


class StackWithLinkedList:
    """
    Stack implementation backed by a linked list.

    Push and pop both run in O(1) time.
    """

    def __init__(self) -> None:
        self.linked_list = LinkedList()

    def push(self, item: Any) -> None:
        self.linked_list.append(Item("", item))

    def pop(self) -> Any:
        item = self.linked_list.tail

        if item is None:
            raise Exception("underflow")

        self.linked_list.delete(item)

        return item.value


def main():
    stack = StackWithLinkedList()

    stack.push("a")
    stack.push("b")
    stack.push("c")

    print(stack.pop())
    print(stack.pop())
    print(stack.pop())


if __name__ == "__main__":
    main()
