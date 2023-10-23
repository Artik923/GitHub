class Vector:
    def __init__(self, *args):
        self.values = sorted([arg for arg in args if isinstance(arg, int)])

    def __str__(self):
        if len(self.values) == 0:
            return "Пустой вектор"
        else:
            return f"Вектор({', '.join(str(val) for val in self.values)})"

    def __add__(self, other):
        if isinstance(other, int):
            new_values = [val + other for val in self.values]
            return Vector(*new_values)
        elif isinstance(other, Vector):
            if len(self.values) != len(other.values):
                return "Сложение векторов разной длины недопустимо"
            else:
                new_values = [self.values[i] + other.values[i] for i in range(len(self.values))]
                return Vector(*new_values)
        else:
            return f"Вектор нельзя сложить с {type(other).__name__}"

    def __mul__(self, scalar):
        if isinstance(scalar, int):
            new_values = [val * scalar for val in self.values]
            return Vector(*new_values)
        elif isinstance(scalar, Vector):
            if len(self.values) != len(scalar.values):
                return "Умножение векторов разной длины недопустимо"
            else:
                new_values = [self.values[i] * scalar.values[i] for i in range(len(self.values))]
                return Vector(*new_values)
        else:
            return f"Вектор нельзя умножать с {type(scalar).__name__}"

v1 = Vector(1,2,3)
print(v1)  # печатает "Вектор(1, 2, 3)"
v2 = Vector(3,4,5)
print(v2)  # печатает "Вектор(3, 4, 5)"
v3 = v1 + v2
print(v3)  # печатает "Вектор(4, 6, 8)"
v4 = v3 + 5
print(v4)  # печатает "Вектор(9, 11, 13)"
v5 = v1 * 2
print(v5)  # печатает "Вектор(2, 4, 6)"
v6 = v5 + 'hi'
print(v6)  # печатает "Вектор нельзя сложить с hi"
v7 = Vector(7,5,8,3)
v8 = v1 + v7
print(v8)
v9 = v1 * v7
print(v9)