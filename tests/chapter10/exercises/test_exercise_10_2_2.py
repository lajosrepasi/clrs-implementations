import pytest

from clrs.chapter10.exercises.exercise_10_2_2 import StackWithLinkedList


def test_push_and_pop():
    stack = StackWithLinkedList()

    stack.push(1)
    stack.push(2)
    stack.push(3)

    assert stack.pop() == 3
    assert stack.pop() == 2
    assert stack.pop() == 1


def test_single_element():
    stack = StackWithLinkedList()

    stack.push("hello")

    assert stack.pop() == "hello"


def test_underflow():
    stack = StackWithLinkedList()

    with pytest.raises(Exception):
        stack.pop()


def test_interleaved_operations():
    stack = StackWithLinkedList()

    stack.push("a")
    stack.push("b")

    assert stack.pop() == "b"

    stack.push("c")

    assert stack.pop() == "c"
    assert stack.pop() == "a"


def test_many_elements():
    stack = StackWithLinkedList()

    for i in range(100):
        stack.push(i)

    for i in range(99, -1, -1):
        assert stack.pop() == i


def test_stack_can_be_reused():
    stack = StackWithLinkedList()

    stack.push(1)
    assert stack.pop() == 1

    stack.push(2)
    stack.push(3)

    assert stack.pop() == 3
    assert stack.pop() == 2
