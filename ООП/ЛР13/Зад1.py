from tkinter import *

#Комманда, которая закрывает графическое окно
def close_window():
    window.destroy ()

# создание графического окна
window = Tk()
window.title ("Проект 1")
window.geometry ('400x100')

#Добавление надписи "Moя первая программа"
lab = Label (window, text="Moя первая программа", font=('Arial', 14))
lab.pack()

#Добавление кнопки, которая закрывает графическое окно
btn = Button (window, text = 'Закрыть', font=('Arial', 14), command = close_window)
btn.pack()

window.mainloop ()
