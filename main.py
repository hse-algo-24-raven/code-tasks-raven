from exceptions import *

def get_tridiagonal_determinant(matrix: list[list[int]]) -> int:
    """Вычисляет определитель трехдиагональной целочисленной квадратной матрицы.
    :param matrix: целочисленная трехдиагональная квадратная матрица.

    :return: значение определителя.
    """
    validate(matrix)


def validate(matrix: list[list[int]]):
    if not matrix:
        raise EmptyListException()
    if len(matrix) == 0:
        raise EmptyListException()

    for idx_row, row in enumerate(matrix):
        if len(row) == 0:
            raise EmptyListException()

        if len(row) != len(matrix[0]) or len(row) != len(matrix):
            raise NotSquareMatrixException()

        if matrix[idx_row - 1][idx_row - 1] != matrix[idx_row][idx_row]:
            raise ItemMatrixException()

        if idx_row < len(matrix) - 1:
            if matrix[idx_row - 1][idx_row] != matrix[idx_row][idx_row + 1]:
                raise ItemMatrixException()

        if idx_row > 1:
            if matrix[idx_row - 1][idx_row - 1] != matrix[idx_row][idx_row - 1]:
                raise ItemMatrixException()

        if idx_row < len(matrix) - 1 and idx_row > 0:
            if row.count(0) != len(row) - 3:
                raise ItemMatrixException()
        else:
            if row.count(0) != len(row) - 2:
                raise ItemMatrixException()

        for idx_item, item in enumerate(row):
            if not isinstance(item, int):
                raise ItemMatrixException()





def main():
    matrix = [[2, -3, 0, 0], [5, 2, -3, 0], [0, 5, 2, -3], [0, 0, 5, 2]]
    print("Трехдиагональная матрица")
    for row in matrix:
        print(row)

    print(f"Определитель матрицы равен {get_tridiagonal_determinant(matrix)}")


if __name__ == "__main__":
    main()
