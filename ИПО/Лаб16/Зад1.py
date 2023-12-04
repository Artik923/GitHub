class House:
    def __init__(self, address, floors, rooms, year_of_construction):
        self._address = address
        self._floors = floors
        self._rooms = rooms
        self._year_of_construction = year_of_construction

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value

    @property
    def floors(self):
        return self._floors

    @floors.setter
    def floors(self, value):
        self._floors = value

    @property
    def rooms(self):
        return self._rooms

    @rooms.setter
    def rooms(self, value):
        self._rooms = value

    @property
    def year_of_construction(self):
        return self._year_of_construction

    @year_of_construction.setter
    def year_of_construction(self, value):
        self._year_of_construction = value

house = House("Ул.Пушкина, д.1", 2, 3, 1990)
house.address = "Ул.Пушкина, д.2"
house.floors = 3
house.rooms = 4
house.year_of_construction = 2000

print(house.address)  # выводит "Ул.Пушкина, д.1"
house.address = "ул.Советская, д.3"  # изменяет адрес
print(house.address)  # выводит "ул. Советская, д. 3"
house._address = "Ул.Ленина, д.7"  # вызывает ошибку
print(house)