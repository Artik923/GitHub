import tkinter as tk
from tkinter import messagebox
import random

numbers = []

def create_array():
    global numbers
    try:
        size = int(entry_size.get())
        numbers = [random.randint(-100, 100) for _ in range(size)]
        text_numbers.delete(1.0, tk.END)
        text_numbers.insert(tk.END, ' '.join(map(str, numbers)))
    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректное значение размера массива")

def calculate_min_max_sum():
    if numbers:
        min_num = min(numbers)
        max_num = max(numbers)
        sum_num = sum(numbers)
        if var_min.get():
            text_min.delete(1.0, tk.END)
            text_min.insert(tk.END, str(min_num))
        if var_max.get():
            text_max.delete(1.0, tk.END)
            text_max.insert(tk.END, str(max_num))
        if var_sum.get():
            text_sum.delete(1.0, tk.END)
            text_sum.insert(tk.END, str(sum_num))
    else:
        messagebox.showerror("Ошибка", "Массив пуст")

root = tk.Tk()
root.title("Число элементов")

label_size = tk.Label(root, text="Размер массива:")
label_size.pack()
entry_size = tk.Entry(root)
entry_size.pack()

button_create = tk.Button(root, text="Создать массив", command=create_array)
button_create.pack()

text_numbers = tk.Text(root, height=2)
text_numbers.pack()

var_min = tk.IntVar()
check_min = tk.Checkbutton(root, text="Минимальный элемент", variable=var_min)
check_min.pack()
text_min = tk.Text(root, height=1)
text_min.pack()

var_max = tk.IntVar()
check_max = tk.Checkbutton(root, text="Максимальный элемент", variable=var_max)
check_max.pack()
text_max = tk.Text(root, height=1)
text_max.pack()

var_sum = tk.IntVar()
check_sum = tk.Checkbutton(root, text="Сумма всех элементов", variable=var_sum)
check_sum.pack()
text_sum = tk.Text(root, height=1)
text_sum.pack()

button_calculate = tk.Button(root, text="Вычислить", command=calculate_min_max_sum)
button_calculate.pack()

root.mainloop()
