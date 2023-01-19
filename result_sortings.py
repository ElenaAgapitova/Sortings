import selection_sort

nums: list = [7, 6, 3, 4, 5, 1, 2, 3]
print(f"Заданный список: {nums}")

# 1. Сортировка выбором:
print(f"Отсортированный список: {selection_sort.selection_sort(nums)}")
