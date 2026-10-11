from clrs.chapter03.log_star import log_star


def test_log_star_zero():
    assert log_star(0) == 0


def test_log_star_one():
    assert log_star(1) == 0


def test_log_star_two():
    assert log_star(2) == 1


def test_log_star_e_squared():
    # ln(e²) = 2, ln(2) < 1
    assert log_star(8) == 2


def test_log_star_sixteen():
    assert log_star(16) == 3


def test_log_star_large_number():
    assert log_star(1_000_000) == 3


def test_log_star_monotonic():
    assert log_star(10) <= log_star(100)
    assert log_star(100) <= log_star(1000)
