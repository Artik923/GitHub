import numpy as np

# Создание одномерного массива
A = np.arange(12)  # Изменим здесь 13 на 12, чтобы получить массив с 12 элементами

# Изменение формы массива для получения матрицы C
C = A.reshape(4, 3)

# Получение транспонированной матрицы C
CT = np.transpose(C)

# Умножение матрицы C на CT
B = np.dot(C, CT)

print("Матрица B:")
print(B)
