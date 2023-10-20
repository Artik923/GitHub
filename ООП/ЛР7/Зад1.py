class Bird:
    def __init__(self, name, weight, wingspan, habitat, food):
        self._name = name
        self._weight = weight
        self._wingspan = wingspan
        self._habitat = habitat
        self._food = food

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        self._weight = value

    @property
    def wingspan(self):
        return self._wingspan

    @wingspan.setter
    def wingspan(self, value):
        self._wingspan = value

    @property
    def habitat(self):
        return self._habitat

    @habitat.setter
    def habitat(self, value):
        self._habitat = value

    @property
    def food(self):
        return self._food

    @food.setter
    def food(self, value):
        self._food = value

# Пример использования класса Bird
my_bird = Bird('Орел', 3.5, 2.1, 'Горы', 'Маленькие животные')
print('Название:', my_bird.name)
print('Вес:', my_bird.weight)
print('Размах крыльев:', my_bird.wingspan)
print('Место обитания:', my_bird.habitat)
print('Еда:', my_bird.food)