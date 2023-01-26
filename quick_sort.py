"""Быстрая сортировка: реально применимая, основана на рекурсии"""

from random import randint as RI


def quick_sort(numbers: list, left: int, right: int) -> list:
    """
    Быстрая сортировка.
    :param numbers: список чисел.
    :param left: левая граница.
    :param right: правая граница.
    :return: отсортированный список.
    """
    i = left
    j = right
    pivot = numbers[RI(left, right)]
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
        quick_sort(numbers, i, right)
    if left < j:
        quick_sort(numbers, left, j)
    return numbers
