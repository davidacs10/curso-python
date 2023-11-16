### Exception Handling ###

number_one = 5
number_two = 1
number_three = "2"

# Excepcion base: try except

try:
    print(number_one + number_two)
    print("No se ha producido un error en la excepcion base.")

except:
    # Se ejecuta si se produce una excepcion
    print("Se ha producido un error en la excepcion base.")

# Flujo completo de una excepcion: try except else finally

try:
    print(number_one + number_three)
    print("No se ha producido un error en el flujo completo de una excepcion.")
except:
    print("Se ha producido un error en el flujo completo de una excepcion.")
else:  # Opcional
    # Solo se ejecuta si no se produce una excepcion
    print("La ejecucion puede continuar en el flujo completo de una excepcion.")
finally:  # Opcional
    # Se ejecuta siempre.
    print("La ejecucion continua en el flujo completo de una excepcion.")

# Excepciones por tipo

try:
    print(number_one + number_three)
    print("No se ha producido un error.")
except ValueError:
    print("Se ha producido un ValueError.")
except TypeError:
    print("Se ha producido un TypeError.")

# Captura de la informacion de la excepcion.

try:
    print(number_one + number_three)
    print("No se ha producido un error.")
except ValueError as error:
    print(error)
except Exception as my_random_error_name:
    print(my_random_error_name)

# try:
#     name = input("Your name: ")
#     year_born = input("Year you were born: ")
#     age = 2023 - year_born
#     print(f"{name} is {age} years old")
# except TypeError:
#     print("Type error occured")
# # Hasta aqui ha ocurrido un error pero no sabemos cual es. Para analizar el problema podemos usar los diferentes tipos de error
# except ValueError:
#     print("Value error occured")
# except ZeroDivisionError:
#     print("Zero Division error occured")
# else:
#     print("I usually run with the try block")
# finally:
#     print("I always run")

# Tambien se puede acortar el codigo de la siguiente manera
# try:
#     name = input("Your name: ")
#     year_born = input("Year you were born: ")
#     age = 2023 - year_born
#     print(f"{name} is {age} years old")
# except Exception as e:
#     print(e)

# Desembalaje


def sum_all_numbers(a, b, c, d, e):
    return a + b + c + d + e


list = [1, 2, 3, 4, 5]
print(sum_all_numbers(*list))
