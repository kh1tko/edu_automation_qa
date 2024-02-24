# # потрібно відсіяти в списку меньше і рівні 5
# a = [3, 3, 3, 4, 5, 7, 7, 8, 9, 0, 5, 5, 5, 7, 8, 9, 132]
#
# new_a = [i for i in a if i >= 6]
# print(new_a)
#
# # Потрібно поміняти ключі і значення місцями в словнику.
# c = {123: '123', (12, 23, 4): 12, 'kie': 'ffds'}
# new_c = {v: k for k, v in c.items()}
# print(new_c)

# # інша компанія
# # task 1
# # Нужно написать функцию которая принимает два списка и выдает список с поочередными элементами из списка 1 и 2
# # [1, 2, 3, 4], [7,6,9] =>> [1, 7, 2, 6, 3, 9, 4]
# a = [1, 2, 3, 4]
# b = [7, 6, 9]
#
# a_b = []
# min_length = min(len(a), len(b))
# for i in range(min_length):
#     a_b.extend([a[i], b[i]])
# a_b.extend(a[min_length:])
# a_b.extend(b[min_length:])
# print(a_b)


# # task2
# # Нужно исправить код и дописать вызовы в assert'ах чтобы отработали assert'ы
# class Folder(object):
#     def __init__(self, name):
#         self.name = name
#
#     @property
#     def path(self):
#         return '/%s' % self.name
#
#
# folder1 = Folder('picture')
# folder2 = Folder('pictures/nature')
#
# assert (folder1.name == 'picture')
# assert (folder1.path == '/picture')
#
# assert (folder2.name == 'pictures/nature')
# assert (folder2.path == '/pictures/nature')
#
# folder1.name = 'pic'
# folder2.name = 'pic/nature'
#
# assert (folder1.name == 'pic')
# assert (folder2.path == '/pic/nature')

# Другая компания
# task_1
# Using this list of hotels:
# hotels = [{'name': 'Hilton', "locations": 2345}, {'name': "Accor", 'locations': 789}, {'name': 'W', "locations":678}]
# Please write code to create a new list of hotel names by each of these methods:
# - using for loops
# - using list comprehensions
# - using the map() functions

hotels = [{'name': 'Hilton', "locations": 2345}, {'name': "Accor", 'locations': 789}, {'name': 'W', "locations": 678}]

# hotel_names_for_loops = []
# for hotel in hotels:
#     hotel_names_for_loops.append(hotel['name'])
#
# print("Using For Loops:", hotel_names_for_loops)

# hotels_names_list_comp = [hotel['name'] for hotel in hotels]
# print(hotels_names_list_comp)

# def get_hotel_name(hotel):
#     return hotel['name']


# # hotel_names_map = list(map(get_hotel_name, hotels))
# print(list(map(get_hotel_name, hotels)))


# task_2
# Write a function named word_count that takes in a string. Return a dictionary with each word in the string as the key
# end the number of times it appers as the value.

# task_4
# Given the list bellow, write code to remove duplicates and preserve initial order of elements occurrence.
# amenities = ['free wifi', 'breakfast', 'gym', 'breakfast', 'pool', 'restaurant']
amenities = ['free wifi', 'breakfast', 'gym', 'breakfast', 'pool', 'restaurant']
amenities_out_double = []
for i in amenities:
    if i not in amenities_out_double:
        amenities_out_double.append(i)
print(amenities_out_double)

# Отсортировать список через лист компрехеншн чтобы он вернул значения выше 2
old_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
new_list = sorted([i for i in old_list if i >= 3])
print(new_list)
