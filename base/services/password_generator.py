from random import choice, shuffle
from string import ascii_uppercase, ascii_lowercase, digits, punctuation


def generate_password(data):
    should_have_letters = data["letters"]
    should_have_numbers = data["numbers"]
    should_have_especial = data["especial"]
    shold_have_capslock = data["capslock"]
    password_length = data["length"]
    generated_password = []

    while len(generated_password) < password_length:
        if should_have_letters and len(generated_password) < password_length :
            generated_password.append(choice(ascii_lowercase))
            if shold_have_capslock and len(generated_password) < password_length:
                generated_password.append(choice(ascii_uppercase))
        if should_have_numbers and len(generated_password) < password_length:
            generated_password.append(choice(digits))
        if should_have_especial and len(generated_password) < password_length:
            generated_password.append(choice(punctuation))
        
    for _ in range(5):
        shuffle(generated_password)

    generated_password = ''.join(map(str, generated_password))

    return generated_password