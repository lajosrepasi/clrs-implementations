"""
Implementations of the Fibonacci sequence using recursive,
iterative, and closed-form approaches.
"""

from math import floor, sqrt

from clrs.utils.timer_utils import Timer


def fib_rec(n: int) -> int:
    """
    Compute the nth Fibonacci number recursively.
    """
    if n == 1:
        return 1

    if n == 0:
        return 0

    return fib_rec(n - 1) + fib_rec(n - 2)


def fib_iter(n: int) -> int:
    """
    Compute the nth Fibonacci number iteratively.
    """
    if n == 0:
        return 0

    f0 = 0
    f1 = 1

    for _ in range(n - 1):
        f0, f1 = f1, f0 + f1

    return f1


def fib_golden_ratio(n: int) -> int:
    """
    Compute the nth Fibonacci number using Binet's formula.
    """
    golden_ratio = (1 + sqrt(5)) / 2

    f = floor(pow(golden_ratio, n) / sqrt(5) + 0.5)

    return f


def main():
    n = 36

    timer = Timer("Fibonacci recursive")
    print(fib_rec(n))
    timer.stop()

    timer = Timer("Fibonacci iterative")
    print(fib_iter(n))
    timer.stop()

    timer = Timer("Fibonacci goden ratio")
    print(fib_golden_ratio(n))
    timer.stop()


if __name__ == "__main__":
    main()
