from string import *
from random import *

id_values = list(ascii_letters + digits)

def random_user_id(id_length):
    user_id = ''
    for _ in range(id_length):
        user_id += choice(id_values)
    return user_id

def user_id_gen_by_user():
    id_length = int(input("What is the ID length: "))
    qty = int(input("How many IDs: "))
    user_ids = []
    for _ in range(qty):
        user_ids.append(random_user_id(id_length))
    return '\n'.join(user_ids)

def rgb_color_gen():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return f'rgb({r},{g},{b})'

hexa_letters = ascii_letters[:6]
hexa_values = list(hexa_letters+digits)

def list_of_hexa_colors(qty):
    colors = []
    for _ in range(qty):
        c = '#'
        for _ in range(6):
            c += choice(hexa_values)
        colors.append(c)
    return colors

def list_of_rgb_colors(qty):
    colors = []
    for _ in range(qty):
        colors.append(rgb_color_gen())
    return colors

def generate_colors(color_type, qty):
    if color_type == 'hexa':
        return list_of_hexa_colors(qty)
    elif color_type == 'rgb':
        return list_of_rgb_colors(qty)
    else:
        return 'Invalid color type'

print(generate_colors('hexa', 3))
print(generate_colors('hexa', 1))
print(generate_colors('rgb', 3))
print(generate_colors('rgb', 1))