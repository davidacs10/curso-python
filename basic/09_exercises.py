# # 1 Iterate 0 to 10 using for loop, do the same using while loop.
# for number in range(11):
#     print(number)

# count = 0
# while count < 11:
#     print(count)
#     count = count + 1

# # 2 Iterate 10 to 0 using for loop, do the same using while loop.
# for number in range(10, -1, -1):
#     print(number)

# count = 10
# while count >= 0:
#     print(count)
#     count = count - 1

# 3 Write a loop that makes seven calls to print(), so we get on the output the following triangle:
# for i in range(1, 8):
#     print("#" * i)

# 4 Use nested loops to create the following:
# for _ in range(8):
#     for _ in range(8):
#         print("#", end=" ")
#     print()

# # 5 Print the following pattern:
# for i in range(11):
#     for _ in range(11):
#         result = _ * i
#         if _ != i:
#             continue
#         print(f"{_} x {i} =", result)

# for i in range(11):  # Iteramos desde 0 hasta 10
#     result = i * i  # Calculamos el resultado de la multiplicación
#     print(f"{i} x {i} = {result}")

# 6 Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
# stack = ["Python", "Numpy", "Pandas", "Django", "Flask"]
# for _ in stack:
#     print(_)

# 7 Use for loop to iterate from 0 to 100 and print only even numbers
# for number in range(2, 102, 2):
#     print(number)

# 8 Use for loop to iterate from 0 to 100 and print only odd numbers
# for number in range(0, 100):
#     if number % 2 == 0:
#         continue
#     print(number)

# 9 Use for loop to iterate from 0 to 100 and print the sum of all numbers.
addition = 0
for number in range(101):
    # En esta linea de codigo estamos agregando a la variable suma el resultado de numero + suma
    addition = number + addition
    if addition != 5050:
        continue
    print(f"The sum of all numbers is {addition}")

# 10 Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
sum_even = 0
sum_odd = 0
for number in range(101):
    if number % 2 == 0:
        sum_even += number
    else:
        sum_odd += number
print(f"The sum of all evens is {sum_even}. And the sum of all odds is {sum_odd}.")

# 11 Go to the data folder and use the countries.py file.
# Loop through the countries and extract all the countries containing the word land.

from countries import countries

countries_with_land = []

for country in countries:
    if "land" in country.lower():
        countries_with_land.append(country)
print("Countries contain word land: ")
for country in countries_with_land:
    print(country)

# 12 This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
fruit = ["banana", "orange", "mango", "lemon"]
for i in reversed(fruit):
    print(i)

fruit = ["banana", "orange", "mango", "lemon"]
length = len(fruit)
for i in range(length):
    print(fruit[length - i - 1])

# 13 Go to the data folder and use the countries_data.py file.
import json
from collections import Counter

with open("basic/countries_data.json", "r") as archivo:
    # Lee el contenido del archivo y carga los datos en una variable
    countries_data = json.load(archivo)

### What are the total number of languages in the data
unique_languages = set()

for dictionary in countries_data:
    if "languages" in dictionary:
        languages = dictionary["languages"]
        unique_languages.update(languages)
number_unique_languages = len(unique_languages)

print(number_unique_languages)

### Find the ten most spoken languages from the data
ten_languages = []

for languages in countries_data:
    if "languages" in languages:
        languages = languages["languages"]
        ten_languages.extend(languages)

languages_frecuency = Counter(ten_languages)

languages_10 = languages_frecuency.most_common(10)

for i, _ in languages_10:
    print(f"{i}:{_} paises")

### Find the 10 most populated countries in the world
# sorted_countries = sorted(countries_data, key=lambda x: x["population"], reverse=True)
# top_10_countries = sorted_countries[:10]

# for country in top_10_countries:
#     print(f"{country['name']}: {country['population']} habitantes")
