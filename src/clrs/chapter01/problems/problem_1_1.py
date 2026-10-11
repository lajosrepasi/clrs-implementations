"""
Problem 1-1
"""


def main():
    n: int = 1
    i: int = 1
    while True:
        i += 1
        n = n * i
        print(i, n)

        if n > 10**6:
            break

    print(i - 1)


if __name__ == "__main__":
    main()
