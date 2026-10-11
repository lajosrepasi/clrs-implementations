"""
Hash table implementation using chaining.
"""

from __future__ import annotations

from collections.abc import Callable, Iterator
from typing import Any

from clrs.chapter10.linked_list import Item, LinkedList


class HashTableIterator:
    """
    Independent iterator for HashTableChaining.
    """

    def __init__(self, slots: list[LinkedList]) -> None:
        self.slots = slots
        self.slot_index = 0
        self.current_item: Item | None = None
        self._advance_to_next_non_empty_slot()

    def _advance_to_next_non_empty_slot(self) -> None:
        """Advance slot_index to the next non-empty linked list bucket."""
        while self.slot_index < len(self.slots):
            ll = self.slots[self.slot_index]
            if not ll.is_empty():
                self.current_item = ll.head
                return
            self.slot_index += 1
        self.current_item = None

    def __iter__(self) -> HashTableIterator:
        return self

    def __next__(self) -> Any:
        if self.current_item is None:
            raise StopIteration

        key = self.current_item.key

        # Advance to next item in list or find next non-empty bucket
        if self.current_item.next is not None:
            self.current_item = self.current_item.next
        else:
            self.slot_index += 1
            self._advance_to_next_non_empty_slot()

        return key


class HashTableChaining:
    """
    Hash table that resolves collisions using linked lists.
    """

    def __init__(
        self,
        hash_func: Callable[[int, int], int] | None = None,
        slot_size: int | None = None,
    ) -> None:
        """
        Create an empty hash table.
        """

        if slot_size is None:
            self.slot_size = 19
        else:
            self.slot_size = slot_size

        self.slots: list[LinkedList] = [LinkedList() for _ in range(self.slot_size)]
        self.hash_func: Callable[[int, int], int] | None = hash_func

        self.size = 0

    def __str__(self) -> str:
        """
        Return a string representation of the table.
        """

        s = ""

        for i in range(self.slot_size):
            if not self.slots[i].is_empty():
                s += str(i) + ": " + str(self.slots[i]) + "\n"

        return s

    def __getitem__(self, key: Any) -> Any:
        """
        Return the value associated with a key.
        """
        return self.search(key)

    def __setitem__(self, key: Any, value: Any) -> None:
        """
        Insert or update a key-value pair.
        """
        self.insert(key, value)

    def __delitem__(self, key: Any) -> None:
        """
        Remove a key from the table.
        """
        self.delete(key)

    def __contains__(self, key: Any) -> bool:
        """
        Check whether a key exists.
        """
        return self.contains(key)

    def __len__(self) -> int:
        """
        Return the number of stored items.
        """
        return self.size

    def __iter__(self) -> Iterator[Any]:
        """
        Return a fresh iterator over stored keys.
        """
        return HashTableIterator(self.slots)

    def insert(self, key: Any, value: Any) -> None:
        """
        Insert or update a key-value pair.
        """
        if self.contains(key):
            item = self.get_linked_list_item_for_key(key)
            assert item is not None
            item.value = value
        else:
            linked_list = self.get_linked_list_for_key(key)
            linked_list.append(Item(key, value))
            self.size += 1

    def search(self, key: Any) -> Any:
        """
        Return the value associated with a key.
        """
        item = self.get_linked_list_item_for_key(key)

        if item is not None:
            return item.value

        return None

    def contains(self, key: Any) -> bool:
        """
        Check whether a key exists.
        """
        return self.search(key) is not None

    def delete(self, key: Any) -> None:
        """
        Remove a key from the table.
        """
        if key in self:
            linked_list = self.get_linked_list_for_key(key)
            linked_list.delete_with_key(key)
            self.size -= 1

    def get_linked_list_item_for_key(self, key: Any) -> Item | None:
        """
        Return the linked-list item for a key.
        """
        linked_list = self.get_linked_list_for_key(key)
        item = linked_list.search(key)

        return item

    def get_linked_list_for_key(self, key: Any) -> LinkedList:
        """
        Return the bucket associated with a key.
        """
        if isinstance(key, str):
            key = hash(key)

        hashed_key = self.hash(key)
        linked_list = self.slots[hashed_key]

        return linked_list

    def hash(self, key: int) -> int:
        """
        Compute the slot index for a key.
        """
        if self.hash_func is not None:
            return self.hash_func(key, self.slot_size - 1)

        return key % self.slot_size


def main():
    hash_table = HashTableChaining(slot_size=21)

    hash_table.insert(12234, "foo")
    hash_table.insert(3452, "thing")
    hash_table.insert(34, "another")
    print(hash_table)

    print("Find items:")
    assert hash_table.search(3452) == "thing"
    print(hash_table.search(3452))
    assert hash_table.search(34) == "another"
    print(hash_table.search(34))
    assert hash_table.search(3434) is None
    print(hash_table.search(3434))

    print("\nDelete item, try to find:")
    assert hash_table.contains(34)
    print("contains?", hash_table.contains(34))
    hash_table.delete(34)
    assert hash_table.search(34) is None
    print(hash_table.search(34))
    hash_table.delete(3345)
    assert hash_table.contains(34) == False
    print("contains?", hash_table.contains(34))

    print("\nchange value")
    assert hash_table.contains(12234)
    print(hash_table.search(12234))
    hash_table.insert(12234, "foo2")
    assert hash_table.contains(12234)
    print(hash_table.search(12234))
    assert hash_table.search(12234) == "foo2"

    print("\nTest indexing")
    assert hash_table[12234] == "foo2"
    print(hash_table[12234])
    hash_table[12234] = "new value"
    assert hash_table[12234] == "new value"
    print(hash_table[12234])
    assert 12234 in hash_table
    print(12234 in hash_table)
    assert 1012234 not in hash_table
    print(1012234 in hash_table)

    print("\nIteration")
    for key in hash_table:
        print(key)

    print("\nString keys")

    hash_table["a"] = 234
    assert hash_table["a"] == 234
    print(hash_table["a"])
    assert "a" in hash_table
    print("a" in hash_table)
    del hash_table["a"]
    assert "a" not in hash_table
    assert hash_table["a"] is None


if __name__ == "__main__":
    main()
