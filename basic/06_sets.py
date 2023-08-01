### Sets ###

# Definicion

my_set = set()
my_other_set = {}

# Esto es un set
print(type(my_set))
# Inicialmente es un dict
print(type(my_other_set))

my_other_set = {"David", "Campos", 25}
# Si ejecutamos varias veces el codigo hasta aqui, nos daremos cuenta que un set es una estructura no ordenada
# Los elementos de un set se organizaran de manera aleatoria.
print(my_other_set)

print(len(my_other_set))

# Insercion

# Lo mismo sucede en este caso, agregamos el elemento y se agrega de forma aleatoria en nuestro set.
my_other_set.add("d4vidwp")
print(my_other_set)

# En esta situacion intentamos duplicar el elemento en nuestro set pero al imprimir solo nos dara uno.
# Un set no acepta elementos duplicados.
my_other_set.add("d4vidwp")
print(my_other_set)

# Busqueda

# Para verificar si existe un elemento dentro de nuestro set usamos el operador in
print("David" in my_other_set)
# Recordamos que en python D no es igual a d
print("david" in my_other_set)

# Eliminacion

# Eliminamos un elemento especifico de nuestro set
my_other_set.remove("d4vidwp")
print(my_other_set)

# Eliminamos todos los elementos de nuestro set
my_other_set.clear()
print(len(my_other_set))

# Eliminamos la variable
del my_other_set
# print(my_other_set)  # name 'my_other_set' is not defined

# Transformacion

# Definimos los elementos de nuestro set
my_set = {"David", "Campos", 25}
# Creamos la variable list, le pasamos la funcion list y le agregamos la variable
# set para convertir nuestro set en una lista
my_list = list(my_set)
print(type(my_list))
print(my_list[0])

my_other_set = {"HTML", "CSS", "Python"}
print(my_other_set)

# Otras operaciones

my_new_set = my_set.union(my_other_set)
print(my_new_set)

# Aqui intetamos usar la funcion union para intentar duplicar los elementos y no se pudo
# Pero pudimos agregar un union y dentro de el agregar nuevos elementos
print(my_new_set.union(my_set).union(my_new_set).union({"d4vidwp", "Coca-cola"}))
# Aqui buscamos las diferencias de my_set con my_other_set
print(my_other_set.difference(my_set))
