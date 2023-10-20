class A:
    def __init__(self, a, b):
        self._a = a
        self._b = b

    @property
    def c(self):
        return self._a ** 2 + 4 * self._b

# Пример использования класса A
my_a = A(2, 3)
print('a:', my_a._a)
print('b:', my_a._b)
print('c:', my_a.c)