
from itertools import product, permutations, combinations, combinations_with_replacement, count, accumulate
# result = list(product("ABC", repeat=2))
# print(result)

# from itertools import count

# for value in count(0, 0.1):
#     if value > 1:
#         break
#     print(round(value, 1))
# # Вывод:
# # 0, 0.1, 0.2, ... 1.0



# from itertools import cycle

# s = ""
# for letter in cycle("ABC"):
#     if len(s) == 10:
#         break
#     s += letter

# print(s)

# # Вывод:
# # ABCABCABCA


# from itertools import repeat
# print(list(repeat("ABC", 5)))

# Вывод:
# ['ABC', 'ABC', 'ABC', 'ABC', 'ABC']


# accumulate(): накопление значений:

# from itertools import accumulate

# for value in accumulate([1, 2, 3, 4, 5]):
#     print(value)

# Вывод:
# 1, 3, 6, 10, 15


# chain() и chain.from_iterable(): объединение коллекций

# from itertools import chain

# values = list(chain("АБВ", "ГДЕ", "ЖЗИ"))
# print(values)

# # Вывод программы:
# # ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И']

# from itertools import chain

# values = list(chain.from_iterable(["АБВ", "ГДЕ", "ЖЗИ"]))

# print(values)

# ----------------------
# product(): декартово произведение

# from itertools import product

# values = list(product([1, 2, 3], "АБВГ"))
# print(values)

# Вывод программы:
# [(1, 'А'), 
# (1, 'Б'), 
# (1, 'В'),
# (1, 'Г'),
# (2, 'А'),
# (2, 'Б'),
# (2, 'В'),
# (2, 'Г'),
# (3, 'А'),
# (3, 'Б'),
# (3, 'В'),
# (3, 'Г')]

# values = list(product([1, 2, 3], "АБВГ", repeat=2))

# product([1, 2, 3], "АБВГ", [1, 2, 3], "АБВГ")
# print(values)

# ----------------------
# permutations(): перестановки без повторений

# values = list(permutations("АБВ"))
# print(values)

# Вывод:
# [('А', 'Б', 'В'),
# ('А', 'В', 'Б'),
# ('Б', 'А', 'В'),
# ('Б', 'В', 'А'),
# ('В', 'А', 'Б'),
# ('В', 'Б', 'А')]

# ----------------------
# combinations(): сочетания без повторений

# values = list(combinations("АБВ", 2))
# print(values)

# Вывод:
# [('А', 'Б'), ('А', 'В'), ('Б', 'В')]

# ----------------------
# combinations_with_replacement(): сочетания с повторениями

# values = list(combinations_with_replacement("АБВ", 2))
# print(values)

# Вывод:
# [('А', 'А'), 
# ('А', 'Б'),
# ('А', 'В'), 
# ('Б', 'Б'),
# ('Б', 'В'),
# ('В', 'В')]

# ----------------------
# enumerate(): индексация элементов

# for index, value in enumerate("ABC", 1):
#     print(index, value)

# Вывод:
# 1 A  
# 2 B  
# 3 C

# ----------------------
# zip(): объединение коллекций по индексам

# print(list(zip("ABCD", [1, 2, 3, 4], strict=True)))

# Вывод:
# [('A', 1), ('B', 2), ('C', 3)]

# enumerate() работает с одной коллекцией и добавляет к каждому элементу его индекс;
# zip() работает с несколькими коллекциями и объединяет элементы с одинаковыми индексами в кортежи.

# data = input()

# for index, element in enumerate(data.split(), 1):
#     print(f"{index}. {element}")

# letters = input()
# letters2 = input()

# for letter, letter2 in zip(letters.split(), letters2.split()):
#     letter = letter.replace(',', '')
#     letter2 = letter2.replace(',', '')
#     print(f"{letter} - {letter2}")


# start, end, step = map(float, input().split())

# for x in count(start, step):
#     if x > end:
#         break
#     print(f"{x:.2f}")

# text = "мама мыла раму"
# words = text.split()
# print(words)
# for value in accumulate(words):
#     print(value)  # ✅ так будут слова

# from itertools import accumulate

# text = "мама мыла раму"
# words = text.split()

# # Явно передаём список и функцию для склеивания
# result = list(accumulate(words, lambda x, y: f"{x} {y}"))
# print(result)
# # for item in result:
# #     print(item)


# num = int(input())
# names = []


# for _ in range(num):
#     name = input()
#     names.append(name)

# names.sort()

# for perm in permutations(names):
#     print(', '.join(perm))

    
    # print(words)
# values = list(permutations("АБВ"))
# print(values)

# from itertools import chain

# line = input()
# products = []

# for _ in line:
#     items = line.split(", ")
#     products.append(items)
#     print(products)

# # chain сглаживает список списков
# all_products = list(chain.from_iterable(products))
# all_products.sort()

# for i, product in enumerate(all_products, 1):
#     print(f"{i}. {product}")
    

# from itertools import chain

# # Собираем список списков
# products = []
# for _ in range(3):
#     products.append(input().split(", "))

# # Выравниваем через chain(*products)
# # *products распаковывает список списков в аргументы для chain
# all_products = list(chain(*products))

# # Сортируем и выводим
# for i, product in enumerate(sorted(all_products), 1):
#     print(f"{i}. {product}")


from itertools import product

# Вводим логическое выражение
expression = input()

# Выводим заголовок
print("a b c f")

# Перебираем все комбинации a, b, c (каждая от 0 до 1)
for a, b, c in product([0, 1], repeat=3):
    # Вычисляем результат
    # eval() выполняет строку как код Python
    # int() преобразует True/False в 1/0
    result = int(eval(expression))
    
    # Выводим строку таблицы
    print(f"{a} {b} {c} {result}")
