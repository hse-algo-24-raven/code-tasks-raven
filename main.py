STR_LENGTH_ERROR_MSG = "Длина строки должна быть целым положительным числом"
"""Сообщение об ошибке при некорректном значении параметра Длина строки"""

NOT_INT_VALUE_TEMPL = "Параметр {0} Не является целым числом"
"""Шаблон сообщения об ошибке при нечисловом значении параметра"""

NEGATIVE_VALUE_TEMPL = "Параметр {0} отрицательный"
"""Шаблон сообщения об ошибке при отрицательном значении параметра"""

N_LESS_THAN_K_ERROR_MSG = "Параметр n меньше чем k"
"""Сообщение об ошибке при значении параметра n меньше чем k"""


def generate_strings_end_1(n: int) -> list[str]:
    """Возвращает строки длиной n, которые заканчиваются на 1"""
    if n == 1:
        return ["1"]
    return [s + "1" for s in (generate_strings_end_1(n - 1) + generate_strings_end_0(n - 1))]
def generate_strings_end_0(n: int) -> list[str]:
    """Возвращает строки длиной n, которые заканчиваются на 0"""
    if n == 1:
        return ["0"]
    return [s + "0" for s in generate_strings_end_1(n - 1)]


def generate_strings(length: int) -> list[str]:
    """Возвращает строки заданной длины, состоящие из 0 и 1, где никакие
    два нуля не стоят рядом.

    :param length: Длина строки.
    :raise ValueError: Если длина строки не является целым положительным
    числом.
    :return: Список строк.
    """
    if not isinstance(length, int) or length <= 0 or isinstance(length, bool):
        raise ValueError(STR_LENGTH_ERROR_MSG)
    return generate_strings_end_1(length) + generate_strings_end_0(length)
    


def binomial_coefficient(n: int, k: int, use_rec=False) -> int:
    """Вычисляет биномиальный коэффициент из n по k.
    :param n: Количество элементов в множестве, из которого производится выбор.
    :param k: Количество элементов, которые нужно выбрать.
    :param use_rec: Использовать итеративную или рекурсивную реализацию функции.
    :raise ValueError: Если параметры не являются целыми неотрицательными
    числами или значение параметра n меньше чем k.
    :return: Значение биномиального коэффициента.
    """
    if not isinstance(n, int) or not isinstance(k, int):
        raise ValueError(NOT_INT_VALUE_TEMPL.format("n" if not isinstance(n, int) else "k"))
    if k < 0:
        raise ValueError(NEGATIVE_VALUE_TEMPL.format("k"))
    if n < 0:
        raise ValueError(NEGATIVE_VALUE_TEMPL.format("n"))
    if k > n:
        raise ValueError(N_LESS_THAN_K_ERROR_MSG)
    if use_rec:
        """рекурсивная реализация"""
        if k == n or k == 0:
            return 1
        return binomial_coefficient(n - 1, k) + binomial_coefficient(n - 1, k - 1)
    else:
        """итерационная реализация"""
        matrix = [[0] * (k + 1) for i in range(0, n + 1)]
        """заполним первый столбец и главную диагональ единицами. получим своеобразную базу"""
        for i in range(0, n + 1):
            matrix[i][0] = 1
        for i in range(1, k + 1):
            matrix[i][i] = 1
        for i in range(1, n + 1):
            for j in range(1, k + 1):
                matrix[i][j] = matrix[i - 1][j] + matrix[i - 1][j - 1]
        return matrix[n][k]
        


def main():
    n = 10
    print(f"Строки длиной {n}:\n{generate_strings(n)}")

    n = 30
    k = 20
    print(
        f"Биномиальный коэффициент (итеративно) при n, k ({n}, {k}) = ",
        binomial_coefficient(n, k),
    )
    print(
        f"Биномиальный коэффициент (рекурсивно) при n, k ({n}, {k}) = ",
        binomial_coefficient(n, k, use_rec=True),
    )


if __name__ == "__main__":
    main()
