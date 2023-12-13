from tkinter import *  # Импортируем все из модуля tkinter
from tkinter import ttk  # Импортируем модуль ttk для использования виджета Progressbar

window = Tk()  # Создаем окно приложения
window.geometry("300x80")  # Задаем размер окна 300x80 пикселей

value_var = IntVar()  # Создаем переменную целого типа для отслеживания прогресса

# Создаем горизонтальный Progressbar длиной 280 пикселей, связанный с переменной value_var
pb = ttk.Progressbar(window, orient="vertical", length = 280, variable=value_var, mode = 'determinate')
pb.pack()  # Размещаем Progressbar в окне приложения

# Определяем функции start и stop для управления Progressbar
def start(): pb.start(100)  # Запускаем Progressbar с шагом 100
def stop(): pb.stop()  # Останавливаем Progressbar

# Создаем кнопки Start и Stop и связываем их с функциями start и stop соответственно
start_btn = ttk.Button(text="Start", command=start)
start_btn.pack()  # Размещаем кнопку Start в окне приложения
stop_btn = ttk.Button(text="Stop", command=stop)
stop_btn.pack()  # Размещаем кнопку Stop в окне приложения

window.mainloop()  # Запускаем главный цикл обработки событий
