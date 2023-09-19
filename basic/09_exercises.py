# 1 Iterate 0 to 10 using for loop, do the same using while loop.
for number in range(11):
    print(number)

count = 0
while count < 11:
    print(count)
    count = count + 1

# 2 Iterate 10 to 0 using for loop, do the same using while loop.
for number in range(10, -1, -1):
    print(number)

count = 10
while count >= 0:
    print(count)
    count = count - 1

# 3 Write a loop that makes seven calls to print(), so we get on the output the following triangle:
for i in range(1, 8):
    print("#" * i)

# 4 Use nested loops to create the following:
# La altura del triángulo.
altura = 8

# Creamos un bucle para iterar sobre las filas del triángulo.
for i in range(altura):
    # Creamos un bucle para iterar sobre los caracteres de cada fila.
    for j in range(altura):
        # Imprimimos un asterisco si el índice de la fila es menor o igual que el índice del carácter.
        if i <= j:
            print("#", end="")
        else:
            print(" ", end="")
    print()
