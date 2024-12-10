INF = float("inf")
COST = "cost"
PATH = "path"
PARAM_ERR_MSG = (
    "Таблица цен не является прямоугольной матрицей с " "числовыми значениями"
)

def validate(price_table: list[list[float | int]]) -> None:
    """Проверяет корректность таблицы."""
    if not price_table or not isinstance(price_table, list) or not all(isinstance(row, list) for row in price_table):
        raise ValueError(PARAM_ERR_MSG)

    row_lengths = [len(row) for row in price_table]
    if len(set(row_lengths)) > 1:
        raise ValueError(PARAM_ERR_MSG)

    for row in price_table:
        if not all(isinstance(x, (int, float)) for x in row):
            raise ValueError(PARAM_ERR_MSG)

    if any(len(row) == 0 for row in price_table):
        raise ValueError(PARAM_ERR_MSG)


def get_min_cost_path(
    price_table: list[list[float | int]],
) -> dict[str:float, str : list[tuple[int, int]]]:
    """Возвращает путь минимальной стоимости в таблице из левого верхнего угла
    в правый нижний. Каждая ячейка в таблице имеет цену посещения. Перемещение
    из ячейки в ячейку можно производить только по горизонтали вправо или по
    вертикали вниз.
    :param price_table: Таблица с ценой посещения для каждой ячейки.
    :raise ValueError: Если таблица цен не является прямоугольной матрицей с
    числовыми значениями.
    :return: Словарь с ключами:
    cost - стоимость минимального пути,
    path - путь, список кортежей с индексами ячеек.
    """
    validate(price_table)

    rows = len(price_table)
    columns = len(price_table[0])
    
    cost = [[INF] * columns for _ in range(rows)]
    prev = [[None] * columns for _ in range(rows)]

    cost[0][0] = price_table[0][0]

    for i in range(rows):
        for j in range(columns):
            if i == 0 and j > 0:
                cost[i][j] = cost[i][j-1] + price_table[i][j]
                prev[i][j] = (i, j-1)
            elif j == 0 and i > 0:
                cost[i][j] = cost[i-1][j] + price_table[i][j]
                prev[i][j] = (i-1, j)
            elif i > 0 and j > 0:
                if cost[i-1][j] < cost[i][j-1]:
                    cost[i][j] = cost[i-1][j] + price_table[i][j]
                    prev[i][j] = (i-1, j)
                else:
                    cost[i][j] = cost[i][j-1] + price_table[i][j]
                    prev[i][j] = (i, j-1)

    path = []
    i = rows - 1 
    j = columns - 1
    
    while i is not None and j is not None:
        path.append((i, j))
        i, j = prev[i][j] if prev[i][j] is not None else (None, None)

    path.reverse()

    return {
        COST: cost[rows-1][columns-1],
        PATH: path
    }

def main():
    table = [[1, 2, 2], [3, 4, 2], [1, 1, 2]]
    print(get_min_cost_path(table))


if __name__ == "__main__":
    main()
