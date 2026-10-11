import pytest

from clrs.chapter11.hash_table_open_addressing import (
    HashTableOpenAddressing,
    double_hash_func,
)


def test_insert_and_search():
    table = HashTableOpenAddressing(10)

    table.insert(42)

    slot = table.search(42)

    assert slot is not None
    assert table.slots[slot] == 42


def test_search_missing_key():
    table = HashTableOpenAddressing(10)

    assert table.search(999) is None


def test_linear_probing_collision():
    table = HashTableOpenAddressing(5)

    table.insert(0)
    table.insert(5)
    table.insert(10)

    assert table.search(0) is not None
    assert table.search(5) is not None
    assert table.search(10) is not None


def test_table_overflow():
    table = HashTableOpenAddressing(3)

    table.insert(1)
    table.insert(2)
    table.insert(3)

    with pytest.raises(Exception):
        table.insert(4)


def test_returns_slot_from_insert():
    table = HashTableOpenAddressing(10)

    slot = table.insert(17)

    assert table.slots[slot] == 17


def test_duplicate_keys():
    table = HashTableOpenAddressing(10)

    table.insert(7)
    table.insert(7)

    found_slot = table.search(7)

    assert found_slot is not None
    assert table.slots[found_slot] == 7


def test_double_hashing_insert_and_search():
    table = HashTableOpenAddressing(
        slot_size=11,
        hash_func=double_hash_func,
    )

    table.insert(10)
    table.insert(21)
    table.insert(32)
    table.insert(43)

    assert table.search(10) is not None
    assert table.search(21) is not None
    assert table.search(32) is not None
    assert table.search(43) is not None


def test_search_after_many_collisions():
    table = HashTableOpenAddressing(5)

    keys = [0, 5, 10, 15]

    for key in keys:
        table.insert(key)

    for key in keys:
        assert table.search(key) is not None


def test_search_stops_at_empty_slot():
    table = HashTableOpenAddressing(10)

    table.insert(5)

    assert table.search(12345) is None


def test_custom_hash_function_is_used():
    called = False

    def custom_hash(k, m, i):
        nonlocal called
        called = True
        return (k + i) % m

    table = HashTableOpenAddressing(
        slot_size=10,
        hash_func=custom_hash,
    )

    table.insert(1)

    assert called
