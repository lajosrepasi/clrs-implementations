"""
Finite-automaton string-matching algorithm.
"""

import re

from clrs.chapter32.hash_string_matching import find_hash
from clrs.chapter32.naive_string_matching import find_naive
from clrs.chapter32.text import SHORT_TEXT
from clrs.utils.timer_utils import Timer


class State:
    """
    A state in the pattern-matching automaton.
    """

    def __init__(self, string: str) -> None:
        self.to_states: dict[int, State] = dict()
        self.string: str = string

    def __str__(self) -> str:
        return "{0}, to: {1}".format(self.string, list(self.to_states.keys()))

    def __repr__(self) -> str:
        return str(self)


class FiniteAutomaton:
    """
    Finite automaton constructed from a string pattern.
    """

    def __init__(self, string: str) -> None:
        self.string: str = string
        self.alphabet: set[str] = set(string)
        self.states: dict[str, State] = dict()
        self.start_state: State = State("")

        self.build_automaton()

        self.current_state = self.start_state

    def next(self, c: str) -> bool:
        """
        Consume a character and return whether a match was found.
        """
        next_state = self.current_state.to_states.get(ord(c), self.start_state)

        if next_state == None:
            self.current_state = self.start_state
        else:
            self.current_state = next_state

        return self.string == self.current_state.string

    def reset(self) -> None:
        """
        Reset the automaton to its start state.
        """
        self.current_state = self.start_state

    def build_automaton(self) -> None:
        """
        Build the automaton's states and transitions.
        """
        self.add_start_state()
        self.add_states_and_default_transition()
        self.add_transitions()

    def add_transitions(self) -> None:
        """
        Add transitions not already defined.
        """
        for state_key in self.states:
            state = self.states[state_key]
            for c in self.alphabet:
                if c not in state.to_states:
                    self.add_transition(state, c)

    def add_transition(self, state: State, c: str) -> None:
        """
        Add the transition for a character from a state.
        """
        next_string = state.string + c

        for i in range(0, len(next_string)):
            state_string_candidate = next_string[i:]

            if state_string_candidate in self.states:
                next_state = self.states[state_string_candidate]
                state.to_states[ord(c)] = next_state
                break
            else:
                state.to_states[ord(c)] = self.start_state

    def add_states_and_default_transition(self) -> None:
        """
        Create states for every prefix of the pattern.
        """
        current_string = ""
        for c in self.string:
            current_state = self.states[current_string]

            next_string = current_string + c
            next_state = State(next_string)
            self.states[next_string] = next_state
            current_state.to_states[ord(c)] = next_state

            current_string = next_string

    def add_start_state(self) -> None:
        """
        Create the start state.
        """
        self.states[""] = self.start_state


def find_finite_automaton(to_find: str, text: str, fa: FiniteAutomaton):
    """
    Find all occurrences of a pattern using a finite automaton.
    """
    indexes = []
    len_t = len(text)

    i = 0
    while i < len_t:
        match = fa.next(text[i])

        if match:
            indexes.append(i - len(to_find) + 1)

        i += 1

    return indexes


def main():
    to_find = "referee"
    text = SHORT_TEXT * 10000

    timer = Timer("Naive impl")
    find_naive(to_find, text)
    timer.stop()

    timer = Timer("Hash impl")
    found_indexes = find_hash(to_find, text)
    timer.stop()

    fa = FiniteAutomaton(to_find)
    timer = Timer("Finit aut impl")
    found_indexes = find_finite_automaton(to_find, text, fa)
    timer.stop()

    timer = Timer("\nRe tool")
    found_indexes_with_re = [m.start() for m in re.finditer(to_find, text)]
    timer.stop()

    print("\nIs OK?", found_indexes == found_indexes_with_re)


if __name__ == "__main__":
    main()
