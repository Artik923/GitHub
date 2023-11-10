#Класс для представления дробей в виде числителя и знаменателя
class Drob(object):

    #Инициализация объекта дроби с числителем a и знаменателем b
    def __init__(self, a=0, b=1):
        self.a = a
        self.b = b
        self.normalize()

    #Приведение дроби к каноническому виду
    def normalize(self):
        gcd = self.gcd(self.a, self.b)
        self.a //= gcd
        self.b //= gcd

    #Нахождение наибольшего общего делителя
    def gcd(self, x, y):
        while y != 0:
            x, y = y, x % y
        return x

    #Преобразование объекта дроби в строку для вывода
    def __str__(self):
        return '{}/{}'.format(self.a, self.b)

    #Проверка равенства двух дробей
    def __eq__(self, other):
        return self.a * other.b == self.b * other.a

    #Проверка, является ли одна дробь меньшей другой
    def __lt__(self, other):
        return self.a * other.b < self.b * other.a

    #Сложение дробей
    def __add__(self, other):
        new_a = self.a * other.b + other.a * self.b
        new_b = self.b * other.b
        return Drob(new_a, new_b)

    #Вычитание одной дроби из другой
    def __sub__(self, other):
        new_a = self.a * other.b - other.a * self.b
        new_b = self.b * other.b
        return Drob(new_a, new_b)

    #Умножение дробей
    def __mul__(self, other):
        new_a = self.a * other.a
        new_b = self.b * other.b
        return Drob(new_a, new_b)

    #Деление одной дроби на другую
    def __truediv__(self, other):
        new_a = self.a * other.b
        new_b = self.b * other.a
        return Drob(new_a, new_b)


# Проверка функций
drob1 = Drob(5, 3)
drob2 = Drob(4, 8)

print(drob1 == drob2)
print(drob1 < drob2)
print(drob1 + drob2)
print(drob1 - drob2)
print(drob1 * drob2)
print(drob1 / drob2)