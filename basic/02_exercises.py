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
radius = int(input("Enter radius :"))
pi = 3.14
area = pi * radius**2
print("The area of the circle is: ", area)
c = 2 * pi * radius
print("The circumference of the circle is: ", c)
