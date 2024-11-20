from profilehooks import profile


def fibonacci_rec(n: int) -> int:
    if n <= 2:
        return 1
    return fibonacci_rec(n - 1) + fibonacci_rec(n - 2)
    """Возвращает N-е число Фибоначчи. Реализована рекурсивно согласно
    формуле вычисления последовательности.

    :param n: порядковый номер числа Фибоначчи
    :return: число Фибоначчи
    """
    pass


def fibonacci_iter(n: int) -> int:
    if n <= 2:
        return 1
    mas = [0] * n
    mas[0] = 1
    mas[1] = 1
    for i in range(2, n):
        mas[i] = mas[i - 1] + mas[i - 2]
    return mas[n-1]
    """Возвращает N-е число Фибоначчи. Реализована итеративно с использованием
    массива для хранения вычисляемых данных.

    :param n: порядковый номер числа Фибоначчи
    :return: число Фибоначчи
    """
    pass


def fibonacci(n: int) -> int:
    prev = 1
    curr = 1
    for i in range(2, n):
        tmp = curr
        curr = tmp + prev
        prev = tmp
    return curr
    """Возвращает N-е число Фибоначчи. Реализована итеративно без использования массива.

    :param n: порядковый номер числа Фибоначчи
    :return: число Фибоначчи
    """
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
