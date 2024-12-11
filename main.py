INF = float("inf")
COST = "cost"
PATH = "path"
PARAM_ERR_MSG = (
    "Таблица цен не является прямоугольной матрицей с " "числовыми значениями"
)


def get_min_cost_path(
    price_table: list[list[float | int | None]],
) -> dict[str : float | None, str : list[tuple[int, int]] | None]:
    if not price_table or not price_table[0]:
        raise ValueError(PARAM_ERR_MSG)

    if len(price_table) == 1 and len(price_table[0]) == 1 and price_table[0][0] is None:
        return {
            COST: None,
            PATH: None
        }

    row_len = len(price_table[0])
    for row in price_table:
        if len(row) != row_len:
            raise ValueError(PARAM_ERR_MSG)
        for elem in row:
            if elem is not None and not isinstance(elem, (int, float)):
                raise ValueError(PARAM_ERR_MSG)

    rows = len(price_table)
    cols = len(price_table[0])

    if price_table[0][0] is None or price_table[rows - 1][cols - 1] is None:
        raise ValueError(PARAM_ERR_MSG)

    dp = [[float(INF)] * cols for i in range(rows)]
    dp[0][0] = price_table[0][0]

    for i in range(rows):
        for j in range(cols):
            if price_table[i][j] is None:
                continue

            if i > 0 and price_table[i - 1][j] is not None:
                dp[i][j] = min(dp[i][j], dp[i - 1][j] + price_table[i][j])

            if j > 0 and price_table[i][j - 1] is not None:
                dp[i][j] = min(dp[i][j], dp[i][j - 1] + price_table[i][j])

    if dp[rows - 1][cols - 1] == float(INF):
        return {
            COST: None,
            PATH: None
        }

    path = []
    i, j = rows - 1, cols - 1
    while i > 0 or j > 0:
        path.append((i, j))
        if i > 0 and dp[i][j] == dp[i - 1][j] + price_table[i][j]:
            i -= 1
        else:
            j -= 1
    path.append((0, 0))
    path.reverse()

    return {
        COST: dp[rows - 1][cols - 1],
        PATH: path
    }


def main():
    table = [[1, 2, 2], [3, None, 2], [None, 1, 2]]
    print(get_min_cost_path(table))


if __name__ == "__main__":
    main()
