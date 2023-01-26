"""Сортировка пузырьком"""


def bubble_sort(numbers: list) -> list:
    """
    Функция сортировки списка пузырьком. Переставляем соседние элементы.
    :param numbers: заданный список.
    :return: отсортированный список
    """
    for i in range(len(numbers) // 2 + 1):
        for j in range(len(numbers) - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers
