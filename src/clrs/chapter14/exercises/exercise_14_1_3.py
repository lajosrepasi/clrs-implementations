"""
Exercise 14.1-3
"""

from clrs.utils.timer_utils import Timer


def rod_cutting_problem_dp(
    n: int, price_table: list[int], cut_price: int
) -> tuple[int, list[int]]:
    solutions = [(0, []) for _ in range(n + 1)]

    for i in range(1, n + 1):
        sol = (-1, [])
        for pi in range(1, len(price_table)):
            if i - pi > -1:
                val = price_table[pi] + solutions[i - pi][0] - cut_price
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

    t = Timer("Dynamic programming:")
    sol = rod_cutting_problem_dp(n, price_table, 9)
    print(sol)
    t.stop()


if __name__ == "__main__":
    main()
