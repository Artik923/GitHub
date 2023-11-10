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
        self.model = model
        self.resolution = resolution
        self.color_depth = color_depth
        self.document_feeder = document_feeder
        self.interface = interface
        self.price = price

    def get_model(self):
        return self.model

    def get_resolution(self):
        return self.resolution

    def get_color_depth(self):
        return self.color_depth

    def is_document_feeder(self):
        return self.document_feeder

    def get_interface(self):
        return self.interface

    def get_price(self):
        return self.price


# Вывод документации класса
print(Scanner.__doc__)

# Создание и инициализация экземпляров класса
scanner1 = Scanner("Epson Perfection V600", 2400, 48, True, "USB", 199.99)
scanner2 = Scanner("Canon CanoScan LiDE 400", 4800, 48, False, "USB", 89.99)
scanner3 = Scanner("HP ScanJet Pro 2500 f1", 1200, 24, True, "USB", 299.99)
scanner4 = Scanner("Brother ADS-2200", 1200, 48, True, "USB", 199.99)
scanner5 = Scanner("Fujitsu ScanSnap iX1500", 600, 24, True, "USB/Wi-Fi", 449.99)

# Вывод информации о сканерах
print("Модель сканера:", scanner1.get_model())
print("Разрешение сканера:", scanner1.get_resolution(), "dpi")
print("Глубина цвета сканера:", scanner1.get_color_depth(), "бит")
print("Наличие автоподатчика документов:", scanner1.is_document_feeder())
print("Тип интерфейса для подключения сканера:", scanner1.get_interface())
print("Цена сканера:", scanner1.get_price(), "руб.")
print()
print("Модель сканера:", scanner2.get_model())
print("Разрешение сканера:", scanner2.get_resolution(), "dpi")
print("Глубина цвета сканера:", scanner2.get_color_depth(), "бит")
print("Наличие автоподатчика документов:", scanner2.is_document_feeder())
print("Тип интерфейса для подключения сканера:", scanner2.get_interface())
print("Цена сканера:", scanner2.get_price(), "руб.")
print()
print("Модель сканера:", scanner3.get_model())
print("Разрешение сканера:", scanner3.get_resolution(), "dpi")
print("Глубина цвета сканера:", scanner3.get_color_depth(), "бит")
print("Наличие автоподатчика документов:", scanner3.is_document_feeder())
print("Тип интерфейса для подключения сканера:", scanner3.get_interface())
print("Цена сканера:", scanner3.get_price(), "руб.")
print()
print("Модель сканера:", scanner4.get_model())
print("Разрешение сканера:", scanner4.get_resolution(), "dpi")
print("Глубина цвета сканера:", scanner4.get_color_depth(), "бит")
print("Наличие автоподатчика документов:", scanner4.is_document_feeder())
print("Тип интерфейса для подключения сканера:", scanner4.get_interface())
print("Цена сканера:", scanner4.get_price(), "руб.")
print()
print("Модель сканера:", scanner5.get_model())
print("Разрешение сканера:", scanner5.get_resolution(), "dpi")
print("Глубина цвета сканера:", scanner5.get_color_depth(), "бит")
print("Наличие автоподатчика документов:", scanner5.is_document_feeder())
print("Тип интерфейса для подключения сканера:", scanner5.get_interface())
print("Цена сканера:", scanner5.get_price(), "руб.")