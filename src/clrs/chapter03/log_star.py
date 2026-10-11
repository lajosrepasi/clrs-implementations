"""
Implementation of the iterated logarithm function.
"""

from math import log


def log_star(n: int) -> int:
    """
    Return the number of times the logarithm must be applied
    to n before the result becomes less than or equal to 1.
    """
    if n <= 1:
        return 0

    iterated_log = log(n)
    i = 1

    while iterated_log > 1:
        iterated_log = log(iterated_log)
        i += 1

    return i


def main():
    print(log_star(1234523456))


if __name__ == "__main__":
    main()
