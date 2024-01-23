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