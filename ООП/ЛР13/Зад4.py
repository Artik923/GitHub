from tkinter import *
import random
import math

#Комманда, которая считает пример
def calculate():
    x = float(ent_x.get())
    result = math.log(math.sqrt(x) - 2 + 1.2) / (2 + math.exp(x) + math.sqrt(2) / math.sqrt(x))
    lab_result.configure(text = str(result))

# создание графического окна
window = Tk()
window.title("Формула")
window.geometry('300x200')

#Добавление надписи "Подсчет по формуле"
lab = Label(window, text="Подсчет по формуле", fg='blue', font=('Arial', 15))
lab.pack()

#Добавление надписи "x ="
lab_x = Label(window, text="x =", font=('Arial', 14))
lab_x.place(x=30, y=40)

ent_x = Entry(window, font=('Arial', 14), width=10)
ent_x.place(x=90, y=40)

#Добавление кнопки, которая запускает комманду calculate
btn = Button(window, text='Вычислить', font=('Arial', 14), width=9, command=calculate)
btn.place(x=92, y=70)

#Добавление надписи "Выражение ="
lab_v = Label(window, text="Выражение =", font=('Arial', 14))
lab_v.place(x=30, y=110)

#Добавление надписи "", куда потом заноситься результат вычисления
lab_result = Label(window, text="", font=('Arial', 14))
lab_result.place(x=150, y=110)

window.mainloop()
