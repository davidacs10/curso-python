# 1 Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add_two_numbers(num1, num2):
    total = num1 + num2
    return total


print(add_two_numbers(2, 3))


# 2 Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
def area_of_circle(r):
    PI = 3.14
    area = PI * r**2
    return area


print(area_of_circle(10))


# 3 Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments.
# Check if all the list items are number types. If not do give a reasonable feedback.
def add_all_nums(*nums):
    total = 0
    for num in nums:
        if isinstance(num, (int, float)):
            total += num
        else:
            return "Please only add numbers"

    return total


print(add_all_nums(1, 3, 5))


# 4 Temperature in °C can be converted to °F using this formula:
# °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
def convert_celsius_to_fahrenheit(c):
    f = (c * 9 / 5) + 32
    return f


print(convert_celsius_to_fahrenheit(40.5555556))


# 5 Write a function called check-season, it takes a month parameter and returns the season:
# Autumn, Winter, Spring or Summer.
def check_season(month):
    month = month.lower()
    season_mapping = {
        "january": "Winter",
        "february": "Winter",
        "march": "Spring",
        "april": "Spring",
        "may": "Spring",
        "june": "Summer",
        "july": "Summer",
        "august": "Summer",
        "september": "Autumn",
        "october": "Autumn",
        "november": "Autumn",
        "december": "Winter",
    }
    if month in season_mapping:
        return season_mapping[month]
    else:
        return "Invalid Month"


print(check_season("december"))


# 6 Write a function called calculate_slope which return the slope of a linear equation
def calculate_slope(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)


x1 = 1
y1 = 2
x2 = 3
y2 = 4

slope = calculate_slope(x1, y1, x2, y2)

print(slope)


# 7 Quadratic equation is calculated as follows:
# ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
import math


def solve_quadratic_eqn(a, b, c):
    discriminant = b**2 - 4 * a * c
    if discriminant < 0:
        return set()
    elif discriminant == 0:
        return {-b / 2 * a}
    else:
        return {
            (-b + math.sqrt(discriminant)) / (2 * a),
            (-b - math.sqrt(discriminant)) / (2 * a),
        }


a = 1
b = 2
c = 3

solutions = solve_quadratic_eqn(a, b, c)
print(solutions)


# 8 Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
def print_list(list):
    for i in list:
        print(i)


vegetables = ["Letucce", "Tomato", "Onion", "Potato"]
print_list(vegetables)


# 9 Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
def reverse_list(list):
    reversed_list = []
    for i in range(len(list) - 1, -1, -1):
        reversed_list.append(list[i])
    return reversed_list


print(reverse_list(vegetables))


# 10 Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
def capitalize_list_items(list):
    capitalize_list = []
    for i in list:
        capitalize_list.append(i.upper())
    return capitalize_list


print(capitalize_list_items(vegetables))


# 11 Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
def add_item(list, string):
    list = []
    for i in string:
        list.append([i])
    return list


food_staff = ["Potato", "Tomato", "Mango", "Milk"]
print(add_item(food_staff, "Meat"))
