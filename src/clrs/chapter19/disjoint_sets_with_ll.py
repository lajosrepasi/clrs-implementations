"""
Disjoint-set implementation using linked lists.

Each set is represented by a linked list, and every item
stores a reference to the set it belongs to.
"""

from __future__ import annotations

from typing import Any

from clrs.chapter10.linked_list import Item as LinkedListItem
from clrs.chapter10.linked_list import LinkedList


class Item(LinkedListItem):
    """
    Element stored in a disjoint set.
    """

    def __init__(self, key: Any, value: Any):
        super().__init__(key, value)
        self.set: Set = Set()


class Set(LinkedList):
    """
    Linked-list representation of a disjoint set.
    """

    def __init__(self) -> None:
        super().__init__()

    def append(self, item: LinkedListItem) -> None:
        super().append(item)
        assert isinstance(item, Item)
        assert item.set is not None
        item.set = self

    @classmethod
    def make_set(cls, item: Item) -> Set:
        """
        Create a singleton set containing the item.
        """
        s = cls()
        s.append(item)

        return s


class DisjointSetsLL:
    """
    Disjoint-set data structure based on linked lists.
    """

    def __init__(self) -> None:
        self.sets: list[Set] = []

    def find_set(self, item: Item) -> Item | None:
        """
        Return the representative of the item's set.
        """
        s = item.set
        assert s is not None
        head = s.head

        assert isinstance(head, Item)
        return head

    def are_in_same_set(self, item1: Item, item2: Item) -> bool:
        """
        Return whether two items belong to the same set.
        """
        return self.find_set(item1) == self.find_set(item2)

    def make_set(self, item: Item) -> Set:
        """
        Create a new singleton set.
        """
        s = Set.make_set(item)

        self.sets.append(s)

        return s

    def union(self, s1: Set, s2: Set):
        """
        Merge two sets using weighted union.
        """
        first_set = s1
        second_set = s2

        if len(s2) > len(s1):
            first_set, second_set = second_set, first_set

        for item in second_set:
            assert isinstance(item, Item)
            item.set = first_set

        if second_set.head is not None:
            first_set.append(second_set.head)
            first_set.tail = second_set.tail

        self.sets.remove(second_set)
        return first_set


def main():
    ds = DisjointSetsLL()
    I = Item

    # Graph:
    # 1--2--3  4--5

    n1 = I(1, 1)
    n2 = I(2, 2)
    n3 = I(3, 3)
    n4 = I(4, 4)
    n5 = I(5, 5)

    ds.make_set(n1)
    ds.make_set(n2)
    ds.make_set(n3)
    ds.make_set(n4)
    ds.make_set(n5)

    ds.union(n1.set, n2.set)
    ds.union(n1.set, n3.set)

    ds.union(n4.set, n5.set)

    assert ds.find_set(n1) != None
    print("n1 set:", ds.find_set(n1))
    assert ds.find_set(n2) != None
    print("n2 set:", ds.find_set(n2))
    assert ds.find_set(n3) != None
    print("n3 set:", ds.find_set(n3))

    print("n4 set:", ds.find_set(n4))
    print("n5 set:", ds.find_set(n5))

    assert ds.are_in_same_set(n1, n2)
    print("n1 and n2 in same set?", ds.are_in_same_set(n1, n2))
    assert not ds.are_in_same_set(n4, n2)
    print("n4 and n2 in same set?", ds.are_in_same_set(n4, n2))


if __name__ == "__main__":
    main()
