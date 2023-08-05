### Loops ###

# While
my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 2
# Es opcional y solo se puede usar else en un while pero dentro de un while podemos usar if elif else dentro del if
else:
    print("Mi condicion es mayor o igual a 10")

print("La ejecucion continua")

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Se detiene la ejecucion")
        break
    print(my_condition)

print("La ejecucion continua")

# For

my_list = [3, 4, 25, 6, 4, 10]

for element in my_list:
    print(element)

my_tuple = (25, 1.75, "David", "Campos")
for element in my_tuple:
    print(element)

my_set = {"David", "Campos", 25}
for element in my_set:
    print(element)

my_dict = {
    "Nombre": "David",
    "Apellido": "Campos",
    "Edad": 25,
    "Lenguajes": {"HTML", "CSS", "Python"},
    1: 1.75,
}
for element in my_dict.values():
    print(element)

my_dict = {
    "Nombre": "David",
    "Apellido": "Campos",
    "Edad": 25,
    "Lenguajes": {"HTML", "CSS", "Python"},
    1: 1.75,
}
for element in my_dict:
    print(element)
    if element == "Edad":
        break
else:
    print("El bucle for para diccionario ha terminado")

for element in my_dict:
    print(element)
    if element == "Edad":
        continue
    print("Se ejecuta")
else:
    print("El bucle for para diccionario ha terminado")
