import math

from clrs.chapter03.e import e


def test_e_limit_1():
    assert e(1) == 1


def test_e_limit_2():
    assert e(2) == 2


def test_e_limit_3():
    assert e(3) == 2.5


def test_e_limit_4():
    assert e(4) == 2.6666666666666665


def test_e_approximates_math_e():
    assert abs(e(20) - math.e) < 1e-12


def test_e_improves_with_more_terms():
    error_5 = abs(e(5) - math.e)
    error_10 = abs(e(10) - math.e)

    assert error_10 < error_5
