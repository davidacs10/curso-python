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
    list.append(item)
    return list


fruits = ["Mango", "Lemon", "Orange"]
print(add_item(fruits, "Papaya"))


# 12 Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
def remove_item(list, item):
    if item in list:
        list.remove(item)
    return list


print(remove_item(fruits, "Mango"))


# 13 Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
def sum_of_numbers(nums):
    total = 0
    for num in range(nums + 1):
        total += num
    return total


print(sum_of_numbers(10))


# 14 Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
def sum_of_odds(nums):
    odd_total = 0
    for num in range(nums + 1):
        if num % 2 == 0:
            odd_total += num
    return odd_total


print(sum_of_odds(5))


# 15 Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that range.
def sum_of_even(nums):
    even_total = 0
    for num in range(nums + 1):
        if num % 2 != 0:
            even_total += num
    return even_total


print(sum_of_even(7))


# 16 Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
def evens_and_odds(nums):
    evens_numbers = []
    odds_numbers = []
    for num in range(nums + 1):
        if num % 2 == 0:
            evens_numbers.append(num)
        else:
            odds_numbers.append(num)
    return f"The numbers of evens is :{len(evens_numbers)}\nThe numbers of odds is: {len(odds_numbers)}"


print(evens_and_odds(100))


# 17 Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return fact


print(factorial(5))


# 18 Call your function is_empty, it takes a parameter and it checks if it is empty or not
def is_empty(lst):
    return len(lst) == 0


lst = []
print(is_empty(lst))
# 19 Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).
import statistics

lst = [1, 2, 3, 4, 5]


# La media (mean) aritmética es la suma de los valores dividida entre el número de observaciones. Es comúnmente denominada «promedio», aunque hay muchas formas de definir el promedio matemáticamente. Es una medida de tendencia central de los datos.
def calculate_mean(lst):
    return statistics.mean(lst)


print(calculate_mean(lst))


# Retorna la mediana (median) (valor central) de los datos numéricos, utilizando el método clásico de «media de los dos del medio». Si data está vacío, se lanza una excepción StatisticsError. data puede ser una secuencia o un iterable.
def calculate_median(lst):
    return statistics.median(lst)


print(calculate_median(lst))


# (mode) Retorna el valor más común del conjunto de datos discretos o nominales data.La moda (cuando existe) es el valor más representativo y sirve como medida de tendencia central.
def calculate_mode(lst):
    return statistics.mode(lst)


print(calculate_mode(lst))


def calculate_range(lst):
    return range(len(lst))


print(calculate_range(lst))


# Retorna la varianza muestral de data, que debe ser un iterable de al menos dos números reales. La varianza, o momento de segundo orden respecto a la media, es una medida de la variabilidad (difusión o dispersión) de los datos. Una alta varianza indica que los datos están dispersos; una baja varianza indica que los datos están agrupados estrechamente alrededor de la media.
def calculate_variance(lst):
    return statistics.variance(lst)


print(calculate_variance(lst))


# Retorna la desviación típica muestral (la raíz cuadrada de la varianza muestral). Consultar variance() para los argumentos y otros detalles.
def calculate_std(lst):
    return statistics.stdev(lst)


print(calculate_std(lst))


# 20 Write a function called is_prime, which checks if a number is prime.
def is_prime(num):
    if num <= 1:
        return False

    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return f"Not prime"

    return f"Is prime"


print(is_prime(920))


# 21 Write a functions which checks if all items are unique in the list.
def unique_items(lst):
    unique_elements = set()
    for i in lst:
        if i in unique_elements:
            return False
        else:
            unique_elements.add(i)

    return True


lst = [1, 2, 3, 4, 4, 4, 4]
print(unique_items(lst))


# 22 Write a function which checks if all the items of the list are of the same data type.
def check_data_type(lst):
    first_element = type(lst[0])
    for i in lst:
        if type(i) != first_element:
            return False
    return True


lst = ["1", "hola", "hola"]
print(check_data_type(lst))


# 23 Write a function which check if provided variable is a valid python variable
def valid_variable(var):
    return var.isidentifier()


print(valid_variable("thirty_days_of_python"))
# 24 Go to the data folder and access the countries-data.py file.
import json
from collections import Counter

with open("data/countries_data.json", "r") as file:
    data = json.load(file)


# 25 Create a function called the most_spoken_languages in the world. It should return 10 or 20 most spoken languages in the world in descending order
def most_spoken_languages(num):
    top_languages = []
    for languages in data:
        top_languages.extend(languages["languages"])

    most_spoken = Counter(top_languages)
    top_spoken_languages = most_spoken.most_common(num)
    print(f"The {num} languages most spoken:")
    for country, count in top_spoken_languages:
        print(f"{country}: {count}")


most_spoken_languages(11)


# 26 Create a function called the most_populated_countries. It should return 10 or 20 most populated countries in descending order.
def most_populated_countries(num):
    most_populated = []
    for country_data in data:
        most_populated.append((country_data["name"], country_data["population"]))

    most_populated_countries_dict = Counter(dict(most_populated))
    top_most_populated_countries = most_populated_countries_dict.most_common(num)
    print(f"The {num} most populated countries in the world:")
    for country, population in top_most_populated_countries:
        print(f"{country}: {population}")


most_populated_countries(5)
