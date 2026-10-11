from clrs.chapter14.rod_cutting_problem import (
    cache,
    rod_cutting_problem_dp,
    rod_cutting_problem_memoised,
    rod_cutting_problem_recursive,
)

PRICE_TABLE = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]


def assert_valid_solution(
    solution: tuple[int, list[int]],
    expected_value: int,
    rod_length: int,
):
    value, cuts = solution

    assert value == expected_value
    assert sum(cuts) == rod_length


def test_recursive_base_case():
    assert rod_cutting_problem_recursive(0, PRICE_TABLE) == (0, [])


def test_memoised_base_case():
    cache.clear()
    assert rod_cutting_problem_memoised(0, PRICE_TABLE) == (0, [])


def test_dp_base_case():
    assert rod_cutting_problem_dp(0, PRICE_TABLE) == (0, [])


def test_recursive_clrs_example_length_4():
    solution = rod_cutting_problem_recursive(4, PRICE_TABLE)

    assert_valid_solution(solution, 10, 4)


def test_memoised_clrs_example_length_4():
    cache.clear()

    solution = rod_cutting_problem_memoised(4, PRICE_TABLE)

    assert_valid_solution(solution, 10, 4)


def test_dp_clrs_example_length_4():
    solution = rod_cutting_problem_dp(4, PRICE_TABLE)

    assert_valid_solution(solution, 10, 4)


def test_recursive_clrs_example_length_7():
    solution = rod_cutting_problem_recursive(7, PRICE_TABLE)

    assert_valid_solution(solution, 18, 7)


def test_memoised_clrs_example_length_7():
    cache.clear()

    solution = rod_cutting_problem_memoised(7, PRICE_TABLE)

    assert_valid_solution(solution, 18, 7)


def test_dp_clrs_example_length_7():
    solution = rod_cutting_problem_dp(7, PRICE_TABLE)

    assert_valid_solution(solution, 18, 7)


def test_recursive_clrs_example_length_10():
    solution = rod_cutting_problem_recursive(10, PRICE_TABLE)

    assert_valid_solution(solution, 30, 10)


def test_memoised_clrs_example_length_10():
    cache.clear()

    solution = rod_cutting_problem_memoised(10, PRICE_TABLE)

    assert_valid_solution(solution, 30, 10)


def test_dp_clrs_example_length_10():
    solution = rod_cutting_problem_dp(10, PRICE_TABLE)

    assert_valid_solution(solution, 30, 10)


def test_all_implementations_return_same_result():
    cache.clear()

    for n in range(0, 11):
        recursive = rod_cutting_problem_recursive(n, PRICE_TABLE)
        memoised = rod_cutting_problem_memoised(n, PRICE_TABLE)
        dp = rod_cutting_problem_dp(n, PRICE_TABLE)

        assert recursive[0] == memoised[0] == dp[0]
        assert sum(recursive[1]) == n
        assert sum(memoised[1]) == n
        assert sum(dp[1]) == n


def test_memoised_populates_cache():
    cache.clear()

    rod_cutting_problem_memoised(8, PRICE_TABLE)

    assert len(cache) > 0


def test_length_larger_than_price_table():
    solution = rod_cutting_problem_dp(15, PRICE_TABLE)

    value, cuts = solution

    assert value > 0
    assert sum(cuts) == 15
