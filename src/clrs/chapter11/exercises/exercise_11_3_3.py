"""
Exercise 11.3-3
"""


def hash(string: str, m: int) -> int:
    h = 0

    for c in string:
        h = (h * 128 + ord(c)) % m

    return h


def main():

    h = hash("other thing 12d a 3", 19)
    print(h)


if __name__ == "__main__":
    main()
