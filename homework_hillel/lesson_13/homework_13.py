# Домашка
# Виберіть який з наступних магічних методів і реалізуйте його в простому класі:
# __ne__: To check if two objects are not equal.
# __lt__: To check if one object is less than another.
# __le__: To check if one object is less than or equal to another.
# __gt__: To check if one object is greater than another.
# __ge__: To check if one object is greater than or equal to another.
# Жодного з цих методів ми не розглядали на уроці, але вони працюють ідентично до метода ___eq__ який ми розглянули на уроці.
# Тобто вам треба буде змінити всього дві букви.
# І написати свою логіку яку ви хочте.
#
# Створіть два обьєта класа в якому ви це реалізували і зробіть перевірку що все працює

class Number:
    def __init__(self, value):
        self.value = value

    def __ne__(self, other):

        return self.value != other.value


if __name__ == '__main__':
    num1 = Number(7)
    num2 = Number(8)
    print(num1 != num2)
