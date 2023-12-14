# Excepciones
# Una excepción es un evento que ocurre durante la ejecución de un programa y que interrumpe el flujo normal de instrucciones. Cuando una excepción se produce, el intérprete de Python busca un bloque de código que pueda manejar esa excepción.

# Excepciones comunes: Estas son errores que ocurren durante la ejecución del programa. Algunos ejemplos incluyen:
### ZeroDivisionError: Ocurre cuando intentamos dividir un número por cero.
### Ejemplo de ZeroDivisionError
### resultado = 10 / 0
### TypeError: Ocurre cuando intentamos realizar una operación no válida para un tipo de dato en particular.
### Ejemplo de TypeError
### resultado = "Hola" + 5
### NameError: Ocurre cuando intentamos utilizar una variable o función que no ha sido definida.
### Ejemplo de NameError
### print(variable_no_definida)


# Manejo de excepciones: Podemos manejar excepciones utilizando bloques try y except. El código que podría causar una excepción va dentro del bloque try, y el código para manejar la excepción va dentro del bloque except.

try:
    # Código que podría causar una excepción
    resultado = 10 / 0
except ZeroDivisionError:
    # Código para manejar la excepción
    print("¡Error! No puedes dividir entre cero.")

# Finally: Podemos usar un bloque finally para especificar código que siempre se ejecutará, ya sea que se haya producido una excepción o no. Por ejemplo, para realizar acciones de limpieza.

try:
    # Código que podría causar una excepción
    resultado = 10 / 0
except ZeroDivisionError:
    # Código para manejar la excepción
    print("¡Error! No puedes dividir entre cero.")
finally:
    # Este bloque siempre se ejecutará
    print("Terminando el programa.")


try:
    print(10 + "5")
except:
    print("Something went wrong")
# En el ejemplo anterior, el segundo operando es una cadena. Podríamos cambiarlo a float o int para agregarlo con el número para que funcione. Pero sin ningún cambio, el segundo bloque, excepto, se ejecutará.
# try:
#     name = input("Enter your name:")
#     year_born = input("Year you were born:")
#     age = 2023 - year_born
#     print(f"Your name is {name} and you are {age} years old")
# except:
#     print("Something went wrong")
# En el ejemplo anterior, el bloque de excepción se ejecutará y no sabemos exactamente el problema. Para analizar el problema, podemos usar los diferentes tipos de error con except.
# En el siguiente ejemplo, manejará el error y también nos dirá el tipo de error generado.
# try:
#     name = input("Enter your name:")
#     year_born = input("Year you were born:")
#     age = 2023 - year_born
#     print(f"Your name is {name} and you are {age} years old")
# except TypeError:
#     print("Type error occured")
# except ValueError:
#     print("Value error occured")
# except ZeroDivisionError:
#     print("Zero Division error occured")

# En el código anterior, la salida será TypeError. Ahora, agreguemos un bloque adicional:
# try:
#     name = input("Enter your name:")
#     year_born = input("Year you born:")
#     age = 2023 - int(year_born)
#     print(f"You are {name}. And your age is {age}.")
# except TypeError:
#     print("Type error occur")
# except ValueError:
#     print("Value error occur")
# except ZeroDivisionError:
#     print("zero division error occur")
# else:
#     print("I usually run with the try block")
# finally:
#     print("I always run.")

# También se acorta el código anterior de la siguiente manera: Agregando nuestra excepcion a una variable.
# try:
#     name = input("Enter your name:")
#     year_born = input("Year you born:")
#     age = 2019 - (year_born)
#     print(f"You are {name}. And your age is {age}.")
# except Exception as e:
#     print(e)


# Desembalaje
def sum_all_nums(a, b, c, d, e):
    return a + b + c + d + e


lst = [1, 2, 3, 4, 5]
print(sum_all_nums(*lst))

# Tambien se puede hacer la opcion de desempaquetado con la funcion range que espera un inicio y un final
numbers = range(2, 7)
print(f"Desempaquetado con la funcion range convertido a lista: {list(numbers)}")
args = [2, 7]
numbers = range(*args)
print(*numbers)


# Una lista o una tupla también se puede desempaquetar de la siguiente manera:
# names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']. Unpack the first five countries and store them in a variable nordic_countries, store Estonia and Russia in es, and ru respectively.

names = ["Finland", "Sweden", "Norway", "Denmark", "Iceland", "Estonia", "Russia"]
*nordic_countries, es, ru = names
print(nordic_countries, es, ru)

numbers = [1, 2, 3, 4, 5, 6, 7]
one, *middle, last = numbers
print(one, middle, last)


# Desempaquetado de diccionarios
def unpacking_person_info(name, country, city, age):
    return f"{name} lives in {country}, {city}. He is {age} year old."


dct = {"name": "David", "country": "Venezuela", "city": "Caracas", "age": 25}
print(unpacking_person_info(**dct))
for index, item in enumerate([20, 30, 40]):
    print(index, item)
