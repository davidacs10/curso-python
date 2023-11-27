# Dictionaries

# 1 Create an empty dictionary called dog
dog = {}
print(type(dog))
# 2 Add name, color, breed, legs, age to the dog dictionary
dog = {
    "name": "Blacky",
    "color": "Black",
    "breed": "German Shepherd",
    "legs": "shorts",
    "age": 1,
}
print(dog)
# 3 Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {
    "first_name": "David",
    "last_name": "Campos",
    "gender": "Male",
    "age": 24,
    "marital status": False,
    "skills": ["HTML5", "CSS3", "Python"],
    "country": "Venezuela",
    "city": "Caracas",
    "address": {"street": "Av. Bolívar", "zip": 1087},
}
# 4 Get the length of the student dictionary
print(len(student))
# 5 Get the value of skills and check the data type, it should be a list
print(type(student.get("skills")))
# 6 Modify the skills values by adding one or two skills
student["skills"].append("Javascript")
print(student)
# 7 Get the dictionary keys as a list
keys = list(student.keys())
print(keys)
# 8 Get the dictionary values as a list
values = list(student.values())
print(values)
# 9 Change the dictionary to a list of tuples using items() method
print(student.items())
# 10 Delete one of the items in the dictionary
student.pop("address")
print(student)
# 11 Delete one of the dictionaries
del dog
