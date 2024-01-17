"""
Задача 2
Візьміть задачу з минулого уроку(
3 зробіть функцію як ми робили з додаванням тільки замість двох
чисел зробіть три числа і протестуйте її всіма трьома методами)
модернізуйте її так що кожний раз коли ми її запускаємо те
що ми туди передаєм та результат повинно записуватись в файл log.txt
Зверніть увагу на те що в файл повинно дозаписуватись, а не затератись.
Уявіть що ця функція являється легасі кодом і ви її не можете змінювати,
тому потрібно використовувати декоратор. Я хотів би бачити таку реалізацію в домашці три функції:
- функція з минулого уроку
- функція що записую текст
- і декоратор"""


def write_result_file_text(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        with open('text.txt', 'a') as file:
            file.write(f'  --->  Result: {result}\n')
        return result

    return wrapper


@write_result_file_text
def add_three_numbers(number_1: int | float, number_2: int | float, number_3: int | float) -> int | float:
    result = (number_1 + number_2) * number_3
    with open('text.txt', 'a') as file:
        file.write(f'Input numbers: {number_1}, {number_2}, {number_3}')
    return result


if __name__ == '__main__':
    print(add_three_numbers(458, 877, 98))
    print(add_three_numbers(45, 87, 8))

