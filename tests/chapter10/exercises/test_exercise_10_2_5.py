from clrs.chapter10.exercises.exercise_10_2_5 import reverse
from clrs.chapter10.linked_list import Item, LinkedList


def test_reverse_empty_list():
    linked_list = LinkedList()

    reverse(linked_list)

    assert linked_list.head is None
    assert linked_list.tail is None
    assert len(linked_list) == 0


def test_reverse_single_item():
    linked_list = LinkedList()
    item = Item(1, "a")
    linked_list.append(item)

    reverse(linked_list)

    assert linked_list.head is item
    assert linked_list.tail is item
    assert item.prev is None
    assert item.next is None


def test_reverse_list():
    linked_list = LinkedList()

    linked_list.append(Item(1, "a"))
    linked_list.append(Item(2, "b"))
    linked_list.append(Item(3, "c"))
    linked_list.append(Item(4, "d"))

    reverse(linked_list)

    assert [item.key for item in linked_list] == [4, 3, 2, 1]


def test_reverse_updates_head_and_tail():
    linked_list = LinkedList()

    first = Item(1, "a")
    second = Item(2, "b")
    third = Item(3, "c")

    linked_list.append(first)
    linked_list.append(second)
    linked_list.append(third)

    reverse(linked_list)

    assert linked_list.head is third
    assert linked_list.tail is first


def test_reverse_updates_next_links():
    linked_list = LinkedList()

    first = Item(1, "a")
    second = Item(2, "b")
    third = Item(3, "c")

    linked_list.append(first)
    linked_list.append(second)
    linked_list.append(third)

    reverse(linked_list)

    assert third.next is second
    assert second.next is first
    assert first.next is None


def test_reverse_updates_prev_links():
    linked_list = LinkedList()

    first = Item(1, "a")
    second = Item(2, "b")
    third = Item(3, "c")

    linked_list.append(first)
    linked_list.append(second)
    linked_list.append(third)

    reverse(linked_list)

    assert third.prev is None
    assert second.prev is third
    assert first.prev is second


def test_reverse_preserves_items():
    linked_list = LinkedList()

    items = [
        Item(1, "a"),
        Item(2, "b"),
        Item(3, "c"),
    ]

    for item in items:
        linked_list.append(item)

    reverse(linked_list)

    assert linked_list.head is items[2]
    assert linked_list.head is not None
    assert linked_list.head.next is items[1]
    assert linked_list.head.next is not None
    assert linked_list.head.next.next is items[0]
    assert linked_list.tail is items[0]


def test_reverse_twice_restores_original_list():
    linked_list = LinkedList()

    linked_list.append(Item(1, "a"))
    linked_list.append(Item(2, "b"))
    linked_list.append(Item(3, "c"))

    reverse(linked_list)
    reverse(linked_list)

    assert [item.key for item in linked_list] == [1, 2, 3]

    assert linked_list.head is not None
    assert linked_list.tail is not None
    assert linked_list.head.key == 1
    assert linked_list.tail.key == 3
