# 1 Declare your age as integer variable
age: int = 26
print(type(age))

# 2 Declare your height as a float variable
height: float = 1.75
print(type(height))

# 3 Declare a variable that store a complex number
complex_number: complex = 20j
print(type(complex_number))

# 4 Write a script that prompts the user to enter base and height of
# the triangle and calculate an area of this triangle (area = 0.5 x b x h)
# base = int(input("Enter base: "))
# height = int(input("Enter height: "))
# area = int(0.5 * base * height)
# print("The area of the triangle is :", area)

# 5 Write a script that prompts the user to enter side a, side b and side c of the triangle.
# Calculate the perimeter of the triangle (perimeter = a + b + c)
# a = int(input("Enter side a: "))
# b = int(input("Enter side b: "))
# c = int(input("Enter side c: "))
# perimeter = a + b + c
# print("The perimeter of the triangle is: ", perimeter)

# 6 Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and
# perimeter (perimeter = 2 x (length + width))
# width = int(input("Enter width: "))
# length = int(input("Enter length: "))
# area = length * width
# perimeter = 2 * (length + width)
# print(area)
# print(perimeter)

# 7 Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14
# radius = int(input("Enter radius :"))
# pi = 3.14
# area = pi * radius**2
# print("The area of the circle is: ", area)
# c = 2 * pi * radius
# print("The circumference of the circle is: ", c)

# 8 Calculate the sople, x-intercept and y-intercept of y = 2x -2
# m = 2
# b = -2
# x_intersection = -b / m
# y_intersection = b
# print("Sople(m): ", m)
# print("Intersection in x: ", x_intersection)
# print("Intersection in y: ", y_intersection)

# 12 Find the length of 'python' and 'dragon' and make a falsy comparison statement.
python = "python"
dragon = "dragon"
print(len(python))
print(len(dragon))
print(python == dragon)

# 13 Use and operator to check if "on" is found in both "python" and "dragon"
print("on" in python and "on" in dragon)

# 14 I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence
jargon = "I hope this course is not full of jargon."
print("jargon" in jargon)

# 15 There is no "on" in both dragon and python
print("on" not in python and "on" not in dragon)

# 16 Find the lenght of the text python and convert the value to float and convert it to string
print(type(float(len(python))))
print(type(str(len(python))))

# 17 Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
print(24 % 2 is 0)

# 18 Check if the floor division of 7 by 3 is equal to the int converted value of 2.7
print(7 // 3 is int(2.7))

# 19 Check if type of "10" is equal to type of 10
print(type("10") == type(10))

# 20 Check if int("9.8") is equal to 10
print(int(float("9.8")) is 10)

# 21 Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
# hours = int(input("Enter hours:"))
# rate = int(input("Enter rate per hour:"))
# earning = hours * rate
# print("Your weekly earning is:", earning)

# 22 Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live.
# Assume a person can live hundred years.
# years = int(input("Enter number of years you have lived:"))
# seconds = 31536000
# years_lived = years * seconds
# print("You have lived for", years_lived, "seconds")

# 23 Write a Python script that displays the following table
print("1 1 1 1 1")
print("2 1 2 4 8")
print("3 1 3 9 27")
print("4 1 4 16 64")
print("5 1 5 25 125")
