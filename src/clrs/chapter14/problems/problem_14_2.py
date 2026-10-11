"""
Problem 14-2

O(n^3) solution.
"""

from clrs.chapter14.lcs import get_lcs, lcs


def longest_palindrome_sequence(A: str) -> str | None:
    chars = [*A]
    l = len(chars)

    current_longest = 0
    current_sol = None
    current_pal = None

    for split in range(1, l):
        first_half_wihtout_split_char = chars[0:split]
        second_half_without_split_char = chars[split:l]

        sol = lcs(
            first_half_wihtout_split_char,
            list(reversed(second_half_without_split_char)),
        )

        if sol[0][-1][-1] > current_longest:
            current_longest = sol[0][-1][-1]
            current_sol = sol
            seq = get_lcs(
                current_sol[1],
                first_half_wihtout_split_char,
                len(first_half_wihtout_split_char),
                len(second_half_without_split_char),
            )

            current_pal = seq + seq[::-1]

    for split in range(1, l - 1):
        split_char = chars[split]
        first_half_with_split_char = chars[0:split]
        second_half_with_split_char = chars[split + 1 : l]

        sol = lcs(
            first_half_with_split_char, list(reversed(second_half_with_split_char))
        )

        if sol[0][-1][-1] + 1 > current_longest:
            current_longest = sol[0][-1][-1] + 1
            current_sol = sol
            seq = get_lcs(
                current_sol[1],
                first_half_with_split_char,
                len(first_half_with_split_char),
                len(second_half_with_split_char),
            )

            current_pal = seq + split_char + seq[::-1]

    return current_pal


def main():
    s = "character"
    print(longest_palindrome_sequence(s))


if __name__ == "__main__":
    main()
