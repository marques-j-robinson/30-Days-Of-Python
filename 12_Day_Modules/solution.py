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