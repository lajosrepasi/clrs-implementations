"""
Fixed-size stack implementation using an array.
"""

from typing import Any


class Stack:
    """
    A bounded LIFO (last-in, first-out) stack.
    """

    def __init__(self, size: int | None = None) -> None:
        """
        Create an empty stack with the given capacity.
        """
        if size is None:
            stack_size = 100
        else:
            stack_size = size

        if stack_size <= 0:
            raise ValueError("size must be positive")

        self.size = stack_size
        self.stack: list[Any]
        self.top: int

        self.reset()

    def reset(self) -> None:
        """
        Remove all items from the stack.
        """
        self.stack = [None] * self.size
        self.top = -1

    def empty(self) -> bool:
        """
        Return True if the stack contains no items.
        """
        return self.top == -1

    def push(self, item: Any) -> None:
        """
        Push an item onto the top of the stack.
        """
        if self.top == self.size - 1:
            raise OverflowError("stack overflow")

        self.top += 1
        self.stack[self.top] = item

    def get_top(self) -> Any:
        """
        Return the top item without removing it.
        """
        if self.empty():
            raise IndexError("stack underflow")

        item = self.stack[self.top]

        return item

    def pop(self) -> Any:
        """
        Remove and return the top item.
        """
        if self.top == -1:
            raise IndexError("stack underflow")

        item = self.stack[self.top]
        self.top -= 1

        return item

    def __len__(self) -> int:
        """
        Return the number of items in the stack.
        """
        return self.top + 1


def main():
    stack = Stack(5)

    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push("a")
    stack.push("b")

    while not stack.empty():
        print(stack.pop())


if __name__ == "__main__":
    main()
