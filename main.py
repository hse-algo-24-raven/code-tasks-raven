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

    @staticmethod
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


def get_invest_distributions(
    profit_matrix: list[list[float]],
) -> dict[str, float | list[list[int]]]:
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
    ProfitValueError.validate_matrix(profit_matrix)

    num_investments = len(profit_matrix)
    num_projects = len(profit_matrix[0])

    dp = [[0] * (num_investments + 1) for _ in range(num_projects + 1)]

    for proj in range(1, num_projects + 1):
        for invest in range(num_investments + 1):
            dp[proj][invest] = max(
                dp[proj - 1][invest - k] + profit_matrix[k - 1][proj - 1]
                if k > 0 and invest >= k else dp[proj - 1][invest]
                for k in range(min(invest + 1, num_investments + 1))
            )

    max_profit = dp[num_projects][num_investments]

    distributions = []

    def backtrack(project_idx, remaining_invest, current_distribution):
        if project_idx == 0:
            if remaining_invest == 0:
                distributions.append(current_distribution)
            return

        for k in range(min(remaining_invest + 1, num_investments + 1)):
            if k == 0 or remaining_invest >= k:
                profit_without_current = dp[project_idx - 1][remaining_invest - k] if k > 0 else dp[project_idx - 1][remaining_invest]
                if profit_without_current + (profit_matrix[k - 1][project_idx - 1] if k > 0 and k - 1 < num_investments else 0) == dp[project_idx][remaining_invest]:
                    backtrack(project_idx - 1, remaining_invest - k, [k] + current_distribution)

    backtrack(num_projects, num_investments, [])
    return {"profit": max_profit, "distributions": distributions}


def main():
    profit_matrix = [[1, 2, 3], [2, 3, 5], [4, 6, 8]]
    print(get_invest_distributions(profit_matrix))


if __name__ == "__main__":
    main()
