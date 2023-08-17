### Classes ###

# Definicion


# Las clases se escriben en camelcase
class MyEmptyPerson:
    # Para poder dejar la clase vacia
    pass


# Puede ejecutar la clase con o sin parentesis, los parentesis
# seran necesarios cuando necesiten algo para poder ejecutarse
print(MyEmptyPerson)
print(MyEmptyPerson())

# Clase con constructor, funciones y propiedades privadas y publicas


class Person:
    def __init__(self, name, surname, alias="Sin alias"):
        # Propiedad publica
        self.full_name = f"{name} {surname} ({alias})"
        # Propiedad privada
        self.__name = name

    def get_name(self):
        return self.__name

    def walk(self):
        print(f"{self.full_name} esta caminando")


my_person = Person("David", "Campos")
print(my_person.full_name)
print(my_person.get_name())
my_person.walk()

my_other_person = Person("David", "Campos", "d4vidwp")
print(my_other_person.full_name)
my_other_person.walk()

my_other_person.full_name = "Jose Campos (Joseito)"
print(my_other_person.full_name)

# Al ser de tipado debil se puede reemplazar la cadena de texto por un entero
my_other_person.full_name = 777
print(my_other_person.full_name)
