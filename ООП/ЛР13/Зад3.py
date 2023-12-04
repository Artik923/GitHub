import random
from tkinter import *

#Комманда, которая выдает на кубике случайное целое число от 1 до 6
def roll_dice():
    dice_value = random.randint(1, 6)
    label.config(text=str(dice_value))

# создание графического окна
window = Tk()
window.title("Брось кубик")
window.geometry('400x200')

#Добавление надписи "Брось кубик"
label = Label(window, text="Брось кубик", font=("Arial", 30),fg='blue')
label.pack()

#Добавление кнопки, которая выполняет комманду roll_dice
button = Button(window, text="Бросить кубик",font=("Arial", 20), command=roll_dice)
button.pack()

window.mainloop()
