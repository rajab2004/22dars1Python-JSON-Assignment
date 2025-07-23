import json

new_students = {"name": "Shahzoda", "surname": "Nazarova", "age": 22}

with open("students.json","r") as json_file:
    students = json.load(json_file)

students.append(new_students)

with open("students.json","w") as f:
    json.dump(students, f, indent=4)

print("qoshildi")
