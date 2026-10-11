"""
Open-address hash table implementation.

Supports linear probing by default and custom probing
strategies through a user-provided hash function.
"""

from collections.abc import Callable


class HashTableOpenAddressing:
    """
    Hash table using open addressing.
    """

    def __init__(
        self, slot_size: int | None = None, hash_func: Callable | None = None
    ) -> None:
        """
        Create an empty hash table.
        """

        if slot_size is None:
            self.slot_size = 10
        else:
            self.slot_size = slot_size

        self.slots: list = [None] * self.slot_size

        self.hash_func = hash_func

    def __str__(self) -> str:
        """
        Return a string representation of the table.
        """
        s = ""
        for i in range(self.slot_size):
            s += str(i) + ": " + str(self.slots[i]) + "\n"

        return s

    def insert(self, key: int) -> int:
        """
        Insert a key into the table.
        """
        i = 0

        while i < self.slot_size:
            slot = self.hash(key, i)

            if self.slots[slot] is None:
                self.slots[slot] = key
                return slot
            i += 1

        raise Exception("Hash table overflow")

    def search(self, key: int) -> int | None:
        """
        Search for a key in the table.
        """
        i = 0

        slot = self.hash(key, i)

        while i < self.slot_size and self.slots[slot] is not None:

            if self.slots[slot] == key:
                return slot

            i += 1

            slot = self.hash(key, i)

        return None

    def hash(self, key: int, i: int) -> int:
        """
        Compute the i-th probe position for a key.
        """
        if self.hash_func is not None:
            return self.hash_func(key, self.slot_size, i)

        return (key + i) % self.slot_size


def double_hash_func(k, m, i):
    """
    Compute a probe position using double hashing.
    """

    def h1(k):
        return k % m

    def h2(k):
        return 1 + k % (m - 1)

    return (h1(k) + i * h2(k)) % m


def main():
    hash_table = HashTableOpenAddressing(slot_size=5)

    hash_table.insert(345)
    hash_table.insert(929)
    hash_table.insert(99)
    hash_table.insert(199)
    hash_table.insert(299)

    print(hash_table)
    print(hash_table.search(929))
    print(hash_table.search(919))


if __name__ == "__main__":
    main()
