from random import randint, shuffle
LETTERS_ARRAY = ['a', 'b', 'c', 'd', 'e' , 'f', 'g', 'h', 'i','j', 'k', 'l', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
NUMBERS_ARRAY = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
ESPECIAL_ARRAY = ['!', '@', '#', '$', '%', '*', '(', ')', '_', '+', '=', '|', ';', '~', '^', ']', '[', '.']

def generate_random_password(data):
    should_have_letters = data["letters"]
    should_have_numbers = data["numbers"]
    should_have_especial = data["especial"]
    shold_have_capslock = data["capslock"]
    password_length = data["length"]
    generated_password = []

    for r in range(password_length + 1):
        randint_letters = randint(0, len(LETTERS_ARRAY) - 1)
        randint_numbers = randint(0, len(NUMBERS_ARRAY) - 1)
        randint_especial = randint(0, len(ESPECIAL_ARRAY) - 1)

        if len(generated_password) == password_length:
            break
        if should_have_letters and len(generated_password) < password_length :
            if shold_have_capslock:
                generated_password.append(LETTERS_ARRAY[randint_letters].upper())
            generated_password.append(LETTERS_ARRAY[randint_letters])
        if should_have_numbers and len(generated_password) < password_length:
            generated_password.append(NUMBERS_ARRAY[randint_numbers])
        if should_have_especial and len(generated_password) < password_length:
            generated_password.append(ESPECIAL_ARRAY[randint_especial])
    
    for shuff in range(5):
        shuffle(generated_password)

    generated_password = ''.join(map(str, generated_password))

    return generated_password
