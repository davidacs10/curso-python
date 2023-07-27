### Listas ###

# En python se pueden crear listas de dos maneras.
# 1-Usando la funcion integrada:

# Esto es una lista vacia, es decir, no tiene elementos.
my_first_list = list()
# Imprime una lista vacia
print(my_first_list)
# Imprime la longitud de la lista, es decir, 0
print(len(my_first_list))

# 2-Usando corchetes []:

my_second_list = []
print(my_second_list)
print(len(my_second_list))

my_first_list = [3, 4, 25, 6, 4, 10]
# Imprime los elementos que estan dentro de la lista.
print(my_first_list)
# La funcion len imprime la cantidad de elementos que hay dentro de la lista en este caso 6.
print(len(my_first_list))

my_second_list = [25, 1.75, "David", "Campos"]
print(my_second_list)
# La funcion len imprime la cantidad de elementos que hay dentro de la lista en este caso 4.
print(len(my_second_list))

# Acceso a lementos y busqueda.

# Podemos acceder a cada elemento de la lista usando su index. Empezando desde el numero 0-1-2-3-4-5...
# Imprime el elemento 25 de la lista.
print(my_first_list[2])

# Podemos asignarle una variable a este elemento
# Imprime el primer elemento. 3
numbers = my_first_list
first_item = numbers[0]
print(first_item)

# Imprime el segundo elemento. 4
numbers = my_first_list
second_item = numbers[1]
print(second_item)

# Imprime el tercero elemento. 25
numbers = my_first_list
third_item = numbers[2]
print(third_item)

# Imprime el cuarto elemento. 6
numbers = my_first_list
fourth_item = numbers[3]
print(fourth_item)

# Imprime el quinto elemento. 4
numbers = my_first_list
fifth_item = numbers[4]
print(fifth_item)

# Imprime el sexto elemento. 10
numbers = my_first_list
sixth_item = numbers[5]
print(sixth_item)

# Los negativos representan que van en reversa, es decir, antes de el 0 vendria el ultimo elemento de la lista
numbers = my_first_list
sixth_item = numbers[-1]
print(sixth_item)

numbers = my_first_list
fifth_item = numbers[-2]
print(fifth_item)

# Para contar los elementos que se repiten
print(my_first_list.count(4))

# Hace referencia al index donde se encuentra el elemento
print(my_second_list.index("Campos"))

# Aqui podemos asignarle una variable que identifique a cada elemento de la lista
# Sin tomar en cuenta el orden. Las variables se colocan por sentido comun.
age, height, name, surname = my_second_list
print(height)

# En este caso desordenamos la lista y daba en name el numero 25.
# Luego de eso lo que hicimos fue acomodar el index de manera manual para asignar sus valores correspondientes
name, surname, age, height = (
    my_second_list[2],
    my_second_list[3],
    my_second_list[0],
    my_second_list[1],
)
print(name)

# Concatenacion

print(my_first_list + my_second_list)

# Creación, inserción, actualización y eliminación

# Agrega un nuevo elemento al final de la lista.
my_second_list.append("d4vidwp")
print(my_second_list)

# Inserta un nuevo elemento en la posicion del index indicada.
my_second_list.insert(2, "Vinotinto")
print(my_second_list)

# Reemplaza un elemento de la lista de acuerdo a su index indicado.
my_second_list[2] = "Morado"
print(my_second_list)

# Elimina un elemento de la lista
my_second_list.remove("Morado")
print(my_second_list)

# Para eliminar el index indicado. Eliminara ultimo si no es espicificado.
my_second_list.pop()
print(my_second_list)

# Aqui le dimos una variable a pop para poder imprimir cual fue el elemento eliminado.
my_pop_element = my_second_list.pop(3)
print(my_pop_element)
print(my_second_list)

# Tambien podemos eliminar el index con del
del my_second_list[2]
print(my_second_list)

# Operaciones con listas

# Copia toda una lista
my_new_list = my_first_list.copy()

# Limpia toda una lista
my_new_list.clear()
print(my_first_list)
print(my_new_list)

# Reversa de una lista
my_second_list.reverse()
print(my_second_list)

# Para ordenar los elementos de una lista de manera ascendente.
my_first_list.sort()
print(my_first_list)

# Para ordenar de manera descendente
my_first_list.sort(reverse=True)
print(my_first_list)

# Sublistas

print(my_first_list[0:3])

# Cambio de tipo

my_first_list = "Hola python :)"
print(my_first_list)
print(type(my_first_list))
