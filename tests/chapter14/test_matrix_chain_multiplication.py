from clrs.chapter14.matrix_chain_multiplication import (
    get_matrices_list,
    get_solution,
    matrix_chain_order,
    number_of_parenthesization,
)


def test_number_of_parenthesization_single_matrix():
    assert number_of_parenthesization(1) == 1


def test_number_of_parenthesization_two_matrices():
    assert number_of_parenthesization(2) == 1


def test_number_of_parenthesization_three_matrices():
    assert number_of_parenthesization(3) == 2


def test_number_of_parenthesization_four_matrices():
    assert number_of_parenthesization(4) == 5


def test_number_of_parenthesization_five_matrices():
    assert number_of_parenthesization(5) == 14


def test_get_matrices_list():
    p = [5, 10, 3, 12]

    assert get_matrices_list(p) == [
        "5x10",
        "10x3",
        "3x12",
    ]


def test_matrix_chain_order_clrs_example_cost():
    p = [30, 35, 15, 5, 10, 20, 25]

    s, cost = matrix_chain_order(p, len(p))

    assert cost == 15125


def test_matrix_chain_order_small_chain():
    p = [5, 10, 3]

    s, cost = matrix_chain_order(p, len(p))

    assert cost == 150


def test_matrix_chain_order_two_matrices():
    p = [10, 20, 30]

    s, cost = matrix_chain_order(p, len(p))

    assert cost == 6000


def test_get_solution_single_matrix():
    matrices = ["5x10"]
    s = [[None]]

    assert get_solution(matrices, s, 1, 1) == "5x10"


def test_get_solution_clrs_example():
    p = [30, 35, 15, 5, 10, 20, 25]

    matrices = get_matrices_list(p)

    s, _ = matrix_chain_order(p, len(p))

    solution = get_solution(matrices, s, 1, len(p) - 1)

    assert isinstance(solution, str)
    assert "*" in solution


def test_solution_contains_all_matrices():
    p = [5, 10, 3, 12]

    matrices = get_matrices_list(p)

    s, _ = matrix_chain_order(p, len(p))

    solution = get_solution(matrices, s, 1, len(p) - 1)

    for matrix in matrices:
        assert matrix in solution


def test_first_subproblem_cost():
    p = [10, 20, 30]

    _, cost = matrix_chain_order(p, len(p))

    assert cost == 6000


def test_matrix_chain_order_clrs_example():
    p = [30, 35, 15, 5, 10, 20, 25]

    _, cost = matrix_chain_order(p, len(p))

    assert cost == 15125


def test_matrix_chain_order_two_matrices():
    p = [10, 20, 30]

    _, cost = matrix_chain_order(p, len(p))

    assert cost == 6000
