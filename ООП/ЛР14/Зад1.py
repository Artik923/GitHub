from tkinter import *
from tkinter import ttk

def save_info():
    info = f"Имя: {nameT.get()}\nФамилия: {lastNameT.get()}\nПол: {'мужской' if polvar.get() == 'm' else 'женский'}\nЛюбимые предметы: "
    subjects = []
    if var1.get() == 1:
        subjects.append('математика')
    if var2.get() == 1:
        subjects.append('английский язык')
    if var3.get() == 1:
        subjects.append('информационные технологии')
    info += ', '.join(subjects)
    with open('info.txt', 'w') as f:
        f.write(info)

window = Tk()
window.title('Регистрация')

name = Label(window, text = 'Имя', width = 20, height = 1, fg = 'green', font = 'arial 18')
lastName = Label(window, text = 'Фамилия', width = 20, height = 1, fg = 'green', font = 'arial 18')
pol = Label(window, text = 'Пол', width = 20, height = 1, fg = 'green', font = 'arial 18')
likePr = Label(window, text = 'Любимые предметы', width = 20, height = 1, fg = 'green', font = 'arial 18')

nameT = Entry(window, width = 30, font = 'arial 14')
lastNameT = Entry(window, width = 30, font = 'arial 14')

polvar = StringVar()
polvar.set(' ')
radio1 = Radiobutton(window, text = 'мужской', variable = polvar, value = 'm')
radio2 = Radiobutton(window, text = 'женский', variable = polvar, value = 'w')

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
check1 = Checkbutton(window, text = 'математика', variable = var1, onvalue = 1, offvalue = 0)
check2 = Checkbutton(window, text = 'английский язык', variable = var2, onvalue = 1, offvalue = 0)
check3 = Checkbutton(window, text = 'информационные технологии', variable = var3, onvalue = 1, offvalue = 0)

btn = Button(window, text = 'Принять', width = 25, height = 5, fg = 'green', font = 'arial 14', command = save_info)

name.pack()
nameT.pack()
lastName.pack()
lastNameT.pack()
pol.pack()
radio1.pack()
radio2.pack()
likePr.pack()
check1.pack()
check2.pack()
check3.pack()
btn.pack()

window.mainloop()