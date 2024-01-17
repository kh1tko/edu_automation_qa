"""
Зробіть словник де буде табличка множення додавання ділення і віднімання чисел від 2 до 9(включно).
(так як робили на уроці). Ці значення запишіть в словник з відповідними ключами "+", "-", "/", "*"

Коли ви підготуєте це, запитайте в користувача яку табличку він хоче побачити
(додавання, віднімання, множення, ділення). і виведіть йому цю табличку.
"""

operation_tables = {
    '+': {},
    '-': {},
    '*': {},
    '/': {}
}

for i in range(2, 10):
    for j in range(2, 10):
        operation_tables['+'][f"{i}+{j}"] = i + j
        operation_tables['-'][f"{i}-{j}"] = i - j
        operation_tables['*'][f"{i}*{j}"] = i * j
        operation_tables['/'][f"{i}/{j}"] = i / j

# Після цього ви можете запитати користувача, яку табличку він хоче побачити,
# і вивести відповідний словник.

selected_operation = input("Оберіть операцію (+, -, *, /): ")

if selected_operation == "+":
    counter = 0
    for key, value in operation_tables[selected_operation].items():
        print(f"{key} = {value}", end=" ")
        counter += 1
        if counter % 8 == 0:
            print("\n")
elif selected_operation == "-":
    counter = 0
    for key, value in operation_tables[selected_operation].items():
        print(f"{key} = {value}", end=" ")
        counter += 1
        if counter % 8 == 0:
            print("\n")
elif selected_operation == "*":
    counter = 0
    for key, value in operation_tables[selected_operation].items():
        print(f"{key} = {value}", end=" ")
        counter += 1
        if counter % 8 == 0:
            print("\n")
elif selected_operation == "/":
    counter = 0
    for key, value in operation_tables[selected_operation].items():
        print(f"{key} = {round(value, 2)}", end=" ")
        counter += 1
        if counter % 8 == 0:
            print("\n")
else:
    print("Невірна операція. Будь ласка, оберіть одну з доступних операцій: +, -, *, /")








