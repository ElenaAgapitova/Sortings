"""Модуль сортировки выбором"""


def selection_sort(numbers: list) -> list:
    """
    Функция сортировки выбором заданного списка от минимального к максимальному.
    Определяем индекс минимального элемента (изначально берем первый элемент),
    сравниваем элементы, если элемент меньше, записываем его индекс, в конце цикла
    переставляем элементы.
    :param numbers: заданный список.
    :return: отсортированный список.
    """
    for i in range(len(numbers) - 1):
        index_min = i
        for j in range(i + 1, len(numbers)):
            if numbers[j] < numbers[index_min]:
                index_min = j
        numbers[i], numbers[index_min] = numbers[index_min], numbers[i]
    return numbers
