import random
import time
from typing import List

# Декоратор для измерения времени выполнения функции
def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Запоминаем время начала выполнения функции
        result = func(*args, **kwargs)  # Выполняем функцию
        end_time = time.time()  # Запоминаем время окончания выполнения функции
        # Выводим размер списка и затраченное время
        print(f"Размер: {len(args[0])}, Потраченное время: {end_time - start_time} секунд")
        return result
    return wrapper

# Применяем декоратор к функции пузырьковой сортировки
@timer
def bubble_sort(lst: List[int]) -> List[int]:
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            # Если текущий элемент больше следующего
            if lst[j] > lst[j + 1]:
                # Меняем их местами
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

# Размеры списков для сортировки
sizes = [10, 100, 1000, 10000, 100000]

# Для каждого размера
for size in sizes:
    # Генерируем список случайных чисел
    lst = [random.randint(0, size) for _ in range(size)]
    # Сортируем список и замеряем время
    bubble_sort(lst)
