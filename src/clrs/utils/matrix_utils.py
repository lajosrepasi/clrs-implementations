"""
Utility functions and a class for working with matrices.
"""

from clrs.utils.array_utils import gen_rand_array


def gen_rand_matrix(columns_num: int, rows_num: int, max_num: int) -> list[list[int]]:
    """Generate a matrix containing random integers."""
    matrix = []

    for _ in range(rows_num):
        row = gen_rand_array(max_num, columns_num)
        matrix.append(row)

    return matrix


def gen_empty_matrix(columns_num: int, rows_num: int) -> list[list[int]]:
    """Generate a matrix initialized with zeros."""
    matrix = []

    for _ in range(rows_num):
        row = [0 for _ in range(columns_num)]
        matrix.append(row)

    return matrix


def print_matrix(
    matrix: list[list[int]] | list[list[int | None]] | list[list[float | int]],
) -> None:
    """Print a matrix row by row."""
    for row in matrix:
        print(row)


def get_matrix_dimensions(m: list[list[int]]) -> tuple[int, int]:
    """Return the dimensions of a matrix as (columns, rows)."""
    return (len(m[0]), len(m))


def get_sub_matrix(
    start_column: int,
    start_row: int,
    columns_num: int,
    rows_num: int,
    matrix: list[list[int]],
):
    """Return a rectangular submatrix from the given matrix."""
    sub_matrix = gen_empty_matrix(columns_num, rows_num)

    for i in range(rows_num):
        for j in range(columns_num):
            sub_matrix[i][j] = matrix[start_row + i][start_column + j]

    return sub_matrix


def add_matrixes(m1: list[list[int]], m2: list[list[int]]) -> list[list[int]]:
    """Return the element-wise sum of two matrices."""
    (columns, rows) = get_matrix_dimensions(m1)
    added_matrix = gen_empty_matrix(columns, rows)

    for i in range(rows):
        for j in range(columns):
            added_matrix[i][j] = m1[i][j] + m2[i][j]

    return added_matrix


def sub_matrixes(m1: list[list[int]], m2: list[list[int]]) -> list[list[int]]:
    """Return the element-wise difference of two matrices."""
    (columns, rows) = get_matrix_dimensions(m1)
    added_matrix = gen_empty_matrix(columns, rows)

    for i in range(rows):
        for j in range(columns):
            added_matrix[i][j] = m1[i][j] - m2[i][j]

    return added_matrix


class Matrix:
    def __init__(self, m: list[list[int]]) -> None:
        self.m = m

    def __add__(self, other_matrix: "Matrix") -> "Matrix":
        return Matrix(add_matrixes(self.m, other_matrix.m))

    def __sub__(self, other_matrix: "Matrix") -> "Matrix":
        return Matrix(sub_matrixes(self.m, other_matrix.m))

    def dimensions(self) -> tuple[int, int]:
        return get_matrix_dimensions(self.m)

    def sub_matrix(
        self, start_column: int, start_row: int, columns_num: int, rows_num: int
    ) -> "Matrix":
        sub_matrix = Matrix(
            get_sub_matrix(start_column, start_row, columns_num, rows_num, self.m)
        )
        return sub_matrix

    def __str__(self):
        s = ""
        for row in self.m:
            s += str(row)
            s += "\n"

        return s


def join_4_matrixes(m1: Matrix, m2: Matrix, m3: Matrix, m4: Matrix) -> Matrix:
    (columns, rows) = m1.dimensions()
    c = gen_empty_matrix(columns * 2, rows * 2)

    for i in range(rows * 2):
        for j in range(columns * 2):
            if i < rows and j < columns:
                c[i][j] = m1.m[i][j]
            if i < rows and j >= columns:
                c[i][j] = m2.m[i][j - columns]
            if i >= rows and j < columns:
                c[i][j] = m3.m[i - rows][j]
            if i >= rows and j >= columns:
                c[i][j] = m4.m[i - rows][j - columns]

    return Matrix(c)


def main():
    m = gen_rand_matrix(5, 7, 100)
    print_matrix(m)

    print("empty matrix:")
    m_empty = gen_empty_matrix(5, 7)
    print_matrix(m_empty)

    print("sub matrix:")
    sub_matrix = get_sub_matrix(2, 3, 3, 3, m)

    print_matrix(sub_matrix)

    print("add matrixes:")
    m1 = gen_rand_matrix(5, 7, 100)
    print_matrix(m1)
    print()
    m2 = gen_rand_matrix(5, 7, 100)
    print()
    print_matrix(m2)
    added_matrix = add_matrixes(m1, m2)
    print()
    print_matrix(added_matrix)


if __name__ == "__main__":
    main()
