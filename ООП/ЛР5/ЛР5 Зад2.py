class Fraction:
    def __init__(self, m, n): # Метод "__init__" инициализирует числитель и знаменатель объекта класса
        self.numerator = m
        self.denominator = n

    def multiply(self, other): # Метод "multiply" возвращает произведение двух дробей
        return f'{self.numerator}*{other.numerator}/{self.denominator}*{other.denominator}'

    def divide(self, other): # Метод "divide" возвращает частное двух дробей
        return f'{self.numerator}*{other.denominator}/{self.denominator}*{other.numerator}'

m2 = 4
n2 = 5
m1 = 2
n1 = 3
fraction1 = Fraction(m1, n1) # Создается объект "fraction1" класса "Fraction" с числителем "m1" и знаменателем "n1"
fraction2 = Fraction(m2, n2) # Создается объект "fraction2" класса "Fraction" с числителем "m2" и знаменателем "n2"
print(f'({m1}/{n1}) * ({m2}/{n2}) = ', fraction1.multiply(fraction2)) # Выводится результат умножения двух дробей
print(f'({m1}/{n1}) / ({m2}/{n2}) = ', fraction1.divide(fraction2)) # Выводится результат деления двух дробей