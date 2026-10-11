import pytest

from clrs.chapter10.my_queue import Queue


def test_queue_is_empty_when_created():
    queue = Queue(3)

    assert queue.empty()


def test_enqueue_and_dequeue():
    queue = Queue(3)

    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    assert queue.dequeue() == 1
    assert queue.dequeue() == 2
    assert queue.dequeue() == 3
    assert queue.empty()


def test_queue_is_fifo():
    queue = Queue(5)

    for item in [1, 2, 3, 4, 5]:
        queue.enqueue(item)

    result = []

    while not queue.empty():
        result.append(queue.dequeue())

    assert result == [1, 2, 3, 4, 5]


def test_queue_overflow():
    queue = Queue(3)

    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    with pytest.raises(OverflowError):
        queue.enqueue(4)


def test_queue_underflow():
    queue = Queue(3)

    with pytest.raises(IndexError):
        queue.dequeue()


def test_queue_wraps_around():
    queue = Queue(3)

    queue.enqueue(1)
    queue.enqueue(2)
    assert queue.dequeue() == 1

    queue.enqueue(3)
    queue.enqueue(4)

    assert queue.dequeue() == 2
    assert queue.dequeue() == 3
    assert queue.dequeue() == 4
    assert queue.empty()


def test_queue_wraps_around_multiple_times():
    queue = Queue(3)

    for i in range(10):
        queue.enqueue(i)
        assert queue.dequeue() == i

    assert queue.empty()


def test_queue_reset():
    queue = Queue(3)

    queue.enqueue(1)
    queue.enqueue(2)

    queue.reset()

    assert queue.empty()

    queue.enqueue(3)

    assert queue.dequeue() == 3


def test_queue_accepts_different_types():
    queue = Queue(3)

    queue.enqueue(42)
    queue.enqueue("hello")
    queue.enqueue([1, 2, 3])

    assert queue.dequeue() == 42
    assert queue.dequeue() == "hello"
    assert queue.dequeue() == [1, 2, 3]


def test_queue_default_size():
    queue = Queue()

    for i in range(100):
        queue.enqueue(i)

    with pytest.raises(OverflowError):
        queue.enqueue(100)


def test_queue_rejects_zero_size():
    with pytest.raises(ValueError):
        Queue(0)


def test_queue_rejects_negative_size():
    with pytest.raises(ValueError):
        Queue(-1)
