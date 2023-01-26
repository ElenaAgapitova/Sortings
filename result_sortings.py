"""Результат сортировок"""

from selection_sort import selection_sort
from bubble_sort import bubble_sort
from quick_sort import quick_sort


nums_1: list = [0, -5, 2, 3, 5, 9, -1, 3]
nums_2: list = [0, -5, 2, 3, 5, 9, -1, 3]
nums_3: list = [0, -5, 2, 3, 5, 9, -1, 3]
print(f"Заданный список: {nums_1}")

# Результат сортировок:
print(f"Отсортированный список выбором: {selection_sort(nums_1)}")
print(f"Отсортированный список пузырьком: {bubble_sort(nums_2)}")
print(f"Отсортированный список быстрой сортировкой: {quick_sort(nums_3, 0, len(nums_3) - 1)}")
