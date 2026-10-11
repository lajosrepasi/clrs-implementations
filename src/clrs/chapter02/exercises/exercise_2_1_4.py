"""
Exercise 2.1-4
"""


def linear_search(a: list[int], x) -> int | None:
    l = len(a)

    for i in range(l):
        if a[i] == x:
            return i

    return None


def main():
    a = [1, 2, 1, 23, 35, 1, 23, 2435, 12, 3]

    print(linear_search(a, 23))
    print(linear_search(a, 423))


if __name__ == "__main__":
    main()
