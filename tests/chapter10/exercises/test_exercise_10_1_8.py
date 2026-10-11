import pytest

from clrs.chapter10.exercises.exercise_10_1_8 import StackWithTwoQueues


def test_push_and_pop():
    stack = StackWithTwoQueues(10)

    stack.push(1)
    stack.push(2)
    stack.push(3)

    assert stack.pop() == 3
    assert stack.pop() == 2
    assert stack.pop() == 1


def test_interleaved_operations():
    stack = StackWithTwoQueues(10)

    stack.push("a")
    stack.push("b")

    assert stack.pop() == "b"

    stack.push("c")

    assert stack.pop() == "c"
    assert stack.pop() == "a"


def test_single_element():
    stack = StackWithTwoQueues(10)

    stack.push(42)

    assert stack.pop() == 42


def test_underflow():
    stack = StackWithTwoQueues(10)

    with pytest.raises(Exception):
        stack.pop()


def test_many_elements():
    stack = StackWithTwoQueues(100)

    for i in range(50):
        stack.push(i)

    for i in range(49, -1, -1):
        assert stack.pop() == i


def test_push_after_emptying_stack():
    stack = StackWithTwoQueues(10)

    stack.push(1)
    assert stack.pop() == 1

    stack.push(2)
    stack.push(3)

    assert stack.pop() == 3
    assert stack.pop() == 2
