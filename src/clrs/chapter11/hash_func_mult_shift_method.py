"""
Multiply-shift hash function implementation.
"""

from clrs.chapter11.hash_table_chaining import HashTableChaining

WORD_BIT_LENGTH = 64
SLOTS_BIT_LENGTH = 4


def mult_shift_method(key: int, _: int) -> int:
    """
    Compute a hash value using the multiply-shift method.
    """
    a = 2**WORD_BIT_LENGTH * 0.76432987

    return int((a * key) % 2**WORD_BIT_LENGTH) >> (WORD_BIT_LENGTH - SLOTS_BIT_LENGTH)


def main():
    hash_table = HashTableChaining(mult_shift_method, 2**SLOTS_BIT_LENGTH)

    hash_table.insert(12234, "other")
    hash_table.insert(3452, "thing")
    hash_table.insert(34, "another")
    hash_table.insert(3324534, "foo")
    print(hash_table)


if __name__ == "__main__":
    main()
