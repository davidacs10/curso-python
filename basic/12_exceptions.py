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
