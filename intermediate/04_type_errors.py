### Type errors ###

# SyntaxError
# print "Hello world!" # SyntaxError
# Cuando hay un error en la sintaxis de el codigo
print("Hello world!")

# NameError
# print(age) # NameError
# Cuando la variable no esta definida 
age = 20
print(age)

# IndexError
languages = ["Python", "JavaScript", "PHP"]
print(languages[0]) # = Python
print(languages[1]) # = JavaScript
print(languages[2]) # = PHP
# print(languages[3]) # = IndexError
# Cuando el indice de la lista esta fuera de el rango.

# ModuleNotFoundError
# import maths # ModuleNotFoundError
# Cuando el modulo requerido no se encuentra
import math

# AttributeError
# print(math.PI) # AttributeError
# Cuando la funcion que estamos invocando no existe en el modulo
print(math.pi)

# KeyError
dct = {"name":"David", "lastname":"Campos", "age":20, "country":"Venezuela"}
# print(dct["city"]) # KeyError
# Cuando la llave no existe en el diccionario.
print(dct["lastname"])

# TypeError
# print(4 + "3") # TypeError
# el error se ejecuta porque no podemos sumarle un numero a un texto
print(4 + int("3"))

# ImportError
# from math import PI
# print(PI) # ImportError
# No hay una funcion llamada PI en el modulo math, en realidad se llama pi en (minusculas)
from math import pi
print(pi)

# ValueError
# print(int("20a")) # ValueError
# No podemos cambiar un string que contenga texto a un entero.

# ZeroDivisionError
# print(2/0) # ZeroDivisionError: division by zero
# No se puede dividir un numero entre cero
print(4/2)