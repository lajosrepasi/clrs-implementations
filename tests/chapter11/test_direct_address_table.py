import pytest

from clrs.chapter11.direct_address_table import DirectAddressTable


def test_insert_and_search():
    table = DirectAddressTable(10)

    table.insert(3, "hello")

    assert table.search(3) == "hello"


def test_overwrite_existing_key():
    table = DirectAddressTable(10)

    table.insert(5, "a")
    table.insert(5, "b")

    assert table.search(5) == "b"


def test_delete():
    table = DirectAddressTable(10)

    table.insert(4, "value")
    table.delete(4)

    assert table.search(4) is None


def test_search_missing_key():
    table = DirectAddressTable(10)

    assert table.search(7) is None


def test_store_multiple_values():
    table = DirectAddressTable(20)

    table.insert(1, "a")
    table.insert(5, "b")
    table.insert(19, "c")

    assert table.search(1) == "a"
    assert table.search(5) == "b"
    assert table.search(19) == "c"


def test_store_different_types():
    table = DirectAddressTable(10)

    table.insert(0, 123)
    table.insert(1, "hello")
    table.insert(2, [1, 2, 3])

    assert table.search(0) == 123
    assert table.search(1) == "hello"
    assert table.search(2) == [1, 2, 3]


def test_delete_missing_key():
    table = DirectAddressTable(10)

    table.delete(3)

    assert table.search(3) is None


def test_search_out_of_bounds():
    table = DirectAddressTable(10)

    with pytest.raises(IndexError):
        table.search(10)


def test_insert_out_of_bounds():
    table = DirectAddressTable(10)

    with pytest.raises(IndexError):
        table.insert(10, "x")


def test_delete_out_of_bounds():
    table = DirectAddressTable(10)

    with pytest.raises(IndexError):
        table.delete(10)
