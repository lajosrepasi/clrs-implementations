"""
This is a test script to simulate the birthday paradox.
"""

from random import randint


def main():
    birthdays = set()
    k = 0

    while True:
        day = randint(1, 365)
        if day in birthdays:
            break
        birthdays.add(day)
        k += 1

    print(k)


if __name__ == "__main__":
    main()
