class Circus:
    def __init__(self, title, city, premiere_date, duration, ticket_price, author, genre, number_of_actors):
        self.title = title
        self.city = city
        self.premiere_date = premiere_date
        self.duration = duration
        self.ticket_price = ticket_price
        self.author = author
        self.genre = genre
        self.number_of_actors = number_of_actors

    def __str__(self):
        return f"Circus: {self.title}, City: {self.city}, Premiere date: {self.premiere_date}, Duration: {self.duration}, Ticket price: {self.ticket_price}, Author: {self.author}, Genre: {self.genre}, Number of actors: {self.number_of_actors}"

class Acrobatic_performances(Circus):
    def __init__(self, title, city, premiere_date, duration, ticket_price, author, genre, number_of_actors, type_of_acrobatics, inventory):
        super().__init__(title, city, premiere_date, duration, ticket_price, author, genre, number_of_actors)
        self.type_of_acrobatics = type_of_acrobatics
        self.inventory = inventory

    def __str__(self):
        return f"Acrobatic performances: {self.title}, City: {self.city}, Premiere date: {self.premiere_date}, Duration: {self.duration}, Ticket price: {self.ticket_price}, Author: {self.author}, Genre: {self.genre}, Number of actors: {self.number_of_actors}, Type of acrobatics: {self.type_of_acrobatics}, Inventory: {self.inventory}"

class Training(Circus):
    def __init__(self, title, city, premiere_date, duration, ticket_price, author, genre, number_of_actors, type_of_training, number_of_animals):
        super().__init__(title, city, premiere_date, duration, ticket_price, author, genre, number_of_actors)
        self.type_of_training = type_of_training
        self.number_of_animals = number_of_animals

    def __str__(self):
        return f"Training: {self.title}, City: {self.city}, Premiere date: {self.premiere_date}, Duration: {self.duration}, Ticket price: {self.ticket_price}, Author: {self.author}, Genre: {self.genre}, Number of actors: {self.number_of_actors}, Type of training: {self.type_of_training}, Number of animals: {self.number_of_animals}"

class Magic_tricks(Circus):
    def __init__(self, title, city, premiere_date, duration, ticket_price, author, genre, number_of_actors, type_of_tricks, inventory):
        super().__init__(title, city, premiere_date, duration, ticket_price, author, genre, number_of_actors)
        self.type_of_tricks = type_of_tricks
        self.inventory = inventory

    def __str__(self):
        return f"Magic tricks: {self.title}, City: {self.city}, Premiere date: {self.premiere_date}, Duration: {self.duration}, Ticket price: {self.ticket_price}, Author: {self.author}, Genre: {self.genre}, Number of actors: {self.number_of_actors}, Type of tricks: {self.type_of_tricks}, Inventory: {self.inventory}"

# Создание экземпляров классов
acro = Acrobatic_performances("Акробатика в воздухе", "Москва", "01.01.2022", "01.01.2022 - 31.12.2022", 2000, "Иванов И.И.", "Акробатика", 10, "силовая акробатика", "трапеция")
training = Training("Цирк с тиграми", "Санкт-Петербург", "01.02.2022", "01.02.2022 - 31.12.2022", 2500, "Петров П.П.", "Дрессировка", 5, "хищники", 3)
focus = Magic_tricks("Магия и иллюзии", "Казань", "01.03.2022", "01.03.2022 - 31.12.2022", 1500, "Сидоров С.С.", "Фокусы", 1, "иллюзия", "карты")

print(acro)
print(training)
print(focus)
