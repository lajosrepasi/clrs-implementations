from clrs.chapter32.naive_string_matching import find_naive


def test_find_naive_finds_single_match():
    assert find_naive("world", "hello world") == [6]


def test_find_naive_finds_multiple_matches():
    assert find_naive("test", "test abc test") == [0, 9]


def test_find_naive_finds_overlapping_matches():
    assert find_naive("ana", "banana") == [1, 3]


def test_find_naive_returns_empty_for_no_match():
    assert find_naive("xyz", "hello world") == []


def test_find_naive_finds_match_at_start():
    assert find_naive("hello", "hello world") == [0]


def test_find_naive_finds_match_at_end():
    assert find_naive("world", "hello world") == [6]


def test_find_naive_handles_pattern_equal_to_text():
    assert find_naive("hello", "hello") == [0]


def test_find_naive_handles_empty_pattern():
    assert find_naive("", "hello") == [0, 1, 2, 3, 4, 5]


def test_find_naive_handles_empty_text():
    assert find_naive("hello", "") == []


def test_find_naive_handles_empty_pattern_and_text():
    assert find_naive("", "") == [0]
