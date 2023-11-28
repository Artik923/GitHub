import random
import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Создание таблицы для хранения результатов
table = [["Количество элементов", "Время выполнения (секунды)"]]

# Задание количества элементов для эксперимента
num_elements = [10, 100, 1000, 10000, 100000]

# Измерение времени выполнения функции для каждого количества элементов
for n in num_elements:
    # Генерация случайного списка из n элементов
    arr = [random.randint(0, 100) for _ in range(n)]

    # Измерение времени выполнения функции
    start_time = time.time()
    bubble_sort(arr)
    end_time = time.time()

    # Вычисление времени выполнения в секундах
    execution_time = end_time - start_time

    # Добавление результатов в таблицу
    table.append([n, execution_time])

# Вывод таблицы
for row in table:
    print("{: <20} {: <30}".format(*row))