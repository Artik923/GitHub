films = ("Звездные войны", "Мстители", "Титаник", "Трансформеры", "Чужой", "Рембо", "Терминатор")  # Создаем кортеж films, содержащий названия фильмов
print(films)

new_tu = tuple(films[:3])   # Создаем новый кортеж new_tu, который содержит первые три фильма из кортежа films
new_tu2 = tuple(films[3:])  # Создаем новый кортеж new_tu2, который содержит оставшиеся четыре фильма из кортежа films
all_tu = (films, new_tu, new_tu2)    # Объединяем все три кортежа в один кортеж all_tu
# Выводим значения new_tu, new_tu2 и all_tu
print(new_tu)
print(new_tu2)
print(all_tu)