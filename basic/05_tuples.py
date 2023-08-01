### Tuples ###

# Definicion

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (25, 1.75, "David", "Campos")
my_other_tuple = (10, 7, 10)

print(my_tuple)
print(my_other_tuple)

# Acceso a elementos y busqueda

print(my_tuple[1])
print(my_other_tuple[1])

print(my_other_tuple.count(10))
print(my_other_tuple.count(7))
print(my_tuple.index(25))

# my_tuple[1] = 1.80  # TypeError: 'tuple' object does not support item assignment

# Concatenacion

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

# Tupla mutable con conversión a lista

# Cambiamos nuestra tupla a lista
my_tuple = list(my_tuple)
# Imprimimos de que tipo es nuestra variable
print(type(my_tuple))

# Aqui procedemos a modificar nuestra lista
my_tuple[1] = 1.80
my_tuple.insert(1, "Morado")
# Luego la volvemos a transformar en una tupla
my_tuple = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))

# Eliminación

# del my_tuple[2] #TypeError: 'tuple' object doesn't support item deletion

del my_tuple
# print(my_tuple)  # NameError: name 'my_tuple' is not defined
