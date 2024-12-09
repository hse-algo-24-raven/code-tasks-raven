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


def __init_matrixes(profit_matrix):
    number_of_steps = len(profit_matrix)
    number_of_projects = len(profit_matrix[0])

    profit_matrix_extended = [None] * (number_of_steps + 1)
    profit_matrix_extended[0] = [0] * (number_of_projects + 1)
    for i in range(1, number_of_steps + 1):
        profit_matrix_extended[i] = [0, *profit_matrix[i - 1]]

    max_profit_matrix = [None] * (number_of_steps + 1)
    for i in range(number_of_steps + 1):
        max_profit_matrix[i] = [0] * (number_of_projects)
        max_profit_matrix[i][0] = profit_matrix_extended[i][1]

    backtrack = [None] * (number_of_steps + 1)
    for i in range(number_of_steps + 1):
        backtrack[i] = [0] * (number_of_projects - 1)

    return (
        number_of_steps,
        number_of_projects,
        profit_matrix_extended,
        max_profit_matrix,
        backtrack,
    )


def __all_checks(profit_matrix):
    if not isinstance(profit_matrix, list) or len(profit_matrix) == 0:
        raise ValueError(PARAM_ERR_MSG)

    for row_index in range(len(profit_matrix)):

        if (
            not isinstance(profit_matrix[row_index], list)
            or len(profit_matrix[row_index]) == 0
        ):
            raise ValueError(PARAM_ERR_MSG)

        if row_index != len(profit_matrix) - 1 and len(profit_matrix[row_index]) != len(
            profit_matrix[row_index + 1]
        ):
            raise ValueError(PARAM_ERR_MSG)

        for column_index in range(len(profit_matrix[0])):
            value = profit_matrix[row_index][column_index]

            if not isinstance(value, int):
                raise ValueError(PARAM_ERR_MSG)

            if row_index > 0:
                last_value = profit_matrix[row_index - 1][column_index]
                if last_value > value:
                    raise ProfitValueError(DECR_PROFIT_ERR_MSG, column_index, row_index)

            if value < 0:
                raise ProfitValueError(NEG_PROFIT_ERR_MSG, column_index, row_index)


def get_invest_distribution(
    profit_matrix: list[list[int]],
) -> dict[str:int, str: list[int]]:
    """Рассчитывает максимально возможную прибыль и распределение инвестиций
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
    distribution - распределение инвестиций между проектами.
    """

    __all_checks(profit_matrix)

    # В случае, если проект один
    if len(profit_matrix[0]) == 1:
        return {PROFIT: profit_matrix[-1][0], DISTRIBUTION: [len(profit_matrix)]}

    (
        number_of_steps,
        number_of_projects,
        profit_matrix_extended,
        max_profit_matrix,
        backtrack,
    ) = __init_matrixes(profit_matrix)

    for project_index in range(
        1, number_of_projects
    ):  # Проход по всем проектам от 1 до n
        for step_max_index in range(
            1, number_of_steps + 1
        ):  # Проход по всем макс. шагам инвестиций от 1 до n+1

            max_profit = 0
            max_amount = 0

            # first_project_step_index проходится по
            # индексам столбца из max_profit_matrix
            #
            # second_project_step_index проходится по
            # индексам столбца из profit_matrix_extended
            for first_project_step_index in range(
                step_max_index + 1
            ):  # Проход по всем шагам инвестиций от 0 до max+1
                second_project_step_index = step_max_index - first_project_step_index

                # +-1 из-за разницы в индексировании таблиц
                first_value = max_profit_matrix[first_project_step_index][
                    project_index - 1
                ]
                second_value = profit_matrix_extended[second_project_step_index][
                    project_index + 1
                ]

                sum_first_second = first_value + second_value

                if sum_first_second > max_profit:
                    # Значит выбрали first_value по
                    # first_project_step_index из сборного проекта
                    #
                    # и second_count по second_project_step_index из нового включаемого
                    max_profit = sum_first_second
                    max_amount = first_project_step_index

            max_profit_matrix[step_max_index][project_index] = max_profit
            backtrack[step_max_index][project_index - 1] = max_amount

    all_way = [0] * number_of_projects
    all_way[number_of_projects - 1] = backtrack[-1][-1]
    remains = number_of_steps
    for i in range(number_of_projects - 2, -1, -1):
        all_way[i] = backtrack[all_way[i + 1]][i - 1]
        all_way[i + 1], remains = remains - all_way[i + 1], all_way[i + 1]
    all_way[0] = remains
    return {PROFIT: max_profit_matrix[-1][-1], DISTRIBUTION: all_way}


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
