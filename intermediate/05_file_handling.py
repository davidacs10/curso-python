### File handling ###

import os

f = open ("../intermediate/ejemplo_1.txt")
print(f)

# Lee el archivo txt
"""txt = f.read()
print(txt)
f.close()"""

# Lee las 10 primeras lineas "depende del valor que le pasemos a read()"
"""Si el archivo se ha cerrado anteriormente no se podra ejecutar el codigo
txt_ten = f.read(10)
print(txt_ten)
f.close()"""

# Lee la primera linea del archivo
"""line = f.readline()
print(type(line))
print(line)
f.close()"""

# Lee todo el texto linea por linea y devuelve una lista de lineas
"""line = f.readlines()
print(type(line))
print(line)
f.close()"""

# Otra forma de obtener todas las lineas como una lista es usando splitlines()
"""line = f.read().splitlines()
print(type(line))
print(line)
f.close()"""

"""Después de abrir un archivo, debemos cerrarlo. 
Hay una alta tendencia a olvidarse de cerrarlos. 
Hay una nueva forma de abrir archivos usando with: cierra los archivos por sí mismo. 
Reescribamos el ejemplo anterior con el método with:"""

with open("../intermediate/ejemplo_1.txt") as f:
    line = f.read().splitlines()
    print(type(line))
    print(line)

# Abrir archivos para escribir y actualizar
    
"""
Para escribir en un fichero existente, debemos añadir un modo como parámetro a la función open():

    "a" - append - se agregará al final del archivo, si el archivo no existe, crea un nuevo archivo.
    "w" - write - sobrescribirá cualquier contenido existente, si el archivo no existe, lo crea.
"""
# Agregara el texto al final
# with open("../intermediate/ejemplo_1.txt", "a") as f:
#     f.write(" Aprendiendo Python")

# Creara un archivo nuevo en caso de que no exista.
with open ("../intermediate/writin_file.txt", "w") as f:
    f.write("Este texto esta escrito en un archivo nuevo")

# Eliminación de archivos
# import os

# os.remove("../intermediate/writtin_file.txt")

"""Si el archivo no existe, el método remove generará un error, 
por lo que es bueno usar una condición como esta:"""
if os.path.exists('./files/example.txt'):
    os.remove('./files/example.txt')
else:
    print('The file does not exist')

# Tipos de archivos

"""
Archivo con extensión txt
El archivo con extensión txt es una forma muy común de datos y 
la hemos cubierto en la sección anterior. Pasemos al archivo JSON

Archivo con extensión json
JSON son las siglas de JavaScript Object Notation. En realidad, 
es un objeto JavaScript stringificado o un diccionario de Python.
"""

person_dct = {
    "name":"David",
    "last_name":"Campos",
    "age":24,
    "country":"Venezuela",
    "city":"Caracas",
    "skills":["HTML", "CSS", "Python"]
}

person_json = '{"name": "David", "last_name": "Campos", "age": 24, "country":"Venezuela", "skills":["HTML", "CSS", "Python"]}'

person_json = '''{
    "name":"David",
    "last_name":"Campos",
    "age":24,
    "country":"Venezuela",
    "city":"Caracas",
    "skills":["HTML", "CSS", "Python"]
}'''

# Cambiar JSON a diccionario

import json

person_dct = json.loads(person_json)
print(type(person_dct))
print(person_dct)
print(person_dct["name"])

# Cambiar el diccionario a JSON

person_json = json.dumps(person_dct, indent=4)
print(type(person_json))
print(person_json)

# Guardar nuestros archivos como JSON
with open("../intermediate/json_example.json", "w", encoding="utf-8") as f:
    json.dump(person_dct, f, ensure_ascii=False, indent=4)

# Archivo con extensión csv
"""
CSV significa valores separados por comas.
Por ejemplo:
"name","country","city","skills"
"David","Venezuela","Caracas","Python"
"""
import csv
with open("../intermediate/csv_example.csv") as f:
    csv_reader = csv.reader(f, delimiter=",")
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f"Column names are: {', '.join(row)}")
            line_count += 1
        else:
            print(f"\t{row[0]} is a student {row[3]}. He lives in {row[1]}, {row[2]}.")
            line_count += 1
    print(f"Numbers of lines {line_count}")

