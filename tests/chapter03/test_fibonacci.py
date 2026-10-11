import pytest

from clrs.chapter03.fibonacci import fib_golden_ratio, fib_iter, fib_rec


@pytest.mark.parametrize(
    ("n", "expected"),
    [
        (0, 0),
        (1, 1),
        (2, 1),
        (3, 2),
        (4, 3),
        (5, 5),
        (6, 8),
        (10, 55),
        (20, 6765),
    ],
)
def test_fib_rec(n, expected):
    assert fib_rec(n) == expected


@pytest.mark.parametrize(
    ("n", "expected"),
    [
        (0, 0),
        (1, 1),
        (2, 1),
        (3, 2),
        (4, 3),
        (5, 5),
        (6, 8),
        (10, 55),
        (20, 6765),
    ],
)
def test_fib_iter(n, expected):
    assert fib_iter(n) == expected


@pytest.mark.parametrize(
    ("n", "expected"),
    [
        (0, 0),
        (1, 1),
        (2, 1),
        (3, 2),
        (4, 3),
        (5, 5),
        (6, 8),
        (10, 55),
        (20, 6765),
    ],
)
def test_fib_golden_ratio(n, expected):
    assert fib_golden_ratio(n) == expected


@pytest.mark.parametrize("n", [0, 1, 2, 5, 10, 20, 30])
def test_all_implementations_agree(n):
    assert fib_rec(n) == fib_iter(n)
    assert fib_iter(n) == fib_golden_ratio(n)
