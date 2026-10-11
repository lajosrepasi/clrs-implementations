"""
Direct-address table implementation.
"""

from typing import Any


class DirectAddressTable:
    """
    Direct-address table storing values by integer key.

    Keys correspond directly to array indexes.
    """

    def __init__(self, size: int):
        """
        Create an empty direct-address table.
        """
        self.array = [None] * size

    def delete(self, k: int) -> None:
        """
        Remove the value stored at key k.
        """
        self.array[k] = None

    def search(self, k: int) -> Any:
        """
        Return the value stored at key k.
        """
        return self.array[k]

    def insert(self, k: int, value: Any) -> None:
        """
        Insert a value at key k.
        """
        self.array[k] = value


def main():
    direct_access_table = DirectAddressTable(25)

    direct_access_table.insert(23, "thing")
    direct_access_table.insert(4, "another")

    print(direct_access_table.search(4))


if __name__ == "__main__":
    main()
