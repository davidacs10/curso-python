### Strings ###

my_first_string = "Hola, Python!"  # Aqui creamos una variable con string
my_other_string = "Hola, python:)"  # Otra variable con string
print(my_first_string)  # imprimiendo la primera variable
print(my_other_string)  # imprimiendo la segunda variable
print(len(my_first_string))  # imprimiento la longitud de los caracteres
print(len(my_other_string))  # imprimiento la longitud de los caracteres
# Imprimiendo ambos strings para formar una oracion
print(my_first_string + " " + my_other_string)

new_line_string = "Este es un string con\nsalto de linea"  # \n para saltar de linea
print(new_line_string)

my_string_tab = "\tEste es un string con indentacion"  # \t para indentar la linea
print(my_string_tab)

my_string_scape = "\\tEste es un string \\nescapado"
print(my_string_scape)

# Formateo

name, surname, age = ("David", "Campos", 25)
print("Mi nombre es: %s %s y tengo %.1f años" % (name, surname, age))
print("Mi nombre es: {} {} y tengo {} años".format(name, surname, age))
print(f"Mi nombre es: {name} {surname} y tengo {age} años")

# Desempaquetado de caracteres

name = "David"  # Creamos la variable con el string
# Creamos el numero de variables que coincidan con el numero
# caracteres del string
a, b, c, d, e = name
print(a)
print(d)
print(b)

# Division

# se crea la variable y luego la variable que contiene nuestro
# string y se abren los corchetes y se empieza a enumerar desde el 0 como primer numero
language_slice = name[1:3]
print(language_slice)

# cuando no indicamos el numero antes de los : este empezara siempre desde el 0
language_slice = name[:2]
print(language_slice)

# cuando indicamos el numero antes de los : este llegara hasta el ultimo caracter
language_slice = name[2:]
print(language_slice)

#
language_slice = name[0:2:3]
print(language_slice)

# Reversa

language_slice = name[::-1]
print(language_slice)

hello = "world"
print(hello[::-1])

# Skip

name = "David"
dvd = name[0:6:2]
print(dvd)

# Funciones del lenguaje

# Pone la primera letra en mayuscula
print(name.capitalize())
# Todo el string en mayuscula
print(name.upper())
# Cuenta los caracteres que se repiten
print(name.count("d"))
# Es numerico el string?
print(name.isnumeric())
# Si es numerico el string
print("1".isnumeric())
# Todo el string en minuscula
print(name.lower())
# Es como si preguntara el string que esta en minuscula es mayuscula? //False
print(name.lower().isupper())
# Empieza el string con "da" //False
print(name.startswith("da"))
# "Da" no es igual a "da" como vimos anteriormente en operadores // False
print("Da" == "da")
print(name.endswith("id"))
