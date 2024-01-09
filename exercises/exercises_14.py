# Importacion de un modulo

import mymodule

print(mymodule.generate_full_name("David", "Campos"))

# Importacion de funciones desde un modulo

from mymodule import generate_full_name, sum_all_nums, gravity, person

print(generate_full_name("David", "Campos"))
print(sum_all_nums(1, 2, 3, 4, 5, 6, 7))
print(gravity)
print(person["first_name"])

# Importar funciones desde un módulo y cambiar el nombre
from mymodule import (
    generate_full_name as full_name,
    sum_all_nums as total,
    gravity as g,
    person as p,
)

print(full_name("David", "Campos"))
print(total(1, 2, 3, 4, 5, 6, 7))
mass = 100
weight = mass * g
print(weight)
print(p)
print(p["first_name"])

from mymodule import (
    random_user_id,
    user_id_gen_by_user,
    rgb_color_gen,
    list_of_hexa_colors,
    list_of_rgb_colors,
    generate_colors,
    shuffle_list,
    seven_random_numbers,
)

# Write a function which generates a six digit/character random_user_id.

print(random_user_id())

# Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.
# print(user_id_gen_by_user())

# Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
print(rgb_color_gen())

# Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).
print(list_of_hexa_colors(2))

# Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
print(list_of_rgb_colors(4))

# Write a function generate_colors which can generate any number of hexa or rgb colors.
print(generate_colors("HEXA", 4))
print(generate_colors("RGB", 4))

# Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
numbers = [1, 2, 3, 4, 5]
print(shuffle_list(numbers))

# Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.
print(seven_random_numbers())
