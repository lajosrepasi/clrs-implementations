from clrs.chapter02.binary_search import binary_search


def test_item_found():
    array = [1, 3, 5, 7, 9]

    result = binary_search(array, 5, 0, len(array) - 1)

    assert result == 2


def test_item_not_found():
    array = [1, 3, 5, 7, 9]

    result = binary_search(array, 6, 0, len(array) - 1)

    assert result == [-1, 3]


def test_item_found_multiple_times():
    array = [1, 3, 5, 5, 5, 7, 9]

    result = binary_search(array, 5, 0, len(array) - 1)

    assert result == 2


def test_item_is_first_element():
    array = [1, 3, 5, 7, 9]

    result = binary_search(array, 1, 0, len(array) - 1)

    assert result == 0


def test_item_is_last_element():
    array = [1, 3, 5, 7, 9]

    result = binary_search(array, 9, 0, len(array) - 1)

    assert result == 4


def test_single_element_found():
    array = [5]

    result = binary_search(array, 5, 0, 0)

    assert result == 0


def test_single_element_not_found():
    array = [5]

    result = binary_search(array, 3, 0, 0)

    assert result == [-1, 0]
