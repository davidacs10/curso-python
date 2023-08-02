### Dictionaries ###

# Definicion

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre": "David", "Apellido": "Campos", "Edad": 25, 1: "Python"}
# Aqui estamos agregando un set a la clave "Lenguajes"
my_dict = {
    "Nombre": "David",
    "Apellido": "Campos",
    "Edad": 25,
    "Lenguajes": {"HTML", "CSS", "Python"},
    1: 1.75,
}

print(my_other_dict)
print(my_dict)

print(len(my_other_dict))
print(len(my_dict))

# Busqueda

# Para la busqueda en vez de buscar por el valor de la clave, se busca es por la clave dentro del diccionario
print(my_dict[1])
print(my_dict["Nombre"])

# Campos retorna falso porque se busca la clave, no el valor.
print("Campos" in my_dict)
print("Apellido" in my_dict)

# Insercion

# Para insertar una nueva clave a nuestro diccionario se selecciona la variable que lo contiene,
# seguido de la clave junto con el valor que queremos insertar
my_dict["Calle"] = "Calle David"
print(my_dict)

# Actualizacion

# Para actualizar se selecciona la variable que contiene el diccionario y
# luego entre corchetes se coloca la clave y esto se iguala a el valor que queremos actualizar
my_dict["Nombre"] = "Jose"
print(my_dict)

# Eliminacion

# Para eliminar se usa del, la variable y su clave.
del my_dict["Calle"]
print(my_dict)

# Otras operaciones

# Imprime los items en forma de lista
print(my_dict.items())
# Imprime las claves en forma de lista
print(my_dict.keys())
# Imprime los valores en forma de lista
print(my_dict.values())

my_list = ["Nombre", 1, "Piso"]

my_new_dict = dict.fromkeys(my_list)
print(my_new_dict)
