from profilehooks import profile

def fibonacci_rec(n: int) -> int:
    if n == 0:
        return 0
    elif n <= 2:
        return 1
    else:
        return fibonacci_rec(n - 1) + fibonacci_rec(n - 2)

def fibonacci_iter(n: int) -> int:
    fibonacci_m = [1, 1]
    for i in range(2, n):
        fibonacci_m += [fibonacci_m[i - 1] + fibonacci_m[i - 2]]
    return fibonacci_m[n - 1]

def fibonacci(n: int) -> int:
    fibonacci_a = 1
    fibonacci_b = 1
    fibonacci_c = 0
    if n <= 2:
        return 1
    for i in range(2, n):
        fibonacci_c = fibonacci_a + fibonacci_b
        fibonacci_a = fibonacci_b
        fibonacci_b = fibonacci_c
    return fibonacci_c

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