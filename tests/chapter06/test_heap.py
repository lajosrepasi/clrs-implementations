import pytest

from clrs.chapter06.heap import Heap


def test_heap_with_duplicate_values():
    heap = Heap([5, 5, 5, 5, 5])

    assert heap.get_max() == 5
    assert len(heap) == 5


def test_heap_with_single_element():
    heap = Heap([42])

    assert heap.get_max() == 42
    assert heap.array == [42]


def test_heap_with_already_valid_heap():
    heap = Heap([100, 50, 75, 20, 30, 60])

    assert heap.get_max() == 100


def test_heap_with_negative_numbers():
    heap = Heap([-10, -3, -20, -1])

    assert heap.get_max() == -1


def test_remove_last_item_until_empty():
    heap = Heap([3, 2, 1])

    heap.remove_last_item()
    heap.remove_last_item()
    heap.remove_last_item()

    assert len(heap) == 0


def test_parent_of_root():
    heap = Heap([])

    assert heap.parent(0) == -1


def test_iterative_and_recursive_heaps_contain_same_elements():
    data = [10, 4, 7, 1, 15, 3, 20]

    recursive_heap = Heap(data)
    iterative_heap = Heap(data, iterative=True)

    assert sorted(recursive_heap.array) == sorted(data)
    assert sorted(iterative_heap.array) == sorted(data)


def test_min_heap_comparator():
    heap = Heap(
        [10, 4, 7, 1, 15, 3, 20],
        compare=lambda a, b: a < b,
    )

    assert heap.array[0] == min(heap.array)


def test_original_array_is_not_modified():
    data = [4, 1, 3, 2, 16, 9, 10]

    Heap(data)

    assert data == [4, 1, 3, 2, 16, 9, 10]


def test_empty_heap_get_max_raises():
    heap = Heap([])

    with pytest.raises(IndexError):
        heap.get_max()
