"""
Exercise 10.1-8

Stack implementation using two queues.
"""

from typing import Any

from clrs.chapter10.my_queue import Queue


class StackWithTwoQueues:
    """
    Stack implemented using two queues.

    Push runs in O(n) time and pop runs in O(1) time.
    """

    def __init__(self, size: int) -> None:
        self.queue1 = Queue(size)
        self.queue2 = Queue(size)

    def push(self, item: Any) -> None:
        empty_queue = self.get_empty_queue()
        not_empty_queue = self.get_not_empty_queue()

        empty_queue.enqueue(item)

        while not not_empty_queue.empty():
            empty_queue.enqueue(not_empty_queue.dequeue())

    def pop(self) -> Any:
        if self.queue1.empty() and self.queue2.empty():
            raise Exception("underflow")

        not_empty_queue = self.get_not_empty_queue()

        return not_empty_queue.dequeue()

    def get_empty_queue(self) -> Queue:
        if self.queue1.empty():
            return self.queue1
        else:
            return self.queue2

    def get_not_empty_queue(self) -> Queue:
        if not self.queue1.empty():
            return self.queue1
        else:
            return self.queue2


def main():
    stack = StackWithTwoQueues(100)

    stack.push("a")
    stack.push("b")
    stack.push("c")
    stack.pop()
    stack.push("d")

    print(stack.pop())
    print(stack.pop())


if __name__ == "__main__":
    main()
