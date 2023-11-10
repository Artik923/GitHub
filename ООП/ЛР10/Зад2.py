# Определение родительского класса "Супермаркет"
class Supermarket:
    # Инициализация атрибутов класса
    def __init__(self, department_name, product_name, country_producer, retail_price, provider):
        self.department_name = department_name
        self.product_name = product_name
        self.country_producer = country_producer
        self.retail_price = retail_price
        self.provider = provider

    # Вывод информации об экземпляре класса
    def __str__(self):
        return f'Отдел: {self.department_name}, Товар: {self.product_name}, Страна-производитель: {self.country_producer}, Цена: {self.retail_price}, Поставщик: {self.provider}'

# Определение дочернего класса "Игрушки"
class Toys(Supermarket):
    # Инициализация атрибутов класса, включая атрибуты родительского класса
    def __init__(self, department_name, product_name, country_producer, retail_price, provider, age_group, type):
        super().__init__(department_name, product_name, country_producer, retail_price, provider)
        self.age_group = age_group
        self.type = type

    # Вывод информации об экземпляре класса, включая информацию из родительского класса
    def __str__(self):
        return super().__str__() + f', Возрастная группа: {self.age_group}, Тип: {self.type}'

# Определение дочернего класса "Фрукты"
class Fruit(Supermarket):
    # Инициализация атрибутов класса, включая атрибуты родительского класса
    def __init__(self, department_name, product_name, country_producer, retail_price, provider, max_rem_of_storage, storage_temperature):
        super().__init__(department_name, product_name, country_producer, retail_price, provider)
        self.max_rem_of_storage = max_rem_of_storage
        self.storage_temperature = storage_temperature

    # Вывод информации об экземпляре класса, включая информацию из родительского класса
    def __str__(self):
        return super().__str__() + f', Максимальное время хранения: {self.max_rem_of_storage}, Температура хранения: {self.storage_temperature}'

# Определение дочернего класса "Габаритный товар"
class Dimensional_goods(Supermarket):
    # Инициализация атрибутов класса, включая атрибуты родительского класса
    def __init__(self, department_name, product_name, country_producer, retail_price, provider, height, width, length):
        super().__init__(department_name, product_name, country_producer, retail_price, provider)
        self.height = height
        self.width = width
        self.length = length

    # Вывод информации об экземпляре класса, включая информацию из родительского класса
    def __str__(self):
        return super().__str__() + f', Высота: {self.height}, Ширина: {self.width}, Длина: {self.length}'

# Создание экземпляров классов
toy = Toys('Игрушки', 'Мягкая игрушка', 'Беларусь', 20, 'Поставщик1', '3+', 'Мягкая игрушка')
fruit = Fruit('Фрукты', 'Яблоки', 'Беларусь', 2, 'Поставщик2', '7 дней', '+1-+4')
dimensional_goods = Dimensional_goods('Мебель', 'Стол', 'Беларусь', 100, 'Поставщик3', '75 см', '120 см', '60 см')

# Вывод информации об экземплярах классов
print(toy)
print(fruit)
print(dimensional_goods)
