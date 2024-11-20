from profilehooks import profile


def fibonacci_rec(n: int) -> int:
    """Возвращает N-е число Фибоначчи. Реализована рекурсивно согласно
    формуле вычисления последовательности.

    :param n: порядковый номер числа Фибоначчи
    :return: число Фибоначчи
    """
    if n <= 2:
        return 1
    return fibonacci_rec(n - 1) + fibonacci_rec(n - 2)
    pass


def fibonacci_iter(n: int) -> int:
    """Возвращает N-е число Фибоначчи. Реализована итеративно с использованием
    массива для хранения вычисляемых данных.

    :param n: порядковый номер числа Фибоначчи
    :return: число Фибоначчи
    """
    array = [1, 1]
    for i in range(2, n):
        array.append(array[i - 2] + array[i - 1])
    return array[-1]
    pass


def fibonacci(n: int) -> int:
    """Возвращает N-е число Фибоначчи. Реализована итеративно без использования массива.
        :param n: по
        рядковый номер числа Фибоначчи
        :return: число Фибоначчи
        """
    previous = 1
    current = 1
    for i in range(2, n):
        t = current
        current = t + previous
        previous = t
    return current
    pass


def main():
    n = 35
    print(f"Вычисление {n} числа Фибоначчи рекурсивно:")
    print(fibonacci_rec(n))

    print(f"\nВычисление {n} числа Фибоначчи итеративно:")
    print(fibonacci_iter(n))

    print(f"\nВычисление {n} числа Фибоначчи итеративно без использования массива:")
    print(fibonacci_iter(n))


if __name__ == "__main__":
    main()
