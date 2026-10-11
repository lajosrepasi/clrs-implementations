import pytest

from clrs.chapter03.mod import mod


@pytest.mark.parametrize(
    ("a", "n"),
    [
        (0, 1),
        (1, 1),
        (5, 2),
        (10, 3),
        (233451, 3532),
        (1000000, 97),
        (-10, 3),
        (10, -3),
        (-10, -3),
    ],
)
def test_mod_matches_python_operator(a, n):
    assert mod(a, n) == a % n


def test_mod_zero_division():
    with pytest.raises(ZeroDivisionError):
        mod(10, 0)
