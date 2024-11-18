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
    


def fibonacci_iter(n: int) -> int:
    """Возвращает N-е число Фибоначчи. Реализована итеративно с использованием
    массива для хранения вычисляемых данных.

    :param n: порядковый номер числа Фибоначчи
    :return: число Фибоначчи
    """
    n_list = [1, 1]
    for i in range(2, n):
        n_list.append(n_list[i - 2] + n_list[i - 1])
    return n_list[-1]


def check(n:object) -> bool:
    """Проверяет n на условие положительного целого числа
    :param n: Проверяемое число
    :return: Результат проверки (True/False)
    """

    if not(isinstance(n, int)) or n < 1:
        return False
    return True


def fibonacci(n: int) -> int:
    """Возвращает N-е число Фибоначчи. Реализована итеративно без использования массива.

    :param n: порядковый номер числа Фибоначчи
    :return: число Фибоначчи
    """
    prev = 1
    current = 1
    for i in range(2, n):
        tmp = current
        current = tmp + prev
        prev = tmp
    return current

@profile()
def main():
    n = 35
    if check(n):
        print(f"Вычисление {n} числа Фибоначчи рекурсивно:")
        print(fibonacci_rec(n))

        print(f"\nВычисление {n} числа Фибоначчи итеративно:")
        print(fibonacci_iter(n))

        print(f"\nВычисление {n} числа Фибоначчи итеративно без использования массива:")
        print(fibonacci(n))
    else:
        print("Неверный ввод")

if __name__ == "__main__":
    main()
