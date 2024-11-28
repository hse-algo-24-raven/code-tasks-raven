from typing import Any


class ErrorMessages():
    """Класс для перечисления шаблонов сообщений об ошибках."""
    NON_LIST_PARAM = "Параметр items не является списком"
    ERROR_DUPLICATE = "Список элементов содержит дубликаты {}"



class Validator:
    """ Класс для валидации входных данных """

    @staticmethod
    def validate_items(items: list[Any]) ->  None:
        """Проверка кореектности входных данных
        :param items: список элементов
        :raise TypeError: если параметр items не является списком
        :raise ValueError: если список элементов содержит дубликаты
        """
        if not isinstance(items, list):
            raise TypeError(ErrorMessages.NON_LIST_PARAM)
        
        if len(items) != len(set(items)):
            raise ValueError(ErrorMessages.ERROR_DUPLICATE)
        

    

def generate_permutations(items: list[Any]) -> list[list[Any]]:
    """
    Генерирует все варианты перестановок элементов указанного множества
    :param items: список элементов
    :return: список перестановок, где каждая перестановка список элементов
    множества
    """

    Validator.validate_items(items)

    items_length = len(items)

    if items_length == 0:
         return []
    

    result_permutations = []
    additional_arr = [0] * items_length 
    result_permutations.append(items[:])

    begin = 0

    while begin < items_length:
        if additional_arr[begin] < begin:
            if begin % 2 == 0:
                    items[0], items[begin] = items[begin], items[0]
            else:
                    items[additional_arr[begin]], items[begin] = items[begin], items[additional_arr[begin]]
            result_permutations.append(items[:])
            additional_arr[begin] += 1
            begin = 0
        else:
            additional_arr[begin] = 0
            begin += 1

    return result_permutations

def main():
    items = [1, 2, 3]
    print(generate_permutations(items))


if __name__ == "__main__":
    main()
