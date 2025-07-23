import json

with open("students.json","r") as json_file:
    students = json.load(json_file)

name = input("name: ")
surname = input("username: ")
age = input("age: ")

students.append({"name":name, "surname":surname, "age":age})

with open("students.json","w") as file:
    json.dump(students, file, indent=4)