# Variables

my_name = "David"
print(my_name)

my_age = 25
print(my_age)

my_bool_variable = True
print(my_bool_variable)

# Esta variable la creamos para poder cambiar el tipo de dato de int a str
my_int_to_str_variable = str(my_age)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

# Concatenacion de variables en un print
print(my_name, my_age, my_bool_variable)
print("Este es el valor de:", my_bool_variable)

# Algunas funciones del sistema
print(len(my_name))  # Solo se puede usar para string
print(
    len(my_int_to_str_variable)
)  # Aqui si puede funcionar porque anteriormente cambiamos el tipo de int a str

# Variables en una sola linea. Cuidado con abusar de esta sintaxis!
name, age, country, alias = "David", 25, "Venezuela", "d4vidwp"
print(
    "Mi nombre es:",
    name,
    ". Tengo:",
    age,
    ". Vivo en:",
    country,
    ". Mi alias es:",
    alias,
    ".",
)

# Inputs
# name = input("Cual es tu nombre? ")
# age = input("Cual es tu edad? ")
# print(name)
# print(age)

# Cambiamos su tipo
name = 25
age = "David"
print(name)
print(age)

# Forzamos el tipo?
address: str = "Mi direccion"
address = 25
address = True
address = 1.5
print(type(address))
