from sys import stdin

# lines = []
# for line in stdin:
#     lines.append(line.rstrip("\n"))
# print(lines)

# Теперь результат:
# ['Первая', 'Вторая', 'Третья']



# lines = stdin.readlines()
# print(lines)

# text = stdin.read()
# print([text])

# # Пример вывода:
# ['Первая\nВторая\nТретья\n']

# open(file, mode='r', encoding=None)

# import os

# print("Текущая директория:", os.getcwd())
# print("Файл существует?", os.path.exists("C:/Practic Python/input_1.txt"))

# with open("C:/Practic Python/input_1.txt", "r", encoding="UTF-8") as f:
#     content = f.read()
#     print("Содержимое файла:")
#     print(content)

# file_in = open("input_1.txt", encoding="UTF-8")
# for line in file_in:
#     print(line.rstrip("\n"))
# file_in.close()

# <<<<<=====================================>>>>
# Так лучше, чтобы файл закрылся всегда
# with open("input_1.txt", encoding="UTF-8") as file_in:
#     for line in file_in:
#         print(line.rstrip("\n"))


# with open("input_1.txt", encoding="UTF-8") as file_in:
#     lines = file_in.readlines()
# print(lines)

# Вывод программы:
# ['Привет!\n', 'Это пример текстового файла.\n', 'А это -- последняя строка, которая должна закончиться переходом на новую.\n']


# with open("input_1.txt", encoding="UTF-8") as file_in:
#     symbols = file_in.read(10)
# print([symbols])

# Вывод программы:
# ['Привет!\nЭт']

# <<<<=======================================================>>>>
# Для записи данных из строковой переменной используется метод write():
# with open("output_1.txt", "w", encoding="UTF-8") as file_out:
#     n = file_out.write("Это первая строка\nА вот и вторая\n")

# print(n)


# Для записи строк из списка в файл используется метод writelines()
# lines = ["Это первая строка\n", "А вот и вторая\n", "И третья - последняя\n"]
# with open("output_2.txt", "w", encoding="UTF-8") as file_out:
#     file_out.writelines(lines)

# Содержимое выходного файла:
# Это первая строка
# А вот и вторая
# И третья - последняя

# <<<<===========================>>>>
# Функция print() может быть использована для вывода данных в файл.
# with open("output_3.txt", "w", encoding="UTF-8") as file_out:
#     print("Вывод в файл с помощью функции print()", file=file_out)

# Содержимое выходного файла:
# Вывод в файл с помощью функции print()


# with open("students.json", encoding="UTF-8") as file_in:
#     records = json.load(file_in)
# pprint(records)


# with open("students.json", encoding="UTF-8") as file_in:
#     records = json.load(file_in)
# records[1]["group_number"] = 2
# with open("students.json", "w", encoding="UTF-8") as file_out:
#     json.dump(records, file_out, ensure_ascii=False, indent=2)

#Вывод программы:
# [{'date_of_birth': '01.01.2001',
#   'first_name': 'Иван',
#   'group_number': 1,
#   'last_name': 'Иванов',
#   'patronymic': 'Иванович',
#   'phone_numbers': ['+7 111 111 1111', '+7 111 111 1112']},
#  {'date_of_birth': '10.10.2001',
#   'first_name': 'Пётр',
#   'group_number': 1,
#   'last_name': 'Петров',
#   'patronymic': 'Петрович',
#   'phone_numbers': ['+7 111 111 1113', '+7 111 111 1114']}]

# records = {
#     1: "First",
#     2: "Second",
#     3: "Third"
# }

# with open("output.json", "w", encoding="UTF-8") as file_out:
#     json.dump(records, file_out, ensure_ascii=False, indent=2)


# ЗАДАЧИ
# 1
# total = 0

# for line in stdin:
#     line = line.strip()
#     if not line:
#         continue
#     total += sum([int(x) for x in line.split()])

# print(total)

# 2

# old_heights = []
# new_heights = []

# for line in stdin:
#     line = line.strip()
#     if not line:
#         continue

#     parts = line.split()
#     old_heights.append(int(parts[1]))
#     new_heights.append(int(parts[2]))

# avg_old = sum(old_heights) / len(old_heights)
# avg_new = sum(new_heights) / len(new_heights)

# difference = avg_new - avg_old
# print(round(difference))

import os

# # Вводим названия файлов
# file1 = input()
# file2 = input()
# file3 = input()

# # Читаем первый файл
# with open(file1, 'r', encoding='utf-8') as f1:
#     text1 = f1.read()

# # Читаем второй файл
# with open(file2, 'r', encoding='utf-8') as f2:
#     text2 = f2.read()

# # Разбиваем текст на слова и кладем в множества
# set1 = set(text1.split())
# set2 = set(text2.split())

# # Находим слова, которые есть только в одном файле
# result = set1 ^ set2

# # Превращаем в список и сортируем
# result_list = list(result)
# result_list.sort()

# # Записываем в третий файл
# with open(file3, 'w', encoding='utf-8') as f3:
#     for word in result_list:
#         f3.write(word + '\n')

# with open("pidrila.txt", 'r', encoding="utf-8") as f_1:
#     text1 = f_1.read()
#     print(text1)

# with open("pidrila.txt", 'a', encoding="utf-8") as f_1:
#     f_1.write("Добавляем в конец файла\n")


import re

# file1 = input()
# file2 = input()

# with open(file1, 'r', encoding='utf-8') as f:
#     text = f.read()

# print("Исходный текс:")
# print(repr(text))
# print()

# lines = text.split('\n')

# clean_lines = []
# for line in lines:
#     line= re.sub(r'[ \t]+', ' ', line)
#     line = line.strip()
#     if line:
#         clean_lines.append(line)

# formatted = '\n'.join(clean_lines)

# with open(file2, 'w', encoding='utf-8') as f:
#     f.write(formatted)
    
#     print(formatted)

# with open('first.txt', 'r', encoding='utf-8') as f:
#     text = f.read()

# text = re.sub(r'[ \t]+', ' ', text)

# text = re.sub(r'\n+', '\n', text)

# lines = text.split('\n')
# lines = [line.strip() for line in lines]
# text = '\n'.join(lines)

# lines = text.split('\n')
# lines = [line.strip() for line in lines]
# text = '\n'.join(lines)

# lines = [line for line in lines if line]
# text = '\n'.join(lines)

# with open("second.txt", 'w', encoding="utf-8") as f:
#     f.write(text)

# print(text)



# Праильное решение задачи 
import re

# file_in = input()
# file_out = input()

# with open(file_in, encoding="UTF-8") as file_in:
#     text = file_in.read()

# while text.find("\t") + 1:
#     text = text.replace("\t", "")
# while text.find("  ") + 1:
#     text = text.replace("  ", " ")

# text = "\n".join(string.strip() for string in text.split("\n") if string)

# with open(file_out, "w", encoding="UTF-8") as file_out:
#     file_out.write(text)

# with open('example_1.txt', 'r', encoding='utf-8') as file:
#     text = file.read()
#     print("Старый текс:")
#     print(text)

# while text.find('\t') + 1:
#     text = text.replace('\t', '')

# text = '\n'.join(string.strip() for string in text.split('\n') if string)
# print('Новый текс:')
# print(text)
 

import json
import sys

# with open("scoring.json", encoding="UTF-8") as f:
#     groups = json.load(f)

# answers = []
# for line in sys.stdin:
#     answers.append(line.strip())

# total_score = 0
# answer_index = 0

# for group in groups:
#     points = group["points"]
#     tests = group["tests"]
#     tests_count = len(tests)
#     points_per_test = points / tests_count

#     correct_count = 0

#     for test in tests:
#         expected = test["pattern"]
#         user_answer = answers[answer_index]
#         answer_index += 1

#         if user_answer == expected:
#             correct_count += 1
    
#     group_score = points_per_test * correct_count
#     total_score += group_score

# print(int(total_score))


# with open("tests.json", encoding="UTF-8") as f:
#     groups = json.load(f)

# answer = []
# for line in sys.stdin:
#     answer.append(line.strip())
    
# total_score = 0
# answer_index = 0

# for group in groups:
#     points = group["points"]
#     tests = group["tests"]
#     tests_count = len(tests)
#     points_per_test = points / tests_count

#     correct_count = 0

#     for test in tests:
#         expected = test["pattern"]
#         user_answer = answer[answer_index]
#         answer_index += 1

#         if user_answer == expected:
#             correct_count += 1

#     group_score = points_per_test * correct_count
#     total_score += group_score

# print(int(total_score))


data = [
    "650975472 591084323 629700 1504180 577023",
    "8460612246 42161437 29409368 58531725 5725268 2198001838",
    "796451 69358 7195510 975628465 9756641",
   " 44200289 126541 979391 93479581 291170 28987042 86139603"
]

even_lines = []
odd_lines = []
eq_lines = []

for line in data:
    numbers = line.split()
    # print(numbers)

    even_nums = []
    odd_nums = []
    eq_nums = []

    for num_str in numbers:
        even_count = 0
        odd_count = 0

        for digit in num_str:
            d = int(digit)
            if d % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
        
        if even_count > odd_count:
            even_nums.append(num_str)
          
        elif odd_count > even_count:
            odd_nums.append(num_str)
        else:
            eq_nums.append(num_str)
    
    even_lines.append(" ".join(even_nums))
    odd_lines.append(" ".join(odd_nums))
    eq_lines.append(" ".join(eq_nums))
print(even_lines)

print("Числа с преобладанием ЧЕТНЫХ цифр:")
for line in even_lines:
    print(line)

# print("\nЧисла с преобладанием НЕЧЕТНЫХ цифр:")
# for line in odd_lines:
#     print(line)

# print("\nЧисла с ОДИНАКОВЫМ количеством четных и нечетных:")
# for line in eq_lines:
#     print(line)
    



    
