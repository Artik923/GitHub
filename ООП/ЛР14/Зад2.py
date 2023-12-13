from tkinter import *  # Импортируем все из модуля tkinter

window = Tk()  # Создаем окно приложения

window.geometry("250x200")  # Задаем размер окна 250x200 пикселей

# Создаем виджет Listbox (список) с возможностью выбора нескольких элементов
list1 = Listbox(window, height = 5, width = 15, selectmode = EXTENDED)

# Создаем виджет Listbox (список) с возможностью выбора одного элемента
list2 = Listbox(window, height = 5, width = 15, selectmode = SINGLE)

# Определяем списки городов
lst1 = ['Минск', 'Молодечно', 'Борисов', 'Жодино', 'Воложин']
lst2 = ['Гродно', 'Ивье', 'Новогрудок', 'Ошмяны', 'Островец']

# Заполняем виджеты Listbox городами из списков
for i in lst1:
    list1.insert(END, i)
for i in lst2:
    list2.insert(END, i)

# Размещаем виджеты Listbox в окне приложения
list1.pack()
list2.pack()

window.mainloop()  # Запускаем главный цикл обработки событий
