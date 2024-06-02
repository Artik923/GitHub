import numpy as np

# Создание одномерного массива
A = np.arange(12, 24)

# Создание двумерных массивов разной формы
B = A.reshape(3, 4)
C = A.reshape(4, 3)
D = A.reshape(2, 6)

print("Массив B:")
print(B)
print("Массив C:")
print(C)
print("Массив D:")
print(D)
