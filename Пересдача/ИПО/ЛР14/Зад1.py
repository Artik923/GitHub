# Определение базового класса для циркового представления
class Circus:
    def __init__(self, title, city, premiere_date, duration, ticket_price, author, genre, number_of_actors):
        # Инициализация атрибутов класса
        self.title = title  # Название представления
        self.city = city  # Город, в котором проходит представление
        self.premiere_date = premiere_date  # Дата премьеры
        self.duration = duration  # Продолжительность представления
        self.ticket_price = ticket_price  # Цена билета
        self.author = author  # Автор представления
        self.genre = genre  # Жанр представления
        self.number_of_actors = number_of_actors  # Количество актеров

    # Метод для вывода информации о представлении
    def __str__(self):
        return f"Цирк: {self.title}, Город: {self.city}, Дата премьеры: {self.premiere_date}, Продолжительность: {self.duration}, Цена билета: {self.ticket_price}, Автор: {self.author}, Жанр: {self.genre}, Количество актеров: {self.number_of_actors}"

# Класс для акробатических представлений, наследуется от базового класса Circus
class Acrobatic_performances(Circus):
    def __init__(self, title, city, premiere_date, duration, ticket_price, author, genre, number_of_actors, type_of_acrobatics, inventory):
        super().__init__(title, city, premiere_date, duration, ticket_price, author, genre, number_of_actors)  # Вызов конструктора базового класса
        self.type_of_acrobatics = type_of_acrobatics  # Тип акробатики
        self.inventory = inventory  # Инвентарь для представления

    # Метод для вывода информации об акробатическом представлении
    def __str__(self):
        return f"Акробатические представления: {self.title}, Город: {self.city}, Дата премьеры: {self.premiere_date}, Продолжительность: {self.duration}, Цена билета: {self.ticket_price}, Автор: {self.author}, Жанр: {self.genre}, Количество актеров: {self.number_of_actors}, Тип акробатики: {self.type_of_acrobatics}, Инвентарь: {self.inventory}"

# Класс для представлений с дрессировкой, наследуется от базового класса Circus
class Training(Circus):
    def __init__(self, title, city, premiere_date, duration, ticket_price, author, genre, number_of_actors, type_of_training, number_of_animals):
        super().__init__(title, city, premiere_date, duration, ticket_price, author, genre, number_of_actors)  # Вызов конструктора базового класса
        self.type_of_training = type_of_training  # Вид дрессировки
        self.number_of_animals = number_of_animals  # Количество животных

    # Метод для вывода информации о представлении с дрессировкой
    def __str__(self):
        return f"Дрессировка: {self.title}, Город: {self.city}, Дата премьеры: {self.premiere_date}, Продолжительность: {self.duration}, Цена билета: {self.ticket_price}, Автор: {self.author}, Жанр: {self.genre}, Количество актеров: {self.number_of_actors}, Вид дрессировки: {self.type_of_training}, Количество животных: {self.number_of_animals}"

# Класс для представлений с фокусами, наследуется от базового класса Circus
class Magic_tricks(Circus):
    def __init__(self, title, city, premiere_date, duration, ticket_price, author, genre, number_of_actors, type_of_tricks, inventory):
        super().__init__(title, city, premiere_date, duration, ticket_price, author, genre, number_of_actors)  # Вызов конструктора базового класса
        self.type_of_tricks = type_of_tricks  # Вид фокусов
        self.inventory = inventory  # Инвентарь для представления

    # Метод для вывода информации о представлении с фокусами
    def __str__(self):
        return f"Фокусы: {self.title}, Город: {self.city}, Дата премьеры: {self.premiere_date}, Продолжительность: {self.duration}, Цена билета: {self.ticket_price}, Автор: {self.author}, Жанр: {self.genre}, Количество актеров: {self.number_of_actors}, Вид фокусов: {self.type_of_tricks}, Инвентарь: {self.inventory}"

# Создание экземпляров классов
acro = Acrobatic_performances("Акробатика в воздухе", "Москва", "01.01.2022", "01.01.2022 - 31.12.2022", 2000, "Иванов И.И.", "Акробатика", 10, "силовая акробатика", "трапеция")
training = Training("Цирк с тиграми", "Санкт-Петербург", "01.02.2022", "01.02.2022 - 31.12.2022", 2500, "Петров П.П.", "Дрессировка", 5, "хищники", 3)
focus = Magic_tricks("Магия и иллюзии", "Казань", "01.03.2022", "01.03.2022 - 31.12.2022", 1500, "Сидоров С.С.", "Фокусы", 1, "иллюзия", "карты")

print(acro)
print(training)
print(focus)
