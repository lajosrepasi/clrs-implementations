from clrs.chapter10.linked_list import Item, LinkedList


def test_new_list_is_empty():
    linked_list = LinkedList()

    assert linked_list.is_empty()
    assert len(linked_list) == 0
    assert linked_list.head is None
    assert linked_list.tail is None


def test_append():
    linked_list = LinkedList()

    linked_list.append(Item("A", 1))
    linked_list.append(Item("B", 2))

    assert len(linked_list) == 2
    assert linked_list.head is not None
    assert linked_list.tail is not None
    assert linked_list.head.key == "A"
    assert linked_list.tail.key == "B"


def test_prepend():
    linked_list = LinkedList()

    linked_list.prepend(Item("A", 1))
    linked_list.prepend(Item("B", 2))

    assert len(linked_list) == 2
    assert linked_list.head is not None
    assert linked_list.tail is not None
    assert linked_list.head.key == "B"
    assert linked_list.tail.key == "A"


def test_search_found():
    linked_list = LinkedList()

    linked_list.append(Item("A", 1))
    linked_list.append(Item("B", 2))

    found = linked_list.search("B")

    assert found is not None
    assert found.value == 2


def test_search_not_found():
    linked_list = LinkedList()

    linked_list.append(Item("A", 1))

    assert linked_list.search("X") is None


def test_insert_after_middle():
    linked_list = LinkedList()

    linked_list.append(Item("A", 1))
    linked_list.append(Item("C", 3))

    linked_list.insert_after_with_key(Item("B", 2), "A")

    assert linked_list.head is not None
    assert linked_list.head.next is not None
    assert linked_list.head.next.next is not None

    assert linked_list.head.next.key == "B"
    assert linked_list.head.next.next.key == "C"


def test_insert_after_tail_updates_tail():
    linked_list = LinkedList()

    linked_list.append(Item("A", 1))

    linked_list.insert_after_with_key(Item("B", 2), "A")

    assert linked_list.tail is not None
    assert linked_list.tail.key == "B"


def test_delete_middle():
    linked_list = LinkedList()

    a = Item("A", 1)
    b = Item("B", 2)
    c = Item("C", 3)

    linked_list.append(a)
    linked_list.append(b)
    linked_list.append(c)

    linked_list.delete(b)

    assert len(linked_list) == 2
    assert a.next == c
    assert c.prev == a


def test_delete_head():
    linked_list = LinkedList()

    a = Item("A", 1)
    b = Item("B", 2)

    linked_list.append(a)
    linked_list.append(b)

    linked_list.delete(a)

    assert linked_list.head == b
    assert b.prev is None


def test_delete_tail():
    linked_list = LinkedList()

    a = Item("A", 1)
    b = Item("B", 2)

    linked_list.append(a)
    linked_list.append(b)

    linked_list.delete(b)

    assert linked_list.tail == a
    assert a.next is None


def test_delete_only_item():
    linked_list = LinkedList()

    a = Item("A", 1)

    linked_list.append(a)

    linked_list.delete(a)

    assert linked_list.is_empty()
    assert len(linked_list) == 0


def test_delete_with_key():
    linked_list = LinkedList()

    linked_list.append(Item("A", 1))
    linked_list.append(Item("B", 2))
    linked_list.append(Item("C", 3))

    linked_list.delete_with_key("B")

    assert len(linked_list) == 2
    assert linked_list.search("B") is None


def test_delete_with_missing_key():
    linked_list = LinkedList()

    linked_list.append(Item("A", 1))

    linked_list.delete_with_key("X")

    assert len(linked_list) == 1


def test_iteration():
    linked_list = LinkedList()

    linked_list.append(Item("A", 1))
    linked_list.append(Item("B", 2))
    linked_list.append(Item("C", 3))

    keys = [item.key for item in linked_list]

    assert keys == ["A", "B", "C"]


def test_len():
    linked_list = LinkedList()

    assert len(linked_list) == 0

    linked_list.append(Item("A", 1))
    linked_list.append(Item("B", 2))

    assert len(linked_list) == 2

    linked_list.delete_with_key("A")

    assert len(linked_list) == 1
