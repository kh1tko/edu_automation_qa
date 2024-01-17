# 1) Напишіть ліст компрехеншин який формує список всіх чисел від 34 до 121 які діляться націло на 3 та на 2
divisible_by_3_and_2 = [num for num in range(34, 122) if num % 3 == 0 and num % 2 == 0]
print(divisible_by_3_and_2)


# 2) Напишіть клас калькулятора де будуть 4 арифметичні дії плюс, мінус, додавання, множення - звичайні методи.
# і зробіть статік метод який буде виводити повідомлення, привіт я калькулятор.

class Calculator:
    def __init__(self, name):
        self.name = name

    def addition(self, a: int | float, b: int | float):
        return a + b

    def subtraction(self, a: int | float, b: int | float):
        return a - b

    def multi(self, a: int | float, b: int | float):
        return a * b

    def division(self, a: int | float, b: int | float):
        if b == 0 or a == 0:
            return 'Не тупи. На ноль не можна ділити)'
        else:
            return a / b

    @staticmethod
    def greet():
        print('Привіт, я калькулятор')


if __name__ == '__main__':
    calc = Calculator('Твій калькулятор')

    Calculator.greet()

    print(f'Результат додавання: {calc.addition(32, 43)}')

    print(f'Результат ділення: {calc.division(9, 3)}')

    print(f'Результат віднімання: {calc.subtraction(3, 2)}')

    print(f'Результат множення: {calc.multi(21, 2)}')
