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
def add_item(list, element):
    list.append(element)
    return list


food_staff = ["Potato", "Tomato", "Mango", "Milk"]
print(add_item(food_staff, "Meat"))


# 12 Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
def remove_item(list, remove_element):
    list.remove(remove_element)
    return list


print(remove_item(food_staff, "Potato"))


# 13 Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
def sum_of_numbers(num):
    addition = 0
    for i in range(num + 1):
        addition = i + addition
    return addition


print(sum_of_numbers(100))


# 14 Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
def sum_of_odds(odd):
    addition = 0
    for i in range(odd + 1):
        if i % 2 == 1:
            addition = addition + i
    return addition


print(sum_of_odds(10))


# 15 Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that range.
def sum_of_odds(even):
    addition = 0
    for i in range(even + 1):
        if i % 2 == 0:
            addition = addition + i
    return addition


print(sum_of_odds(10))


# 16 Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
def evens_and_odds(num):
    while num < 1:
        raise ValueError("El numero debe ser positivo")
    even = []
    odd = []
    for i in range(num + 1):
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return f"""The number of evens are {len(even)}
The number of evens are {len(odd)}"""


print(evens_and_odds(100))


# 17 Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(4))


# 18 Call your function is_empty, it takes a parameter and it checks if it is empty or not
def is_empty(list):
    if len(list) == 0:
        return "Is empty"
    else:
        return "Is not empty"


list = []
print(is_empty(list))


# 19 Write different functions which take lists. They should calculate_mean, calculate_median,
# calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).
import statistics


def calculate_mean(list):
    mean = statistics.mean(list)
    return f"The mean of the list is:{mean}"


list = [1, 2, 2.5, 3, 3.5, 1, 1, 2, 3]
print(calculate_mean(list))


def calculate_median(list):
    median = statistics.median(list)
    return f"The medium of the list is:{median}"


list = [9, 6, 6, 7, 9, 7, 8]
print(calculate_median(list))


def calculate_mode(list):
    mode = statistics.mode(list)
    return f"The mode of the list is:{mode}"


list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(calculate_mode(list))


def calculate_range(list):
    range = max(list) - min(list)
    return f"The range of the list is: {range}"


numeros = [3, 7, 2, 8, 6, 4, 5, 1, 9]
print(calculate_range(numeros))


def calculate_variance(list):
    variance = statistics.variance(list)
    return f"The variance of the list is:{variance}"


list = [1, 2, 2.5, 3, 3.5, 1, 1, 2, 7, 8, 6]
print(calculate_variance(list))


def calculate_std(list):
    std = statistics.stdev(list)
    return f"The standard deviation of the list is:{std}"


list = [1, 2, 2.5, 3, 3.5, 1, 1, 2, 7, 8, 6]
print(calculate_std(list))


# 20 Write a function called is_prime, which checks if a number is prime.
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return f"The number {n} is not prime"
    return f"The number {n} is prime"


print(is_prime(6))


# 21 Write a functions which checks if all items are unique in the list.
def is_unique_item(list):
    unique_items = set()
    for element in list:
        if element in unique_items:
            return "The list has no unique items"
        unique_items.add(element)
    return "The list has unique items"


list = [1, 2, 3, 4, 5]
print(is_unique_item(list))


# 22 Write a function which checks if all the items of the list are of the same data type.
def same_data_type(list):
    if len(list) == 0:
        return "It has no elements"
    for i in list:
        if type(i) != type(list[0]):
            return "Not all elements have the same datatype"
    return "All elements have the same datatype"


list = [1, 2, "3", 4, 5]
print(same_data_type(list))

# 23 Write a function which check if provided variable is a valid python variable
import keyword


def valid_python_variable(variable_name):
    if variable_name in keyword.kwlist:
        return "The name of this variable is reserved"

    if variable_name.isidentifier():
        return "This name is a valid identifier"
    else:
        return "This name is not a valid identifier"


print(valid_python_variable("raise"))
print(valid_python_variable("1var"))
print(valid_python_variable("my_var"))

# 24 Vaya a la carpeta de datos y acceda al archivo countries-data.py.
import json
from collections import Counter

with open("countries_data.json", "r") as file:
    countries_data = json.load(file)


# 24.1 Cree una función llamada most_spoken_languages en el mundo.
# Debería devolver los 10 o 20 idiomas más hablados del mundo en orden descendente.
def most_spoken_languages(countries_data, top_n=10):
    ten_languages = []

    for languages in countries_data:
        if "languages" in languages:
            languages = languages["languages"]
            ten_languages.extend(languages)

    languages_frecuency = Counter(ten_languages)

    languages_10 = languages_frecuency.most_common(top_n)

    for i, _ in languages_10:
        return f"{i}:{_} paises"


# 24.2 Cree una función llamada most_populated_countries.
# Debería devolver los 10 o 20 países más poblados en orden descendente.
def most_populated_countries(countries_data, top_n=10):
    sorted_countries = sorted(
        countries_data["countries"], key=lambda x: x["population"], reverse=True
    )
    return sorted_countries[:top_n]


print(most_spoken_languages(countries_data, 5))
