### Type hints ###

"""
los type hints son una característica de Python que permite especificar el 
tipo de datos en el código, y FastAPI aprovecha esta característica para mejorar 
la documentación y la validación estática de las APIs web construidas con él.

Usando las declaraciones de tipos para tus variables, los editores y 
otras herramientas pueden proveerte un soporte mejor.
"""

def full_name(first_name, last_name):
    return first_name.title() + " " + last_name.title()

print(full_name("john", "doe")) # OUTPUT: John Doe

def full_name(first_name: str, last_name: str):
    return first_name.title() + " " + last_name.title()

print(full_name("john", "doe"))

"""Lo que hicimos fue tipar estas variables. Aunque no modifica nada si no lo hacemos
pero esto nos proporciona un mejor soporte desde el editor de codigo a la hora de querer
agregarle una funcion especifica a esta variable a la hora de colocoar un punto (.) Ahora
en el ejemplo anterior colocamos el (.) y no tuvimos que adivinar cual era la funcion de los
textos para poner la primera letra en mayuscula"""

"""def get_name_with_age(name: str, age: int):
    name_with_age = name + " is this old " + age
    return name_with_age

print(get_name_with_age("David", 26))"""

"""Tenemos un TypeError que no nos permite concatenar cadenas de texto junto con enteros.
Ahora que sabemos esto podemos arreglarlo agregando un str a la variable age"""

def get_name_with_age(name: str, age: int):
    name_with_age = name + " is this old " + str(age)
    return name_with_age

print(get_name_with_age("David", 26))

# Declarando tipos
from typing import List, Tuple, Set, Dict

def process_items(items: List[str]):
    for item in items:
        print(item.title())

"""Esto significa: la variable items es una list y cada uno de los ítems 
en esta lista es un str. Con esta declaración tu editor puede proveerte 
soporte inclusive mientras está procesando ítems de la lista."""

def process_items(items_t: Tuple[int, int, str], items_s: Set[bytes]):
    return items_t, items_s

"""
La variable items_t es un tuple con 3 ítems, un int, otro int, y un str.
La variable items_s es un set y cada uno de sus ítems es de tipo bytes.
"""

def process_items(prices: Dict[str, float]):
    for item_name, item_price in prices.items():
        print(item_name) 
        print(item_price)

"""
La variable prices es un dict:
Los keys de este dict son de tipo str (Digamos que son el nombre de cada ítem).
Los valores de este dict son de tipo float (Digamos que son el precio de cada ítem).
"""

# Clases como tipos

from typing import Optional

def say_hi(name: Optional[str] = None):
    if name is not None:
        print(f"Hey {name}")
    else:
        print("Hello world")

say_hi("David")
say_hi()

class Person():
    def __init__(self, name: str):
        self.name = name


def get_person_name(one_person: Person):
    return one_person.name

person = Person("David")
print(get_person_name(person))

"""
este código muestra cómo usar type hints para especificar los tipos 
de argumentos y valores de retorno de funciones, así como los atributos 
de clases, lo que puede ayudar a mejorar la claridad y la documentación 
del código, así como a detectar errores en tiempo de desarrollo.
"""