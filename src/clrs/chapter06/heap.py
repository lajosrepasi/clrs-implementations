"""
Binary heap data structure implementation.
"""

from typing import Any, Callable


class Heap:
    """
    Binary heap supporting custom ordering through a comparison function.
    """

    def __init__(
        self,
        array: list[Any] | None = None,
        iterative: bool = False,
        compare: Callable[[Any, Any], bool] | None = None,
    ):
        """
        Create a heap from an array.

        The input array is copied and transformed into a heap.
        """
        self.array = [] if array is None else array.copy()

        if compare is None:
            self.compare = lambda a, b: a > b
        else:
            self.compare = compare

        if len(self):
            if iterative:
                self.build_max_heap_it()
            else:
                self.build_max_heap()

    def __len__(self) -> int:
        return len(self.array)

    def __str__(self) -> str:
        return str(self.array)

    def build_max_heap(self) -> None:
        """
        Transform the array into a heap using recursive heapify.
        """
        last_non_leaf_node_index = len(self) // 2 - 1
        for i in range(last_non_leaf_node_index, -1, -1):
            self.max_heapify(i)

    def build_max_heap_it(self) -> None:
        """
        Transform the array into a heap using iterative heapify.
        """
        last_non_leaf_node_index = len(self) // 2 - 1
        for i in range(last_non_leaf_node_index, -1, -1):
            self.max_heapify_it(i)

    def max_heapify(self, i: int) -> None:
        """
        Restore the heap property recursively starting at index i.
        """
        A = self.array
        l = self.left(i)
        r = self.right(i)

        largest = None

        if l < len(self) and self.compare(A[l], A[i]):
            largest = l
        else:
            largest = i

        if r < len(self) and self.compare(A[r], A[largest]):
            largest = r

        if largest != i:
            self.swap(largest, i)
            self.max_heapify(largest)

    def max_heapify_it(self, i: int) -> None:
        """
        Restore the heap property iteratively starting at index i.
        """
        A = self.array
        l = self.left(i)
        r = self.right(i)

        largest = None

        while i < len(self):
            if l < len(self) and self.compare(A[l], A[i]):
                largest = l
            else:
                largest = i

            if r < len(self) and self.compare(A[r], A[largest]):
                largest = r

            if largest != i:
                self.swap(largest, i)
                i = largest
                l = self.left(largest)
                r = self.right(largest)
            else:
                break

    def left(self, i: int) -> int:
        """
        Return the index of the left child.
        """
        return 2 * i + 1

    def right(self, i: int) -> int:
        """
        Return the index of the right child.
        """
        return 2 * i + 2

    def parent(self, i: int) -> int:
        """
        Return the index of the parent node.
        """
        return (i - 1) // 2

    def swap(self, i: int, j: int) -> None:
        """
        Swap two elements in the heap array.
        """
        A = self.array

        A[i], A[j] = A[j], A[i]

    def remove_last_item(self) -> None:
        """
        Remove the last element from the heap.
        """
        self.array.pop()

    def get_max(self) -> Any:
        """
        Return the root element of the heap.
        """
        if not self.array:
            raise IndexError("Heap is empty.")
        return self.array[0]


def main():
    array = [10, 12, 34, 1234, 234, 65, 211, 30, 1234, 1, 34, 110, 5, 45, 467]

    h = Heap(array)
    h_it = Heap(array, True, compare=lambda a, b: a < b)

    print(h)
    print("heap iterative", h_it)


if __name__ == "__main__":
    main()
