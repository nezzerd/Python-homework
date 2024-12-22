from collections import namedtuple

Student = namedtuple('Student', ['name', 'grade', 'city'])

students = (
    Student(name="Леонид", grade=85, city="Москва"),
    Student(name="Александр", grade=90, city="Одинцово"),
    Student(name="Иван", grade=70, city="Люберцы"),
    Student(name="Данил", grade=95, city="Зеленоград"),
    Student(name="Евгений", grade=65, city="Химкиг"),
    Student(name="Станислав", grade=80, city="Долгопрудный"),
)


def good_students(students):
    average_grade = sum(student.grade for student in students) / len(students)
    good_students_list = [student.name for student in students if student.grade >= average_grade]
    print(f"Ученики {', '.join(good_students_list)} в этом семестре хорошо учатся!")


good_students(students)
