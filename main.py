from collections import deque

def rabbits(target_month: int, rabbit_lifetime: int) -> int:
    if target_month <= 2:
        return 1
    
    rabbits_age = deque([0] * rabbit_lifetime)
    rabbits_age[0] = 1
    rabbits_age[1] = 1
    
    for i in range(2, target_month):
        rabbits_age.appendleft(rabbits_age[0] + rabbits_age[1] - rabbits_age.pop())

    return (rabbits_age[0])

def main():
    n = 35
    lifetime = 5
    print(f"\nВычисление числа пар кроликов по состоянию на {n} месяц")
    print(f"при продолжительности жизни кролика {lifetime} месяцев")
    print("количество пар кроликов составит:", rabbits(n, lifetime))


if __name__ == "__main__":
    main()
