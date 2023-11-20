# Ejercicios variables

# 1 Declarar una variable de nombre y asignarle un valor
name = "David"
# 2 Declarar una variable de apellido y asignarle un valor
last_name = "Campos"
# 3 Declarar una variable de nombre completo y asignarle un valor
full_name = name + " " + last_name
# 4 Declarar una variable de país y asignarle un valor
country = "Spain"
# 5 Declarar una variable de ciudad y asignarle un valor
city = "Madrid"
# 6 Declarar una variable de edad y asignarle un valor
age = "20"
# 7 Declarar una variable de año y asignarle un valor
year = 2022
# 8 Declarar una variable is_married y asignarle un valor
is_married = False
# 9 Declarar una variable is_true y asignarle un valor
is_true = True
# 10 Declarar una variable is_light_on y asignarle un valor
is_light_on = True
# 11 Declarar varias variables en una línea
full_name, country, city, age, year = "David Campos", "Spain", "Madrid", 20, 2024

# 12 Comprueba el tipo de datos de todas tus variables usando la función incorporada type()
print(type(name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
# 13 Usando la función incorporada len(), encuentra la longitud de tu nombre
print(len(name))
# 14 Compara la longitud de tu nombre y tu apellido
print(len(last_name))
# 15 Declare 5 como num_one y 4 como num_two
num_one = 5
num_two = 4
# 16 Suma num_one y num_two y asigna el valor a un total variable
sum = num_one + num_two
# 17 Reste num_two de num_one y asigne el valor a una variable diff
diff = num_two - num_one
# 18 Multiplicar num_two y num_one y asignar el valor a un producto variable
product = num_two * num_one
# 19 Divida num_one por num_two y asigne el valor a una división variable
divide = num_one + num_two
# 20 Utilice la división de módulos para encontrar num_two dividido por num_one y asigne el valor a un residuo variable
modulus = num_two % num_one
# 21 Calcule num_one a la potencia de num_two y asigne el valor a una variable exp
exp = num_one**num_two
# 22 Encuentre la división de num_one por num_two y asigne el valor a una variable floor_division
floor_division = num_one // num_two
# 23 El radio de un círculo es de 30 metros.
r = 30
# 24 Calcule el área de un círculo y asigne el valor a un nombre de variable de area_of_circle
pi = 3.14
area_of_circle = pi * r**2
print(area_of_circle)
# 25 Calcule la circunferencia de un círculo y asigne el valor a un nombre de variable de circum_of_circle
circum_of_circle = 2 * pi * r
# 26 Tome el radio como entrada del usuario y calcule el área.
r = float(input("Ingrese radio: "))
area_of_circle = pi * r**2
print(area_of_circle)
# 27 Utilice la función de entrada incorporada para obtener el nombre, los apellidos, el país y la edad de un usuario y almacenar el valor en sus nombres de variables correspondientes
name = input("Name: ")
print(name)
last_name = input("last_name: ")
print(last_name)
country = input("country: ")
print(country)
age = int(input("age: "))
print(age)
# 28 Ejecute help('keywords') en el shell de Python o en su archivo para comprobar las palabras reservadas o palabras clave de Python
help("keywords")
print(help)
