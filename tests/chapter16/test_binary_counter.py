from clrs.chapter16.binary_counter import BinaryCounter


def test_counter_initially_zero():
    counter = BinaryCounter(4)

    assert str(counter) == "0000"


def test_increment_sequence():
    counter = BinaryCounter(3)

    expected = [
        "001",
        "010",
        "011",
        "100",
        "101",
        "110",
        "111",
        "000",
    ]

    for value in expected:
        counter.increment()
        assert str(counter) == value


def test_decrement_sequence():
    counter = BinaryCounter(3)

    expected = [
        "111",
        "110",
        "101",
        "100",
        "011",
        "010",
        "001",
        "000",
    ]

    for value in expected:
        counter.decrement()
        assert str(counter) == value


def test_increment_then_decrement_returns_to_original():
    counter = BinaryCounter(8)

    for _ in range(100):
        counter.increment()

    original = str(counter)

    counter.increment()
    counter.decrement()

    assert str(counter) == original


def test_decrement_then_increment_returns_to_original():
    counter = BinaryCounter(8)

    for _ in range(50):
        counter.increment()

    original = str(counter)

    counter.decrement()
    counter.increment()

    assert str(counter) == original


def test_overflow_wraps_to_zero():
    counter = BinaryCounter(3)

    for _ in range(7):
        counter.increment()

    assert str(counter) == "111"

    counter.increment()

    assert str(counter) == "000"


def test_underflow_wraps_to_maximum():
    counter = BinaryCounter(3)

    assert str(counter) == "000"

    counter.decrement()

    assert str(counter) == "111"


def test_numeric_value_matches_binary_string():
    counter = BinaryCounter(5)

    for expected in range(32):
        assert int(str(counter), 2) == expected
        counter.increment()

    assert int(str(counter), 2) == 0


def test_single_bit_counter():
    counter = BinaryCounter(1)

    assert str(counter) == "0"

    counter.increment()
    assert str(counter) == "1"

    counter.increment()
    assert str(counter) == "0"

    counter.decrement()
    assert str(counter) == "1"
