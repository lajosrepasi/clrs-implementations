"""
Circular queue implementation based on the queue data structure.
"""

from typing import Any


class Queue:
    """
    A bounded circular queue with FIFO semantics.
    """

    def __init__(self, size: int | None = None) -> None:
        """
        Create an empty queue with the given maximum capacity.
        """
        if size is None:
            queue_size = 100
        else:
            queue_size = size

        if queue_size <= 0:
            raise ValueError("size must be positive")

        self.size = queue_size
        self.queue: list[Any]
        self.head: int
        self.tail: int

        self.reset()

    def reset(self) -> None:
        """
        Reset the queue to an empty state.
        """

        self.queue = [None] * (self.size + 1)

        self.head = 0
        self.tail = 0

    def empty(self) -> bool:
        """
        Return True if the queue contains no elements.
        """

        return self.head == self.tail

    def enqueue(self, item: Any) -> None:
        """
        Add an item to the end of the queue.
        """

        if (self.head == 0 and self.tail == self.size) or (self.tail + 1 == self.head):
            raise OverflowError("queue overflow")

        self.queue[self.tail] = item

        if self.tail == self.size:
            self.tail = 0
        else:
            self.tail += 1

    def dequeue(self) -> Any:
        """
        Remove and return the item at the front of the queue.
        """

        if self.empty():
            raise IndexError("queue underflow")

        item = self.queue[self.head]

        if self.head == self.size:
            self.head = 0
        else:
            self.head += 1

        return item


def main():
    queue = Queue(6)

    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)
    queue.enqueue(6)

    while not queue.empty():
        print(queue.dequeue())

    queue.enqueue("a")
    queue.enqueue("b")
    queue.dequeue()
    queue.enqueue("c")

    while not queue.empty():
        print(queue.dequeue())


if __name__ == "__main__":
    main()
