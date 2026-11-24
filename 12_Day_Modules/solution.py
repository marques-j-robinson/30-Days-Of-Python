import string
import random

id_values = list(string.ascii_letters + string.digits)

def random_user_id():
    user_id = ''
    for i in range(6):
        user_id += random.choice(id_values)
    return user_id