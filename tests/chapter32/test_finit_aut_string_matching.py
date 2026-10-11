from clrs.chapter32.finite_aut_string_matching import (
    FiniteAutomaton,
    State,
    find_finite_automaton,
)
from clrs.chapter32.naive_string_matching import find_naive


def test_state_has_empty_transitions():
    state = State("abc")

    assert state.string == "abc"
    assert state.to_states == {}


def test_automaton_creates_pattern_states():
    automaton = FiniteAutomaton("abab")

    assert set(automaton.states) == {
        "",
        "a",
        "ab",
        "aba",
        "abab",
    }


def test_automaton_start_state():
    automaton = FiniteAutomaton("abc")

    assert automaton.current_state == automaton.start_state
    assert automaton.current_state.string == ""


def test_automaton_matches_pattern():
    automaton = FiniteAutomaton("abc")

    assert automaton.next("a") is False
    assert automaton.next("b") is False
    assert automaton.next("c") is True


def test_automaton_resets():
    automaton = FiniteAutomaton("abc")

    automaton.next("a")
    automaton.reset()

    assert automaton.current_state == automaton.start_state


def test_find_finite_automaton_finds_single_match():
    automaton = FiniteAutomaton("world")

    assert find_finite_automaton("world", "hello world", automaton) == [6]


def test_find_finite_automaton_finds_multiple_matches():
    automaton = FiniteAutomaton("test")

    assert find_finite_automaton("test", "test abc test", automaton) == [0, 9]


def test_find_finite_automaton_finds_overlapping_matches():
    automaton = FiniteAutomaton("ana")

    assert find_finite_automaton("ana", "banana", automaton) == [1, 3]


def test_find_finite_automaton_returns_empty_for_no_match():
    automaton = FiniteAutomaton("xyz")

    assert find_finite_automaton("xyz", "hello world", automaton) == []


def test_find_finite_automaton_finds_match_at_start():
    automaton = FiniteAutomaton("hello")

    assert find_finite_automaton("hello", "hello world", automaton) == [0]


def test_find_finite_automaton_finds_match_at_end():
    automaton = FiniteAutomaton("world")

    assert find_finite_automaton("world", "hello world", automaton) == [6]


def test_find_finite_automaton_handles_pattern_equal_to_text():
    automaton = FiniteAutomaton("hello")

    assert find_finite_automaton("hello", "hello", automaton) == [0]


def test_find_finite_automaton_handles_pattern_longer_than_text():
    automaton = FiniteAutomaton("hello world!")

    assert find_finite_automaton("hello world!", "hello", automaton) == []


def test_find_finite_automaton_handles_empty_text():
    automaton = FiniteAutomaton("hello")

    assert find_finite_automaton("hello", "", automaton) == []


def test_find_finite_automaton_can_reuse_automaton():
    automaton = FiniteAutomaton("test")

    assert find_finite_automaton("test", "test abc test", automaton) == [0, 9]
    assert find_finite_automaton("test", "abc test", automaton) == [4]


def test_find_finite_automaton_matches_naive_implementation():
    for pattern in ["the", "string", "algorithm", "xyz"]:
        automaton = FiniteAutomaton(pattern)

        assert find_finite_automaton(pattern, "the string algorithm", automaton) == (
            find_naive(pattern, "the string algorithm")
        )
