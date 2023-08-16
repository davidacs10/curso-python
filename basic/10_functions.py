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
