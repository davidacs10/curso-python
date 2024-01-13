### List Comprehension ### 

# La comprensión de listas en Python es una forma concisa y elegante de crear listas. En lugar de usar bucles tradicionales para construir una lista elemento por elemento, puedes utilizar la comprensión de listas para hacerlo en una sola línea.

# Primer ejemplo
language = "Python"
lst = list(language)
print(type(lst))
print(lst)

lst = [i for i in language]
print(type(lst))
print(lst)

# Segundo ejemplo
# Si deseamos generar una lista de numeros
numbers = [i for i in range(1, 11)]
print(numbers)

# Es posible hacer operaciones matematicas durante la iteracion
numbers = [i * i for i in range(1, 11)]
print(numbers)

# Tambien es posible hacer una lista de tuplas
numbers = [(i, i * i) for i in range(1, 6)]
print(numbers)

# La compresion de listas se puede combinar con la expresion if

# Generando numeros pares
even_numbers = [i for i in range(11) if i % 2 == 0]
print(even_numbers)

# Generando numeros impares
odd_numbers = [i for i in range(11) if i % 2 != 0]
print(odd_numbers)

# Filtrar los numeros positivos de la siguiente lista
positive_even_numbers = [i for i in range (-10, 11) if i % 2 == 0 and i > 0]
print(positive_even_numbers)

# Aplanamiento de una matriz tridimensional
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [number for row in list_of_lists for number in row]
print(flattened_list)