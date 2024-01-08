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
)

print(random_user_id())
# print(user_id_gen_by_user())
print(rgb_color_gen())
print(list_of_hexa_colors(2))
print(list_of_rgb_colors(4))
print(generate_colors("HEXA", 4))
print(generate_colors("RGB", 4))
numbers = [1, 2, 3, 4, 5]
print(shuffle_list(numbers))
