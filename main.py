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
    if n > 2:
        arr = [0]*n
        arr[0] = 1
        arr[1] = 1

        for i in range(2, n):
            arr[i] = arr[i-1] + arr[i-2]

        return arr[n-1]
    else:
        return 1
    

def fibonacci(n: int) -> int:
    """Возвращает N-е число Фибоначчи. Реализована итеративно без использования массива.

    :param n: порядковый номер числа Фибоначчи
    :return: число Фибоначчи
    """
    pred = 1
    pred_pred = 1
    result = 1

    for i in range(2, n):
        result = pred + pred_pred
        pred_pred = pred
        pred = result

    return result
    
def main():
    n = 3
    print(f"Вычисление {n} числа Фибоначчи рекурсивно:")
    print(fibonacci_rec(n))

    print(f"\nВычисление {n} числа Фибоначчи итеративно:")
    print(fibonacci_iter(n))

    print(f"\nВычисление {n} числа Фибоначчи итеративно без использования массива:")
    print(fibonacci(n))


if __name__ == "__main__":
    main()
