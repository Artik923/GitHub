class Car:
    def __init__(self, brand, max_passengers, cost, stock):
        self._brand = brand
        self._max_passengers = max_passengers
        self._cost = cost
        self._stock = stock

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, brand):
        self._brand = brand

    @property
    def max_passengers(self):
        return self._max_passengers

    @max_passengers.setter
    def max_passengers(self, max_passengers):
        self._max_passengers = max_passengers

    @property
    def cost(self):
        return self._cost

    @cost.setter
    def cost(self, cost):
        self._cost = cost

    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, stock):
        self._stock = stock

    @property
    def availability(self):
        return self._stock > 0


class Order:
    def __init__(self, customer_name, phone_number, cars):
        self._customer_name = customer_name
        self._phone_number = phone_number
        self._cars = cars

    @property
    def customer_name(self):
        return self._customer_name

    @customer_name.setter
    def customer_name(self, customer_name):
        self._customer_name = customer_name

    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        self._phone_number = phone_number

    @property
    def cars(self):
        return self._cars

    @cars.setter
    def cars(self, cars):
        self._cars = cars

    def calculate_order_cost(self):
        try:
            if len(self._cars) == 0:
                raise ValueError("Количество автомобилей в заявке равно нулю")
            return sum(car.cost for car in self._cars)
        except ValueError as e:
            print(f"Ошибка: {e}")


class DeferredOrder(Order):
    def __init__(self, customer_name, phone_number, cars, discount):
        super().__init__(customer_name, phone_number, cars)
        self._discount = discount

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, discount):
        self._discount = discount

    def calculate_order_cost(self):
        try:
            if len(self._cars) == 0:
                raise ValueError("Количество автомобилей в заявке равно нулю")
            return sum(car.cost for car in self._cars) * (1 - self._discount / 100)
        except ValueError as e:
            print(f"Ошибка: {e}")


class CarShowroom:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name
