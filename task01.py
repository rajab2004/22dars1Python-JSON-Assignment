import json 
students = [
    {"name": "Ali", "surname": "Valiyev", "age": 20},
    {"name": "Laylo", "surname": "Karimova", "age": 21},
    {"name": "Bekzod", "surname": "Xolmatov", "age": 19}
]

with open("students.json", "w") as file:
    json.dump(students, file, indent=4)