PATH_LENGTH_ERROR_MSG = "Длина маршрута должна быть целым положительным числом"
"""Сообщение об ошибке при некорректном значении параметра Длина маршрута"""

NOT_INT_VALUE_TEMPL = "Параметр {0} Не является целым числом"
"""Шаблон сообщения об ошибке при нечисловом значении параметра"""

NEGATIVE_VALUE_TEMPL = "Параметр {0} отрицательный"
"""Шаблон сообщения об ошибке при отрицательном значении параметра"""

N_LESS_THAN_K_ERROR_MSG = "Параметр n меньше чем k"
"""Сообщение об ошибке при значении параметра n меньше чем k"""

def validate_path_length(length):
    if length is None:
        raise ValueError(PATH_LENGTH_ERROR_MSG)
    if not isinstance(length, int):
        raise ValueError(PATH_LENGTH_ERROR_MSG)
    if isinstance(length, bool): 
        raise ValueError(PATH_LENGTH_ERROR_MSG)
    if length <= 0:
        raise ValueError(PATH_LENGTH_ERROR_MSG)
    
    
    
    

def get_triangle_path_count(length: int) -> int:
    """Вычисляет количество замкнутых маршрутов заданной длины между тремя
    вершинами треугольника A, B и C. Маршруты начинаются и оканчиваются в
    вершине A vertex. Допустимыми являются все пути между различными вершинами.
    :param length: Длина маршрута.
    :raise ValueError: Если длина маршрута не является целым положительным
    числом.
    :return: Количество маршрутов.
    """
    validate_path_length(length)
    return path_to_a(length)

def path_to_a(n):
    if n == 0:
        return 1
    return path_to_b(n-1) + path_to_c(n-1)

def path_to_b(n):
    if n == 0:
        return 0
    return path_to_a(n-1) + path_to_c(n-1)

def path_to_c(n):
    if n == 0:
        return 0
    return path_to_a(n-1) + path_to_b(n-1)


def validate_binomial_parameters(n, k):

    if not isinstance(n, int):
        raise ValueError(NOT_INT_VALUE_TEMPL.format("n"))
    
    if not isinstance(k, int):
        raise ValueError(NOT_INT_VALUE_TEMPL.format("k"))
    
    if k < 0:
        raise ValueError(NEGATIVE_VALUE_TEMPL.format("k"))
    
    if n < 0:
        raise ValueError(NEGATIVE_VALUE_TEMPL.format("n"))
    
    if n < k:
        raise ValueError(N_LESS_THAN_K_ERROR_MSG)


def binomial_coefficient(n: int, k: int, use_rec=False) -> int:
    """Вычисляет биномиальный коэффициент из n по k.
    :param n: Количество элементов в множестве, из которого производится выбор.
    :param k: Количество элементов, которые нужно выбрать.
    :param use_rec: Использовать итеративную или рекурсивную реализацию функции.
    :raise ValueError: Если параметры не являются целыми неотрицательными
    числами или значение параметра n меньше чем k.
    :return: Значение биномиального коэффициента.
    """
    validate_binomial_parameters(n, k)

    if use_rec:
        return binomial_recursive(n, k)
    return binomial_iterative(n, k)

def binomial_recursive(n, k):
    if k == 0 or n == k:
        return 1
    return binomial_recursive (n-1, k) + binomial_recursive(n - 1, k - 1)


def binomial_iterative(n, k):
    if k == 0 or n == k:
        return 1
    
    coefficient = 1
    for i in range(1, k + 1):
        coefficient *= n - (i - 1) 
        coefficient //= i

    return coefficient

def main():
    n = 10
    print(f"Количество маршрутов длиной {n} = {get_triangle_path_count(n)}")

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
