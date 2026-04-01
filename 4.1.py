# def имя_функции(аргументы):
#     тело функции


# def only_even(numbers):
#     result = True
#     for x in numbers:
#        if x % 2 != 0:
#            result = False
#            break
#     return result

# print(only_even([2, 4, 6]))
# print(only_even([1, 2, 3]))

# Вывод программы:
# True
# False

# def say_hello():
#     print("Привет, бро!")

# # Вызываем функцию
# say_hello()
# say_hello()

# def only_even(numbers):
#     for x in numbers:
#         if x % 2 != 0:
#             return False
#     return True

# print(only_even([2, 4, 6]))
# print(only_even([1, 2, 3]))

# Вывод программы:
# True
# False


# def only_even(numbers):
#     for i, x in enumerate(numbers):
#         if x % 2 != 0:
#             return False, i
#     return True

# print(only_even([2, 4, 6]))
# print(only_even([1, 2, 3]))

# Вывод программы:
# True
# (False, 0)

# def check_password(pwd):
#     return pwd == password

# password = "Python"
# print(check_password("123"))

# Вывод программы:
# False

# def list_modify():
#     del sample[-1]

# sample = [1, 2, 3]
# list_modify()
# print(sample)
# # Вывод программы:
# # [1, 2]

# def list_modify():
#     sample = [4, 5, 6]

# sample = [1, 2, 3]
# list_modify()
# print(sample)

# Вывод программы:
# [1, 2, 3]

# def list_modify_1(list_arg):
#     # создаём новый локальный список, не имеющий связи с внешним
#     list_arg = [1, 2, 3, 4]

# def list_modify_2(list_arg):
#     # меняем исходный внешний список, переданный как аргумент
#     list_arg += [4]

# sample_1 = [1, 2, 3]
# sample_2 = [1, 2, 3]
# list_modify_1(sample_1)
# list_modify_2(sample_2)
# print(sample_1)
# print(sample_2)

# Вывод программы:
# [1, 2, 3]
# [1, 2, 3, 4]


# Так делать плохо
# def inc():
#     global x
#     x += 1
#     print(f"Количество вызовов функции равно {x}.")

# x = 0
# inc()
# inc()
# inc()

# # Вывод программы:

# Количество вызовов функции равно 1.
# Количество вызовов функции равно 2.
# Количество вызовов функции равно 3.


# def f(count):
#     count += 1
#     print(f'Количество вызовов функции равно {count}.')
#     return count

# count_f = 0
# count_f = f(count_f)
# count_f = f(count_f)
# count_f = f(count_f)

# Вывод программы:
# Количество вызовов функции равно 1.
# Количество вызовов функции равно 2.
# Количество вызовов функции равно 3.


# ==============================================>>>
# Пример из жизни:
# def count_even(num):
#     even = 0
#     for digit in str(num):
#         if int(digit) % 2 == 0:
#             even += 1
#     return even

# # Теперь просто вызываем функцию
# print(count_even(650975472))  # 5
# print(count_even(591084323))  # 4



# def multiply(x, y):  # x и y — это ПАРАМЕТРЫ
#     return x * y

# result = multiply(4, 5)  # 4 и 5 — это АРГУМЕНТЫ

# def greet(name, greeting="Привет"):
#     print(f"{greeting}, {name}!")

# greet("Антон")              # Привет, Антон!
# greet("Антон", "Пердун")   # Здарова, Антон!

# def count_even_odd(num):
#     even = 0
#     odd = 0
#     for digit in str(num):
#         if int(digit) % 2 == 0:
#             even += 1
#         else:
#             odd += 1
#     return even, odd  # возвращаем кортеж

# even_count, odd_count = count_even_odd(650975472)
# print(f"Четных: {even_count}, Нечетных: {odd_count}")


# x = 10  # глобальная переменная

# def my_func():
#     y = 5  # локальная переменная (только внутри функции)
#     print(x)  # можно читать глобальную
#     # x = 20  # так нельзя изменить глобальную!

# def change_global():
#     global x  # говорим, что хотим менять глобальную
#     x = 20

# change_global()
# print(x)  # 20

# Задача прошлой темы с числами ===========>

# def count_even_odd(num):
#     """Считает количество четных и нечетных цифр в числе"""
#     even = 0
#     odd = 0
#     for digit in str(num):
#         if int(digit) % 2 == 0:
#             even += 1
#         else:
#             odd += 1
#     return even, odd

# def classify(num):
#     """Определяет тип числа: even, odd или eq"""
#     even, odd = count_even_odd(num)
#     if even > odd:
#         return "even"
#     elif odd > even:
#         return "odd"
#     else:
#         return "eq"

# # Используем
# numbers = [650975472, 591084323, 629700, 1504180]

# for num in numbers:
#     print(f"{num}: {classify(num)}")



# <<<===================================>>>>
# Плохо — делает два дела
# def process_number(num):
#     count = count_digits(num)
#     save_to_file(count)
#     return count

# # Хорошо — разделили
# def count_digits(num):
#     return len(str(num))

# def save_to_file(data):
#     with open("result.txt", "w") as f:
#         f.write(str(data))

# def print_hello(name):
#     print(f'Hello, {name}')

# print_hello('Жопа')

# def find_nod(a, b):
#     while b:
#         a, b = b, a % b
#     return a

# print(find_nod(48, 36))


# def split_numbers(text):
#     parts = text.split()
#     result = tuple(int(x) for x in parts)
#     return result

# print(split_numbers("1 2 3 4 5"))

# _printed = set()

# def modern_print(text):
#     if text not in _printed:
#         print(text)
#         _printed.add(text)

# modern_print("Hello!")
# modern_print("Hello!")
# modern_print("How do you do?")
# modern_print("Hello!")


# def can_eat(horse, other):
#     hx, hy = horse
#     ox, oy = other
#     dx = abs(hx - ox)
#     dy = abs(hy - oy)
#     return (dx == 1 and dy == 2) or (dx == 2 and dy == 1)

# print(can_eat((2, 1), (4, 2)))


# def get_dict(text):
#     result = {}
    
#     # Разбиваем строку на пары по ;
#     pairs = text.split(';')
    
#     for pair in pairs:
#         # Разбиваем пару на ключ и значение по =
#         key, value = pair.split('=')
        
#         # Пробуем преобразовать значение в число
#         # Сначала проверяем на отрицательное число
#         if value.startswith('-'):
#             # Проверяем, является ли это целым числом (без точки)
#             if value[1:].isdigit():
#                 value = int(value)
#             # Проверяем, является ли это дробным числом
#             elif value[1:].replace('.', '', 1).isdigit() and value.count('.') == 1:
#                 value = float(value)
#         else:
#             # Проверяем на целое число
#             if value.isdigit():
#                 value = int(value)
#             # Проверяем на дробное число
#             elif value.replace('.', '', 1).isdigit() and value.count('.') == 1:
#                 value = float(value)
        
#         result[key] = value
    
#     return result

# print(get_dict('id=3-76;ip=127.0.0.1;phone=+7-(123)-456-78-90'))


# def merge(tuple1, tuple2):
#     result = []
#     i = 0  # указатель для первого кортежа
#     j = 0  # указатель для второго кортежа
    
#     # Идем, пока не дошли до конца хотя бы одного кортежа
#     while i < len(tuple1) and j < len(tuple2):
#         if tuple1[i] < tuple2[j]:
#             result.append(tuple1[i])
#             i += 1
#         else:
#             result.append(tuple2[j])
#             j += 1
    
#     # Добавляем оставшиеся элементы из первого кортежа
#     while i < len(tuple1):
#         result.append(tuple1[i])
#         i += 1
    
#     # Добавляем оставшиеся элементы из второго кортежа
#     while j < len(tuple2):
#         result.append(tuple2[j])
#         j += 1
    
#     return tuple(result)

# print(merge((1, 2), (3, 4, 5)))
# print(merge((7, 12), (1, 9, 50)))


# total = 0


# def move(player, number):
#     global total

#     if player == "Петя":
#         total += number
#     elif player == "Ваня":
#         total -= number


# def game_over():
#     if total > 0:
#         return "Петя"
#     elif total < 0:
#         return "Ваня"
#     else:
#         return "Ничья"
    
# move('Петя', 2)
# move('Ваня', 0)
# print(game_over())


# def filter_numbers(numbers, even=None, positive=None):
#     result = list(numbers)
    
#     if even is not None:
#         if even:
#             result = [x for x in result if x % 2 == 0]
#         else:
#             result = [x for x in result if x % 2 != 0]
    
#     if positive is not None:
#         if positive:
#             result = [x for x in result if x > 0]
#         else:
#             result = [x for x in result if x < 0]
    
#     return result

# # Примеры
# print(filter_numbers([-3, -2, -1, 0, 1, 2, 3], even=True))
# # [-2, 0, 2]

# print(filter_numbers([-3, -2, -1, 0, 1, 2, 3], positive=True))
# # [1, 2, 3]

# print(filter_numbers([-3, -2, -1, 0, 1, 2, 3], even=True, positive=True))
# [2]


# import random
# import string

# def generate_password(length):
#     chars = string.ascii_letters + string.digits
#     password = ''
#     for _ in range(length):
#         password += random.choice(chars)
#     return password

# Примеры
# print(generate_password(8))
# print(generate_password(12)) 


# def validate_password(password):
#     if len(password) < 8:
#         return False, "Слишком короткий (минимум 8 символов)"
    
#     has_upper = False
#     has_digit = False
#     has_special = False
#     specials = "!@#$%^&*"
    
#     for char in password:
#         if char.isupper():
#             has_upper = True
#         if char.isdigit():
#             has_digit = True
#         if char in specials:
#             has_special = True
    
#     if not has_upper:
#         return False, "Нет заглавной буквы"
#     if not has_digit:
#         return False, "Нет цифры"
#     if not has_special:
#         return False, "Нет спецсимвола"
    
#     return True, "Надежный пароль!"

# # Примеры
# print(validate_password("qwerty"))           # (False, 'Слишком короткий...')
# print(validate_password("qwerty123"))        # (False, 'Нет заглавной буквы')
# print(validate_password("Qwerty123"))        # (False, 'Нет спецсимвола')
# print(validate_password("Qwerty123!"))       # (True, 'Надежный пароль!')


# def swap(a, b):
#     a[:], b[:] = b[:], a[:]


# # Ввод:
# a = b = [1, 2]
# c = d = [2, 1]
# print(a, b, c, d)
# swap(a, c)
# print(a, b, c, d)
# # Вывод:
# # [1, 2] [1, 2] [2, 1] [2, 1]
# # [2, 1] [2, 1] [1, 2] [1, 2]

# x = [1, 2]
# y = [3, 4]

# def swap_wrong(a, b):
#     a = b
#     b = a

# swap_wrong(x, y)
# print(x, y)


# original = [[1, 2], [3, 4]]
# copy_surface = original[:]
# copy_surface[0][1] = 999
# print(original)  # [[999, 2], [3, 4]]  — изменилось!

# d = {'a': 1, 'b': {'c': 2}}
# e = d.copy()
# e['b']['c'] = 99
# e['a'] = 100
# print(d['a'])
# print(d['b']['c'])

# def create_dict(key, value, d={}):
#     d[key] = value
#     return d

# print(create_dict('a', 1))
# print(create_dict('b', 2))
# print(create_dict('c', 3))

# month_dict = {
#     1: {'ru': 'Январь', 'en': 'January'},
#     2: {'ru': 'Февраль', 'en': 'February'},
#     3: {'ru': 'Март', 'en': 'March'},
#     4: {'ru': 'Апрель', 'en': 'April'},
#     5: {'ru': 'Май', 'en': 'May'},
#     6: {'ru': 'Июнь', 'en': 'June'},
#     7: {'ru': 'Июль', 'en': 'July'},
#     8: {'ru': 'Август', 'en': 'August'},
#     9: {'ru': 'Сентябрь', 'en': 'September'},
#     10: {'ru': 'Октябрь', 'en': 'October'},
#     11: {'ru': 'Ноябрь', 'en': 'November'},
#     12: {'ru': 'Декабрь', 'en': 'December'}
# }

# def get_month_name(month_number, lang):
#     return month_dict[month_number][lang]

# print(get_month_name(3, "en"))        # Март
# print(get_month_name(7, 'ru'))  # March


# def take_small(money):
#     result = []
#     for i in money:
#         if i < 100:
#             result.append(i)
#     return result


# money = [1, 5, 200, 0.5, 0.05, 10, 25, 1000, 5000, 1, 2, 100, 0.1, 5, 2000, 0.01]
# print(take_small(money))



# def fragments(numbers):
#     if not numbers:
#         return []
    
#     result = []
#     current = [numbers[0]]

#     for i in range(1, len(numbers)):
#         if numbers[i] >= current[-1]:
#             current.append(numbers[i])
#         else:
#             result.append(current)
#             current = [numbers[i]]
    
#     result.append(current)
#     return result

# numbers = fragments([-4, -2, 5, 0, 3, 7, -8, -2, 6, 7, 6, 8, 10, 5, 7, 8])
# print(fragments(numbers))

# def find_mountains(heights):
#     mountains = []
#     n = len(heights)
    
#     for i in range(1, n - 1):
#         if heights[i] > heights[i - 1] and heights[i] > heights[i + 1]:
#             mountains.append(i + 1) 
#     return tuple(mountains)


# def final_price(price, discount=1):
#     return price - price * discount / 100


# print(final_price(1000, 5))
# # Значение скидки не задано, используется значение по умолчанию
# print(final_price(1000))

# def add_value(x, list_arg=[]):
#     list_arg += [x]
#     return list_arg

# print(add_value(0))
# print(add_value(0, [1, 2, 3]))
# print(add_value(1))


# def add_value(x, list_arg=None):
#     if list_arg is None:
#         list_arg = []
#     list_arg += [x]
#     return list_arg

# print(add_value(0))
# print(add_value(0, [1, 2, 3]))
# print(add_value(1))


# def final_price(price, discount=1):
#     return price - price * discount / 100

# print(final_price(1000, discount=5))
# print(final_price(discount=10, price=1000))


# def final_price(*prices, discount=1):
#     return [price - price * discount / 100 for price in prices]

# print(final_price(100, 200, 300, discount=5))


# def final_price(*prices, discount=1, **kwargs):
#     low = kwargs.get("price_low", min(prices))
#     high = kwargs.get("price_high", max(prices))
#     return [price - price * discount / 100 for price in prices if low <= price <= high]

# print(final_price(100, 200, 300, 400, 500, discount=5))
# print(final_price(100, 200, 300, 400, 500, discount=5, price_low=200))
# print(final_price(100, 200, 300, 400, 500, discount=5, price_high=200))
# print(final_price(100, 200, 300, 400, 500, discount=5, price_low=200, price_high=350))

# def sum_three(x, y, z):
#     return x + y + z

# numbers = [10, 20, 30]
# print(sum_three(*numbers))   # 60 / Распаковка списка/кортежа

# def greet(name, age):
#     print(f"{name}, age {age}")

# person = {"name": "Alice", "age": 25}
# greet(**person)   # Alice, age 25 / Распаковка словаря


# def func(a, b, c, d):
#     print(a, b, c, d)

# args = [1, 2]
# kwargs = {"c": 3, "d": 4}
# func(*args, **kwargs)   # 1 2 3 4


# def logger(func):
#     def wrapper(*args, **kwargs):
#         print(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
#         result = func(*args, **kwargs)
#         print(f"Result: {result}")
#         return result
#     return wrapper

# @logger
# def add(x, y):
#     return x + y

# add(5, 3)
# # Calling add with args=(5, 3), kwargs={}
# # Result: 8


# def apply_transformations(data, transforms):
#     """Применяет все функции из списка transforms к данным (каждая функция принимает и возвращает список)"""
#     for transform in transforms:
#         data = transform(data)
#     return data

# # Примеры функций-преобразований
# def scale_to_01(data):
#     min_val = min(data)
#     max_val = max(data)
#     return [(x - min_val) / (max_val - min_val) for x in data]

# def add_noise(data):
#     import random
#     return [x + random.uniform(-0.05, 0.05) for x in data]

# def clip_outliers(data):
#     return [max(0, min(1, x)) for x in data]  # ограничиваем диапазон [0,1]

# pipeline = [scale_to_01, add_noise, clip_outliers]
# raw_data = [10, 20, 30, 100, 200]
# processed = apply_transformations(raw_data, pipeline)
# print(processed)


# def conditional_sum(data, condition):
#     total = 0
#     for x in data:
#         if condition(x):
#             total += x
#     return total

# numbers = [1, 2, 3, 4, 5, 6]


# def is_even(num):
#     return num % 2 == 0

# print(conditional_sum(numbers, is_even))


# def greater_than_three(num):
#     return num > 3

# print(conditional_sum(numbers, greater_than_three))  # 15


# def only_pos(x):
#     return x > 0

# result = filter(only_pos, [-1, 5, 6, -10, 0])
# print(", ".join(str(x) for x in result))


# def square(x):
#     return x ** 2

# result = map(square, range(5))
# print(", ".join(str(x) for x in result))

# numbers = [1, 2, 3]
# squared_pairs = map(lambda x: (x, x**2), numbers)  # итератор кортежей (1,1), (2,4), (3,9)
# result_dict = dict(squared_pairs)
# print(result_dict)  # {1: 1, 2: 4, 3: 9}

# numbers = list(map(int, input().split()))

# result = filter(lambda x: x > 0, [-1, 5, 6, -10, 0])
# print(", ".join(str(x) for x in result))

# lines = ["abcd", "ab", "abc", "abcdef"]
# print(sorted(lines, key=lambda line: len(line)))

# lines = ["abcd", "ab", "ba", "acde"]
# print(sorted(lines, key=lambda line: (len(line), line)))

# words = ["apple", "banana", "kiwi", "ara", "avocado", "blueberry"]
# # Сортировка по длине, потом по алфавиту
# print(sorted(words, key=lambda w: (len(w), w)))

# lines = ["abcd", "ab", "ba", "acde"]
# print(sorted(lines, key=lambda line: (-len(line), line)))

# lines = ["abcd", "ab", "ba", "acde"]
# print(min(lines, key=lambda line: (-len(line), line)))

from functools import reduce
# reduce(функция, последовательность, [начальное_значение])
# numbers = range(1, 7)
# print(reduce(lambda x, y: x + y, numbers))

# letters = ['a', 'b', 'a', 'c', 'b', 'a']
# counts = reduce(lambda acc, letter: {**acc, letter: acc.get(letter, 0) + 1}, letters, {})
# print(counts)  # {'a': 3, 'b': 2, 'c': 1}

# data = [10, 20, 30, 40]
# result = reduce(lambda acc, x: (acc[0] + x, acc[1] + 1), data, (5, 1))
# print(result)  # (100, 4)
# print(result[0] / result[1])  # 25.0


# numbers = [1, 2, 3, 4, 5, 6]
# # 1. Отфильтровать чётные
# # 2. Удвоить
# # 3. Найти сумму
# result = reduce(lambda x, y: x + y,
#                 map(lambda x: x * 2,
#                     filter(lambda x: x % 2 == 0, numbers)))
# print(result)  # 2*2 + 4*2 + 6*2 = 4+8+12=24

# data = ["ab", "abcd", "abc"]

# result = reduce(lambda acc, s: max(acc, len(s)), data, 0)
# print(result)

dicts = [{'a': 1}, {'b': 2}, {'a': 3}]

merged = reduce(
    lambda acc, d: {k: acc.get(k, 0) + v for k, v in d.items()} | acc,
    dicts,
    {}
)
print(merged)  # {'a': 4, 'b': 2}

from functools import reduce

numbers = [5, 1, 8, 3, 9, 2, 7]

def top_two(acc, x):
    first, second = acc
    if x > first:
        # новый максимум, старый максимум становится вторым
        return (x, first)
    elif x > second:
        # новый второй максимум
        return (first, x)
    else:
        return (first, second)

result = reduce(top_two, numbers, (float('-inf'), float('-inf')))
print(result[1])  # 8