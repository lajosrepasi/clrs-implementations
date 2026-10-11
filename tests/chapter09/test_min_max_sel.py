from clrs.chapter09.min_max_sel import max_sel, min_max, min_sel


def test_min_sel():
    array: list = [5, 1, 9, 3, 7]

    assert min_sel(array) == 1


def test_min_sel_negative_numbers():
    array: list = [3, -7, 4, -2, 0]

    assert min_sel(array) == -7


def test_min_sel_single_element():
    array: list = [42]

    assert min_sel(array) == 42


def test_max_sel():
    array: list = [5, 1, 9, 3, 7]

    assert max_sel(array) == 9


def test_max_sel_negative_numbers():
    array: list = [3, -7, 4, -2, 0]

    assert max_sel(array) == 4


def test_max_sel_single_element():
    array: list = [42]

    assert max_sel(array) == 42


def test_min_max_even_length():
    array: list = [5, 1, 9, 3]

    assert min_max(array) == (1, 9)


def test_min_max_odd_length():
    array: list = [5, 1, 9, 3, 7]

    assert min_max(array) == (1, 9)


def test_min_max_negative_numbers():
    array: list = [-5, -10, -2, -7]

    assert min_max(array) == (-10, -2)


def test_min_max_single_element():
    array: list = [42]

    assert min_max(array) == (42, 42)


def test_min_max_duplicates():
    array: list = [4, 4, 4, 4]

    assert min_max(array) == (4, 4)
