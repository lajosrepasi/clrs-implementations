"""
Exercise 2.1-5
"""


def add_binary_nums(a: list[int], b: list[int]) -> list[int]:
    ax = [0] + a
    bx = [0] + b

    n = len(a)
    s = [0 for _ in range(n + 1)]

    r = 0
    for i in range(n, -1, -1):
        x = ax[i] + bx[i] + r

        s[i] = x % 2

        if x <= 1:
            r = 0
        else:
            r = 1

    return s


def main():
    print(add_binary_nums([1, 1, 1], [1, 1, 1]))


if __name__ == "__main__":
    main()
