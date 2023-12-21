def find_twins(n):
    twins = []
    for i in range(n, 2*n - 1):
        if is_prime(i) and is_prime(i + 2):
            twins.append((i, i + 2))
    return twins

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

n = int(input("Введите число n: "))
twins = find_twins(n)
print("Пары близнецов:")
for twin in twins:
    print(twin)

def find_max(matrix):
    max_val = matrix[0][0]
    max_i = 0
    max_j = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] > max_val:
                max_val = matrix[i][j]
                max_i = i
                max_j = j
    return max_i, max_j

def swap_max(matrix_a, matrix_b):
    max_i_a, max_j_a = find_max(matrix_a)
    max_i_b, max_j_b = find_max(matrix_b)
    
    matrix_a[max_i_a][max_j_a], matrix_b[max_i_b][max_j_b] = matrix_b[max_i_b][max_j_b], matrix_a[max_i_a][max_j_a]

matrix_A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix_B = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

print("Исходные матрицы:")
print("Матрица A:")
for row in matrix_A:
    print(row)
print("Матрица B:")
for row in matrix_B:
    print(row)

swap_max(matrix_A, matrix_B)

print("Матрицы после обмена максимальных элементов:")
print("Матрица A:")
for row in matrix_A:
    print(row)
print("Матрица B:")
for row in matrix_B:
    print(row)