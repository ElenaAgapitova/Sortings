"""Быстрая сортировка: реально применимая, основана на рекурсии"""

from random import randint as ri


def quick_sort_1(numbers: list, left: int, right: int) -> list:
    """
    Быстрая сортировка c помощью рекурсии.
    :param numbers: список чисел.
    :param left: левая граница.
    :param right: правая граница.
    :return: отсортированный список.
    """
    i = left
    j = right
    pivot = numbers[ri(left, right)]
    while i <= j:
        while numbers[i] < pivot:
            i += 1
        while numbers[j] > pivot:
            j -= 1
        if i <= j:
            numbers[i], numbers[j] = numbers[j], numbers[i]
            i += 1
            j -= 1
    if i < right:
        quick_sort_1(numbers, i, right)
    if left < j:
        quick_sort_1(numbers, left, j)
    return numbers


def quick_sort_2(numbers: list) -> list:
    """
    Быстрая сортировка другой способ реализации.
    :param numbers: список чисел.
    :return: отсортированный список.
    """
    if len(numbers) <= 1:
        return numbers

    pivot = numbers[0]
    left = list(filter(lambda item: item < pivot, numbers))
    center = [item for item in numbers if item == pivot]
    right = list(filter(lambda item: item > pivot, numbers))

    return quick_sort_2(left) + center + quick_sort_2(right)
