student = {
    "name": "Вася",
    "age": 19,
    "program": "Прикладные математики и информатика",
    "programming_languages": ["Python", "JavaScript"]
}

print(f"Имя: {student['name']}")
print(f"Возраст: {student['age']}")
print(f"Факультет: {student['program']}")
print(f"Языки программирования: {', '.join(student['programming_languages'])}")