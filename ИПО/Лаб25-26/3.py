import numpy as np

# Создание массива из случайных чисел
A = np.random.normal(loc=0, scale=1, size=(3, 4))

# Получение одномерного массива с таким же размером
A_flattened = A.flatten()

print("Одномерный массив A_flattened:")
print(A_flattened)
