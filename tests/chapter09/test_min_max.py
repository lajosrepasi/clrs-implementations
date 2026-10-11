from clrs.chapter09.min_max import min_max_effective, min_max_naive, minimum


def test_minimum():
    array: list = [5, 1, 9, 3, 7]

    assert minimum(array) == 1


def test_minimum_negative_numbers():
    array: list = [3, -7, 4, -2, 0]

    assert minimum(array) == -7


def test_minimum_single_element():
    array: list = [42]

    assert minimum(array) == 42


def test_min_max_naive():
    array: list = [5, 1, 9, 3, 7]

    assert min_max_naive(array) == (1, 9)


def test_min_max_effective_even_length():
    array: list = [5, 1, 9, 3]

    assert min_max_effective(array) == (1, 9)


def test_min_max_effective_odd_length():
    array: list = [5, 1, 9, 3, 7]

    assert min_max_effective(array) == (1, 9)


def test_min_max_with_duplicates():
    array: list = [4, 4, 4, 4]

    expected = (4, 4)

    assert min_max_naive(array) == expected
    assert min_max_effective(array) == expected


def test_min_max_negative_numbers():
    array: list = [-5, -10, -2, -7]

    expected = (-10, -2)

    assert min_max_naive(array) == expected
    assert min_max_effective(array) == expected


def test_min_max_single_element():
    array: list = [42]

    expected = (42, 42)

    assert min_max_naive(array) == expected
    assert min_max_effective(array) == expected


def test_min_max_effective_matches_naive():
    test_cases: list = [
        [5],
        [5, 1],
        [5, 1, 9],
        [5, 1, 9, 3, 7],
        [-5, -10, -2, -7],
        [4, 4, 4, 4],
        [10, 2, 8, 6, 1, 3, 9],
    ]

    for array in test_cases:
        assert min_max_effective(array) == min_max_naive(array)
