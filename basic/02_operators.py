### Operadores Aritmeticos ###

# Operaciones con enteros
print(3 + 4)
print(4 - 3)
print(4 * 3)
print(4 / 3)
print(3 % 3)
print(4 // 4)
print(2**4)
print(2**3 + 3 - 7 / 1 // 4)

# Operaciones con cadena de texto
print("Hola " + "David " + "Como estas?")
print(
    "Hola " + str(5)
)  # No podemos sumar datos diferentes pero aqui estamos forzando el dato int 5 a str

# Operaciones mixtas
print("Hola " * 5)
print("Hola " * (2**3))

my_float = 2.5 * 2
print("Hola " * int(my_float))

### Operadores Comparativos ###

# Operaciones con enteros

print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(3 <= 4)
print(3 != 4)
print(3 == 4)

# Operaciones con cadenas de texto

print("Hola" > "Python")
print("Hola" < "Python")
print("Hola" >= "Python")
print("Hola" <= "Python")
print("Hola" == "Python")
print("Hola" != "Python")
print("aaaa" >= "abaa")  # Ordenacion alfabetica ASCII
print(len("Hola") > len("Jugo"))  # Cuenta caracteres
print(len("Hola") >= len("Jugo"))

# Operadores logicos

print(3 > 4 and "Hola" > "Python")
print(3 > 4 or "Hola" > "Python")
print(3 < 4 and "Hola" < "Python")
print(3 < 4 or "Hola" > "Python")
print(3 < 4 or ("Hola" > "Python" and 4 == 4))
print(not (3 > 4))
