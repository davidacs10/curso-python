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
