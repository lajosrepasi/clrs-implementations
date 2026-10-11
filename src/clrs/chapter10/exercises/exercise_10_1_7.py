"""
Exercise 10.1-7

Queue implementation using two stacks.
"""

from typing import Any

from clrs.chapter10.stack import Stack


class QueueWithTwoStacks:
    """
    Queue implemented with two stacks.

    Elements are moved between stacks whenever the
    active stack changes.
    """

    def __init__(self, size: int) -> None:
        self.stack1 = Stack(size)
        self.stack2 = Stack(size)

        self.using_stack1 = True

    def enqueue(self, item: Any) -> None:
        if self.using_stack1:
            self.stack1.push(item)
        else:
            while not self.stack2.empty():
                self.stack1.push(self.stack2.pop())
            self.stack1.push(item)
            self.using_stack1 = True

    def dequeue(self) -> Any:
        if self.using_stack1:
            while not self.stack1.empty():
                self.stack2.push(self.stack1.pop())
            self.using_stack1 = False
            return self.stack2.pop()
        else:
            return self.stack2.pop()


class QueueWithTwoStacks2:
    """
    Queue implemented with two stacks using the
    standard amortized O(1) approach.
    """

    def __init__(self, size: int) -> None:
        self.stack1 = Stack(size)
        self.stack2 = Stack(size)

    def enqueue(self, item: Any) -> None:
        self.stack1.push(item)

    def dequeue(self) -> Any:
        if self.stack2.empty():
            while not self.stack1.empty():
                self.stack2.push(self.stack1.pop())

        return self.stack2.pop()


def main():
    queue = QueueWithTwoStacks(100)

    queue.enqueue(1)
    queue.enqueue(2)
    print(queue.dequeue())
    print(queue.dequeue())
    queue.enqueue(3)
    queue.enqueue(4)

    print(queue.dequeue())
    print(queue.dequeue())

    print("------------")

    queue = QueueWithTwoStacks2(100)

    queue.enqueue(1)
    queue.enqueue(2)
    print(queue.dequeue())
    print(queue.dequeue())
    queue.enqueue(3)
    queue.enqueue(4)

    print(queue.dequeue())
    print(queue.dequeue())


if __name__ == "__main__":
    main()
