from tkinter import *

#Комманда, которая меняет текст при нажатии на кнопку
def clicked():
    lab.configure(text='Первые и не последние!', font=('Arial', 20), fg='red')

#Комманда, которая закрывает графическое окно
def close_window():
    window.destroy()

# создание графического окна
window = Tk()
window.title('Проект 2')
window.geometry('400x100')

#Добавление надписи 'Первые успехи!'
lab = Label(window, text='Первые успехи!', font=('Arial', 20), fg='blue')
lab.grid(column=1, row=0)

#Добавление кнопки, которая заменяет фразу 'Первые успехи!' на 'Первые и не последние!'
btn = Button(window, text='Приветствие', font=('Arial', 14), command=clicked)
btn.grid(column=0, row=1)

#Добавление кнопки, которая закрывает графическое окно
btn1 = Button(window, text='Закрыть', font=('Arial', 14), command=close_window)
btn1.grid(column=2, row=1)

window.mainloop()
