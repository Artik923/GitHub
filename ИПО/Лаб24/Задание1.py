def modify_array(arr):
    # Создаем новый список
    new_arr = []
    for num in arr:
        # Добавляем текущий элемент в новый список
        new_arr.append(num)
        # Если текущий элемент отрицательный, добавляем его квадрат в новый список
        if num < 0:
            new_arr.append(num**2)
    # Возвращаем новый список
    return new_arr

# Создание исходного массива для демонстрации работы функции
arr = [1, -2, 3, -4, 5]
# Вызов функции modify_array и сохранение результата в переменной modified_arr
modified_arr = modify_array(arr)
# Вывод результата на экран
print(modified_arr)
