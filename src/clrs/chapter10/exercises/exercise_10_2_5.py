"""
Exercise 10.2-5
"""

from clrs.chapter10.linked_list import Item, LinkedList


def reverse(linked_list: LinkedList):
    """
    Reverse a doubly linked list in place.
    """
    head = linked_list.head
    tail = linked_list.tail

    item = linked_list.head
    prev = None

    while item is not None:
        next_item = item.next
        item.next = prev
        item.prev = next_item

        prev = item
        item = next_item

    linked_list.head = tail
    linked_list.tail = head


def main():
    linked_list = LinkedList()

    linked_list.append(Item(1, "a"))
    linked_list.append(Item(2, "b"))
    linked_list.append(Item(3, "c"))
    linked_list.append(Item(4, "d"))

    print(linked_list)

    reverse(linked_list)

    print(linked_list)


if __name__ == "__main__":
    main()
