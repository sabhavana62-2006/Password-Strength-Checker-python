import random
import string

def generate_password():

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    all_characters = lowercase + uppercase + digits + symbols

    password = "".join(random.choice(all_characters) for i in range(12))

    return password