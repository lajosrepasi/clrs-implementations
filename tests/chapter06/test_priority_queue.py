import pytest

from clrs.chapter06.priority_queue import MinPriorityQueue, PriorityQueue


class TestPriorityQueue:
    def test_insert_and_maximum(self):
        pq = PriorityQueue()

        pq.insert(100, "A")
        pq.insert(101, "B")
        pq.insert(1001, "D")
        pq.insert(99, "C")

        assert pq.maximum() == "D"

    def test_extract_in_priority_order(self):
        pq = PriorityQueue()

        pq.insert(100, "A")
        pq.insert(101, "B")
        pq.insert(1001, "D")
        pq.insert(99, "C")

        assert pq.extract_maximum() == "D"
        assert pq.extract_maximum() == "B"
        assert pq.extract_maximum() == "A"
        assert pq.extract_maximum() == "C"

    def test_maximum_does_not_remove_item(self):
        pq = PriorityQueue()

        pq.insert(100, "A")
        pq.insert(200, "B")

        assert pq.maximum() == "B"
        assert pq.maximum() == "B"
        assert len(pq) == 2

    def test_empty_queue(self):
        pq = PriorityQueue()

        assert pq.empty()
        assert len(pq) == 0
        assert pq.extract_maximum() is None

    def test_maximum_on_empty_queue(self):
        pq = PriorityQueue()

        with pytest.raises(IndexError):
            pq.maximum()


class TestMinPriorityQueue:
    def test_insert_and_minimum(self):
        pq = MinPriorityQueue()

        pq.insert(100, "A")
        pq.insert(101, "B")
        pq.insert(1001, "D")
        pq.insert(99, "C")

        assert pq.minimum() == "C"

    def test_minimum_does_not_remove_item(self):
        pq = MinPriorityQueue()

        pq.insert(100, "A")
        pq.insert(50, "B")

        assert pq.minimum() == "B"
        assert pq.minimum() == "B"
        assert len(pq) == 2

    def test_extract_in_priority_order(self):
        pq = MinPriorityQueue()

        pq.insert(100, "A")
        pq.insert(101, "B")
        pq.insert(1001, "D")
        pq.insert(99, "C")

        assert pq.extract_minimum() == (99, "C")
        assert pq.extract_minimum() == (100, "A")
        assert pq.extract_minimum() == (101, "B")
        assert pq.extract_minimum() == (1001, "D")

    def test_duplicate_keys(self):
        pq = MinPriorityQueue()

        pq.insert(99, "A")
        pq.insert(99, "B")
        pq.insert(100, "C")

        assert pq.minimum() == "A"

        assert pq.extract_minimum() == (99, "A")
        assert pq.extract_minimum() == (99, "B")
        assert pq.extract_minimum() == (100, "C")

    def test_contains(self):
        pq = MinPriorityQueue()

        pq.insert(100, "A")
        pq.insert(200, "B")

        assert "A" in pq
        assert "B" in pq
        assert "C" not in pq

    def test_empty_queue(self):
        pq = MinPriorityQueue()

        assert pq.empty()
        assert len(pq) == 0
        assert pq.extract_minimum() is None

    def test_minimum_on_empty_queue(self):
        pq = MinPriorityQueue()

        with pytest.raises(IndexError):
            pq.minimum()

    def test_decrease_key(self):
        pq = MinPriorityQueue()

        pq.insert(100, "A")
        pq.insert(200, "B")
        pq.insert(300, "C")

        pq.decrease_key(50, 200, "B")

        assert pq.minimum() == "B"
        assert pq.extract_minimum() == (50, "B")
        assert pq.extract_minimum() == (100, "A")
        assert pq.extract_minimum() == (300, "C")

    def test_decrease_key_with_duplicate_old_key(self):
        pq = MinPriorityQueue()

        pq.insert(100, "A")
        pq.insert(100, "B")
        pq.insert(200, "C")

        pq.decrease_key(50, 100, "B")

        assert pq.extract_minimum() == (50, "B")
        assert pq.extract_minimum() == (100, "A")
        assert pq.extract_minimum() == (200, "C")
