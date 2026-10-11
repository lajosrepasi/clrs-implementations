"""
Approximation of Euler's number using the infinite series expansion.
"""

import math


def e(limit: int) -> float:
    """
    Approximate Euler's number using the first `limit` terms of the series.
    """
    calced_e = 1

    fact_aggreg = 1

    for i in range(1, limit):
        fact_aggreg *= i
        calced_e += 1 / fact_aggreg

    return calced_e


def main():
    for l in range(1, 100):
        print("%.20f" % e(l))

    print("e from math: %.20f" % math.e)


if __name__ == "__main__":
    main()
