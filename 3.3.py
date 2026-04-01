# numbers = []
# for i in range(5):
#     numbers.append(int(input()))
# print(numbers)

# numbers = [int(input()) for i in range(5)]
# print(numbers)

# numbers = [int(input()) for i in range(5)]
# avg = sum(numbers) // len(numbers)
# print(sum(numbers))
# numbers = [element for element in numbers if element > avg]

# new_numbers = [] тоже самое что выше
# for element in numbers:
#     if element > avg:
#         new_numbers.append(element)
# numbers = new_numbers
# print(numbers)

# numbers = (int(input()) for i in range(5)) # Это выражение возвращает генератор-объект,
                                           # который выдаёт значения по одному — не загружая 
                                           # в память весь список сразу.


# matrix = [[int(x) for x in input().split()] for i in range(5)]
# print(matrix)

# zeros = [[0] * 5 for i in range(5)]
# print(zeros)

# Вывод программы:
# [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]] 

# zeros[0][0] = 1
# print(zeros)

# Вывод программы:
# [[1, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

# text = "Строка символов"
# codes = [ord(symbol) for symbol in text]
# print(codes)
# Вывод программы:
# [1057, 1090, 1088, 1086, 1082, 1072, 32, 1089, 1080, 1084, 1074, 1086, 1083, 1086, 1074]

# countries = {
#     "Россия": ["русский"],
#     "Беларусь": ["белорусский", "русский"],
#     "Бельгия": ["немецкий", "французский", "нидерландский"],
#     "Вьетнам": ["вьетнамский"]
# }

# multiple_lang = [country for (country, lang) in countries.items() if len(lang) > 1]

# print(multiple_lang)

# Вывод программы:
# ['Беларусь', 'Бельгия']

# countries = {country: capital for country, capital in [
#     ("Россия", "Москва"),
#     ("Беларусь", "Минск"),
#     ("Сербия", "Белград")
# ]}
# print(countries)

# Вывод программы:
# {'Россия': 'Москва', 'Беларусь': 'Минск', 'Сербия': 'Белград'}

# numbers = (int(input()) for i in range(5))
# print(numbers)

from sys import getsizeof

# numbers_iter = (i for i in range(10 ** 6))  # генератор
# print(f"Итератор занимает {getsizeof(numbers_iter)} байт.")
# numbers_list = list(range(10 ** 6))         # список
# print(f"Список занимает {getsizeof(numbers_list)} байт.")

from timeit import timeit

# print(round(timeit("s = '; '.join(str(x) for x in range(10 ** 7))", number=10), 3))

# print(round(timeit("s = '; '.join([str(x) for x in list(range(10 ** 7))])", number=10), 3))

# x = 10
# print(id(x))
# x = 20
# print(id(x))

# Вывод программы (значения будут меняться от запуска к запуску программы):
# 2198530255152
# 2198530255184

# x = 1
# y = x
# print(id(x))
# print(id(y))
# print(x is y)

# Примерный вывод:
# 2109716588848
# 2109716588848 
# True

# x = [el ** 2 for el in range(5)]
# y = [el ** 2 for el in range(5)]
# print(x == y)
# print(x is y)

# Результат:
# True
# False

# x = 5
# print(f'{x}, id = {id(x)}')
# x = 10
# print(f'{x}, id = {id(x)}')

# Результат:
# 5, id = 4311950120
# 10, id = 4311950280

# numbers = [1, 2, 3]
# print(f"{numbers}, id = {id(numbers)}")
# numbers += [4]
# print(f"{numbers}, id = {id(numbers)}")

# Результат:
# [1, 2, 3], id = 2095932585856
# [1, 2, 3, 4], id = 2095932585856

# numbers = [1, 2, 3]
# print(f"{numbers}, id = {id(numbers)}")
# numbers = numbers + [4]
# print(f"{numbers}, id = {id(numbers)}")

# Результат:
# [1, 2, 3], id = 1438332303232  
# [1, 2, 3, 4], id = 1438341470336

# x = [1, 2, 3] Чтобы создать отдельный объект, можно использовать срез:
# y = x[:]
# x[0] = 0
# print(x)
# print(y)

# # Результат:
# # [0, 2, 3]  
# # [1, 2, 3]

# numbers = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # Но если список вложенный, срез копирует только внешний список:
# numbers_copy = numbers[:]
# print([numbers_copy[i] is numbers[i] for i in range(len(numbers))])

# Результат:
# [True, True, True]

# numbers_copy = [elem[:] for elem in numbers]

# print([numbers_copy[i] is numbers[i] for i in range(len(numbers))])

# Результат:
# [False, False, False]

# from copy import deepcopy
# numbers_copy = deepcopy(numbers)
# print(numbers_copy)

# a = -4
# b = -3
# result = ...


# result = []
# for x in range(a, b + 1):
#     result.append(x ** 2)
#     print(result)

# result = [x ** 2 for x in range(a, b + 1)]


# result = [i ** 2 for i in (range(a, b + 1) if a <= b else range(a, b - 1, -1))]
# print(result)

# a = 1
# b = 5
# d = 2

# result = []
# for i in range(a, b + 1):
#     print(i)
#     if i % d == 0:
#         result.append(i)

# print(result)

# result = [i for i in range(a, b + 1) if i % d == 0]
# print(result)

# numbers = [1, 2, 3, 4, 5]
# # set_list = set()
# # for x in numbers:
# #     if x % 2 == 0:
# #         set_list.add(x)
# # print(set_list)

# even_numbers = {x for x in numbers if x % 2 == 0}
# print(even_numbers)

# numbers = [number for number in range(16, 100, 4)]
# numbers = [1, 2, 3, 4, 5]
# set_list = set()
# for x in numbers:
#     if x == int(x ** 0.5) ** 2:
#         set_list.add(x)

# print(set_list)

# set_list = {x for x in numbers if x == int(x ** 0.5) ** 2}
# print(set_list)

# sentence = 'Мама мыла раму'
# # new_list = []
# # sentence_new = sentence.split()
# # for x in sentence_new:
# #     new_list.append(len(x))
    
# # print(new_list)

# new_list = [len(x) for x in sentence.split()]
# print(new_list)
text = '2 + 2 = 4'

# text = '33 коровы,\n' + \
#     '33 коровы,\n' + \
#     '33 коровы -\n' + \
#     'Свежая строка.\n' + \
#     '33 коровы,\n' + \
#     'Стих родился новый,\n' + \
#     'Как стакан парного молока.\n' + \
#     'Стих родился новый,\n' + \
#     'Как стакан парного молока.\n'

# new_text = text.split()
# print(new_text)

# new_text = ''.join(x for x in text if x.isdigit())
# print(new_text)

# string = 'открытое акционерное общество'

# new_string = '-'.join(x[0].upper() for x in string.split())
# print(new_string)

# numbers = [3, 1, 2, 3, 2, 2, 1]
# # new_numbers = set(numbers)
# # print(new_numbers)
# new_list = ' - '.join(str(x) for x in sorted(set(numbers)))
# print(new_list)

# words = 'Ехали медведи на велосипеде'
# letter = 'аяуюёзеиыaeiouy'
# words_list = words.split()
# result = []

# for word in words_list:
#     word_lower = word.lower()
#     vowel_count = 0
    
#     for char in word_lower:
#         if char in letter:
#             vowel_count += 1
        
#     if vowel_count >= 3:
#         result.append(word)
    
# print(result)


# result = [word for word in words.split() if sum(1 for c in word.lower() if c in 'аяуюёзеиыaeiouy') >= 3]
# print(result)  # ['Exali', 'медведи', 'велосипеде']

# text = 'Мама мыла раму!'

# # char_count = {}

# # for char in text.lower():
# #     if char.isalpha():
# #         char_count[char] = char_count.get(char, 0) + 1

# # print(char_count)

# char_count = {char: text.lower().count(char) for char in set(text.lower()) if char.isalpha()}
# print(char_count)

# # ========================================================
# # Обычный цикл
# squares = {}
# for x in range(5):
#     squares[x] = x ** 2
# print(squares)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# # Словарное включение
# squares = {x: x ** 2 for x in range(5)}
# print(squares)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
# # ===========================================================

# data = {'a': [1, 2, 1], 'b': [2, 3, 2, 5, 1]}
# data_2 = {'a': [1, 2, 3], 'b': [5, 2, 5], 'c': [7, 15, 3]}

# result = set()

# for key in data_2:
#     values = data_2[key]
#     if len(values) > len(set(values)):
#         result.add(key)

# print(result)

# result = {key for key in data if len(data[key]) > len(set(data[key]))}
# print(result)

# data = {'a': [1, 2, 3], 'b': [2, 3, 4, 5]}

# result = ""

# for key in data:
#     values = data[key]
#     summa = sum(values)
    
# result = min(data, key=lambda key: (sum(data[key]), key))
# print(result)

# data = {'a': [1, 2, 3], 'b': [2, 3, 4, 5]}

# # Шаг 1: Берем первый ключ как начальный минимум
# min_key = None
# min_sum = float('inf')  # бесконечность (очень большое число)

# # Шаг 2: Проходим по всем ключам
# for key in data:
#     current_sum = sum(data[key])  # считаем сумму значений
    
#     # Шаг 3: Сравниваем
#     if current_sum < min_sum:
#         # Нашли меньшую сумму → обновляем
#         min_sum = current_sum
#         min_key = key
#     elif current_sum == min_sum:
#         # Суммы равны → выбираем лексикографически меньший
#         if key < min_key:
#             min_key = key

# # Шаг 4: Выводим результат
# print(min_key)

# students = {}
# students["Антон"] = 20
# # и так далее...

# students["Мария"] = 19
# students["Дмитрий"] = 20
# print(students)
# print(students["Мария"])
# print(students.get("Петр", "Не найден"))

# students["Иван"] = 18
# students["Антон"] += 1
# students["Мария"] += 1
# for name, age in students.items():
#     print(f"Имя: {name}, Возраст: {age}")

# dict = {'Антон': 21, 'Мария': 20, 'Дмитрий': 21, 'Елена': 20, 'Иван': 18}

# del students["Дмитрий"]

# count_20 = 0
# for age in students.values():
#     if age == 20:
#         count_20 += 1

# total_age = sum(students.values())
# average = total_age // len(students)
# print(count_20, average)

# numbers = {1, 2, 3, 4, 5}

# # вывод: {1: [1], 2: [1, 2], 3: [1, 3], 4: [1, 2, 4], 5: [1, 5]}

# numbers_1 = {15, 49, 36}
# вывод : {15: [1, 3, 5, 15], 36: [1, 2, 3, 4, 6, 9, 12, 18, 36], 49: [1, 7, 49]}

# result = {}

# for num in numbers_1:
#     divisors = []
#     for i in range(1, num + 1):
#         if num % i == 0:
#             divisors.append(i)
#     result[num] = divisors

# print(result)

# result = {num: [i for i in range(1, num + 1) if num % i == 0] for num in numbers}
# print(result)

# numbers = set(range(11, 50, 2))

# result = set()

# for num in numbers:
#     # 1 и меньше — не простые
#     if num <= 1:
#         continue
    
#     # Предполагаем, что число простое
#     is_prime = True
    
#     # Проверяем делимость на числа от 2 до num-1
#     for i in range(2, num):
#         if num % i == 0:
#             # Нашли делитель — число не простое
#             is_prime = False
#             break  # дальше проверять смысла нет
    
#     # Если число простое — добавляем в результат
#     if is_prime:
#         result.add(num)

# print(result)  # {2, 3, 5}


text = 'ехали медведи на велосипеде'        
# вывод: {('велосипеде', 'медведи'), ('велосипеде', 'ехали')}
# text_1 = 'а за ними кот задом наперед'
# # вывод: set()

words = text.split()
# result = set()

# for i in range(len(words)):
#     for j in range(i + 1, len(words)):
#         # print(i, j, words[i], words[j])
#         word1 = words[i]
#         word2 = words[j]
#         letters1 = set(word1)
#         letters2 = set(word2)
#         # print(letters1)
#         # print(letters2)
#         common = letters1 & letters2
#         # print(common)

#         if len(common) > 2:
#             if word1 < word2:
#                 pair = (word1, word2)
#             else:
#                 pair = (word2, word1)

#             result.add(pair)

# print(result)

#Однострочник

# result = {(word1, word2) if word1 < word2 else (word2, word1)
#  for i, word1 in enumerate(text)
#  for word2 in text[i+1:]
#  if len(set(word1) & set(word2)) > 2}

# print(result)

# result = {(w1, w2) if w1 < w2 else (w2, w1) for i, w1 in enumerate(text.split()) for w2 in text.split()[i+1:] if len(set(w1) & set(w2)) > 2}

# (lambda t: {(min(a, b), max(a, b))for a in t.split()for b in t.split()if a < b and len(set(a) & set(b)) > 2})(text)


from itertools import accumulate

text = "мама мыла раму"

# Проверяем split
words = text.split()
print(f"words = {words}")  # должно быть ['мама', 'мыла', 'раму']

# Теперь accumulate
for value in accumulate(words):
    print(f"value = {value}")  # должно быть ['мама'], потом ['мама', 'мыла'] и т.д.
    print(' '.join(value))