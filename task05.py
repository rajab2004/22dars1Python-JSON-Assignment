import json

with open("students.json","r") as json_file:
    students = json.load(json_file)

filtr_students = []

for student in students:
    if int(student['age']) > 20:
        filtr_students.append(student)


print("20dan katta yoshlilar")
for student in filtr_students:
    print(f"{student['name']}, {student['surname']}, {student['age']} yosh")