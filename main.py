import random
import numpy as np

MATRIX = "matrix"
DET = "determinant"


def get_random_matrix_and_det(size):
    det = random.randint(-1000, 1000)

    if isinstance(size, int) and isinstance(det, int) and size <= 0:
        raise Exception("Некорректный тип данных или размер матрицы")
    if size == 1:
        return [[det]], det

    while True:
        matrix = [[0] * size for i in range(size)]
        diag_elems = [1] * (size - 1) + [det]
        random.shuffle(diag_elems)
        for i in range(size):
            matrix[i][i] = diag_elems[i]

        for i in range(random.randint(size, size * 3)):
            row1, row2 = random.sample(range(size), 2)
            coeff = random.randint(-2, 2)
            for j in range(size):
                matrix[row1][j] += coeff * matrix[row2][j]

        for i in range(random.randint(size, size * 3)):
            column1, column2 = random.sample(range(size), 2)
            coeff = random.randint(-2, 2)
            for j in range(size):
                matrix[j][column1] += coeff * matrix[j][column2]

        zero_count = sum(cell == 0 for row in matrix for cell in row)
        count_elements = size * size

        if zero_count / count_elements <= 0.1:
            break

    return {MATRIX: matrix, DET: det}


def main():
    n = 10
    print(f"Генерация матрицы порядка {n}")
    result = get_matrix(n)
    print("\nОпределитель сгенерированной матрицы равен", result[DET])
    print("\n".join(["\t".join([str(cell) for cell in row]) for row in result[MATRIX]]))
    print(
        "\nОпределитель, рассчитанный numpy, равен",
        round(np.linalg.det(np.array(result[MATRIX]))),
    )


if __name__ == "__main__":
    main()
