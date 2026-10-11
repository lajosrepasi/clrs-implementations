"""
Implementation of the modulo operation using its mathematical definition.
"""

from math import floor


def mod(a: int, n: int) -> int:
    """
    Return the remainder of a divided by n.
    """
    return a - n * floor(a / n)


def main():
    print(233451 % 3532)
    print(mod(233451, 3532))


if __name__ == "__main__":
    main()
