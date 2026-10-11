"""
Exercise 10.2-3

Queue implementation using a doubly linked list.
"""

from typing import Any

from clrs.chapter10.linked_list import Item, LinkedList


class QueueWithLinkedList:
    """
    Queue implementation backed by a linked list.

    Enqueue and dequeue both run in O(1) time.
    """

    def __init__(self) -> None:
        self.linked_list = LinkedList()

    def enqueue(self, item: Any) -> None:
        self.linked_list.append(Item("", item))

    def dequeue(self) -> Any:
        item = self.linked_list.head

        if item is None:
            raise Exception("underflow")

        self.linked_list.delete(item)

        return item.value


def main():
    queue = QueueWithLinkedList()

    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)

    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())


if __name__ == "__main__":
    main()
