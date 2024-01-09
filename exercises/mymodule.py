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
        color = f"#{random.randint(0, 0xFFFFFF):06X}"
        colors.append(color)
    return colors


def list_of_rgb_colors(num_colors):
    colors = []
    for _ in range(num_colors):
        color = rgb_color_gen()
        colors.append(color)
    return colors


def generate_colors(type_color, num_colors):
    if type_color.lower() == "hexa":
        return list_of_hexa_colors(num_colors)
    elif type_color.lower() == "rgb":
        return list_of_rgb_colors(num_colors)
    else:
        return f"Please insert a valid type of color."


def shuffle_list(input_list):
    shuffle_list = input_list.copy()
    random.shuffle(shuffle_list)
    return shuffle_list

def seven_random_numbers():
    random_numbers = set()
    
    while len(random_numbers) < 7:
        number = random.randint(0,9)
        random_numbers.add(number)
    
    array = list(random_numbers)
    return array