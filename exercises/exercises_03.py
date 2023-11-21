# Operadores
# 1 Declara tu edad como variable entera
age = 23
age = int(age)
# 2 Declarar la altura como una variable flotante
height = 1.79
height = float(height)
# 3 Declarar una variable que almacene un número complejo
complex_number = 4j
complex_number = complex(4j)
# 4 Escriba un script que solicite al usuario que introduzca la base y la altura del triángulo y calcule un área de este triángulo (área = 0,5 x b x h).
base = int(input("Base: "))
height = int(input("Height: "))
area = 0.5 * base * height
area = int(area)
print(f"The area of the circle is: {area}")
# 5 Escriba un script que pida al usuario que escriba el lado a, el lado b y el lado c del triángulo. Calcula el perímetro del triángulo (perímetro = a + b + c).
side_a = int(input("Enter side a:"))
side_b = int(input("Enter side b:"))
side_c = int(input("Enter side c:"))
perimeter = side_a + side_b + side_c
print(perimeter)
# 6 Obtenga la longitud y el ancho de un rectángulo usando el mensaje. Calcula su área (área = largo x ancho) y perímetro (perímetro = 2 x (largo + ancho))
height = int(input("Enter height:"))
width = int(input("Enter width:"))
rectangle_area = height * width
print(rectangle_area)
rectangle_perimeter = 2 * (height + width)
print(rectangle_perimeter)
# 7 Obtener el radio de un círculo usando el mensaje. Calcule el área (área = pi x r x r) y la circunferencia (c = 2 x pi x r) donde pi = 3.14.
pi = 3.14
r = int(input("Enter radius:"))
circle_area = pi * r**2
circunference = 2 * pi * r
print(circle_area)
print(circunference)
# 8 Encuentra la longitud de 'python' y 'dragon' y haz una afirmación de comparación falsa.
word_1 = "python"
word_2 = "dragon"
print(len(word_1))
print(len(word_2))
print(len(word_1) is not len(word_2))
# 9 Use y para comprobar si 'on' se encuentra tanto en 'python' como en 'dragon'
comparation = "on" in word_1 and "on" in word_2
print(comparation)
# 10 Espero que este curso no esté lleno de jerga. Use el operador in para verificar si hay jerga en la oración.
phrase_1 = "I hope this course is not full of jargon"
print("jargon" in phrase_1)
# 11 No hay 'on' tanto en 'python' y 'dragon'
print("on" not in word_1 and "on" not in word_2)
# 12 Encuentre la longitud del texto python y convierta el valor a float y conviértalo en cadena
word_1 = len(word_1)
word_1 = float(word_1)
word_1 = str(word_1)
print(word_1)
# 13 Los números pares son divisibles por 2 y el resto es cero. ¿Cómo se comprueba si un número es par o no usando python?
number = 4
even = number % 2 == 0
odd = number % 2 == 1
print(even)
print(odd)
# 14 Compruebe si la división del piso de 7 por 3 es igual al valor int convertido de 2.7.
floor_division = 7 // 3
value = int(2.7)
print(floor_division == value)
# 15 Compruebe si el tipo de '10' es igual al tipo de 10
type_value_1 = "10"
type_value_2 = 10
print(type_value_1 == type_value_2)
# 16 Compruebe si int('9.8') es igual a 10
value_1 = int(float("9.8"))
value_2 = 10
print(value_1 == value_2)
# 17 Escriba un script que solicite al usuario que ingrese las horas y la tarifa por hora. ¿Calcular el salario de la persona?
hours = int(input("Enter hours: "))
rate = int(input("Enter hours: "))
earning = hours * rate
print(f"Your weekly earning is: {earning}")
# 18 Escriba un script que pida al usuario que introduzca el número de años. Calcula el número de segundos que una persona puede vivir. Supongamos que una persona puede vivir cien años
years = int(input("Numbers of years: "))
seconds = 31536000
seconds_lived = years * seconds
print(f"You have lived for {seconds_lived} seconds.")
# 19 Escriba un script de Python que muestre la siguiente tabla
first_row = "1 1 1 1 1"
second_row = "2 1 2 4 8"
third_row = "3 1 3 9 27"
fourth_row = "4 1 4 16 64"
fifth_row = "5 1 5 25 125"
print(f"{first_row}\n{second_row}\n{third_row}\n{fourth_row}\n{fifth_row}")
