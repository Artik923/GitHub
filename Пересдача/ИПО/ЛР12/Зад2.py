"""
Класс Scanner описывает сканеры и содержит информацию о них.

Атрибуты класса:
- model (строка) - модель сканера
- resolution (число) - разрешение сканера в dpi
- color_depth (число) - глубина цвета сканера в битах
- document_feeder (булево значение) - наличие автоподатчика документов
- interface (строка) - тип интерфейса для подключения сканера
- price (число) - цена сканера

Методы класса:
- get_model() - возвращает модель сканера
- get_resolution() - возвращает разрешение сканера
- get_color_depth() - возвращает глубину цвета сканера
- is_document_feeder() - возвращает True, если у сканера есть автоподатчик документов, иначе False
- get_interface() - возвращает тип интерфейса для подключения сканера
- get_price() - возвращает цену сканера

"""
class Scanner:
    def __init__(self, model, resolution, color_depth, document_feeder, interface, price):
        self.set_model(model)
        self.set_resolution(resolution)
        self.set_color_depth(color_depth)
        self.set_document_feeder(document_feeder)
        self.set_interface(interface)
        self.set_price(price)

    def __del__(self):
        print("Деструктор вызван для", self.get_model())

    def set_model(self, model):
        self.model = model

    def get_model(self):
        return self.model

    def set_resolution(self, resolution):
        self.resolution = resolution

    def get_resolution(self):
        return self.resolution

    def set_color_depth(self, color_depth):
        self.color_depth = color_depth

    def get_color_depth(self):
        return self.color_depth

    def set_document_feeder(self, document_feeder):
        self.document_feeder = document_feeder

    def is_document_feeder(self):
        return self.document_feeder

    def set_interface(self, interface):
        self.interface = interface

    def get_interface(self):
        return self.interface

    def set_price(self, price):
        self.price = price

    def get_price(self):
        return self.price

# Создание списка из 10 объектов класса Scanner
scanners = []
for i in range(10):
    model = input("Введите модель сканера: ")
    resolution = int(input("Введите разрешение сканера: "))
    color_depth = int(input("Введите глубину цвета сканера: "))
    document_feeder = bool(input("Введите наличие автоподатчика документов (True/False): "))
    interface = input("Введите тип интерфейса для подключения сканера: ")
    price = float(input("Введите цену сканера: "))
    scanners.append(Scanner(model, resolution, color_depth, document_feeder, interface, price))
    
# Вывод информации о военных воздушных судах
for Scanner in scanners:
    Scanner.display_info()

# Завершение программы, деструктор будет вызван для каждого объекта