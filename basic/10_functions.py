### Functions ###


def my_function():
    print("Esto es una funcion")


my_function()

# Función con parámetros de entrada/argumentos


def sum_two_values(first_value, second_value):
    print(first_value + second_value)


sum_two_values(5, 7)
sum_two_values(1234, 4321)
sum_two_values("Hola", "Mundo")
sum_two_values(1.2, 1.2)

# Función con parámetros de entrada/argumentos y retorno


def sum_two_values_with_return(first_value, second_value):
    my_sum = first_value + second_value
    return my_sum


# Retorna un none
my_result = sum_two_values(1.4, 5.2)
print(my_result)

my_result = sum_two_values_with_return(40, 10)
print(my_result)

# Función con parámetros de entrada/argumentos por clave


def print_name(name, surname):
    print(f"{name} {surname}")


print_name(surname="Campos", name="David")

# Función con parámetros de entrada/argumentos por defecto


def print_name_with_default(name, surname, alias="Sin alias"):
    print(f"{name} {surname} {alias}")


print_name_with_default("David", "Campos")
print_name_with_default("David", "Campos", "d4vidwp")

# Función con parámetros de entrada/argumentos arbitrarios


def print_upper_texts(*texts):
    # Lo interpreta como una tupla
    print(type(texts))
    for text in texts:
        print(text.upper())


print_upper_texts("Hola", "David", "Python")
print_upper_texts("Hola")
