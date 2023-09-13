# 1 Create an empty dictionary called dog
dog = {}

# 2 Add name, color, breed, legs, age to the dog dictionary
dog = {"name": "Max", "breed": "Jack russell", "legs": "short", "age": "3"}

# 3 Create a student dictionary and add first_name, last_name, gender, age, marital status,
# skills, country, city and address as keys for the dictionary
student = {
    "first_name": "David",
    "last_name": "Campos",
    "gender": "male",
    "age": 26,
    "marital_status": False,
    "skills": ["WSL, GIT, HTML, CSS, PYTHON"],
    "country": "Venezuela",
    "city": "Anzoategui",
    "address": "472 Street",
}

# 4 Get the length of the student dictionary
print(len(student))

# 5 Get the value of skills and check the data type, it should be a list
print(student["skills"])
print(type(student["skills"]))

# 6 Modify the skills values by adding one or two skills
student["skills"].append("SQL")
student["skills"].append("Javascript")
print(student["skills"])

# 7 Get the dictionary keys as a list
keys = student.keys()
print(keys)

# 8 Get the dictionary values as a list
values = student.values()
print(values)

# 9 Change the dictionary to a list of tuples using items() method
print(student.items())

# 10 Delete one of the items in the dictionary
student.pop("address")
student.popitem()
del student["country"]
print(student)

# 11 Delete one of the dictionaries
print(dog.clear())
del dog
