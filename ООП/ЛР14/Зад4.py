from tkinter import *  # Импортируем все из модуля tkinter
from tkinter import ttk  # Импортируем модуль ttk для использования виджета Progressbar
import math  # Импортируем модуль math для использования функции cos

window = Tk()  # Создаем окно приложения
window.geometry("400x600")  # Задаем размер окно приложения 300x200 пикселей

value_var = DoubleVar()  # Создаем переменную типа DoubleVar для отслеживания прогресса

def tabulate():  # Определяем функцию tabulate для табулирования функции
    x = 0.01  # Задаем начальное значение x
    while x <= 0.9:  # Пока x не превысит 0.9
        y = 2.5 + math.cos(-x)  # Вычисляем значение функции y = 2.5 + cos(-x)
        listbox_x.insert(END, f"x={x:.2f}")  # Добавляем значение x в Listbox_x
        listbox_y.insert(END, f"y={y:.2f}")  # Добавляем значение y в Listbox_y
        value_var.set(x * 100)  # Обновляем значение Progressbar
        window.update()  # Обновляем окно, чтобы отобразить изменения
        x += 0.01  # Увеличиваем x на 0.01

# Создаем кнопку Start и связываем ее с функцией tabulate
start_btn = ttk.Button(text="Расчёт", command=tabulate)
start_btn.pack()  # Размещаем кнопку Start в окне приложения

listbox_x = Listbox(window, width=25, height=30)  # Создаем виджет Listbox (список) шириной 25 символов и высотой 30 строк для x
listbox_x.pack(side=LEFT)  # Размещаем Listbox_x в окне приложения слева

listbox_y = Listbox(window, width=25, height=30)  # Создаем виджет Listbox (список) шириной 25 символов и высотой 30 строк для y
listbox_y.pack(side=RIGHT)  # Размещаем Listbox_y в окне приложения справа

# Создаем горизонтальный Progressbar длиной 280 пикселей, связанный с переменной value_var
pb = ttk.Progressbar(window, orient="horizontal", length=280, variable=value_var, mode='determinate', maximum=90)
pb.pack()  # Размещаем Progressbar в окне приложения

window.mainloop()  # Запускаем главный цикл обработки событий
