def calculate_determinant(matrix: list[list[int]]) -> int:
    """Вычисляет определитель целочисленной квадратной матрицы

    :param matrix: целочисленная квадратная матрица
    :raise Exception: если значение параметра не является целочисленной
    квадратной матрицей
    :return: значение определителя матрицы - цело число
    """
    validate(matrix)
    order = len(matrix)
    if order == 1:
        return matrix[0][0]
    if order == 2:
        return matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
    
    row_with_max_zeros = find_row_with_max_zeros(matrix)
    
    det = 0
    for idx, value in enumerate(matrix[row_with_max_zeros]):
        if value == 0:
            continue
        minor = find_minor(matrix, idx, row=row_with_max_zeros)
        co_factor = (-1) ** (row_with_max_zeros + idx) * calculate_determinant(minor)
        det += value * co_factor
    return det  

def find_minor(matrix, col, row):
    """Возвращает минор, полученный удалением строки и столбца из матрицы
    
    :param matrix: исходная матрица 
    :param col: индекс столбца, который нужно удалить
    :param row: инлекс строки, которую нужно удалить
    :return: минорная матрица 
    """
    return [i[:col] + i[col + 1:] for i in matrix[:row] + matrix[row + 1:]]

def find_row_with_max_zeros(matrix: list[list[int]]) -> int:
    max_zeros = -1
    row_index = -1
    for i, row in enumerate(matrix):
        num_zeros = row.count(0)
        if num_zeros > max_zeros:
            max_zeros = num_zeros
            row_index = i
    if max_zeros == 0:
        return 0
    return row_index


def validate(matrix: list[list[int]]) -> None:
    """Проверяет исходные данные на корректность
    (входной параметр - не пустая матрица,
    все строки матрицы одинаковой длины,
    матрица д.б. квадратной)

    :param matrix: целочисленная квадратная матрица
    """
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise Exception("Входные данные должны быть непустым списком.")

    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise Exception("Каждая строка матрицы должна быть непустым списком.")

        for item in row:
            if not isinstance(item, int):
                raise Exception("Матрица должна содержать только целые числа.")
    
    row_length = len(matrix[0])
    if any(len(row) != row_length for row in matrix):
        raise Exception("Все строки матрицы должны быть одной длины.")

    if len(matrix) != row_length:
        raise Exception("Матрица должна быть квадратной.")


def main():
    matrix = [
            [3, 7, -5, 1, 19, 5, 0, -2, 4, 10],
            [-2, 2, 4, -6, 1, 0, 3, 5, 7, 1],
            [5, -5, -7, 5, 8, 9, -1, 0, 2, 2],
            [-4, 3, 5, -6, 17, -1, 9, 0, 2, 3],
            [3, -3, -5, 8, -9, -1, 0, 2, 4, 7],
            [-3, 2, 4, -6, 1, 0, 3, 5, 7, 11],
            [2, -5, -7, 7, 8, 9, -1, 0, -2, 5],
            [-4, 3, 15, -6, 7, -1, 9, 1, 2, 13],
            [3, -3, -5, 8, 9, -1, 0, 2, 4, 17],
            [-13, 2, 4, -6, 1, 0, -3, 5, 7, 1],
        ]
    print("Матрица")
    for row in matrix:
        print(row)

    print(f"Определитель матрицы равен {calculate_determinant(matrix)}")


if __name__ == "__main__":
    main()
