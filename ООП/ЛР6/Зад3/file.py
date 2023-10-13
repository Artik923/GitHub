import random

class File:
    def __init__(self, name, size, creation_date):
        self.name = name
        self.size = size
        self.creation_date = creation_date
        self.num_of_accesses = 0

    def print_info(self):
        print(f'Имя файла: {self.name}\n'
              f'  Размер: {self.size}\n'
              f'  Дата создания: {self.creation_date}\n'
              f'  Количество обращений: {self.num_of_accesses}\n')