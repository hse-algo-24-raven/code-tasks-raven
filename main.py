def validate_matrix(matrix: list[list[int]]):
    if matrix is None:
        raise Exception("Матрица не должна быть пустой")
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise Exception("Матрица должна быть непустым списком")
    
    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise Exception("Каждая строка матрицы должна быть непустым списком")
        for item in row:
            if not isinstance(item, int):
                raise Exception("Матрица должна состоять только из целых чисел")
    for row in matrix:
        if len(row) != len(matrix):
            raise Exception("Матрица должна быть квадратной")

def calculate_determinant(matrix: list[list[int]]) -> int:
    """Вычисляет определитель целочисленной квадратной матрицы

    :param matrix: целочисленная квадратная матрица
    :raise Exception: если значение параметра не является целочисленной
    квадратной матрицей
    :return: значение определителя
    """
    validate_matrix(matrix)

    if len(matrix) == 1:
        return matrix[0][0]
    
    determinant = 0
    for column_idx, value in enumerate(matrix[0]):
        reduced_matrix = [
            [item for col_idx, item in enumerate(row) if col_idx != column_idx]
            for idx, row in enumerate(matrix) if idx != 0
        ]
        co_factor = (-1)**column_idx * calculate_determinant(reduced_matrix)
        determinant += value * co_factor

    return determinant


def main():
    matrix = [[1, 2], [3, 4]]
    print("Матрица")
    for row in matrix:
        print(row)

    print(f"Определитель матрицы равен {calculate_determinant(matrix)}")


if __name__ == "__main__":
    main()
