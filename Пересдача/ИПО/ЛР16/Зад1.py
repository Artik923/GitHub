class House:
    def __init__(self, address, floors, rooms, year_of_construction):
        # Инициализация атрибутов дома
        self._address = address
        self._floors = floors
        self._rooms = rooms
        self._year_of_construction = year_of_construction

    @property
    def address(self):
        # Возвращает адрес дома
        return self._address

    @address.setter
    def address(self, value):
        # Устанавливает новый адрес дома
        self._address = value

    @property
    def floors(self):
        # Возвращает количество этажей в доме
        return self._floors

    @floors.setter
    def floors(self, value):
        # Устанавливает новое количество этажей в доме
        self._floors = value

    @property
    def rooms(self):
        # Возвращает количество комнат в доме
        return self._rooms

    @rooms.setter
    def rooms(self, value):
        # Устанавливает новое количество комнат в доме
        self._rooms = value

    @property
    def year_of_construction(self):
        # Возвращает год постройки дома
        return self._year_of_construction

    @year_of_construction.setter
    def year_of_construction(self, value):
        # Устанавливает новый год постройки дома
        self._year_of_construction = value

    def __str__(self):
        # Возвращает строковое представление дома
        return f"Адрес: {self._address}, Этажи: {self._floors}, Комнаты: {self._rooms}, Год постройки: {self._year_of_construction}"

house = House("Ул.Пушкина, д.1", 2, 3, 1990)
house.address = "Ул.Пушкина, д.2"
house.floors = 3
house.rooms = 4
house.year_of_construction = 2000

print(house.address)  # выводит "Ул.Пушкина, д.2"
house.address = "ул.Советская, д.3"  # изменяет адрес
print(house.address)  # выводит "ул. Советская, д. 3"
house._address = "Ул.Ленина, д.7"  # вызывает ошибку, так как _address - это приватный атрибут
print(house)  # выводит информацию о доме
