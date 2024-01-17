# 1) сортування списка по зростанню числа, від меншого до більшого.
# Функція приймає список з чисел і повертає відсортований список.

def list_sorted_up(list_a: list):
    return sorted(list_a)


# 2) сортування списка на спад, від  більшого до меншого.
# Функція приймає список з чисел і повертає відсортований список.

def list_sorted_down(list_a: list):
    return sorted(list_a, reverse=True)


# 3) сортування за кількістю букв у слові.
# Функція приймає список з слів і повертає відсортований список.

def list_sorted_words(list_a: list):
    return sorted(list_a, key=len)


if __name__ == '__main__':
    print(list_sorted_up([5, 4, -6, 9, 0, 5, 4, 98, 12]))
    print(list_sorted_down([9, 65, 74, 101, 13, 7, 86, 65]))
    print(list_sorted_words(['BMW', 'Renault', 'Mercedes', 'Suzuki', 'Volvo', 'Tesla']))
