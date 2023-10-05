class Student:
    def __init__(self, full_name, group_number, grades): # Метод "__init__" инициализирует атрибуты объекта класса
        self.full_name = full_name
        self.group_number = group_number
        self.grades = grades

    def print_info(self): # Метод "print_info" выводит информацию о студенте
        print(f'ФИ: {self.full_name}\nНомер группы: {self.group_number}\nУспеваемость: {self.grades}')

# Создание списка студентов
students = [
    Student('Иванов Иван Иванович', 'Группа 1', [4, 5, 3, 4, 5]),
    Student('Петров Петр Петрович', 'Группа 2', [3, 4, 5, 4, 3]),
    Student('Сидоров Сидор Сидорович', 'Группа 1', [5, 5, 5, 5, 5]),
    Student('Козлов Козел Козлович', 'Группа 2', [2, 3, 4, 3, 2]),
    Student('Николаев Николай Николаевич', 'Группа 1', [4, 4, 4, 4, 4]),
    Student('Алексеев Алексей Алексеевич', 'Группа 2', [5, 5, 5, 5, 5]),
    Student('Васильев Василий Васильевич', 'Группа 1', [3, 3, 3, 3, 3]),
    Student('Григорьев Григорий Григорьевич', 'Группа 2', [4, 4, 4, 4, 4]),
    Student('Дмитриев Дмитрий Дмитриевич', 'Группа 1', [2, 2, 2, 2, 2]),
    Student('Сергеев Сергей Сергеевич', 'Группа 2', [5, 5, 5, 5, 5])
]

# Вывод информации о студентах
for student in students:
    student.print_info()

# Сортировка списка студентов по возрастанию среднего балла
students.sort(key=lambda student: sum(student.grades) / len(student.grades))