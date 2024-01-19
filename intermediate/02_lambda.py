### Lambda ###

x = lambda var1, var2, var3: var1 + var2 + var3
print(x(1, 2, 3))

# Ejemplo de la funcion
def sum_two_nums(a, b):
    return a + b

print(sum_two_nums(1, 2))

# Ejemplo de la funcion lambda
sum_two_numbs = lambda a, b: a + b
print(sum_two_nums(3, 1))

# Encapsulamiento de una lambda
print((lambda a, b: a + b)(1, 5))

# Al cuadrado
square = lambda x: x ** 2
print(square(5))

# Al cubo
cube = lambda x: x ** 3
print(cube(3))

# Función lambda dentro de otra función

def power(x):
    return lambda n: x ** n

cube = power(2)(3) # La funcion power ahora necesita 2 argumentos x que es el numero y el lambda n que es el exponente
print(cube)
two_power_of_five = power(2)(5)
print(two_power_of_five)