### Exercises: Level 1 ###

# Write a function which count number of lines and number of words in a text.
def count_lines_and_words(file_name):

    try:
        with open(file_name, "r", encoding="utf-8") as f:
            content = f.read()
            num_lines = len(content.splitlines())
            words = content.split()
            num_words = len(words)

            return num_lines, num_words
    except FileNotFoundError:
        print(f"El archivo '{file_name}' no fue encontrado.")
        return None, None
    except Exception as e:
        print(f"Error al procesar el archivo {e}")
        return None, None
    
# All the files are in the data the folder: 
# a) Read obama_speech.txt file and count number of lines and words 
obama_speech = "../curso-python/intermediate/data/obama_speech.txt"
lines, words = (count_lines_and_words(obama_speech))

if lines is not None and words is not None:
    print(f"El {obama_speech} tiene {lines} lineas y {words} palabras")

# b) Read michelle_obama_speech.txt file and count number of lines and words 
michelle_speech = "../curso-python/intermediate/data/michelle_obama_speech.txt"
lines, words = (count_lines_and_words(michelle_speech))

if lines is not None and words is not None:
    print(f"El {michelle_speech} tiene {lines} lineas y {words} palabras")

# c) Read donald_speech.txt file and count number of lines and words
donald_speech = "../curso-python/intermediate/data/donald_speech.txt"
lines, words = (count_lines_and_words(donald_speech))

if lines is not None and words is not None:
    print(f"El {donald_speech} tiene {lines} lineas y {words} palabras")

# d) Read melina_trump_speech.txt file and count number of lines and words
melina_trump_speech = "../curso-python/intermediate/data/melina_trump_speech.txt"
lines, words = (count_lines_and_words(melina_trump_speech))

if lines is not None and words is not None:
    print(f"El {melina_trump_speech} tiene {lines} lineas y {words} palabras")


"""
Read the countries_data.json data file in data directory, 
create a function that finds the ten most spoken languages
"""
# import json
# from collections import Counter
# def most_spoken_languages(file_name, top_n):
#     try:
#         with open(file_name, "r", encoding="utf-8") as f:
#             data = json.load(f)
#         language_lst = []
#         for languages in data:
#             languages = languages["languages"]
#             language_lst.extend(languages)
        
#         languages_frecuency = Counter(language_lst)
#         languages_frecuency = language_lst.most_common(top_n)
#         return languages_frecuency
        
    
#     except FileNotFoundError:
#         print(f"El archivo '{file_name}' no fue encontrado.")
#         return None
#     except json.JSONDecodeError:
#         print(f"Error al decodificar el archivo JSON.")
#         return None
#     except Exception as e:
#         print(f"Error al procesar el archivo: {e}")
#         return None
    
# file_name = "intermediate/data/countries_data.json"
# result = most_spoken_languages(file_name, 5)

# print(result)
import json
from collections import Counter

def most_spoken_languages(filename, top_n):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)

        languages_lst = []
        for i in data:
            if "languages" in i:
                languages = i["languages"]
                languages_lst.extend(languages)
        
        languages_frecuency = Counter(languages_lst)
        common_languages = [(count, language) for language, count in languages_frecuency.most_common(top_n)]

        return common_languages
    
    except FileNotFoundError:
        print(f"El archivo '{filename}' no fue encontrado.")
        return None
    except json.JSONDecodeError:
        print(f"Error al decodificar el archivo JSON.")
        return None
    except Exception as e:
        print(f"Error al procesar el archivo: {e}")
        return None

file_name = "../curso-python/intermediate/data/countries_data.json"

result = most_spoken_languages(file_name, 3)

if result is not None:
    print(result)

"""Read the countries_data.json data file in data directory, 
create a function that creates a list of the ten most populated countries"""
def most_populated_countries(filename, top_n):
    try:
        with open(filename, 'r') as file:
                data = json.load(file)

        sorted_countries = sorted(data, key=lambda x: x["population"], reverse=True)
        top_countries = sorted_countries[:top_n]

        lst = []
        for country in top_countries:
            country_data = {"country":country["name"], "population":country["population"]}
            lst.append(country_data)

        print(lst)
    except FileNotFoundError:
        print(f"El archivo '{filename}' no fue encontrado.")
        return None
    except json.JSONDecodeError:
        print(f"Error al decodificar el archivo JSON.")
        return None
    except Exception as e:
        print(f"Error al procesar el archivo: {e}")
        return None
file_name = "../curso-python/intermediate/data/countries_data.json"
most_populated_countries(file_name, 3)

### Exercises: Level 2 ###

# Extract all incoming email addresses as a list from the email_exchange_big.txt file.
import re

# def extract_email_address(archive):
#     with open(archive, "r") as file:
#         content = file.read()

#         pattern_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
#         found_email = re.findall(pattern_email, content)

#         return found_email
    
# archive = "../curso-python/intermediate/data/email_exchanges_big.txt"
# emails = extract_email_address(archive)

# if emails:
#     print("Direcciones de correo electrónico encontradas:")
#     for email in emails:
#         print(email)
# else:
#     print("No se encontraron direcciones de correo electrónico en el archivo.")

"""
Find the most common words in the English language. Call the name of your function 
find_most_common_words, it will take two parameters - a string or a file and a positive integer, 
indicating the number of words. Your function will return an array of tuples in descending order. 
Check the output
"""

def find_most_common_words(file_path, num_words):
    try:

        with open(file_path, "r") as file:
            text = file.read()

        words = re.findall(r"\b\w+\b", text.lower())
        word_counts = Counter(words)
        sorted_words = sorted(word_counts.items(), key=lambda x:x[1], reverse=True)
        return sorted_words[:num_words]
    
    except FileNotFoundError:
        print(f"Error: El archivo '{file_path}' no fue encontrado.")

    except Exception as e:
        print(f"Error inesperado: {e}")


# Use the function, find_most_frequent_words to find: 
# a) The ten most frequent words used in Obama's speech
        
file = "../curso-python/intermediate/data/obama_speech.txt"
frequent_words_obama_speech = find_most_common_words(file, 10) 
print(frequent_words_obama_speech)

# b) The ten most frequent words used in Michelle's speech 

file = "../curso-python/intermediate/data/michelle_obama_speech.txt"
frequent_words_michelle_speech = find_most_common_words(file, 10)
print(frequent_words_michelle_speech)

# c) The ten most frequent words used in Trump's speech

file = "../curso-python/intermediate/data/donald_speech.txt"
frequent_words_trump_speech = find_most_common_words(file, 10)
print(frequent_words_trump_speech)

# d) The ten most frequent words used in Melina's speech

file = "../curso-python/intermediate/data/melina_trump_speech.txt"
frequent_words_melina_speech = find_most_common_words(file, 10)
print(frequent_words_melina_speech)
