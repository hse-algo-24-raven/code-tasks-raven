INF = float("inf")
COST = "cost"
PATH = "path"
PARAM_ERR_MSG = (
    "Таблица цен не является прямоугольной матрицей с " "числовыми значениями"
)

def is_table_empty(price_table):
    if not price_table or not price_table[0]:
        raise ValueError(PARAM_ERR_MSG)

def is_only_elem_none(price_table):
    if len(price_table) == 1 and len(price_table[0]) == 1 and price_table[0][0] is None:
        return {
            COST: None,
            PATH: None
        }

def validate_elems_on_price_table(price_table):
    row_len = len(price_table[0])
    for row in price_table:
        if len(row) != row_len:
            raise ValueError(PARAM_ERR_MSG)
        for elem in row:
            if elem is not None and not isinstance(elem, (int, float)):
                raise ValueError(PARAM_ERR_MSG)

def is_first_or_last_elems_none(price_table):
    rows = len(price_table)
    cols = len(price_table[0])
    if price_table[0][0] is None or price_table[rows - 1][cols - 1] is None:
        raise ValueError(PARAM_ERR_MSG)

def get_min_cost_path(
    price_table: list[list[float | int | None]],
) -> dict[str : float | None, str : list[tuple[int, int]] | None]:
    is_table_empty(price_table)

    is_only_elem_none(price_table)

    validate_elems_on_price_table(price_table)

    rows = len(price_table)
    cols = len(price_table[0])

    is_first_or_last_elems_none(price_table)

    dynamic_price_table = [[INF] * cols for row in range(rows)]
    dynamic_price_table[0][0] = price_table[0][0]

    for row in range(rows):
        for col in range(cols):
            if price_table[row][col] is None:
                continue

            if row > 0 and price_table[row - 1][col] is not None:
                dynamic_price_table[row][col] = min(dynamic_price_table[row][col], dynamic_price_table[row - 1][col] + price_table[row][col])

            if col > 0 and price_table[row][col - 1] is not None:
                dynamic_price_table[row][col] = min(dynamic_price_table[row][col], dynamic_price_table[row][col - 1] + price_table[row][col])

    if dynamic_price_table[rows - 1][cols - 1] == INF:
        return {
            COST: None,
            PATH: None
        }

    path = []
    row, col = rows - 1, cols - 1
    while row > 0 or col > 0:
        path.append((row, col))
        if row > 0 and dynamic_price_table[row][col] == dynamic_price_table[row - 1][col] + price_table[row][col]:
            row -= 1
        else:
            col -= 1
    path.append((0, 0))
    path.reverse()

    return {
        COST: dynamic_price_table[rows - 1][cols - 1],
        PATH: path
    }


def main():
    table = [[1, 2, 2], [3, None, 2], [None, 1, 2]]
    print(get_min_cost_path(table))


if __name__ == "__main__":
    main()
