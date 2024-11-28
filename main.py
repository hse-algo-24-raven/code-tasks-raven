from collections import deque
from typing import Any


def is_list_have_duplicates(array: list[Any]):
    """Проверка на то находится ли в массиве какой-либо дубликат
    :param array: список элементов
    :raise TypeError: если параметр array не является списком
    :return: True, если есть дубликат в списке, иначе False
    """

    if not isinstance(array, list):
        raise TypeError("Параметр array не является списком")

    dict_was_encountered = dict()
    for value in array:
        if value in dict_was_encountered and dict_was_encountered[value]:
            return True
        dict_was_encountered[value] = True
    return False


def generate_permutations(items: list[Any]) -> list[list[Any]]:
    """Генерирует все варианты перестановок элементов указанного множества
    :param items: список элементов
    :raise TypeError: если параметр items не является списком
    :raise ValueError: если список элементов содержит дубликаты
    :return: список перестановок, где каждая перестановка список элементов
    множества
    """

    if not isinstance(items, list):
        raise TypeError("Параметр items не является списком")

    if is_list_have_duplicates(items):
        raise ValueError("Список элементов содержит дубликаты")

    if len(items) == 0:
        return []

    queue = deque()
    queue.append([items[0]] if len(items) != 0 else [])

    for i in range(1, len(items)):
        n = len(queue)
        for j in range(n):
            a = queue.popleft()
            b = items[i]

            for k in range(len(a) + 1):
                queue.append(a[:k] + [b] + a[k:])
    return list(queue)


def main():
    items = [1, 2, 3]
    print(generate_permutations(items))


if __name__ == "__main__":
    main()
