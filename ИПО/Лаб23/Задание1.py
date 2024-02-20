import numpy as np

# Генерируем случайное количество строк и столбцов от 15 до 100
rows = np.random.randint(15, 101)
cols = np.random.randint(15, 101)

# Создаем массив с указанным количеством строк и столбцов,
# заполняем его случайными целыми числами от 1 до 1000
array = np.random.randint(1, 1001, size=(rows, cols))

# Выводим массив на экран
np.set_printoptions(threshold=np.inf)
print("Массив:")
print(array)

# Находим минимальный элемент в массиве
min_element = np.min(array)

# Выводим минимальный элемент на экран
print("Минимальный элемент в массиве:")
print(min_element)

# Вычисляем произведение матрицы на минимальный элемент
product = array * min_element

# Выводим результат на экран
print("Произведение матрицы на минимальный элемент:")
print(product)

