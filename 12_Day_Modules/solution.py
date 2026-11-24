import string
import random

id_values = list(string.ascii_letters + string.digits)

def random_user_id(id_length):
    user_id = ''
    for _ in range(id_length):
        user_id += random.choice(id_values)
    return user_id

def user_id_gen_by_user():
    id_length = int(input("What is the ID length: "))
    qty = int(input("How many IDs: "))
    user_ids = []
    for _ in range(qty):
        user_ids.append(random_user_id(id_length))
    return '\n'.join(user_ids)