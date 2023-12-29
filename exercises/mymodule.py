def generate_full_name(first_name, last_name):
    return first_name + " " + last_name


def sum_all_nums(*args):
    s = 0
    for i in args:
        s += i
    return s


gravity = 9.8


person = {
    "first_name": "David",
    "last_name": "Campos",
    "age": 25,
    "country": "Venezuela",
}

import random
import string


def random_user_id():
    random_id = "".join(random.choices(string.ascii_letters + string.digits, k=6))
    return random_id


def user_id_gen_by_user():
    number_of_characters = int(input("Insert number of characters: "))
    number_of_id = int(input("Insert number of IDs: "))

    if number_of_characters <= 0 or number_of_id <= 0:
        print("Please insert a number greater than 0")
        return

    for _ in range(number_of_id):
        random_id = "".join(
            random.choices(string.ascii_letters + string.digits, k=number_of_characters)
        )

        print(f"ID Gen: {random_id}")


def rgb_color_gen():
    rgb_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    return f"rgb{rgb_color}"


def list_of_hexa_colors(num_colors):
    colors = []
    for _ in range(num_colors):
        color = f"#{random.randint(0, 0xFFFFFF):06x}"
        colors.append(color)
    return colors
