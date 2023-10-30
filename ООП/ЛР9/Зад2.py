import math

class ПрямоугольныйТреугольник:
    def __init__(self, катет1, катет2):
        self.катет1 = катет1
        self.катет2 = катет2

    def площадь(self):
        return 0.5 * self.катет1 * self.катет2

class ПроизвольныйТреугольник:
    def __init__(self, сторона1, сторона2, сторона3):
        self.сторона1 = сторона1
        self.сторона2 = сторона2
        self.сторона3 = сторона3

    def площадь(self):
        # Используем формулу Герона для нахождения площади произвольного треугольника
        s = (self.сторона1 + self.сторона2 + self.сторона3) / 2
        return math.sqrt(s * (s - self.сторона1) * (s - self.сторона2) * (s - self.сторона3))

# Создаем экземпляры классов
прямоугольный_треугольник = ПрямоугольныйТреугольник(3, 4)
произвольный_треугольник = ПроизвольныйТреугольник(5, 12, 13)

# Вызываем полиморфный метод для нахождения площади каждого треугольника
print(f"Площадь прямоугольного треугольника: {прямоугольный_треугольник.площадь()}")
print(f"Площадь произвольного треугольника: {произвольный_треугольник.площадь()}")
