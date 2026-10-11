"""
Exercise 3.1-3
"""


def main():
    for divider in range(1, 10000):
        largest_elements_share = 1 / divider
        elements_to_go_though_share = 1 - 2 * largest_elements_share

        comparisons = largest_elements_share * elements_to_go_though_share

        print(comparisons)


if __name__ == "__main__":
    main()
