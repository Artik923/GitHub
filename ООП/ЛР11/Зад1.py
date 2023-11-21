class Human:
    def __init__(self, имя, возраст):
        self.имя = имя
        self.возраст = возраст

    def __str__(self):
        return f"Человек: {self.имя}, Возраст: {self.возраст}"

class Student(Human):
    def __init__(self, имя, возраст, университет):
        super().__init__(имя, возраст)
        self.университет = университет

    def __str__(self):
        return f"Студент: {self.имя}, Возраст: {self.возраст}, Университет: {self.университет}"

class Father(Human):
    def __init__(self, имя, возраст, количество_детей):
        super().__init__(имя, возраст)
        self.количество_детей = количество_детей

    def __str__(self):
        return f"Отец: {self.имя}, Возраст: {self.возраст}, Количество детей: {self.количество_детей}"

class FatherStudent(Student, Father):
    def __init__(self, имя, возраст, университет, количество_детей):
        Студент.__init__(self, имя, возраст, университет)
        Отец.__init__(self, имя, возраст, количество_детей)

    def __str__(self):
        return f"Студент-Отец: {self.имя}, Возраст: {self.возраст}, Университет: {self.университет}, Количество детей: {self.количество_детей}"
