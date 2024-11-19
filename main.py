from profilehooks import profile


def fibonacci_rec(n: int) -> int:
    """Возвращает N-е число Фибоначчи. Реализована рекурсивно согласно
    формуле вычисления последовательности.

    :param n: порядковый номер числа Фибоначчи
    :return: число Фибоначчи
    """
    return (fibonacci_rec(n - 1) + fibonacci_rec(n - 2)) if n > 2 else 1


def fibonacci_iter(n: int) -> int:
    """Возвращает N-е число Фибоначчи. Реализована итеративно с использованием
    массива для хранения вычисляемых данных.

    :param n: порядковый номер числа Фибоначчи
    :return: число Фибоначчи
    """
    prefix_fibonacci_list = [1] * max(n, 1)  # Как минимум 1 элемент
    for i in range(2, n):  # Если n <= 2, тогда тело цикла пропускается
        prefix_fibonacci_list[i] = (
            prefix_fibonacci_list[i - 1] + prefix_fibonacci_list[i - 2]
        )
    return prefix_fibonacci_list[-1]


def fibonacci(n: int) -> int:
    """Возвращает N-е число Фибоначчи. Реализована итеративно без использования массива.

    :param n: порядковый номер числа Фибоначчи
    :return: число Фибоначчи
    """
    current_element = previous_element = pre_previous_element = 1

    for i in range(2, n):  # Если n <= 2, тогда тело цикла пропускается
        current_element = previous_element + pre_previous_element
        pre_previous_element = previous_element
        previous_element = current_element
    return current_element


def main():
    n = 35
    print(f"Вычисление {n} числа Фибоначчи рекурсивно:")
    print(fibonacci_rec(n))

    print(f"\nВычисление {n} числа Фибоначчи итеративно:")
    print(fibonacci_iter(n))

    print(f"\nВычисление {n} числа Фибоначчи итеративно без использования массива:")
    print(fibonacci(n))


if __name__ == "__main__":
    main()
