# Ввод чисел с клавиатуры и запись в файл file1_NN.txt
N = int(input("Введите количество чисел: "))
numbers = []
for i in range(N):
    number = int(input("Введите число: "))
    numbers.append(number)

with open("file1_NN.txt", "w") as file:
    for number in numbers:
        file.write(str(number) + "\n")

# Чтение чисел из файла file1_NN.txt и запись четных чисел в файл file2_NN.txt в порядке убывания
even_numbers = []
with open("file1_NN.txt", "r") as file:
    for line in file:
        number = int(line.strip())
        if number % 2 == 0:
            even_numbers.append(number)

even_numbers.sort(reverse=True)

with open("file2_NN.txt", "w") as file:
    for number in even_numbers:
        file.write(str(number) + "\n")