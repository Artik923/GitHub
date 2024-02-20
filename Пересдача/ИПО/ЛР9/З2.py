# Функция для поиска максимального элемента в матрице
def find_max(matrix):
    max_val = matrix[0][0]  # Начальное максимальное значение
    max_i = 0  # Индекс строки максимального значения
    max_j = 0  # Индекс столбца максимального значения
    for i in range(len(matrix)):  # Проходим по всем строкам матрицы
        for j in range(len(matrix[i])):  # Проходим по всем элементам строки
            if matrix[i][j] > max_val:  # Если текущий элемент больше максимального
                max_val = matrix[i][j]  # Обновляем максимальное значение
                max_i = i  # Обновляем индекс строки
                max_j = j  # Обновляем индекс столбца
    return max_i, max_j  # Возвращаем индексы максимального элемента

# Функция для обмена максимальных элементов двух матриц
def swap_max(matrix_a, matrix_b):
    max_i_a, max_j_a = find_max(matrix_a)  # Находим максимальный элемент первой матрицы
    max_i_b, max_j_b = find_max(matrix_b)  # Находим максимальный элемент второй матрицы
    
    # Обмениваем максимальные элементы матриц
    matrix_a[max_i_a][max_j_a], matrix_b[max_i_b][max_j_b] = matrix_b[max_i_b][max_j_b], matrix_a[max_i_a][max_j_a]

# Исходные матрицы
matrix_A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix_B = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

print("Исходные матрицы:")
print("Матрица A:")
for row in matrix_A:  # Выводим каждую строку матрицы A
    print(row)
print("Матрица B:")
for row in matrix_B:  # Выводим каждую строку матрицы B
    print(row)

# Обмениваем максимальные элементы матриц
swap_max(matrix_A, matrix_B)

print("Матрицы после обмена максимальных элементов:")
print("Матрица A:")
for row in matrix_A:  # Выводим каждую строку матрицы A
    print(row)
print("Матрица B:")
for row in matrix_B:  # Выводим каждую строку матрицы B
    print(row)
