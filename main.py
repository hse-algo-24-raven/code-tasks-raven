PROFIT = "profit"
DISTRIBUTION = "distribution"
DISTRIBUTIONS = "distributions"
PARAM_ERR_MSG = (
    "Таблица прибыли от проектов не является прямоугольной "
    "матрицей с числовыми значениями."
)
NEG_PROFIT_ERR_MSG = "Значение прибыли не может быть отрицательным."
DECR_PROFIT_ERR_MSG = "Значение прибыли не может убывать с ростом инвестиций."


class ProfitValueError(Exception):
    def __init__(self, message, project_idx=None, row_idx=None):
        super().__init__(message)
        self.project_idx = project_idx
        self.row_idx = row_idx


def validate_matrix(matrix):
    """
    Проверяет корректность таблицы с распределением прибыли от проектов.
    :param matrix: Таблица с распределением прибыли от проектов.
    Проекты указаны в столбцах, уровни инвестиций в строках.
    :raise ValueError: если таблица:
     - None или пустая;
     - не является списком списков;
     - не является прямоугольной матрицей;
     - содержит некорректные (ненумерические) значения.
    :raise ProfitValueError: если:
     - значения прибыли отрицательные;
     - значения прибыли убывают при увеличении уровня инвестиций.
    """
    if not matrix or not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise ValueError(PARAM_ERR_MSG)

    if any(len(row) == 0 for row in matrix):
        raise ValueError(PARAM_ERR_MSG)

    row_length = len(matrix[0])
    for row_idx, row in enumerate(matrix):
        if len(row) != row_length:
            raise ValueError(PARAM_ERR_MSG)

        for col_idx, value in enumerate(row):
            if not isinstance(value, (int, float)):
                raise ValueError(PARAM_ERR_MSG)

            if value < 0:
                raise ProfitValueError(NEG_PROFIT_ERR_MSG, col_idx, row_idx)

    for project_idx in range(len(matrix[0])):
        for row_idx in range(1, len(matrix)):
            if matrix[row_idx][project_idx] < matrix[row_idx - 1][project_idx]:
                raise ProfitValueError(DECR_PROFIT_ERR_MSG, project_idx, row_idx)


def backtrack(project_idx, remaining_investment, current_distribution, profit_table, profit_matrix, num_investments, num_projects, distributions):
    """
    Вспомогательная функция для нахождения всех возможных вариантов распределения инвестиций между проектами.
    :param project_idx: Индекс текущего проекта.
    :param remaining_investment: Оставшийся объём инвестиций.
    :param current_distribution: Текущее распределение инвестиций.
    :param profit_table: Таблица с максимальными значениями прибыли.
    :param profit_matrix: Исходная таблица с распределением прибыли.
    :param num_investments: Общее количество уровней инвестиций.
    :param num_projects: Общее количество проектов.
    :param distributions: Список для хранения всех вариантов распределения.
    """
    if project_idx == 0:
        if remaining_investment == 0:
            distributions.append(current_distribution)
        return

    for investment_level in range(min(remaining_investment + 1, num_investments + 1)):
        if investment_level == 0 or remaining_investment >= investment_level:
            profit_without_current = profit_table[project_idx - 1][remaining_investment - investment_level] if investment_level > 0 else profit_table[project_idx - 1][remaining_investment]
            if profit_without_current + (profit_matrix[investment_level - 1][project_idx - 1] if investment_level > 0 and investment_level - 1 < num_investments else 0) == profit_table[project_idx][remaining_investment]:
                backtrack(project_idx - 1, remaining_investment - investment_level, [investment_level] + current_distribution, profit_table, profit_matrix, num_investments, num_projects, distributions)


def get_invest_distributions(profit_matrix: list[list[float]]) -> dict[str, float | list[list[int]]]:
    """
    Рассчитывает максимально возможную прибыль и распределение инвестиций
    между несколькими проектами. Инвестиции распределяются кратными частями.
    :param profit_matrix: Таблица с распределением прибыли от проектов в
    зависимости от уровня инвестиций. Проекты указаны в столбцах, уровни
    инвестиций в строках.
    :raise ValueError: Если таблица прибыли от проектов не является
    прямоугольной матрицей с числовыми значениями.
    :raise ProfitValueError: Если значение прибыли отрицательно или убывает
    с ростом инвестиций.
    :return: Словарь с ключами:
    profit - максимально возможная прибыль от инвестиций,
    distributions - список со всеми вариантами распределения инвестиций между
    проектами, обеспечивающими максимальную прибыль.
    """
    validate_matrix(profit_matrix)

    num_investments = len(profit_matrix)
    num_projects = len(profit_matrix[0])

    profit_table = [[0] * (num_investments + 1) for _ in range(num_projects + 1)]

    for project_idx in range(1, num_projects + 1):
        for investment_level in range(num_investments + 1):
            profit_table[project_idx][investment_level] = max(
                profit_table[project_idx - 1][investment_level - level] + profit_matrix[level - 1][project_idx - 1]
                if level > 0 and investment_level >= level else profit_table[project_idx - 1][investment_level]
                for level in range(min(investment_level + 1, num_investments + 1))
            )

    max_profit = profit_table[num_projects][num_investments]
    distributions = []

    backtrack(num_projects, num_investments, [], profit_table, profit_matrix, num_investments, num_projects, distributions)

    return {PROFIT: max_profit, DISTRIBUTIONS: distributions}


def main():
    profit_matrix = [[1, 2, 3], [2, 3, 5], [4, 6, 8]]
    result = get_invest_distributions(profit_matrix)
    print(result)


if __name__ == "__main__":
    main()
