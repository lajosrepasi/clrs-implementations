from clrs.chapter14.lcs import (
    LEFT,
    LEFT_UP,
    UP,
    get_lcs,
    get_lcs_list,
    lcs,
)


def test_lcs_clrs_example_length():
    x = ["A", "B", "C", "B", "D", "A", "B"]
    y = ["B", "D", "C", "A", "B", "A"]

    c, _ = lcs(x, y)

    assert c[len(x)][len(y)] == 4


def test_lcs_clrs_example_sequence():
    x = ["A", "B", "C", "B", "D", "A", "B"]
    y = ["B", "D", "C", "A", "B", "A"]

    _, b = lcs(x, y)

    result = get_lcs_list(b, x, len(x), len(y))

    assert len(result) == 4


def test_lcs_binary_sequence_example():
    x = [1, 0, 0, 1, 0, 1, 0, 1]
    y = [0, 1, 0, 1, 1, 0, 1, 1, 0]

    c, b = lcs(x, y)

    assert c[len(x)][len(y)] == 6
    assert get_lcs_list(b, x, len(x), len(y)) == [1, 0, 0, 1, 1, 0]


def test_lcs_empty_sequences():
    c, b = lcs([], [])

    assert c == [[0]]
    assert b == [[None]]

    assert get_lcs_list(b, [], 0, 0) == []


def test_lcs_one_empty_sequence():
    c, b = lcs([1, 2, 3], [])

    assert c[-1][-1] == 0
    assert get_lcs_list(b, [1, 2, 3], 3, 0) == []


def test_lcs_identical_sequences():
    x = [1, 2, 3, 4]

    c, b = lcs(x, x)

    assert c[len(x)][len(x)] == 4
    assert get_lcs_list(b, x, len(x), len(x)) == [1, 2, 3, 4]


def test_lcs_no_common_elements():
    x = [1, 2, 3]
    y = [4, 5, 6]

    c, b = lcs(x, y)

    assert c[len(x)][len(y)] == 0
    assert get_lcs_list(b, x, len(x), len(y)) == []


def test_get_lcs_string_reconstruction():
    x = ["A", "B", "C", "D"]
    y = ["A", "X", "C", "D"]

    _, b = lcs(x, y)

    assert get_lcs(b, x, len(x), len(y)) == "ACD"


def test_direction_table_contains_only_valid_markers():
    x = [1, 2, 3]
    y = [2, 3]

    _, b = lcs(x, y)

    valid = {None, UP, LEFT, LEFT_UP}

    for row in b:
        for cell in row:
            assert cell in valid
