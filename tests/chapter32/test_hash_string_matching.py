from clrs.chapter32.hash_string_matching import find_hash, hash


def test_hash_returns_sum_of_character_codes():
    assert hash("abc") == ord("a") + ord("b") + ord("c")


def test_hash_returns_zero_for_empty_string():
    assert hash("") == 0


def test_find_hash_finds_single_match():
    assert find_hash("world", "hello world") == [6]


def test_find_hash_finds_multiple_matches():
    assert find_hash("test", "test abc test") == [0, 9]


def test_find_hash_finds_overlapping_matches():
    assert find_hash("ana", "banana") == [1, 3]


def test_find_hash_returns_empty_for_no_match():
    assert find_hash("xyz", "hello world") == []


def test_find_hash_finds_match_at_start():
    assert find_hash("hello", "hello world") == [0]


def test_find_hash_finds_match_at_end():
    assert find_hash("world", "hello world") == [6]


def test_find_hash_handles_pattern_equal_to_text():
    assert find_hash("hello", "hello") == [0]


def test_find_hash_handles_pattern_longer_than_text():
    assert find_hash("hello world!", "hello") == []


def test_find_hash_handles_empty_pattern():
    assert find_hash("", "hello") == []


def test_find_hash_handles_empty_text():
    assert find_hash("hello", "") == []


def test_find_hash_handles_empty_pattern_and_text():
    assert find_hash("", "") == []


def test_find_hash_verifies_hash_collisions():
    # "ab" and "ba" have the same additive hash.
    assert hash("ab") == hash("ba")

    assert find_hash("ab", "baab") == [2]
