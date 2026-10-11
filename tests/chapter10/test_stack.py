import pytest

from clrs.chapter10.stack import Stack


def test_stack_is_empty_when_created():
    stack = Stack(3)

    assert stack.empty()


def test_push_and_pop():
    stack = Stack(3)

    stack.push(1)
    stack.push(2)
    stack.push(3)

    assert stack.pop() == 3
    assert stack.pop() == 2
    assert stack.pop() == 1
    assert stack.empty()


def test_stack_is_lifo():
    stack = Stack(5)

    for item in [1, 2, 3, 4, 5]:
        stack.push(item)

    result = []

    while not stack.empty():
        result.append(stack.pop())

    assert result == [5, 4, 3, 2, 1]


def test_get_top():
    stack = Stack(3)

    stack.push(1)
    stack.push(2)

    assert stack.get_top() == 2
    assert not stack.empty()

    assert stack.pop() == 2


def test_get_top_does_not_remove_item():
    stack = Stack(3)

    stack.push("A")

    assert stack.get_top() == "A"
    assert stack.get_top() == "A"

    assert stack.pop() == "A"


def test_stack_overflow():
    stack = Stack(2)

    stack.push(1)
    stack.push(2)

    with pytest.raises(OverflowError):
        stack.push(3)


def test_stack_underflow_pop():
    stack = Stack(2)

    with pytest.raises(IndexError):
        stack.pop()


def test_stack_underflow_get_top():
    stack = Stack(2)

    with pytest.raises(IndexError):
        stack.get_top()


def test_stack_reset():
    stack = Stack(3)

    stack.push(1)
    stack.push(2)

    stack.reset()

    assert stack.empty()

    stack.push(3)

    assert stack.pop() == 3


def test_stack_accepts_different_types():
    stack = Stack(3)

    stack.push(42)
    stack.push("hello")
    stack.push([1, 2, 3])

    assert stack.pop() == [1, 2, 3]
    assert stack.pop() == "hello"
    assert stack.pop() == 42


def test_default_size():
    stack = Stack()

    for i in range(100):
        stack.push(i)

    with pytest.raises(OverflowError):
        stack.push(100)


def test_invalid_size_zero():
    with pytest.raises(ValueError):
        Stack(0)


def test_invalid_size_negative():
    with pytest.raises(ValueError):
        Stack(-1)


def test_stack_length():
    stack = Stack(5)

    assert len(stack) == 0

    stack.push(1)
    stack.push(2)

    assert len(stack) == 2

    stack.pop()

    assert len(stack) == 1
