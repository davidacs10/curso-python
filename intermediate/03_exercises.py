countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
countries_and_numbers = countries + numbers

### EXERCISES LEVEL 1 ###

# Explain the difference between map, filter, and reduce.
"""
map() aplica una funcion a un iterable y devuelve un iterable como resultado.
filter() aplica una funcion a un iterable para filtrar resultados en un iterable.
reduce() aplica una funcion a un iterable pero a diferencia de los otros 2, 
este devuelve un resultado unico.
"""
# Explain the difference between higher order function, closure and decorator
"""
Higher order function: Son funciones que pueden llamar a otras funciones.
closure: Son funciones que tienen funciones de si mismas.
decorator: Son funciones que pueden modificar otras funciones sin alterarlas.
"""
# Define a call function before map, filter or reduce, see examples.
def call_function(value):
    if value == countries:
        for i in countries:
            print(i)
    elif value == names:
        for i in names:
            print(i)
    elif value == numbers:
        for i in numbers:
            print(i)
# Use for loop to print each country in the countries list.
call_function(countries)
# Use for to print each name in the names list.
call_function(names)
# Use for to print each number in the numbers list.
call_function(numbers)

### EXERCISES LEVEL 2 ###
from functools import reduce

# Use map to create a new list by changing each country to uppercase in the countries list
def change_to_upper(lst):
    upper_case = lst.upper()
    return upper_case

print(list(map(change_to_upper, countries)))
# Use map to create a new list by changing each number to its square in the numbers list
def square(num):
    return num ** 2

print(list(map(square, numbers)))
# Use map to change each name to uppercase in the names list
print(list(map(change_to_upper, names)))
# Use filter to filter out countries containing 'land'.
def countries_with_land(value):
    country_with_land = value.endswith("land")
    return country_with_land

print(list(filter(countries_with_land, countries)))
# Use filter to filter out countries having exactly six characters.
def countries_with_six_characters(value):
    if len(value) == 6:
        return value
    
print(list(filter(countries_with_six_characters, countries)))
# Use filter to filter out countries containing six letters and more in the country list.
def countries_len(value):
    if len(value) >= 6:
        return value
    
print(list(filter(countries_len, countries)))    
# Use filter to filter out countries starting with an 'E'
def countries_with_e(value):
    return value.startswith("E")

print(list(filter(countries_with_e, countries)))  
# Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
chain_list_iterators = list((map(change_to_upper, filter(countries_len, filter(countries_with_e, countries)))))
print(chain_list_iterators)
# Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.
def get_string_lists(value):
    if value == str(value):
        return value

print(list(filter(get_string_lists, countries_and_numbers)))
# Use reduce to sum all the numbers in the numbers list.
def sum_numbers(x, y):
    return x + y

print(reduce(sum_numbers, numbers))
# Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
def contatenate_lst(sentence, country):
    if sentence:
        return f"{sentence}, {country}"
    else:
        return country

result_sentence = reduce(contatenate_lst, countries)
last_comma_index = result_sentence.rfind(",")
if last_comma_index != -1:
    result_sentence = f"{result_sentence[:last_comma_index]} and{result_sentence[last_comma_index + 1:]} are north European countries."

print(result_sentence)
# Declare a function called categorize_countries that returns a list of countries with some common pattern (you can find the countries list in this repository as countries.py(eg 'land', 'ia', 'island', 'stan')).
from countries import countries

def categorize_countries(func):
    matching_countries = list(filter(func, countries))
    return matching_countries

def pattern(value):
    return lambda country: value.lower() in country.lower()

print(categorize_countries(pattern("land")))
print(categorize_countries(pattern("ia")))
print(categorize_countries(pattern("island")))
print(categorize_countries(pattern("stan")))

# Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter.
def count_countries_by_initial_letter():
    def starts_with_letter(letter):
        return lambda country: country.lower().startswith(letter.lower())
    
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    country_counts = {}
    for letter in alphabet:
        filtered_countries = list(filter(starts_with_letter(letter), countries))
        country_counts[letter] = len(filtered_countries)

    return country_counts

print(count_countries_by_initial_letter())

# Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.py list in the data folder.
def get_first_ten_countries(lst):
    return lst[:10]

print(get_first_ten_countries(countries))
# Declare a get_last_ten_countries function that returns the last ten countries in the countries list.
def get_last_ten_countries(lst):
    return lst[-10:]

print(get_last_ten_countries(countries))

### EXERCISES LEVEL 3 ###

# Use the countries_data.py file and follow the tasks below:
from countries_data import countries_data as data
# Sort countries by name, by capital, by population
def sort_by_name():
    return sorted(data, key= lambda x: x["name"])

def sort_by_capital():
    return sorted(data, key= lambda x: x["capital"])

def sort_by_population():
    return sorted(data, key= lambda x: x["population"])

def sort_countries_by(type):
    if type == "name":
        return sort_by_name()
    elif type == "capital":
        return sort_by_capital()
    elif type == "population":
        return sort_by_population()

print(sort_countries_by("name"))
print(sort_countries_by("capital"))
print(sort_countries_by("population"))

# Sort out the ten most spoken languages by location.
def sort_languages_by_location():
    all_languages = [language for country in data for language in country.get("languages", [])]
    language_counts = {language: all_languages.count(language) for language in set(all_languages)}
    sorted_languages = sorted(language_counts.items(), key=lambda x: x[1], reverse=True)
    return sorted_languages[:10]

print(sort_languages_by_location())

# Sort out the ten most populated countries.
def sort_countries_by_population():

    sorted_countries = sorted(data, key=lambda x: x["population"], reverse=True)
    for country in sorted_countries[:10]:
        print(f"{country['name']}: {country['population']}")

sort_countries_by_population()