# 1 Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add_two_numbers(num1, num2):
    return num1 + num2


print(add_two_numbers(2, 2))


# 2 Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
def area_of_circle(r):
    PI = 3.14
    return PI * r**2


print(area_of_circle(10))


# 3 Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
def add_all_nums(*nums):
    total = 0
    for num in nums:
        total += num
    return total


print(add_all_nums(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


# 4 Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


print(convert_celsius_to_fahrenheit(41))


# 5 Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
def check_season(month):
    month = month.lower()
    autumn = ["september", "october", "november"]
    winter = ["december", "january", "february"]
    spring = ["march", "april", "may"]
    summer = ["june", "july", "august"]
    if month in autumn:
        return f"Is Autumn"
    elif month in winter:
        return f"Is Winter"
    elif month in spring:
        return f"Is Spring"
    elif month in summer:
        return f"Is Summer"
    else:
        return f"Please enter a valid month"


print(check_season("JunE"))


# 6 Write a function called calculate_slope which return the slope of a linear equation
def calculate_slope(x1, y1, x2, y2):
    delta_y = y2 - y1
    delta_x = x2 - x1
    slope = delta_y / delta_x
    return slope


print(calculate_slope(1, 2, 3, 4))

# 7 Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
import math


def solve_quadratic_eqn(a, b, c):
    discriminant = math.sqrt(b**2 - 4 * a * c)
    solution_1 = (-b + discriminant) / (2 * a)
    solution_2 = (-b - discriminant) / (2 * a)
    return solution_1, solution_2


print(solve_quadratic_eqn(1, -3, 2))


# 8 Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
def print_list(list):
    for i in list:
        print(i)


numbers = [1, 2, 3, 4, 5]
print_list(numbers)


# 9 Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
def reverse_list(list):
    new_list = []
    for item in reversed(list):
        new_list.append(item)
    return new_list


fruits = ["Mango", "Lemon", "Orange"]
print(reverse_list(fruits))


# 10 Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items.
def capitalize_list_items(list):
    capitalized_items = []
    for i in list:
        capitalized_items.append(i.capitalize())
    return capitalized_items


fruits = ["mango", "lemon", "Orange"]
print(capitalize_list_items(fruits))


# 11 Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
def add_item(list, item):
    list = []
    list.append(item)
    return list


fruits = ["Mango", "Lemon", "Orange"]
print(add_item(fruits, "Papaya"))
# 12 Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.

# 13 Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.

# 14 Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.

# 15 Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.
