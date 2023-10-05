class Counter:
    def __init__(self):
        self.value = 0

    def start_from(self, value=0):
        self.value = value

    def increment(self):
        self.value += 1

    def display(self):
        print(f'Текущее значение счетчика = {self.value}')

    def reset(self):
        self.value = 0

# Создание экземпляра класса Counter
counter = Counter()

# Проверка работы методов
counter.start_from(5)
counter.display()  # Вывод: Текущее значение счетчика = 5

counter.increment()
counter.display()  # Вывод: Текущее значение счетчика = 6

counter.reset()
counter.display()  # Вывод: Текущее значение счетчика = 0
