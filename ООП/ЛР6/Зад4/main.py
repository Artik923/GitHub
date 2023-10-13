# Импортируем класс PotatoBed из модуля gryadka
from gryadka import PotatoBed

# Создаем объект класса PotatoBed с 5 грядками
graydka = PotatoBed(5)

# Выращиваем картошку на каждой грядке
for _ in range(3):
    graydka.grow_potatoes()
    
    # Вывод информации о каждой картофелине
    for potato in graydka.potatoes:
        print(f"Картошка {potato.number} сейчас {potato.get_stage()}")
    
    # Проверка созрела ли картошка
    if graydka.check_maturity():
        print("Вся картошка созрела. Можно собирать!")
    else:
        print("Картошка ещё не созрела!")
    
    print()