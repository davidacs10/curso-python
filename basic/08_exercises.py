# 1 Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback:
# You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:
# age = int(input("Enter your age: "))
# if age >= 18:
#     print("You are old enough to drive.")
# else:
#     print("You need", 18 - age, "more years to learn to drive.")

# 2 Compare the values of my_age and your_age using if … else. Who is older (me or you)?
# Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to
# print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom
# text if my_age = your_age. Output:
# my_age = int(input("Enter your age: "))
# your_age = int(input("Enter his age: "))
# if my_age > your_age:
#     difference = my_age - your_age
#     if difference == 1:
#         print("I'm older than you by 1 year")
#     else:
#         print("I'm older than your by", difference, "years")
# elif my_age < your_age:
#     difference = your_age - my_age
#     if difference == 1:
#         print("You're older than me by 1 year")
#     else:
#         print("You're older than me by", difference, "years")
# else:
#     print("We have the same age")

# 3 Get two numbers from the user using input prompt. If a is greater than b return a is greater than b,
# if a is less b return a is smaller than b, else a is equal to b. Output:
# a = int(input("Enter number one: "))
# b = int(input("Enter number two: "))
# if a > b:
#     print(a, "is greather than", b)
# elif a < b:
#     print(a, "is smaller than", b)
# else:
#     print(a, "is equal to", b)

# 4 Write a code which gives grade to students according to theirs scores:
# name = str(input("Enter your name: "))
# score = float(input("Enter your score: "))
# if score >= 85 and score <= 100:
#     print(name, " Your calification is: A")
# elif score >= 70 and score <= 84.9:
#     print(name, "Your calification is: B")
# elif score >= 60 and score <= 69.9:
#     print(name, "Your calification is: C")
# elif score >= 50 and score <= 59.9:
#     print(name, "Your calification is: D")
# else:
#     print(name, "Your calification is: F")

# 5 Check if the season is Autumn, Winter, Spring or Summer.
# If the user input is: September, October or November, the season is Autumn.
# December, January or February, the season is Winter.
# March, April or May, the season is Spring June, July or August, the season is Summer

# month = str(input("Introduce month: "))
# if month in ("September", "september", "October", "october", "November", "november"):
#     season = "Autumn"
# elif month in ("December", "december", "January", "january", "February", "february"):
#     season = "Winter"
# elif month in ("March", "march", "April", "april", "May", "may"):
#     season = "Spring"
# else:
#     season = "Summer"

# print(season)

# 5 The following list contains some fruits:
# If a fruit doesn't exist in the list add the fruit to the list and print the modified list.
# If the fruit exists print('That fruit already exist in the list')
# fruits = ["banana", "orange", "mango", "lemon"]
# new_fruit = str(input("Enter your fruit: "))

# if new_fruit not in fruits:
#     fruits.append(new_fruit)
#     print(fruits)
# else:
#     print("That fruit already exist in the list")

# 6 Here we have a person dictionary. Feel free to modify it!
person = {
    "first_name": "David",
    "last_name": "Campos",
    "age": 26,
    "country": "Venezuela",
    "is_marred": False,
    "skills": ["JavaScript", "React", "Node", "MongoDB", "Python"],
    "address": {"street": "Space street"},
}

if "skills" in person:
    i = int(len("skills")) // 3
    middle_skill = person["skills"][i]
    print(middle_skill)
else:
    print("No have skills dictionary")
