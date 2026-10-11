"""
Doubly linked list implementation.
"""

from __future__ import annotations

from collections.abc import Iterator
from typing import Any


class Item:
    """
    Node stored in a linked list.
    """

    def __init__(self, key: Any, value: Any) -> None:
        """
        Create a linked list node.
        """
        self.prev: Item | None = None
        self.next: Item | None = None
        self.key = key
        self.value = value

    def __str__(self) -> str:
        """
        Return a string representation of the node.
        """
        return "%s: %s" % (self.key, self.value)


class LinkedListIterator:
    """
    Independent iterator for LinkedList.
    """

    def __init__(self, head: Item | None) -> None:
        self.current = head

    def __iter__(self) -> LinkedListIterator:
        return self

    def __next__(self) -> Item:
        if self.current is None:
            raise StopIteration

        item = self.current
        self.current = self.current.next
        return item


class LinkedList:
    """
    Doubly linked list storing key-value items.
    """

    def __init__(self):
        """
        Create an empty linked list.
        """
        self.head: Item | None = None
        self.tail: Item | None = None
        self.len: int = 0

    def __str__(self) -> str:
        """
        Return a string representation of the list.
        """
        item_strings = []

        item = self.head

        while item is not None:
            item_strings.append(str(item))
            item = item.next

        return "LinkedList [" + ", ".join(item_strings) + "]"

    def __len__(self) -> int:
        """
        Return the number of items in the list.
        """
        return self.len

    def __iter__(self) -> Iterator[Item]:
        """
        Return a fresh, independent iterator over the list.
        """
        return LinkedListIterator(self.head)

    def is_empty(self) -> bool:
        """
        Return True if the list is empty.
        """
        return self.head is None and self.tail is None

    def append(self, item: Item) -> None:
        """
        Append an item to the end of the list.
        """
        if self.head is None:
            self.set_initial_item(item)
        elif self.tail is not None:
            self.tail.next = item
            item.prev = self.tail
            self.tail = item

        self.len += 1

    def prepend(self, item: Item) -> None:
        """
        Insert an item at the beginning of the list.
        """
        if self.tail is None:
            self.set_initial_item(item)
        elif self.head is not None:
            self.head.prev = item
            item.next = self.head
            self.head = item

        self.len += 1

    def search(self, key: Any) -> Item | None:
        """
        Find the first item with the given key.
        """
        item = self.head

        while item is not None and not item.key == key:
            item = item.next

        return item

    def insert_after_with_key(self, item: Item, key: Any) -> None:
        """
        Insert an item after the item with the given key.
        """
        after_item = self.search(key)

        if after_item is not None:
            self.insert_after(item, after_item)

    def insert_after(self, item: Item, after_item: Item) -> None:
        """
        Insert an item after another item.
        """
        after_item_next = after_item.next

        if after_item_next is not None:
            after_item_next.prev = item
            item.next = after_item_next
        else:
            self.tail = item

        item.prev = after_item
        after_item.next = item

        self.len += 1

    def delete_with_key(self, key: Any) -> None:
        """
        Delete the first item with the given key.
        """
        item_to_delete = self.search(key)

        if item_to_delete is not None:
            self.delete(item_to_delete)

    def delete(self, item: Item) -> None:
        """
        Remove an item from the list.
        """
        delete_next = item.next
        delete_prev = item.prev

        if delete_next is not None:
            delete_next.prev = delete_prev
        else:
            self.tail = delete_prev

        if delete_prev is not None:
            delete_prev.next = delete_next
        else:
            self.head = delete_next

        if delete_next is None and delete_prev is None:
            self.head = None
            self.tail = None

        item.next = None
        item.prev = None

        self.len -= 1

    def set_initial_item(self, item: Item) -> None:
        """
        Initialize an empty list with its first item.
        """
        self.head = item
        self.tail = item


def main():
    linked_list = LinkedList()

    linked_list.append(Item("item", 1))
    bingyom = Item("thing", 10)
    linked_list.prepend(bingyom)
    linked_list.append(Item("something", 100))
    print(linked_list)
    print(len(linked_list))

    print("\nTest iteration")
    for i in linked_list:
        print(i)

    print("\nAdd item after item")
    linked_list.insert_after_with_key(Item("another item", 11), "item")
    for i in linked_list:
        print(i)

    print("\nAdd item after thing")
    print("tail:", linked_list.tail)
    linked_list.insert_after_with_key(Item("another thing", 1121), "thing")
    print(linked_list)
    print("tail:", linked_list.tail)

    print("\nDelete item")
    linked_list.delete_with_key("item")
    print(linked_list)

    print("\nDelete another thing")
    print(len(linked_list))
    print(linked_list)
    linked_list.delete_with_key("another thing")
    print(len(linked_list))
    print(linked_list)

    print("\nDelete another item")
    linked_list.delete_with_key("another item")
    print(linked_list)
    print("tail:", linked_list.tail)

    print("\nSearches:")
    found = linked_list.search("thing")
    if found is not None:
        print(found.value)
    print(linked_list.search("nothing"))

    print("\nDelete item")
    linked_list.delete_with_key("another item")
    print(linked_list)
    print("head:", linked_list.head)


if __name__ == "__main__":
    main()
