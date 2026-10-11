"""
Solutions to the rod-cutting problem using recursion, memoization, and dynamic programming.
"""

from clrs.utils.timer_utils import Timer

cache = {}


def rod_cutting_problem_memoised(
    n: int, price_table: list[int]
) -> tuple[int, list[int]]:
    """
    Return the maximum obtainable revenue and corresponding cuts using memoization.
    """
    key = "{0}-{1}".format(str(n), ",".join(str(p) for p in price_table))

    if key in cache:
        return cache[key]

    if n <= 0:
        return (0, [])

    opt = -1
    opt_cut = []

    for i in range(1, n + 1):
        (val, cut) = rod_cutting_problem_memoised(n - i, price_table)

        p_i = None

        if i > (len(price_table) - 1):
            p_i = 0
        else:
            p_i = price_table[i]

        if val + p_i > opt:
            opt = val + p_i
            opt_cut = [i] + cut.copy()

    sol = (opt, opt_cut)

    cache[key] = sol

    return sol


def rod_cutting_problem_recursive(
    n: int, price_table: list[int]
) -> tuple[int, list[int]]:
    """
    Return the maximum obtainable revenue and corresponding cuts using recursion.
    """

    if n <= 0:
        return (0, [])

    opt = -1
    opt_cut = []

    for i in range(1, n + 1):
        (val, cut) = rod_cutting_problem_recursive(n - i, price_table)

        p_i = None

        if i > (len(price_table) - 1):
            p_i = 0
        else:
            p_i = price_table[i]

        if val + p_i > opt:
            opt = val + p_i
            opt_cut = [i] + cut.copy()

    return (opt, opt_cut)


def rod_cutting_problem_dp(n: int, price_table: list[int]) -> tuple[int, list[int]]:
    """
    Return the maximum obtainable revenue and corresponding cuts using bottom-up dynamic programming.
    """
    solutions = [(0, []) for _ in range(n + 1)]

    for i in range(1, n + 1):
        sol = (-1, [])
        for pi in range(1, len(price_table)):
            if i - pi > -1:
                val = price_table[pi] + solutions[i - pi][0]
                if val > sol[0]:
                    sol = (val, [pi])

        solutions[i] = sol

    latest_cut = solutions[-1]
    opt_cut = []
    i = n
    while i > 0:
        opt_cut += latest_cut[1]
        i -= latest_cut[1][0]

        if i > 0:
            latest_cut = solutions[i]

    return (solutions[-1][0], opt_cut)


def main():
    price_table = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    n = 23

    print("Rod cutting solutions\n")

    t = Timer("Recursive:")
    sol = rod_cutting_problem_recursive(n, price_table)
    print(sol)
    t.stop()

    print("\n")
    t = Timer("Recursive with memoisation:")
    sol = rod_cutting_problem_memoised(n, price_table)
    print(sol)
    t.stop()

    print("\n")
    t = Timer("Dynamic programming:")
    sol = rod_cutting_problem_dp(n, price_table)
    print(sol)
    t.stop()


if __name__ == "__main__":
    main()
