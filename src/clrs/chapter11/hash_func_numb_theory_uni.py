"""
Universal hash function implementation.
"""

from collections.abc import Callable

from clrs.chapter11.hash_table_chaining import HashTableChaining


def create_hash_function(a: int, b: int) -> Callable:
    """
    Create a universal hash function with parameters a and b.
    """
    p = 31

    def h(key: int, m: int) -> int:
        """
        Map a key to a hash table slot.
        """
        return ((a * key + b) % p) % m

    return h


def main():
    hash_func = create_hash_function(3, 4)

    hash_table = HashTableChaining(hash_func=hash_func, slot_size=10)

    hash_table.insert(12234, "other")
    hash_table.insert(3452, "thing")
    hash_table.insert(34, "another")
    hash_table.insert(3324534, "foo")
    print(hash_table)


if __name__ == "__main__":
    main()
