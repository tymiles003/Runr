import string
import random

def id_generator(size=4, chars=string.ascii_lowercase):
    return ''.join(random.choice(chars) for _ in range(size))
