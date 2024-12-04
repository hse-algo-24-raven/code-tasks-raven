STR_LENGTH_ERROR_MSG = "Длина строки должна быть целым положительным числом"
"""Сообщение об ошибке при некорректном значении параметра Длина строки"""

NOT_INT_VALUE_TEMPL = "Параметр {0} Не является целым числом"
"""Шаблон сообщения об ошибке при нечисловом значении параметра"""

NEGATIVE_VALUE_TEMPL = "Параметр {0} отрицательный"
"""Шаблон сообщения об ошибке при отрицательном значении параметра"""

N_LESS_THAN_K_ERROR_MSG = "Параметр n меньше чем k"
"""Сообщение об ошибке при значении параметра n меньше чем k"""

def generate_strings(length: int) -> list[str]:
    """Возвращает строки заданной длины, состоящие из 0 и 1, где никакие
    два нуля не стоят рядом.

    :param length: Длина строки.
    :raise ValueError: Если длина строки не является целым положительным
    числом.
    :return: Список строк.
    """
    if not isinstance(length, int) or length <= 0:
        raise ValueError(STR_LENGTH_ERROR_MSG)

    if length == 1:
        return ["0", "1"]

    prev = generate_strings(length - 1)
    result = []
    for s in prev:
        if s[-1] == "0":
            result.append(s + "1")
        else:
            result.append(s + "0")
            result.append(s + "1")
    return result

def binomial_coefficient(n: int, k: int, use_rec=False) -> int:
    """Вычисляет биномиальный коэффициент из n по k.
    :param n: Количество элементов в множестве, из которого производится выбор.
    :param k: Количество элементов, которые нужно выбрать.
    :param use_rec: Использовать итеративную или рекурсивную реализацию функции.
    :raise ValueError: Если параметры не являются целыми неотрицательными
    числами или значение параметра n меньше чем k.
    :return: Значение биномиального коэффициента.
    """
    if not isinstance(n, int) or not isinstance(k, int) or n < 0 or k < 0:
        raise ValueError(STR_LENGTH_ERROR_MSG)
    if k > n:
        raise ValueError(N_LESS_THAN_K_ERROR_MSG)
    if use_rec:
        """ Рекурсивный способ """
        if k == 0 or k == n:
            return 1
        return binomial_coefficient(n - 1, k - 1) + binomial_coefficient(n - 1, k)
    else:
        """ Итеративный способ """
        k = min(k, n - k)
        c = 1
        for i in range(k):
            c = c * (n - i) // (i + 1)
        return c


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
