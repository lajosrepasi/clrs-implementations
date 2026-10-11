"""
Exercise 5.1-3
"""

from random import random


def get_biased_random_0_1():
    r = random()
    p = 0.7600481946383613

    if r > p:
        return 0
    else:
        return 1


def get_random_0_1():
    while True:
        n1 = get_biased_random_0_1()
        n2 = get_biased_random_0_1()

        if n1 != n2:
            n1_n2_str = str(n1) + str(n2)
            if n1_n2_str == "01":
                return 1
            else:
                return 0


def main():

    for _ in range(100):
        print(get_random_0_1())


if __name__ == "__main__":
    main()
