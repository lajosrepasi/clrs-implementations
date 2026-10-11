"""
Multiplication-method hash function.
"""

from math import floor

from clrs.chapter11.hash_table_chaining import HashTableChaining


def mult_method(key: int, m: int) -> int:
    """
    Compute a hash value using the multiplication method.
    """
    A = 0.76432987

    return floor(m * ((A * key) % 1))


def main():
    hash_table = HashTableChaining(mult_method)

    hash_table.insert(12234, "thing")
    hash_table.insert(3452, "other")
    hash_table.insert(34, "foo")
    print(hash_table)


if __name__ == "__main__":
    main()
