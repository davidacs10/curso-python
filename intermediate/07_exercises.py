### Exercises ###

"""Read this url and find the 10 most frequent words. 
romeo_and_juliet = 'https://www.gutenberg.org/cache/epub/1513/pg1513.txt'"""

import requests
import re
# from bs4 import BeautifulSoup
from collections import Counter
import numpy as np
from collections import defaultdict

romeo_and_juliet = 'https://www.gutenberg.org/cache/epub/1513/pg1513.txt'

response = requests.get(romeo_and_juliet)
print(response)
print(response.status_code)
html_content = response.text

# soup = BeautifulSoup(html_content, 'html.parser')
# text = soup.get_text()

pattern = r'[^\w\s]'
clean_text = re.sub(pattern, "", html_content)

words = clean_text.lower().split()
word_counts = Counter(words)

top_10_common_words = word_counts.most_common(10)
print(top_10_common_words)

# Read the cats API and cats_api = 'https://api.thecatapi.com/v1/breeds' and find :
# the min, max, mean, median, standard deviation of cats' weight in metric units.

cats_api = 'https://api.thecatapi.com/v1/breeds'
response = requests.get(cats_api)
breeds_data = response.json()

weights = []

# Obtener los pesos de los gatos en unidades métricas
for breed in breeds_data:
    weight = breed.get('weight', {}).get('metric', None)
    if weight:
        # Algunos pesos pueden estar en un rango, por lo que solo tomamos el primer valor
        weight = weight.split()[2]
        weights.append(float(weight))

# Realizar los cálculos estadísticos
if weights:
    min_weight = np.min(weights)
    max_weight = np.max(weights)
    mean_weight = np.mean(weights)
    median_weight = np.median(weights)
    std_weight = np.std(weights)

    # Imprimir los resultados
    print("Mínimo peso:", min_weight)
    print("Máximo peso:", max_weight)
    print("Media del peso:", mean_weight)
    print("Mediana del peso:", median_weight)
    print("Desviación estándar del peso:", std_weight)
else:
    print("No se encontraron datos de peso para los gatos.")

# the min, max, mean, median, standard deviation of cats' lifespan in years.

lifespan = []
for breed in breeds_data:
    life = breed.get('life_span')
    if life:
        life = life.split()[0]
        lifespan.append(float(life))

if lifespan:
    min_lifespan = np.min(lifespan)
    max_lifespan = np.max(lifespan)
    mean_lifespan = np.mean(lifespan)
    median_lifespan = np.median(lifespan)
    std_lifespan = np.std(lifespan)

    print("Mínimo de logevidad:", min_weight)
    print("Máximo de logevidad:", max_weight)
    print("Media de logevidad:", mean_weight)
    print("Mediana de logevidad:", median_weight)
    print("Desviación estándar de logevidad:", std_weight)

# Create a frequency table of country and breed of cats

frequency_table = defaultdict(int)

# Construir la tabla de frecuencias
for breed in breeds_data:
    country = breed.get('origin')
    name = breed.get('name')
    frequency_table[(country, name)] += 1

# Imprimir la tabla de frecuencias
print("Tabla de frecuencias de país y raza de gatos:")
print("-" * 60)
print("| País                 | Raza                 | Frecuencia |")
print("-" * 60)
for (country, name), frequency in frequency_table.items():
    print(f"| {country:<20} | {name:<20} | {frequency:<10} |")
print("-" * 60)

# Read the countries API and find

countries_api = 'https://restcountries.com/v3.1/all'
response = requests.get(countries_api)
countries = response.json()

# the 10 largest countries

countries_areas = [(country['name']['common'], country['area']) for country in countries]
countries_areas_known = [(name, area) for name, area in countries_areas if area is not None]
countries_areas_known_sorted = sorted(countries_areas_known, key=lambda x: x[1], reverse=True)
top_10_countries = (countries_areas_known_sorted[:10])
print("Los 10 países más grandes:")
for rank, (country, area) in enumerate(top_10_countries, start=1):
    print(f"{rank}. {country}: {area} km²")

# the 10 most spoken languages

all_languages = [language for country in countries for language in country.get('languages', {}).values()]
language_counter = Counter(all_languages)

top_most_spoken_languages = language_counter.most_common(10)

for rank, (language, count) in enumerate(top_most_spoken_languages, start=1):
    print(f"{rank}. {language}: {count} países")

# the total number of languages in the countries API

unique_languages = set()

for country in countries:
    languages = country.get('languages', {})
    for language in languages.values():
        unique_languages.add(language)

total_languages = len(unique_languages)
print(total_languages)


