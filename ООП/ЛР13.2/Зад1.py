import tkinter as tk
from tkinter import ttk

def calculate_income():
    amount = float(amount_entry.get())
    term = int(term_entry.get())
    rate = float(rate_entry.get())
    compound = compound_combobox.get()

    if compound == 'Простые проценты':
        income = amount + (amount * rate / 100) * (term / 365)
    elif compound == 'Сложные проценты':
        income = amount * (1 + rate / (100 * 12)) ** (term / 30)

    income_label['text'] = 'Доход по вкладу: ' + str(income)

root = tk.Tk()

amount_label = tk.Label(root, text='Сумма')
amount_label.pack()
amount_entry = tk.Entry(root)
amount_entry.pack()

term_label = tk.Label(root, text='Срок (дней)')
term_label.pack()
term_entry = tk.Entry(root)
term_entry.pack()

rate_label = tk.Label(root, text='Процентная ставка')
rate_label.pack()
rate_entry = tk.Entry(root)
rate_entry.pack()

compound_label = tk.Label(root, text='Схема начисления процентов')
compound_label.pack()
compound_combobox = ttk.Combobox(root, values=['Простые проценты', 'Сложные проценты'])
compound_combobox.pack()

calculate_button = tk.Button(root, text='Вычислить', command=calculate_income)
calculate_button.pack()

income_label = tk.Label(root, text='')
income_label.pack()

root.mainloop()
