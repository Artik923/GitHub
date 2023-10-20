class Candy:
    def __init__(self, name, weight, sugar_content):
        self._name = name
        self._weight = weight
        self._sugar_content = sugar_content

    @property
    def name(self):
        return self._name

    @property
    def weight(self):
        return self._weight

    @property
    def sugar_content(self):
        return self._sugar_content

# Пример использования класса Candy
candy1 = Candy("Шоколад", 50, 10)
candy2 = Candy("Мармеладные мишки", 30, 20)
candy3 = Candy("Леденец", 15, 15)

gift = [candy1, candy2, candy3]

# Сортировка конфет в подарке по весу
sorted_gift = sorted(gift, key=lambda x: x.weight)
print("Подарки отсортерованные по весу:")
for candy in sorted_gift:
    print(candy.name)

# Поиск конфет в подарке, соответствующих заданному диапазону содержания сахара
min_sugar_content = 10
max_sugar_content = 20
matching_candies = [candy for candy in gift if min_sugar_content <= candy.sugar_content <= max_sugar_content]
print("Конфеты с количество сахара между", min_sugar_content, "и", max_sugar_content, ":")
for candy in matching_candies:
    print(candy.name)