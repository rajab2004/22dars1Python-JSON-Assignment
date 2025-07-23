import json

with open("students.json", "r") as json_file:
    file = json.load(json_file)


    for i in file:
        print(f"{i['name']} - {i['age']} yosh")


