import os
import json

file_name = "students.json"


if not os.path.exists(file_name):
    
    with open(file_name, 'w') as f:
        json.dump([], f, indent=4)
    print(f"{file_name} fayli yaratildi.")
else:
    print(f"{file_name} fayli allaqachon mavjud.")
