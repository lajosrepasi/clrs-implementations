import pytest

from clrs.chapter10.exercises.exercise_10_2_3 import QueueWithLinkedList


def test_enqueue_and_dequeue():
    queue = QueueWithLinkedList()

    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    assert queue.dequeue() == 1
    assert queue.dequeue() == 2
    assert queue.dequeue() == 3


def test_single_element():
    queue = QueueWithLinkedList()

    queue.enqueue("hello")

    assert queue.dequeue() == "hello"


def test_underflow():
    queue = QueueWithLinkedList()

    with pytest.raises(Exception):
        queue.dequeue()


def test_interleaved_operations():
    queue = QueueWithLinkedList()

    queue.enqueue("a")
    queue.enqueue("b")

    assert queue.dequeue() == "a"

    queue.enqueue("c")

    assert queue.dequeue() == "b"
    assert queue.dequeue() == "c"


def test_many_elements():
    queue = QueueWithLinkedList()

    for i in range(100):
        queue.enqueue(i)

    for i in range(100):
        assert queue.dequeue() == i


def test_queue_can_be_reused():
    queue = QueueWithLinkedList()

    queue.enqueue(1)
    assert queue.dequeue() == 1

    queue.enqueue(2)
    queue.enqueue(3)

    assert queue.dequeue() == 2
    assert queue.dequeue() == 3


def test_mixed_types():
    queue = QueueWithLinkedList()

    queue.enqueue(123)
    queue.enqueue("abc")
    queue.enqueue([1, 2, 3])

    assert queue.dequeue() == 123
    assert queue.dequeue() == "abc"
    assert queue.dequeue() == [1, 2, 3]
