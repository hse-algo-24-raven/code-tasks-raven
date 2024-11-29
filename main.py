from collections import deque
from typing import Any

NOT_LIST_VALUE_TEMPL = "Параметр {0} не является списком"
"""Шаблон сообщения об ошибке при условии, что параметр не является списком"""

LIST_HAS_DUPLICATES = "Список элементов содержит дубликаты"
"""Сообщение об ошибке при условии, что в переданном списке был найден дубликат"""


def is_list_have_duplicates(items: list[Any]):
    """Проверка на то находится ли в массиве какой-либо дубликат
    :param array: список элементов
    :raise TypeError: если параметр array не является списком
    :return: True, если есть дубликат в списке, иначе False
    """

    if not isinstance(items, list):
        raise TypeError(NOT_LIST_VALUE_TEMPL.format("items"))

    dict_was_encountered = dict()
    for value in items:
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

    # Если items не список, то вызовется исключение из функции ниже
    if is_list_have_duplicates(items):
        raise ValueError(LIST_HAS_DUPLICATES)

    if len(items) == 0:
        return []

    queue = deque()
    queue.append([items[0]])

    for i in range(1, len(items)):
        for _ in range(len(queue)):
            current_permutation = queue.popleft()
            current_item = items[i]

            for j in range(len(current_permutation) + 1):
                queue.append(
                    current_permutation[:j] + [current_item] + current_permutation[j:]
                )
    return list(queue)


def main():
    items = [1, 2, 3]
    print(generate_permutations(items))


if __name__ == "__main__":
    main()
