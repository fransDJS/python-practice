# sp = []
# n = int(input())

# for i in range(n):
#     text = input()
#     sp.append(text)

# target = input()

# for x in sp:
#     if target.lower() in x.lower():
#         print("Ответ:", x)
#     else:
#         continue
    

# s = [input() for _ in range(int(input()))]
# word = input().lower()
# print(*[i for i in s if word in i.lower()], sep='\n')

#Ввод:
# 5 - кол-во строк
# Язык Python прекрасен
# C# - отличный язык программирования
# Stepik - отличная платформа
# BEEGEEK FOREVER!
# язык Python появился 20 февраля 1991
# язык - поисковый запрос

#Вывод:
# Язык Python прекрасен
# C# - отличный язык программирования
# язык Python появился 20 февраля 1991

# temps = [20, 25, 100, 22, 120, 18]
# for i, temp in enumerate(temps, start=1):
#     if temp > 50:
#         print(f"Внимание! Опасная температура {temp} в позиции {i}")

# images = ["cat.jpg", "dog.jpg", "bird.jpg"]
# new_images = []

# for i, name in enumerate(images):
#     # Формируем новую строку и сохраняем её в переменную
#     new_name = f"{i}_{name}"
    
#     # Добавляем в список именно НОВОЕ имя
#     new_images.append(new_name)
    
#     print(new_name)

# # Проверяем результат
# print("Весь список:", new_images)

# items = ["яблоко", "банан", "вишня", "груша", "дыня"]

# for i, item in enumerate(items):
#     if i % 2 == 0:
#         print(item)


# import pandas as pd

# df = pd.DataFrame({'name': ['Ivan', 'Daria', 'Oleg']})

# # Вместо цикла for мы пишем:
# df['initial'] = df['name'].apply(lambda x: x[0])

# print(df)

# n = int(input())
# a = []
# b = []

# for i in range(n):
#     text = input()
#     a.append(text)

# k = int(input())

# for j in range(k):
#     text_search = input()
#     b.append(text_search)

# for h in a:
#     count = 0
#     for g in b:
#         if g.lower() in h.lower():
#             count += 1

#     if count == len(b):
#         print(h)

# list_comprehension = [i for i in range(3)]
# set_comprehension = {i for i in range(3)}
# dict_comprehension = {i: i ** 2 for i in range(3)}
# generator_expression = (i for i in range(3))
# print(type()) # 

# print((1,) is (1,)) #True

data = (1, (2, 3), 4) # Как распаковать одной строкой?
a, *b, c = data

print(a) # 1
print(b) # 2
print(c) # 3 
# print(d) # 4
