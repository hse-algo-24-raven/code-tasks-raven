PROFIT = "profit"
DISTRIBUTION = "distribution"
PARAM_ERR_MSG = (
    "Таблица прибыли от проектов не является прямоугольной "
    "матрицей с числовыми значениями"
)
NEG_PROFIT_ERR_MSG = "Значение прибыли не может быть отрицательно"
DECR_PROFIT_ERR_MSG = "Значение прибыли не может убывать с ростом инвестиций"


class ProfitValueError(Exception):
    def __init__(self, message, project_idx, row_idx):
        self.project_idx = project_idx
        self.row_idx = row_idx
        super().__init__(message)


def get_invest_distribution(
        profit_matrix: list[list[int]],
) -> dict[str:int, str: list[int]]:
    """Рассчитывает максимально возможную прибыль и распределение инвестиций
    между несколькими проектами. Инвестиции распределяются кратными частями.
    :rtype: object
    :param profit_matrix: Таблица с распределением прибыли от проектов в
    зависимости от уровня инвестиций. Проекты указаны в столбцах, уровни
    инвестиций в строках.
    :raise ValueError: Если таблица прибыли от проектов не является
    прямоугольной матрицей с числовыми значениями.
    :raise ProfitValueError: Если значение прибыли отрицательно или убывает
    с ростом инвестиций.
    :return: Словарь с ключами:
    profit - максимально возможная прибыль от инвестиций,
    distribution - распределение инвестиций между проектами.
    """
    __validate_profit(profit_matrix)
    amount_projects = len(profit_matrix[0])
    parts_money = len(profit_matrix)

    extended_profit_matrix = [[0 for col in range(amount_projects + 1)]]
    extended_profit_matrix += [[0] + [col for col in row] for row in profit_matrix]

    extended_result_matrix = [[0] * (amount_projects + 1) for row in range(parts_money + 1)]

    for idx_col in range(1, amount_projects + 1):
        for idx_row in range(1, parts_money + 1):

            level_max = 0
            for level in range(idx_row + 1):
                prev_value = extended_result_matrix[level][idx_col - 1]
                cur_value = extended_profit_matrix[idx_row - level][idx_col]

                level_max = max(level_max, prev_value + cur_value)

            extended_result_matrix[idx_row][idx_col] = level_max
    result_profit = extended_result_matrix[-1][-1]

    distribution_list = []
    remaining_parts_money = parts_money
    balance = result_profit
    extended_remaining_profit_matrix = [[0] * (amount_projects + 1)]
    extended_remaining_profit_matrix += [[0] + [col for col in row] for row in profit_matrix]

    for idx_col in range(amount_projects, 0, -1):
        extended_remaining_profit_matrix[0][idx_col] = (
            extended_result_matrix)[parts_money - (amount_projects - idx_col)][idx_col - 1]
    idx_col = amount_projects
    idx_row = parts_money
    while remaining_parts_money > 0:

        cur_level_max = 0
        remaining_balance_max = 0
        profits = [profit[idx_col - 1] for profit in extended_result_matrix[:idx_row + 1]]
        for level in range(idx_row + 1):

            cur_waste = extended_remaining_profit_matrix[level][idx_col]
            cur_balance = balance - cur_waste
            if cur_balance in profits and cur_balance > remaining_balance_max:
                remaining_balance_max = cur_balance
                cur_level_max = level
        remaining_parts_money -= cur_level_max
        balance -= (balance - remaining_balance_max)
        distribution_list.append(cur_level_max)
        idx_col -= 1
        idx_row = remaining_parts_money

    while len(distribution_list) < amount_projects:
        distribution_list.append(0)
    distribution_list = distribution_list[::-1]

    result_distribution = {}
    result_distribution[PROFIT] = result_profit
    result_distribution[DISTRIBUTION] = distribution_list
    return result_distribution



def __validate_profit(matrix: list[list[int]]) -> None:
    """
    Проверяет матрицу на валидность,
    :param matrix: Таблица с распределением прибыли от проектов в
    зависимости от уровня инвестиций, которую нужно проверить
    :raise ValueError: Если таблица прибыли от проектов не является
    прямоугольной матрицей с числовыми значениями.
    :raise ProfitValueError: Если значение прибыли отрицательно или убывает
    с ростом инвестиций.
    """
    # Проверка на пустую матрицу
    if not matrix:
        raise ValueError(PARAM_ERR_MSG, 0, 0)

    for idx_row, row in enumerate(matrix):

        # Проверка на пустую строку в матрице
        if not row:
            raise ValueError(PARAM_ERR_MSG, 0, idx_row)

        # Проверка на прямоугольность матрицы
        if len(row) != len(matrix[0]):
            raise ValueError(PARAM_ERR_MSG, 0, idx_row)

        for idx_col, col in enumerate(row):

            # Проверка на целое число в столбце
            if not isinstance(col, int):
                raise ValueError(PARAM_ERR_MSG, idx_col, idx_row)

            # Проверка на неотрицательное число
            if col < 0:
                raise ProfitValueError(NEG_PROFIT_ERR_MSG, idx_col, idx_row)

    for idx_col, col in enumerate(matrix[0]):
        for idx_row in range(len(matrix) - 1):  # Берем len(matrix) - 1, так как проверяем текущий и следующий элемент

            # Проверка на увеличение прибыли
            if matrix[idx_row][idx_col] > matrix[idx_row + 1][idx_col]:
                raise ProfitValueError(DECR_PROFIT_ERR_MSG, idx_col, idx_row + 1)


def main():
    profit_matrix = [
        [15, 18, 16, 17],
        [20, 22, 23, 19],
        [26, 28, 27, 25],
        [34, 33, 29, 31],
        [40, 39, 41, 37],
    ]
    print(get_invest_distribution(profit_matrix))


if __name__ == "__main__":
    main()
