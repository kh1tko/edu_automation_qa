import random
import string


def generate_password(length: int, alphabets: str) -> list:
    password = ''
    choices = ''

    for alphabet in alphabets:
        if alphabet.lower() == 'latin':
            choices += string.ascii_letters
        elif alphabet.lower() == 'cyrillic':
            choices += 'абвгдеєжзиіїйклмнопрстуфхцчшщьюяАБВГДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ'
        elif alphabet.lower() == 'numbers':
            choices += string.digits

    if 'lower' in alphabets:
        choices = choices.lower()
    elif 'upper' in alphabets:
        choices = choices.upper()

    for _ in range(length):
        password += random.choice(choices)
    return password


if __name__ == '__main__':
    alphabets = input(
        "Choose alphabets and case selection for the password (latin, cyrillic, numbers, (lower or upper)), separated by commas: ").split(
        ', ')
    length = int(input("Enter password length: "))

    password = generate_password(length, alphabets)
    print("Generated password: ", password)
