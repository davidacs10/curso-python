"""
1 Calculadora de Cuadrados:
Crea una función lambda que tome un número como argumento y devuelva su cuadrado. Luego, utiliza esta
función para calcular el cuadrado de varios números.
"""
square = lambda x: x**2
print(square(6))
numbers = [2, 4, 5, 6, 7, 8]
print(list(map(square, numbers)))

"""
2 Filtrar Números Pares:
Escribe una función lambda que filtre una lista de números y devuelva solo los números pares.
Prueba la función con una lista de números.
"""
even_numbers = lambda x: x % 2 == 0
print(even_numbers(2))
print(list(filter(even_numbers, numbers)))

"""
3 Ordenar Palabras por Longitud:
Define una función lambda que tome una cadena como argumento y devuelva su longitud.
Utiliza esta función como clave para ordenar una lista de palabras por longitud.
"""
length = lambda x: len(x)
print(length("hola"))
words = ["hello", "python", "love", "dog", "programming"]
print(sorted(words, key=length))

"""
4 Operaciones Matemáticas Básicas:
Crea funciones lambda para realizar operaciones matemáticas básicas como suma, resta,
multiplicación y división. Luego, utiliza estas funciones para realizar operaciones en dos números.
"""
suma = lambda a, b: a + b
resta = lambda a, b: a - b
multiplicacion = lambda a, b: a * b
divison = lambda a, b: a / b
print(suma(4, 2))
print(resta(4, 2))
print(multiplicacion(4, 2))
print(divison(4, 2))

"""
5 Generador de Números Primos:
Implementa una función lambda que verifique si un número es primo.
Luego, utiliza esta función en un generador para obtener una lista de números primos en un rango dado.
"""
is_prime = lambda num: num > 1 and all(num % i != 0 for i in range(2, int(num**0.5) + 1))
print(is_prime(25))

def prime_number_generator(start, end):
    return (num for num in range(start, end + 1) if is_prime(num))

print(list(prime_number_generator(10,50)))

"""
6 Conversión de Temperatura:
Define funciones lambda para convertir temperaturas de Celsius a Fahrenheit y viceversa.
Luego, aplica estas funciones a una lista de temperaturas.
"""
celsius_to_fahrenheit = lambda celsius: (celsius * 1.8) + 32
fahrenheit_to_celsius = lambda fahrenheit: (fahrenheit - 32) / 1.8

celsius = [0, 10, 20, 30, 40]

temperaturas_fahrenheit = list(map(celsius_to_fahrenheit, celsius))
print(temperaturas_fahrenheit)

nuevas_temperaturas_celsius = list(map(fahrenheit_to_celsius, temperaturas_fahrenheit))
print(nuevas_temperaturas_celsius)

"""
7 Filtrar Nombres Cortos:
Escribe una función lambda que filtre una lista de nombres y devuelva solo
aquellos que tienen una longitud inferior a cierto valor.
Prueba la función con una lista de nombres.
"""
length_names = lambda name: len(name) <= 5
names = ["David", "Jose", "George", "Abraham", "Luis", "Antoine"]
print(list(sorted(filter(length_names, names))))

"""
8 Comprobador de Números Positivos:
Crea una función lambda que tome un número como argumento y devuelva
True si es positivo y False si es negativo.
Utiliza esta función para filtrar una lista de números.
"""
positive_numbers = lambda num: num > 0
numbers = [i for i in range(-10, 11)]
print(numbers)
print(f"Filtrando numeros positivos: {list(filter(positive_numbers, numbers))}")