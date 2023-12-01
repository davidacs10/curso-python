# Loops

# 1 Iterate 0 to 10 using for loop, do the same using while loop.
for i in range(11):
    print(f"for loop: {i}")

print("----------------")

count = 1
while count <= 10:
    print(f"while loop {count}")
    count = count + 1

# 2 Iterate 10 to 0 using for loop, do the same using while loop.
numbers = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
for number in numbers:
    print(f"for loop reverse: {number}")

print("----------------")

count = 10
while 0 <= count:
    print(f"while loop reverse {count}")
    count = count - 1

# 3 Write a loop that makes seven calls to print(), so we get on the output the following triangle:
for i in range(1, 8):
    print("#" * i)
# 4 Use nested loops to create the following:
for i in range(1, 8):
    print("# " * 8)
# 5 Print the following pattern:
for i in range(0, 11):
    print(f"{i} * {i} = {i * i}")
# 6 Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
stack = ["Python", "Numpy", "Pandas", "Django", "Flask"]
for tech in stack:
    print(tech)

# 7 Use for loop to iterate from 0 to 100 and print only even numbers
for i in range(101):
    if i % 2 == 0:
        print(i)
# 8 Use for loop to iterate from 0 to 100 and print only odd numbers
for i in range(101):
    if i % 2 != 0:
        print(i)
# 9 Use for loop to iterate from 0 to 100 and print the sum of all numbers.
total = 0
for i in range(101):
    total += i
print(f"The sum of all numbers is {total}.")
# 10 Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
even_sum = 0
odd_sum = 0
for i in range(1, 101):
    if i % 2 == 0:
        even_sum = even_sum + i
    else:
        odd_sum = odd_sum + i
print(f"The sum of all evens is {even_sum}. And the sum of all odds is {odd_sum}.")
# 11 Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.
from data import country

countries = country.countries
land = []
for i in countries:
    if i.endswith("land"):
        land.append(i)
print(land)
# 12 This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
fruit = ["banana", "orange", "mango", "lemon"]
reverse_fruit_list = []
for i in reversed(fruit):
    reverse_fruit_list.append(i)
print(reverse_fruit_list)
# 13 Go to the data folder and use the countries_data.py file.
import json
from collections import Counter

with open("data/countries_data.json", "r") as file:
    data = json.load(file)
# 14 What are the total number of languages in the data
total_languages = set()
for laguages in data:
    total_languages.update(laguages["languages"])
print(len(total_languages))
# 15 Find the ten most spoken languages from the data
ten_languages = []
for languages in data:
    ten_languages.extend(languages["languages"])

# Contabiliza la frecuencia de cada lenguaje
most_spoken_language = Counter(ten_languages)
# Obtiene los 10 lenguajes más comunes
top_10_languages = most_spoken_language.most_common(10)
print(top_10_languages)
# Imprime los resultados
print("Los 10 lenguajes más hablados:")
for language, count in top_10_languages:
    print(f"{language}: {count}")
# 16 Find the 10 most populated countries in the world
most_populated = []
for country_data in data:
    most_populated.append((country_data["name"], country_data["population"]))
# Contabiliza la frecuencia de cada país
most_populated_country = Counter(dict(most_populated))
# Obtiene los 10 países con mayor población
top_10_populated_countries = most_populated_country.most_common(10)
print("Los 10 países más poblados del mundo:")
for countries, population in top_10_populated_countries:
    print(f"{countries}: {population}")
