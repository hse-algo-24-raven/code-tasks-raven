from typing import Any


class ErrorMessages():
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
    if lenght == 0:
        return []

    items = sorted(items)
    result = []
    total_permutations = __factorial(lenght)

    for _ in range(total_permutations):
        result.append(items[:])
        pivot_index = lenght - 2

        while pivot_index >= 0 and items[pivot_index] >= items[pivot_index + 1]:
            pivot_index -= 1

        if pivot_index < 0:
            break

        left = lenght - 1
        while items[pivot_index] >= items[left]:
            left -= 1

        items[pivot_index], items[left] = items[left], items[pivot_index]
        items = items[:pivot_index + 1] + items[pivot_index + 1:][::-1]

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
    last_number = [0 for _ in range(length)]
    result = []
    for i in range(length ** length):

        while length in last_number:
            index = last_number.index(length)
            last_number[index - 1] += 1
            last_number[index] = 0
        if len(last_number) == len(set(last_number)):
            result.append([items[_] for _ in last_number])
        last_number[-1] += 1

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
        raise TypeError(ErrorMessages.ERROR_ITEMS_NOT_IS_LIST)
    if len(set(array)) != len(array):
        raise ValueError(ErrorMessages.ERROR_DUPLICATE_ITEMS)


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
