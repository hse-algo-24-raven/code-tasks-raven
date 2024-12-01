from typing import Any


class Config():
    ERROR_ITEMS_NOT_IS_LIST = "Параметр items не является списком"
    ERROR_DUPLICATE_ITEMS = "Список элементов содержит дубликаты"


def generate_permutations(items: list[Any]) -> list[list[Any]]:
    """Генерирует все варианты перестановок элементов указанного множества
    :param items: список элементов
    :raise TypeError: если параметр items не является списком
    :raise ValueError: если список элементов содержит дубликаты
    :return: список перестановок, где каждая перестановка список элементов
    множества
    """
    __validate(items)
    lenght = len(items)
    items = sorted(items)
    result = []
    total_permutations = __factorial(lenght)

    for _ in range(total_permutations):
        result.append(items[:])
        k = lenght - 2

        while k >= 0 and items[k] >= items[k + 1]:
            k -= 1

        if k < 0:
            break

        left = lenght - 1
        while items[k] >= items[left]:
            left -= 1

        items[k], items[left] = items[left], items[k]
        items = items[:k + 1] + items[k + 1:][::-1]

    return result


def stupid_solution(items: list[Any]) -> list[list[Any]]:
    """
    Генерирует все варианты перестановок элементов указанного множества, не эффективно (O(n**n))
    :param items: список элементов
    :raise TypeError: если параметр items не является списком
    :raise ValueError: если список элементов содержит дубликаты
    :return: список перестановок, где каждая перестановка список элементов
    множества
    """
    __validate(items)
    length = len(items)
    if length == 0:
        return []
    x = [0 for _ in range(length)]
    result = []
    for i in range(length ** length):

        while length in x:
            index = x.index(length)
            x[index - 1] += 1
            x[index] = 0
        if len(x) == len(set(x)):
            result.append([items[_] for _ in x])
        x[-1] += 1

    return result


def __validate(array: list[Any]) -> None:
    """
    Проверяет список на правильность введенных данных
    :param array: проверяемый список
    :raise TypeError: если параметр items не является списком
    :raise ValueError: если список элементов содержит дубликаты
    :return: функция ничего не возвращает, если все ОК, то работа программы продолжится
    """
    if not isinstance(array, list):
        raise TypeError(Config.ERROR_ITEMS_NOT_IS_LIST)
    if len(set(array)) != len(array):
        raise ValueError(Config.ERROR_DUPLICATE_ITEMS)


def __factorial(n: int) -> int:
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def main():
    items = [1, 2]
    print(generate_permutations(items))


if __name__ == "__main__":
    main()
