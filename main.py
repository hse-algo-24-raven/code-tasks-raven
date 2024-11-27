def validate(matrix: list[list[int]]):
    if matrix is None:
        raise Exception("Параметр не является трехдиагональной матрицей")

    n = len(matrix)

    if n == 0:
        raise Exception("Параметр не является трехдиагональной матрицей")

    for i in matrix:
        if len(i) != n:
            raise Exception("Параметр не является трехдиагональной матрицей")

    for i in range(n):
        for j in range(n):
            if abs(i - j) >= 2:
                if matrix[i][j] != 0:
                    raise Exception("Параметр не является трехдиагональной матрицей")
            else:
                if matrix[i][j] != matrix[-1 * j - 1][-1 * i - 1]:
                    raise Exception("Параметр не является трехдиагональной матрицей")


def get_tridiagonal_determinant(matrix: list[list[int]]) -> int:
    """Вычисляет определитель трехдиагональной целочисленной квадратной матрицы.
    :param matrix: целочисленная трехдиагональная квадратная матрица.

    :return: значение определителя.
    """

    validate(matrix)

    n = len(matrix)

    #Определитель 1x1 матрицы
    if n == 1:
        return matrix[0][0]

    #Создаём массив для хранения подопределителей
    det = [0] * n
    det[0] = matrix[0][0]  #Определитель 1x1
    det[1] = matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]  #Определитель 2x2

    #Вычисляем определитель
    for i in range(2, n):
        det[i] = (matrix[i][i] * det[i - 1]
                  - matrix[i][i - 1] * matrix[i - 1][i] * det[i - 2])

    return det[n - 1]


def main():
    matrix = [[2, -3, 0, 0], [5, 2, -3, 0], [0, 5, 2, -3], [0, 0, 5, 2]]
    print("Трехдиагональная матрица")
    for row in matrix:
        print(row)

    print(f"Определитель матрицы равен {get_tridiagonal_determinant(matrix)}")


if __name__ == "__main__":
    main()
