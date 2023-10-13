from studenty import Student, byGPA_key
import random
 
def main():
    # Создание списка студентов
    students = [
        Student(
            input('Введите фамилию и имя студента: '),
            input('Введите номер группы: '),
            [random.randint(1, 10) for i_grade in range(5)]
        )
        for i_student in range(10)
    ]
    # Сортировка по среднему баллу студентов
    students_sort = sorted(students, key=byGPA_key)
    for student in students_sort: # Вывод информации о студентах
        student.print_info()

if __name__ == "__main__":
    main()