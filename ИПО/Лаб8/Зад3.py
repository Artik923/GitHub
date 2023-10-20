sequence = input("Введите последовательность символов: ")

# Создаем пустое множество
char_set = set()

# Определяем гласные буквы английского алфавита
vowels = {'a', 'e', 'i', 'o', 'u'}

# Добавляем гласные буквы и цифру 5 в множество
for char in sequence:
    if char.lower() in vowels or char == '5':
        char_set.add(char)

print("Множество символов:", char_set)