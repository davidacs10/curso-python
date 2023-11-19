# 01

# number = int(input("Numero: "))

# if number % 2 == 0:
#     print("Es par")
# else:
#     print("Es impar")

# 02
# import random

# options = ["piedra", "papel", "tijera"]
# user_wins = 0
# computer_wins = 0
# rounds = 1

# while True:
#     print("*" * 10)
#     print("Piedra, papel o tijera")
#     print("*" * 10)
#     print("ROUND ", rounds)
#     print("*" * 10)

#     user_option = str(input("Elige una opcion: "))
#     user_option = user_option.lower()
#     computer_option = random.choice(options)

#     if not user_option in options:
#         print("Escribe una opcion valida")
#         continue

#     print(f"El usuario ha sacado: {user_option}")
#     print(f"El computador ha sacado: {computer_option}")

#     if user_option == computer_option:
#         print("Empate")
#     elif (
#         (user_option == "piedra" and computer_option == "tijera")
#         or (user_option == "tijera" and computer_option == "papel")
#         or (user_option == "papel" and computer_option == "piedra")
#     ):
#         print("Gana el usuario")
#         user_wins += 1
#     else:
#         print("Gana el computador")
#         computer_wins += 1

#     rounds += 1
#     if user_wins == 2:
#         print("El ganador es el usuario")
#         break
#     if computer_wins == 2:
#         print("El ganador es el computador")
#         break
# 03

# my_dict = {
#     "name": "David",
#     "last_name": "Campos",
#     "age": 25,
#     "stack": ["HTML5", "CSS3", "Python"],
# }
# my_dict["nametwo"] = "Alejandro"
# my_dict["stack"].append("JavaScript")
# my_dict["stack"].append("TypeScript")
# print(my_dict)

# people = [
#     {"name": "David", "last_name": "Campos"},
#     {"name": "Alejandro", "last_name": "Perez"},
#     {"name": "Juan", "last_name": "Sanchez"},
# ]

# for person in people:
#     for n, l in person.items():
#         print(f"{n}:{l}")
