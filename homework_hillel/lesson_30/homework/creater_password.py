import random
import string


def generate_password(length, alphabets):
    password = ''
    choices = ''

    if 'latin' in alphabets:
        choices += string.ascii_letters
    if 'cyrillic' in alphabets:
        choices += 'абвгдеєжзиіїйклмнопрстуфхцчшщьюяАБВГДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ'
    if 'numbers' in alphabets:
        choices += string.digits

    for _ in range(length):
        password += random.choice(choices)

    return password


if __name__ == '__main__':
    alphabets = input("Choose alphabets for the password (latin, cyrillic, numbers), separated by commas: ").split(', ')
    length = int(input("Enter password length: "))

    password = generate_password(length, alphabets)
    print("Generated password: ", password)
