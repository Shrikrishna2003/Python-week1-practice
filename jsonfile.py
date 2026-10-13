import json

name = input("Enter the name: ")
marks = int(input("Enter the marks: "))

print(name, type(name))
print(marks, type(marks))

person = {"name" : name, "marks" : marks}

print(type(person))

strObj = json.dumps(person)

print(strObj, type(strObj))

with open("data.json",  "w") as f:
    f.write(strObj)

# json.loads() ---> JSON string obj to Python data
python_data = json.loads(strObj)
print(python_data, python_data["name"], 
type(python_data))

# json.load() ---> JSON file to Python data
with open("data.json", "r") as f:
    python_data = json.load(f)
    print(python_data, type(python_data))

# json.dump

import json
student = {
    "name" : "Roshan",
    "age": 23,
    "course" : "python",
    "mobile" : 9876543210
}

with open("student.json", "w") as f:
    json.dump(student, f)