### Package manager ###

import numpy

print(numpy.version.version)

lst = [1, 2, 3, 4, 5]
np_arr = numpy.array(lst)
print(np_arr)
print(len(np_arr))
print(np_arr * 2)

# pip show packagename # Nos da informacion sobre el paquete
# pip list # Nos muestra nuestra lista actual de paquetes instalados
# pip freeze # Nos da el nombre de los paquetes instalados junto con su version

import requests
"""A estas alturas ya está familiarizado con la forma de leer 
o escribir en un archivo ubicado en su máquina local. A veces, 
nos gustaría leer desde un sitio web usando una URL o desde una 
API. API son las siglas de Application Program Interface 
(Interfaz de programación de aplicaciones). Es un medio para 
intercambiar datos estructurados entre servidores principalmente 
como datos json. Para abrir una conexión de red, necesitamos un 
paquete llamado requests, que permite abrir una conexión de red 
e implementar operaciones CRUD (create, read, update and delete). 
En esta sección, cubriremos solo la lectura o la obtención de parte de un CRUD."""

# url = "https://github.com/Asabeneh"

# response = requests.get(url)
# print(response)
# print(response.headers)
# print(response.status_code)
# print(response.text)

url = "https://restcountries.com/v3.1/all?fields=name"

response = requests.get(url)
print(response)
print(response.status_code)
countries = response.json()
print(countries[:1])

country_names = [country['name']['official'] for country in countries]
for common in country_names:
    print(common)