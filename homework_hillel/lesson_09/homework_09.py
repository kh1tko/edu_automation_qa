# 1) додайте requirements.txt на ваш гіт ---> Done!


# 2) Виберіть будь-яку помилку яка вам подобається і
# зробіть функцію яка перевіряє на цю помилку(в функції try except)
def convert_to_int(value: str):
    try:
        result = int(value)
        return result
    except ValueError as e:
        return f'Помилка: {e}! -->(Данне значення неможливо перетворити на число)<--'


# Приклад використання
print(convert_to_int("hello, world!"))  # Помилка
print(convert_to_int("42"))  # 42


# 3) зробіть функцію як ми робили з додаванням тільки замість двох чисел зробіть три числа
# і протестуйте її всіма трьома методами

def add_three_numbers(number_1: int | float, number_2: int | float, number_3: int | float) -> int | float:
    result = (number_1 + number_2) * number_3
    return result


# 4) перепишіть декоратор який заміряє час з уроку в домашку, можете його поклацати, як він працює

from datetime import datetime
import time


def func_wrapper_time(func):
    def wrapper(*arg, **kwarg):
        start = datetime.now()
        result = func(*arg, **kwarg)
        delta_time = datetime.now() - start
        print("Час виконання функції ось такий: ", delta_time)
        return result

    return wrapper


@func_wrapper_time
def foo_1(*arg, **kwarg):
    print('foo_1')
    time.sleep(1)


foo_1()
