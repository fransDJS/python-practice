# s = 'Tom Marvolo Riddle'
# tokens = s.split()
# first_name = tokens[0]
# middle_name = tokens[1]
# last_name = tokens[2]
# s2 = first_name + ' ' + middle_name + ' ' + last_name
# print(tokens[3])
# print(s2)

# houses = ['Ravenclaw', 'Hufflepuff', 'Gryffindor']
# houses.append('Slytherin')

# # цикл 'for'. отступы вновь важны!
# for house in houses:
#     print('Ten points to', house, end='!\n')

# # set (неупорядоченные коллекции)
# birth_name = 'Tom Marvolo Riddle'
# birth_name_letters = set(birth_name)
# birth_name_lower_letters = set(birth_name.lower())
# nickname_lower_letters = set('I am Lord Voldemort'.lower())
# print(birth_name_lower_letters == nickname_lower_letters)

# word = "коллекция"
# letters = set(word)
# print(letters)

# vowels = {"а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"}
# letter = input("Введите букву русского алфавита: ")
# if letter.lower() in vowels:
#     print("Гласная буква")
# else:
#     print("Согласная буква")

# s_1 = {1, 2, 3}
# s_2 = {3, 4, 5}
# s_union = s_1 | s_2
# # s_union = s_1.union(s_2)
# print(s_union) # {1, 2, 3, 4, 5}

# s_1 = {1, 2, 3}
# s_2 = {3, 4, 5}
# s_intersection = s_1 & s_2
# # s_intersection = s_1.intersection(s_2)
# print(s_intersection) # {3}
 
# s_1 = {1, 2, 3}
# s_2 = {3, 4, 5}
# s_dif = s_1 - s_2
# # s_dif = s_1.difference(s_2)
# print(s_dif) # {1, 2}

# s_1 = {1, 2, 3}
# s_2 = {3, 4, 5}
# s_sym_dif = s_1 ^ s_2
# # s_sym_dif = s_1.symmetric_difference(s_2)
# print(s_sym_dif) 1, 2, 4, 5}

# vowels = {"а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"}
# letters = set("коллекция")
# print(", ".join(letters & vowels))
# Например, найти согласные
# print(", ".join(letters - vowels))  # разность множеств

# Или все буквы слова
# print(", ".join(letters))

# s_1 = {1, 2, 3}
# s_2 = {3, 1, 2}
# print(s_1 == s_2) #True

# s_1 = {1, 2, 3}
# s_2 = {1, 2, 3, 4}
# print(s_1 <= s_2) #True

# s_1 = {1, 2, 3, 4}
# s_2 = {1, 2, 3}
# print(s_1 >= s_2) #True

# name = "Французов Андрей Дмитриевич".replace(" ", "")
# letters = set(name)

# print(", ".join(letters).lower())

# countries_and_capitals = {"Россия": "Москва",
# "США": "Вашингтон",
# "Франция": "Париж"}
# print(countries_and_capitals["Франция"])

# countries_and_capitals = {"Россия": "Москва",
#                           "США": "Вашингтон",
#                           "Франция": "Париж"}
# countries_and_capitals["Сербия"] = "Белград"
# print(countries_and_capitals)

# d = {"key": "old_value"}
# d["key"] = "new_value"
# print(d["key"])

# countries_and_capitals = {"Россия": "Москва",
#                           "США": "Вашингтон",
#                           "Франция": "Париж"}
# if "Сербия" in countries_and_capitals:
#     print(countries_and_capitals["Сербия"])
# else:
#     print("Страна пока не добавлена в словарь")

# countries_and_capitals = {"Россия": "Москва",
# "США": "Вашингтон",
# "Франция": "Париж"}
# for country in countries_and_capitals:
#     print(f"У страны {country} столица — {countries_and_capitals[country]}.")

# создаём пустой словарь
# countries = dict()
# # вводим первую строку до цикла (можно заменить, использовав оператор-морж)
# country = input()
# # создаём счётчик номеров строк
# str_number = 0
# # продолжаем цикл, пока не введена строка «СТОП»
# while country != "СТОП":
#     # если введённой страны нет в словаре, создаём ключ и записываем по ключу список из одного номера строки
#     if country not in countries:
#         countries[country] = [str_number]
#     # иначе добавляем в список по ключу новое значение номера строки
#     else:
#         countries[country].append(str_number)
#     # увеличиваем счётчик
#     str_number += 1
#     # вводим следующую строку
#     country = input()
# # выводим название страны и полученные списки с новой строки
# for country in countries:
#     print(f"{country}: {countries[country]}")


# создаём пустой словарь
# countries = dict()
# # вводим первую строку до цикла (можно заменить, использовав оператор-морж)
# country = input()
# # создаём счётчик номеров строк
# str_number = 0
# # продолжаем цикл, пока не введена строка «СТОП»
# while country != "СТОП":
#     # Если страна country есть среди ключей, то get() возвращает список, 
#     # хранящийся по этому ключу, иначе get() возвращает пустой список. 
#     # Добавляем в список значение str_number.
#     countries[country] = countries.get(country, []) + [str_number]
#     # увеличиваем счётчик
#     str_number += 1
#     # вводим следующую строку
#     country = input()
# # выводим название страны и полученные списки с новой строки
# for country in countries:
#     print(f"{country}: {countries[country]}")

# data_1 = set(input())
# data_2 = set(input())

# data_intersection = data_1 & data_2
# print("".join(data_intersection))

# n = int(input())
# all_words = []

# for _ in range(n):
#     text = input()
#     words = text.split()
#     all_words.extend(words)

# unique_words = set(all_words)  

# for word in unique_words:
#     print(word)

# n = int(input())
# unique_words = set()

# for _ in range(n):
#     text = input()
#     words = set(text.split())
#     unique_words = unique_words | words

# print()
# for word in unique_words:
#     print(word)

# counter = {}

# while True:
#     line = input().strip()
    
#     if line == "":
#         break

#     words = line.split()

#     for word in words:
#         if word in counter:
#             counter[word] += 1
#         else:
#             counter[word] = 1

# for description, count in counter.items():
#     print(description, count)


# TRANSLITERATE_DICT = {
#     'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'E',
#     'Ж': 'ZH', 'З': 'Z', 'И': 'I', 'Й': 'I', 'К': 'K', 'Л': 'L', 'М': 'M',
#     'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U',
#     'Ф': 'F', 'Х': 'KH', 'Ц': 'TC', 'Ч': 'CH', 'Ш': 'SH', 'Щ': 'SHCH',
#     'Ы': 'Y', 'Э': 'E', 'Ю': 'IU', 'Я': 'IA', 'Ь': '', 'Ъ': ''
# }


# result = ''

# for char in input():
#     char_copy = char.upper()
#     # print(char_copy)
#     if char_copy in TRANSLITERATE_DICT:
#         if char.isupper():
#             char = TRANSLITERATE_DICT[char_copy].capitalize()
#             print('uper:', char)
#         else:
#             char = TRANSLITERATE_DICT[char_copy].lower()
#             print("lower",char)
#     result += char

# print(result)
numbers = input().split()
result = []

for num_str in numbers:
    num = int(num_str)
    binary = f'{num:b}'
    
    digit = len(binary) # 3
    units = binary.count('1') # 2
    zeros = binary.count('0') # 1

    stats = {
        "digits": digit,
        "units": units,
        "zeros": zeros
    }

    result.append(stats)

print(result)








