### Regular Expressions ###

"""Una expresion regular es una cadena de texto especial
que nos ayuda a buscar un patron en alguna data. regex tambien
pueden ser usado para encontrar coincidencias en la data

Lo primero que tenemos que hacer es importar el modulo re"""

import re

# Metodos en el modulo re

# match
txt = "I love to learn programming languages"
match = re.match("I love to learn", txt, re.I)
print(match)

# Podemos obtener el inicio y el final del match como una tupla usando span
span = match.span()
print(span)

# Busquemos la posicion de inicio y parada del span
start, end = span
print(start, end)
sub_string = txt[start:end]
print(sub_string)

# search
txt = """Python es el mejor lenguaje de programacion que un ser humano haya creado.
Recomiendo aprender python como primer lenguaje"""
search = re.search("primer", txt, re.I)
print(search)

# Podemos obtener el inicio y el final del search como una tupla usando span
span = search.span()
print(span)

# Busquemos la posicion de inicio y parada del span
start, end = span
print(start, end)
sub_string = txt[start:end]
print(sub_string)

# findall retorna todas las coincidencias como una lista
findall = re.findall("lenguaje", txt, re.I)
print(findall)
findall = re.findall("python", txt, re.I)
print(findall)

"""Desde que estamos usando re.I estamos incluyendo mayusculas y minusculas.
En caso de no usar la bandera debemos aplicar otros metodos"""
#Primer metodo
findall = re.findall("[P|p]ython", txt)
print(findall)

#Segundo metodo
findall = re.findall("[Pp]ython", txt)
print(findall)

# Reemplazando un sub_string
txt = """Python es el mejor lenguaje de programacion que un ser humano haya creado.
Recomiendo aprender python como primer lenguaje"""

replace = re.sub("[P|p]ython", "JavaScript", txt)
print(replace)

# Podemos aplicarlo en el siguiente ejemplo
txt = """%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing. 
T%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.
I fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs. 
D%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher?"""

replace = re.sub("%", "", txt)
print(replace)

# Division del texto mediante la division de expresiones regulares
txt = """I am teacher and  I love teaching.
There is nothing as rewarding as educating and empowering people.
I found teaching more interesting than any other jobs.
Does this motivate you to be a teacher?"""
splitting = re.split("\n", txt)
print(splitting)

# Escritura de patrones RegEx
pattern = r"apple"
txt = """Apple and banana are fruits. An old cliche says an apple a day a doctor way has 
been replaced by a banana a day keeps the doctor far far away."""
matches = re.findall(pattern, txt)
print(f"Escritura de patrones RegEx {matches}")

# Tomando en cuenta que no distingue entre mayusculas y minusculas
matches = re.findall(pattern, txt, re.I)
print(f"Flag I {matches}")

# O podemos usar el metodo de conjunto de caracteres
pattern = r"[Aa]pple"
matches = re.findall(pattern, txt)
print(f"Conjunto de caracteres {matches}")

# Corchetes
txt = """Apple and banana are fruits. An old cliche says an apple a day a doctor way has
 been replaced by a banana a day keeps the doctor far far away."""
pattern = r"[Aa]pple"
matches = re.findall(pattern, txt)
print(matches)

# Si quieres agregar otro patron de busqueda como banana hacemos lo siguiente
pattern = r"[Aa]pple|[Bb]anana"
matches = re.findall(pattern, txt)
print(matches)

# Caracter de escape(\) RegEx
pattern = r"\d"
txt = "This regular expression example was made on December 6,  2019 and revised on July 8, 2021"
matches = re.findall(pattern, txt)
print(matches)

# Una o más veces(+)
pattern = r"\d+"
txt = "This regular expression example was made on December 6,  2019 and revised on July 8, 2021"
matches = re.findall(pattern, txt)
print(matches)

# Punto(.)
pattern = r"[a]." # Esto quiere decir la letra a y el punto cualquier caracter que venga despues excepto un salto de linea
txt = """Apple and banana are fruits"""
matches = re.findall(pattern, txt)
print(matches)

pattern = r"[a].+" # . cualquier caracter y + cualquier caracter una o mas veces
txt = """Apple and banana are fruits"""
matches = re.findall(pattern, txt)
print(matches)

# Cero o muchas veces(*)
# Es posible que el patron se repita cero o muchas veces
pattern = r"[a].*" 
txt = """Apple and banana are fruits"""
matches = re.findall(pattern, txt)
print(matches)

# Cero o una vez(?)
# Es posible que el patrón no ocurra o que ocurra una vez.
pattern = r"[Ee]-?mail" 
txt = """I am not sure if there is a convention how to write the word e-mail.
Some people write it as email others may write it as Email or E-mail."""
matches = re.findall(pattern, txt)
print(matches)

# Cuantificador en RegEx
# Podemos especificar la longitud de la subcadena que buscamos en un texto, utilizando un corchete.
txt = "This regular expression example was made on December 6,  2019 and revised on July 8, 2021"
pattern = r"\d{4}" # Exactamente 4 digitos
matches = re.findall(pattern, txt)
print(matches)

txt = "This regular expression example was made on December 6,  2019 and revised on July 8, 2021"
pattern = r"\d{1,4}" # 1 a 4 digitos
matches = re.findall(pattern, txt)
print(matches)

# Empieza con ^
txt = "This regular expression example was made on December 6,  2019 and revised on July 8, 2021"
regex_pattern = r"^This"  # ^ quiere decir empieza con This
matches = re.findall(regex_pattern, txt)
print(matches)

# Negacion
txt = "This regular expression example was made on December 6,  2019 and revised on July 8, 2021"
regex_pattern = r"[^a-zA-Z ]+"  # Dentro de los corchetes significa negacion, no incluye letras ni espacios 
matches = re.findall(regex_pattern, txt)
print(matches)
