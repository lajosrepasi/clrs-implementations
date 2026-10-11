from clrs.chapter10.exercises.exercise_10_1_7 import (
    QueueWithTwoStacks,
    QueueWithTwoStacks2,
)


def _run_common_queue_tests(queue):
    assert queue.dequeue is not None

    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    assert queue.dequeue() == 1
    assert queue.dequeue() == 2

    queue.enqueue(4)
    queue.enqueue(5)

    assert queue.dequeue() == 3
    assert queue.dequeue() == 4
    assert queue.dequeue() == 5


def test_queue_with_two_stacks():
    _run_common_queue_tests(QueueWithTwoStacks(100))


def test_queue_with_two_stacks2():
    _run_common_queue_tests(QueueWithTwoStacks2(100))


def test_queue_with_two_stacks_underflow():
    queue = QueueWithTwoStacks(10)

    try:
        queue.dequeue()
        assert False
    except Exception:
        pass


def test_queue_with_two_stacks2_underflow():
    queue = QueueWithTwoStacks2(10)

    try:
        queue.dequeue()
        assert False
    except Exception:
        pass


def test_queue_with_two_stacks_single_item():
    queue = QueueWithTwoStacks(10)

    queue.enqueue("a")

    assert queue.dequeue() == "a"


def test_queue_with_two_stacks2_single_item():
    queue = QueueWithTwoStacks2(10)

    queue.enqueue("a")

    assert queue.dequeue() == "a"


def test_queue_with_two_stacks_interleaved():
    queue = QueueWithTwoStacks(20)

    queue.enqueue(1)
    assert queue.dequeue() == 1

    queue.enqueue(2)
    queue.enqueue(3)

    assert queue.dequeue() == 2

    queue.enqueue(4)

    assert queue.dequeue() == 3
    assert queue.dequeue() == 4


def test_queue_with_two_stacks2_interleaved():
    queue = QueueWithTwoStacks2(20)

    queue.enqueue(1)
    assert queue.dequeue() == 1

    queue.enqueue(2)
    queue.enqueue(3)

    assert queue.dequeue() == 2

    queue.enqueue(4)

    assert queue.dequeue() == 3
    assert queue.dequeue() == 4
