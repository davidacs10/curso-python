### Condicionales ###


# if

my_condition = False

# Es lo mismo que if my_condition == True
if my_condition:
    # En este caso como declaramos que es falso no se va a ejecutar.
    print("Se ejecuta la condicion del if")

my_condition = 4 * 6

if my_condition == 10:
    print("Se ejecuta la condicion del segundo if")

# if, elif, else

if my_condition > 10 and my_condition < 20:
    print("Es mayor a 10 y menor que 20")

elif my_condition == 25:
    print("Es igual a 25")

else:
    print("Es menor o igual que 10 o mayor o igual que 20 o distinto de 25")

print("La ejecucion continua")

# Condicional con inspeccion de valor

my_string = ""

if not my_string:
    print("Mi cadena de texto es vacia")

if my_string == "Hola python":
    print("Los string coinciden")
else:
    print("No hay texto")
