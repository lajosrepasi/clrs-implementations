"""
Priority queue implementations using a binary heap.
"""

from typing import Generic, TypeVar

from clrs.chapter06.heap import Heap

K = TypeVar("K")
V = TypeVar("V")


class PriorityQueue(Generic[K, V]):
    """
    A max-priority queue that associates keys with values.
    """

    def __init__(self) -> None:
        self.heap: Heap = Heap()
        self.key_value_map: dict[K, V] = {}

    def __len__(self) -> int:
        """
        Return the number of elements in the queue.
        """
        return len(self.heap)

    def empty(self) -> bool:
        """
        Return True if the queue is empty.
        """
        return len(self.key_value_map) == 0

    def maximum(self) -> V:
        """
        Return the value associated with the maximum key.
        """
        if self.empty():
            raise IndexError("priority queue is empty")

        return self.key_value_map[self.heap.get_max()]

    def extract_maximum(self) -> V | None:
        """
        Remove and return the value with the maximum key.
        """
        if self.empty():
            return None

        h = self.heap
        h_length = len(self.heap)

        if h_length == 0:
            return None

        max_key = h.get_max()

        maximum = self.maximum()

        h.swap(0, len(h) - 1)
        h.remove_last_item()
        h.max_heapify(0)
        del self.key_value_map[max_key]

        return maximum

    def insert(self, key: K, value: V) -> None:
        """
        Insert a key-value pair into the priority queue.
        """
        h = self.heap

        self.key_value_map[key] = value

        h.array.append(key)

        i = len(h) - 1
        p = h.parent(i)

        while i > 0 and h.array[p] < h.array[i]:
            h.swap(i, p)
            i, p = p, h.parent(p)


class MinPriorityQueue(Generic[K, V]):
    """
    A min-priority queue that supports duplicate keys.
    """

    def __init__(self) -> None:
        self.heap = Heap(iterative=True, compare=lambda a, b: a < b)
        self.key_value_map = {}

    def minimum(self) -> V:
        """
        Return the value associated with the minimum key.
        """

        if self.empty():
            raise IndexError("priority queue is empty")

        key = self.heap.get_max()
        return self.key_value_map[key][0]

    def __len__(self) -> int:
        """
        Return the number of elements in the queue.
        """
        return len(self.heap)

    def empty(self) -> bool:
        """
        Return True if the queue is empty.
        """
        return len(self.key_value_map) == 0

    def __contains__(self, value: V) -> bool:
        """Return True if the queue contains the given value."""

        return any(value in values for values in self.key_value_map.values())

    def extract_minimum(self) -> tuple[K, V] | None:
        """
        Remove and return the minimum key and associated value.
        """
        h = self.heap
        h_length = len(self.heap)

        if h_length == 0:
            return None

        min_key: K = h.get_max()

        minimum: V = self.minimum()

        h.swap(0, len(h) - 1)
        h.remove_last_item()
        h.max_heapify(0)

        self.key_value_map[min_key] = self.key_value_map[min_key][1:]

        if len(self.key_value_map[min_key]) == 0:
            del self.key_value_map[min_key]

        return (min_key, minimum)

    def insert(self, key: K, value: V) -> None:
        """
        Insert a key-value pair into the priority queue.
        """
        h = self.heap

        if key in self.key_value_map:
            self.key_value_map[key] = self.key_value_map[key] + [value]
        else:
            self.key_value_map[key] = [value]

        h.array.append(key)

        i = len(h) - 1
        self.heapify_from(i)

    def heapify_from(self, i: int) -> None:
        """
        Restore the heap property by moving an item toward the root.
        """
        h = self.heap

        p = h.parent(i)

        while i > 0 and h.array[p] > h.array[i]:
            h.swap(i, p)
            i, p = p, h.parent(p)

    def decrease_key(self, key: K, prev_key: K, value: V) -> None:
        """
        Change the priority of a value from prev_key to key.
        """
        self.key_value_map[prev_key].remove(value)

        i = self.heap.array.index(prev_key)
        del self.heap.array[i]

        self.heap.build_max_heap_it()

        if len(self.key_value_map[prev_key]) == 0:
            del self.key_value_map[prev_key]

        self.insert(key, value)


def main():
    pq = PriorityQueue()

    pq.insert(100, "A")
    pq.insert(101, "B")
    pq.insert(1001, "D")
    pq.insert(99, "C")

    print(pq.extract_maximum())
    print(pq.extract_maximum())
    print(pq.extract_maximum())
    print(pq.extract_maximum())
    print(pq.extract_maximum())

    print("\nmin pq")
    pq = MinPriorityQueue()

    pq.insert(100, "A")
    pq.insert(101, "B")
    pq.insert(1001, "D")
    pq.insert(99, "C")
    pq.insert(99, "D")

    print(pq.extract_minimum())
    print(pq.extract_minimum())
    print(pq.extract_minimum())
    print(pq.extract_minimum())
    print(pq.extract_minimum())


if __name__ == "__main__":
    main()
