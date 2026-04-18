# numbers = [2, 6, 3, 14, 10, 4, 11, 16, 12, 5, 4, 16, 1, 0, 8, 16, 10, 10, 8, 5, 1, 11, 10, 
#            10, 12, 0, 0, 6, 14, 8, 2, 12, 14, 5, 6, 12, 1, 2, 
#            10, 14, 9, 1, 15, 1, 2, 14, 16, 6, 7, 5
#         ]

# print(len(numbers))
# print(numbers[-1])
# print(numbers[::-1])
# if 5 and 17 in numbers:
#     print("YES")
# else:
#     print("NO")
# print(numbers[1:-1])

# l = []
# n = int(input())

# for i in range(1, n + 1):
#     if n % i == 0:
#         l.append(i)
    
# print(l)
# n = 25
# result = ([i for i in range(1, n + 1) if n % i == 0])
# print(result)

# count = 0
# l = []
# n = int(input())

# for i in range(n):
#     n2 = int(input())
#     count += n2
#     l.append(count)
#     count = n2

# print(l[1:])

# n = int(input())          # количество строк
# lines = []
# for _ in range(n):
#     lines.append(input()) # считываем строки
# k = int(input())          # номер символа

# result = []
# for s in lines:
#     if len(s) >= k:
#         result.append(s[k-1])   # индекс k-1, т.к. нумерация с 0

# print(''.join(result))

# n = int(input())
# l = []

# for i in range(n):
#     k = input()
#     l.extend(k)

# print(l)

# class Circle:
#     def __init__(self, radius):
#         self._radius = radius
    
#     @property
#     def area(self):
#         return 3.14159 * self._radius ** 2
    
# # Создаём круг с радиусом 5
# my_circle = Circle(5)

# # Обращаемся к area как к атрибуту (без скобок!)
# print(my_circle.area)  # 3.14159 * 25 = 78.53975

# n = int(input())
# result = []

# for i in range(n, n ** 2 + 1):
#     if i % 2 != 0:
#         result.append(i)

    

# print(result)

# def comp(array1, array2):
#     # Если хоть один None — сразу False
#     if array1 is None or array2 is None:
#         return False
    
#     # Если длины разные — точно False
#     if len(array1) != len(array2):
#         return False
    
#     # Квадраты первого массива (сортируем)
#     squares = sorted([x * x for x in array1])
#     # Сортируем второй массив
#     sorted_array2 = sorted(array2)
    
#     # Сравниваем
#     return squares == sorted_array2

# print(comp([2, 3, 4], [4, 9, 16]))

# text_1 = [['Goodbye'], {'Great': 'Job'}]
# text = ['Hello', 'Goodbye', 'Hello Again']
# result = []
# new_text = text_1[::2]
# result.append(new_text)
# print(new_text)

# strings = ["hello", "world", "madam", "python"]
# strings_1 = ["level", "refer", "code", "12321"]

# result = []

# for word in strings:
#     if word != word[::-1]:
#          line = (word, word[::-1])
#          result.append(line)
#     else:
#         result.append(word)

# print(result)

# resut_1 = [(word, word[::-1]) if word != word[::-1] else word for word in strings]
# print(resut_1)
    
# def count(s):
#     word_count = {}
#     for word in s:
#         word_count.setdefault(word, 0)
#         word_count[word] += 1
#     return word_count

# print(count('aba')) #{'a': 2, 'b': 1}))
# print(count('')) #{})
# print(count('aa')) #{'a' : 2})
# print(count('aabb')) #{'b' : 2, 'a' : 2})

# players = [("Alice", 10), ("Bob", 15), ("Charlie", 20), ("Dave", 25)]
# max_difference = 6
# new_players = ""

# for i in players:
#     print(i[1])
#     if i[1] <= max_difference:
#         new_players += i[0]
#         print(new_players)


m = int(input())
p = int(input())
n = int(input())

for i in range(n):
    print(f"{i + 1} {m}")
    m = m  + m * p / 100
    

