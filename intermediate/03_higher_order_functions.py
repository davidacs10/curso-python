### Higher Order Functions ###

# Funcion como parametro
def sum_numbers(nums):
    return sum(nums)

def higher_order_function(f, lst):
    summating = f(lst)
    return summating

lst = [1, 2, 3, 4, 5]

print(higher_order_function(sum_numbers, lst))

# Funcion como valor devuelto
# Square
def square(x):
    return x ** 2

# Cube
def cube(x):
    return x ** 3

# Absolute value
def absolute(x):
    if x >= 0:
        return x
    else:
        return -(x)

# Higher order function returning function
def higher_order_function(type):
    if type == "square":
        return square
    elif type == "cube":
        return cube
    elif type == "absolute":
        return absolute

result = higher_order_function("square")
print(result(3))
result = higher_order_function("cube")
print(result(3))
result = higher_order_function("absolute")
print(result(-3))

# Cierres de Python
def add_ten():
    ten = 10
    def add(num):
        return num + ten
    return add

closure_result = add_ten()
print(closure_result(5))
closure_result = add_ten()
print(closure_result(10))

def funcion_externa(x):
    def funcion_interna(y):
        return x + y
    return funcion_interna

closure = funcion_externa(10)
result = closure(5)
print(result)

# Decoradores de Python
# Normal function
def greeting():
    return "Welcome to Python"

def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_upper = func.upper()
        return make_upper
    return wrapper

g = uppercase_decorator(greeting)
print(g())


"""
En este caso, en lugar de llamar explícitamente al decorador 
(g = uppercase_decorator(greeting)), utilizamos la sintaxis de decorador 
@uppercase_decorator justo antes de la definición de la función greeting. 
Esto es equivalente a aplicar el decorador manualmente. Al llamar a greeting(), 
obtenemos el mismo resultado en mayúsculas.
"""
@uppercase_decorator
def hello():
    return "Hello Python"
"""
Sin embargo, la sintaxis de decorador @ espera una definición de función y no una llamada a función.
"""
print(hello())

# Aplicación de varios decoradores a una sola función
"""
Estas funciones decoradoras son funciones de orden superior
que toman funciones como parámetros
"""
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_upper = func.upper()
        return make_upper
    return wrapper

def split_string_decorator(function):
    def wrapper():
        func = function()
        make_split = func.split()
        return make_split
    return wrapper

@split_string_decorator
@uppercase_decorator
def hello_python():
    return "Hello Python"

print(hello_python())

# Aceptación de parámetros en funciones de decorador

def decorator_with_parameters(function):
    def wrapper_accepting_parameters(para1, para2, para3):
        function(para1, para2, para3)
        print(f"I live in {para3}")
    return wrapper_accepting_parameters

@decorator_with_parameters
def print_full_name(first_name, last_name, country):
    print(f"I am {first_name} {last_name}. I love to learn.")

print_full_name("David", "Campos", "Venezuela")

# Funciones de orden superior incorporadas

"""Algunas de las funciones integradas de orden superior que cubrimos en esta parte son:
map(), filter() y reduce(). La función lambda se puede pasar como parámetro 
y el mejor caso de uso de las funciones lambda es en funciones como map(), filter() y reduce()."""

"""
Python - Función de mapa
Se utiliza para aplicar una función a todos los elementos de una o más secuencias (listas, tuplas, etc.).
y devuelve un iterador que produce los resultados.
"""

"""
Sintaxis
map(function, iterable)
"""

# Ejemplo 1
numbers = [1, 2, 3, 4, 5]
def square(x):
    return x ** 2
numbers_squared = map(square, numbers)
print(list(numbers_squared))

# Apliquemos este ejemplo con lambda
numbers_squared = map(lambda x : x ** 2, numbers)
print(list(numbers_squared))

# Ejemplo 2
numbers_str = ["1", "2", "3", "4", "5"]
print(numbers_str)
numbers_int = map(int, numbers_str)
print(list(numbers_int))

# Ejemplo 3
names = ["David", "Alejandro", "Campos", "Specht"]

def change_to_upper(name):
    return name.upper()

change_to_uppercase = map(change_to_upper, names)
print(list(change_to_uppercase))

# Apliquemos este ejemplo con lambda
change_to_uppercase = map(lambda name: name.upper(), names)
print(list(change_to_uppercase))

"""
Lo que hace este map es iterar sobre una lista de nombres
los cambia a mayusculas y devuelve una lista con nombres en mayuscula
"""

"""
Python - Función de filtro
Se utiliza para filtrar elementos de una secuencia (como una lista)
basándose en una función que devuelve valores booleanos (True o False).
"""

"""
Sintaxis
filter(function, iterable)
"""

# Ejemplo 1
# Vamos a filtrar solo los numeros pares
numbers = [1, 2, 3, 4, 5]

def is_even(num):
    if num % 2 == 0:
        return True
    return False

only_even_numbers = filter(is_even, numbers)
print(list(only_even_numbers))

# Ejemplo 2
numbers = [1, 2, 3, 4, 5]

def is_odd(num):
    if num % 2 != 0:
        return True
    return False

only_odd_numbers = filter(is_odd, numbers)
print(list(only_odd_numbers))

# Ejemplo 3
names = ["David", "Jose", "Alejandro", "Mathias", "Abraham"]

def is_long_name(name):
    if len(name) > 5:
        return True
    return False

is_long = filter(is_long_name, names)
print(list(is_long))

"""
Python - Función de reducción
La función reduce() está definida en el módulo functools y debemos importarla desde este módulo. 
Al igual que el mapa y el filtro, toma dos parámetros, una función y un iterable. 
Sin embargo, no devuelve otro iterable, sino que devuelve un único valor.
"""

from functools import reduce

# Ejemplo 1
numbers_str = ["1", "2", "3", "4", "5"]
def sum_numbers(x, y):
    return int(x) + int(y)

total = reduce(sum_numbers, numbers_str)
print(total)