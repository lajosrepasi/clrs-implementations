from clrs.chapter11.hash_table_chaining import HashTableChaining


def test_insert_and_search():
    table = HashTableChaining()

    table.insert(1, "one")

    assert table.search(1) == "one"


def test_search_missing_key():
    table = HashTableChaining()

    assert table.search(123) is None


def test_update_existing_key():
    table = HashTableChaining()

    table.insert(1, "one")
    table.insert(1, "updated")

    assert table.search(1) == "updated"
    assert len(table) == 1


def test_delete_existing_key():
    table = HashTableChaining()

    table.insert(1, "one")
    table.delete(1)

    assert table.search(1) is None
    assert len(table) == 0


def test_delete_missing_key():
    table = HashTableChaining()

    table.delete(123)

    assert len(table) == 0


def test_contains():
    table = HashTableChaining()

    table.insert(5, "five")

    assert 5 in table
    assert 10 not in table


def test_len():
    table = HashTableChaining()

    table.insert(1, "a")
    table.insert(2, "b")
    table.insert(3, "c")

    assert len(table) == 3


def test_indexing():
    table = HashTableChaining()

    table[10] = "value"

    assert table[10] == "value"


def test_delitem():
    table = HashTableChaining()

    table[10] = "value"
    del table[10]

    assert table[10] is None


def test_string_keys():
    table = HashTableChaining()

    table["hello"] = 123

    assert table["hello"] == 123
    assert "hello" in table


def test_collision_handling():
    table = HashTableChaining(slot_size=5)

    table.insert(0, "a")
    table.insert(5, "b")
    table.insert(10, "c")

    assert table.search(0) == "a"
    assert table.search(5) == "b"
    assert table.search(10) == "c"


def test_iteration():
    table = HashTableChaining()

    table.insert(1, "a")
    table.insert(2, "b")
    table.insert(3, "c")

    keys = set(table)

    assert keys == {1, 2, 3}


def test_iteration_empty_table():
    table = HashTableChaining()

    assert list(table) == []


def test_delete_reduces_size():
    table = HashTableChaining()

    table.insert(1, "a")
    table.insert(2, "b")

    assert len(table) == 2

    table.delete(1)

    assert len(table) == 1


def test_multiple_updates_keep_size():
    table = HashTableChaining()

    table.insert(1, "a")
    table.insert(1, "b")
    table.insert(1, "c")

    assert len(table) == 1
    assert table.search(1) == "c"
