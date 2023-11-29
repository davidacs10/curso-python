# Conditionals
# 1 Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:
# age = int(input("Enter your age: "))
# if age >= 18:
#     print("You are old enough to drive")
# else:
#     print(f"You need {18 - age} more years to learn to drive.")
# 2 Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:
# my_age = int(input("Enter my age: "))
# your_age = int(input("Enter your age: "))
# one_year_difference = my_age - your_age
# if my_age - your_age >= 2:
#     print(f"I am {my_age - your_age} years older than you")
# elif my_age - your_age == 1:
#     print(f"I am {my_age - your_age} year older than you")
# elif my_age == your_age:
#     print("We have the same age")
# elif your_age - my_age == 1:
#     print(f"You are {your_age - my_age} year older than me")
# else:
#     print(f"You are {your_age - my_age} years older than me")
# 3 Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:
# a = int(input("Insert number: "))
# b = int(input("Insert number: "))
# if a > b:
#     print(f"{a} is greater than {b}")
# elif a == b:
#     print(f"{a} and {b} are equal")
# else:
#     print(f"{a} is smaller than {b}")
# 4 Write a code which gives grade to students according to theirs scores:
# score = int(input("Enter your score: "))
# if score >= 80 and score <= 100:
#     print("A")
# elif score >= 70 and score <= 79:
#     print("B")
# elif score >= 60 and score <= 69:
#     print("C")
# elif score >= 50 and score <= 59:
#     print("D")
# else:
#     print("F")
# 5 Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer
# season = input("Enter month: ")
# season = season.lower()
# autumn = ["september", "october", "november"]
# winter = ["december", "january", "february"]
# spring = ["march", "april", "may"]
# summer = ["june", "july", "august"]

# if season in autumn:
#     print("the season is Autumn")
# elif season in winter:
#     print("the season is Winter")
# elif season in spring:
#     print("the season is Spring")
# elif season in summer:
#     print("the season is Summer")
# else:
#     ("Please enter a valid month")
# 6 The following list contains some fruits:
# fruits_input = input("Enter fruit :")
# fruits = ["banana", "orange", "mango", "lemon"]
# if fruits_input in fruits:
#     print("That fruit already exist in the list")
# else:
#     fruits.append(fruits_input)
#     print(fruits)
# 7 Here we have a person dictionary. Feel free to modify it!
#  * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
#  * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
#  * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
#  * If the person is married and if he lives in Finland, print the information in the following format:
person = {
    "first_name": "David",
    "last_name": "Campos",
    "gender": "Male",
    "age": 24,
    "is_married": True,
    "skills": ["React", "Node", "MongoDB"],
    "country": "Venezuela",
    "city": "Caracas",
    "address": {"street": "Av. Bolívar", "zip": 1087},
}
front_end = ["JavaScript", "React"]
back_end = ["Node", "Python", "MongoDB"]
full_stack = ["React", "Node", "MongoDB"]

if "skills" in person:
    print(person["skills"][len(person["skills"]) // 2])

if "Python" in person["skills"]:
    print("The person is learning Python.")

if "JavaScript" in person["skills"] and "React" in person["skills"]:
    print("He is a front end developer")
elif (
    "Node" in person["skills"]
    and "Python" in person["skills"]
    and "MongoDB" in person["skills"]
):
    print("He is a back-end developer")
elif (
    "React" in person["skills"]
    and "Node" in person["skills"]
    and "MongoDB" in person["skills"]
):
    print("He is a fullstack developer")
else:
    print("This person does not know any programming languages yet.")

first_name = person["first_name"]
last_name = person["last_name"]
country = person["country"]

if person.get("is_married") and person.get("country") == country:
    print(f"{first_name} {last_name} is from {country}. He is also married.")
