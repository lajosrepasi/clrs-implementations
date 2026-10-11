"""
Exercise 11.4-1
"""

from clrs.chapter11.hash_table_open_addressing import (
    HashTableOpenAddressing,
    double_hash_func,
)


def insert_values(hash_table):
    hash_table.insert(10)
    hash_table.insert(22)
    hash_table.insert(31)
    hash_table.insert(4)
    hash_table.insert(15)
    hash_table.insert(28)
    hash_table.insert(17)
    hash_table.insert(88)
    hash_table.insert(59)


def main():
    hash_table_linear_probe = HashTableOpenAddressing(slot_size=11)
    insert_values(hash_table_linear_probe)
    print("Linear probe")
    print(hash_table_linear_probe)

    print("\n")

    hash_table_double_hash = HashTableOpenAddressing(
        slot_size=11, hash_func=double_hash_func
    )
    insert_values(hash_table_double_hash)
    print("Double hash")
    print(hash_table_double_hash)


if __name__ == "__main__":
    main()
