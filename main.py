from profilehooks import profile


def fibonacci_rec(n: int) -> int:
    """Возвращает N-е число Фибоначчи. Реализована рекурсивно согласно
    формуле вычисления последовательности.

    :param n: порядковый номер числа Фибоначчи
    :return: число Фибоначчи
    """
    if n <= 2:
        return 1
    if n > 2:
        return fibonacci_rec(n-1) + fibonacci_rec(n-2)
    


def fibonacci_iter(n: int) -> int:
    """Возвращает N-е число Фибоначчи. Реализована итеративно с использованием
    массива для хранения вычисляемых данных.

    :param n: порядковый номер числа Фибоначчи
    :return: число Фибоначчи
    """
    if n <= 2:
        return 1
    
    fib_numbers = [0]*n
    fib_numbers[0] = 1
    fib_numbers[1] = 1

    for i in range(2, n):
        fib_numbers[i] = fib_numbers[i-1] + fib_numbers[i-2]

    return fib_numbers[n-1]


def fibonacci(n: int) -> int:
    """Возвращает N-е число Фибоначчи. Реализована итеративно без использования массива.

    :param n: порядковый номер числа Фибоначчи
    :return: число Фибоначчи
    """
    if n <= 2:
        return 1
    
    a = 1
    b = 1
    fib = 0
    for i in range(2, n):
        fib = a + b
        a = b
        b = fib

    return fib


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
