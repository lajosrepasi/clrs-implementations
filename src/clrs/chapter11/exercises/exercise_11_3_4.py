"""
Exercise 11.3-4
"""

from math import floor, sqrt


def mult_method(key: int, m: int) -> int:
    A = (sqrt(5) - 1) / 2

    return floor(m * ((A * key) % 1))


def main():
    m = list(map(lambda k: mult_method(k, 1000), [61, 62, 63, 64, 65]))
    print(m)


if __name__ == "__main__":
    main()
