import numpy as np

# Определение матрицы
A = np.array([[1, 2], [3, 4]])

# Вычисление определителя
det_A = np.linalg.det(A)
print("Определитель матрицы A:", det_A)

# Решение системы уравнений
b = np.array([1, 2])
x = np.linalg.solve(A, b)
print("Решение системы уравнений Ax = b:", x)
