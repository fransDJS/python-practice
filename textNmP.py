import numpy as np

# np.array(object, dtype=None, copy=True, order='K', subok=False, ndmin=0)

# arr1 = np.array([1, 2, 3])
# print(arr1)  # [1 2 3]

# arr2 = np.array((4, 5, 6))
# print(arr2) # [4 5 6]

# <==============================================>
# np.zeros(shape, dtype=float, order='C') 
# zeros_arr = np.zeros((2, 3)) 
# print(zeros_arr) #выводит:
# [[0. 0. 0.]
#  [0. 0. 0.]]

# <==============================================>
# np.ones(shape, dtype=None, order='C')
# ones_arr = np.ones((3, 2))
# print(ones_arr) Код выводит: 
#               [[1. 1.]
#               [1. 1.]
#               [1. 1.]]

# <==============================================>
# np.empty(shape, dtype=float, order='C')
# empty_arr = np.empty((2, 2))
# print(empty_arr)

# <==============================================>
# np.arange(start, stop, step, dtype=None)
# arange_arr = np.arange(0, 20, 5)
# print(arange_arr) #Код выводит: [ 0  5 10 15]

# <==============================================>
# np.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)
# linspace_arr = np.linspace(3, 9, num=3)
# print(linspace_arr) 
# Код выводит: [3. 6. 9.]

# <==============================================>
# np.full(shape, fill_value, dtype=None, order='C')
# full_arr = np.full((4, 3), 5)
# print(full_arr)

# arr = np.array(np.arange(0, 5))
# print(arr)


# <==============================================>
# arr = np.array([[1, 2, 3], [4, 5, 6]])
# print(arr.ndim)  
# #Код выводит: 2

# <==============================================>
# arr = np.array([[1, 2, 3], [4, 5, 6]])
# print(arr.shape)  
# Код  выводит: (2, 3)

# <==============================================>
# matrix = np.eye(3)
# print(matrix)

# <==============================================>
# random_array = np.random.rand(2, 3)
# print(random_array)

# <==============================================>
# random_integers = np.random.randint(1, 55, size=(5, 5))
# print(random_integers)


#Задачи
# arr = np.array([1.2, 2.5, 3.8, 4.1])
# print(f"Исходный массив: {arr}")
# print(f"Тип данных: {arr.dtype}")
# arr_int = arr.astype(np.int64)
# print(f"Массив округленных целых чисел: {arr_int}")
# print(f"Тип данных: {arr_int.dtype}")


# import numpy as np

# arr1 = np.full((3, 3), 2)
# arr2 = arr1 ** 3
# print(arr1 + arr2)

# arr1 = np.arange(1, 10).reshape(3, 3)

# print(arr1**2)

# matrix_a = np.array([[10, 20, 30],
#                      [80, 100, 120],
#                      [210, 240, 270]])

# matrix_b = np.array([[5, 5, 5],
#                      [10, 10, 10],
#                      [30, 30, 30]])

# result = matrix_a / matrix_b
# print(result * matrix_b)

import numpy as np

# matrix_a = np.array([
#     [10, 10, 10],
#     [80, 50, 40],
#     [210, 120, 90],
# ])
# matrix_b = np.arange(1, 4)

# matrix_c = matrix_a * matrix_b
# print(matrix_c)

# arange_arr = np.arange(1, 4)
# print(arange_arr)

# import numpy as np 

# matrix_a = np.arange(1, 10).reshape(3,3)
# matrix_b = np.array([[10],[20],[30]])

# print(matrix_a)


# arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# print(arr[::2]) #[0 2 4 6 8]

# matrix = np.array([[1, 2, 3],
#                    [4, 5, 6],
#                    [7, 8, 9]])

# print(matrix[1, :]) #[4 5 6]
# print(matrix[:, 1]) #[2 5 8]
# print(matrix[:2, :2])  #[[1 2]
#                         #[4 5]]

# tensor = np.array([
#     [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
#     [[10, 11, 12], [13, 14, 15], [16, 17, 18]],
#     [[19, 20, 21], [22, 23, 24], [25, 26, 27]]
# ])

# print(tensor[1, :, :])
# print("=" * 20)
# print(tensor[:, :, 1])
# print("=" * 20)
# print(tensor[:2, :2, :2])

# arr = np.array([0,1,2,3,4,5])
# print(arr[::-1])

# import numpy as np
# arr = np.array([[1, 2, 3],
#                 [4, 5, 6],
#                 [7, 8, 9]])

# print(f"Вторая строка:{arr[1]} \nТретий столбец:{arr[:, 2]}")

# import numpy as np
# arr = np.array([[[1, 2],
#                  [3, 4]],
#                 [[5, 6],
#                  [7, 8]],
#                 [[9, 10],
#                  [11, 12]]])

# print(f"Первый слой:\n{arr[0]}")
# print(f"Вторая строка первого слоя::{arr[0, 1]}")
# print(f"Первый столбец первого слоя:{arr[0, :, 0]}")

# import numpy as np
# arr = np.array([[1, 2, 3, 4],
#                 [5, 6, 7, 8],
#                 [9, 10, 11, 12],
#                 [13, 14, 15, 16]])

# print(arr[::2])


# arr = np.array([[1, 2, 3, 4],
#                    [5, 6, 7, 8],
#                    [9, 10, 11, 12],
#                    [13, 14, 15, 16]])

# print(f"Матрица из второй и третьей строк, а также третьего и четвёртого столбцов:\n{arr[1:3, 2:4]}")

# import numpy as np
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# print(f"Элементы в обратном порядке с шагом 2:\n{arr[::-2,]}")

# arr = np.array([[[1, 2, 3],
#                  [4, 5, 6],
#                  [7, 8, 9]],

#                 [[10, 11, 12],
#                  [13, 14, 15],
#                  [16, 17, 18]],

#                 [[19, 20, 21],
#                  [22, 23, 24],
#                  [25, 26, 27]]])

# print(f"Все первые столбцы:\n{arr[:, :, 0]}")
# print()
# print(f"Все вторые столбцы:\n{arr[:, :, 1]}")

# import numpy as np

# # Представь, что это цены на товары за год
# prices = np.array([100, 150, 200, 250, 300])

# # Логарифмическая доходность (финансы)
# log_returns = np.log(prices[1:] / prices[:-1])
# print("Логарифмическая доходность:", log_returns)

# # Стандартизация (для машинного обучения)
# normalized = (prices - np.mean(prices)) / np.std(prices)
# print("Стандартизованные цены:", normalized)

# # Пример 1
# a = np.array([10, 20, 30])
# b = np.array([1, 2, 3])
# result = np.where(a > 15, a, b)
# print(result)
# # a > 15: [False, True, True]
# # результат: [1, 20, 30]

# # Пример 2
# scores = np.array([45, 78, 92, 38])
# result = np.where(scores >= 60, "Зачёт", "Незачёт")
# print(result)
# # результат: ['Незачёт' 'Зачёт' 'Зачёт' 'Незачёт']


# # Пример 3
# arr = np.array([-3, -1, 0, 2, 5])
# result = np.where(arr < 0, arr * -1, arr)
# print(result)
# # отрицательные → положительные (модуль)
# # результат: [3, 1, 0, 2, 5]


import numpy as np

# # 1. Создай матрицу 100x5 со случайными числами
# X = np.random.randn(100, 5)

# # 2. Посмотри форму
# print(X.shape)  # (100, 5)

# # 3. Возьми первые 10 строк, столбцы 0,2,4
# X_subset = X[:10, [0, 2, 4]]

# # 4. Посчитай среднее и std для каждого столбца
# means = np.mean(X, axis=0)
# stds = np.std(X, axis=0)

# # 5. Нормализуй данные (стандартизация)
# X_norm = (X - means) / stds

# # 6. Найди строки, где значение в столбце 0 > 1
# X_filtered = X[X[:, 0] > 1]

# # 7. Замени все отрицательные значения на 0
# X_clean = np.where(X < 0, 0, X)

# # 8. Создай целевую переменную: 1 если среднее по строке > 0
# y = (np.mean(X, axis=1) > 0).astype(int)

# print("Готов к ML!")

# import numpy as np

# # Допустим, это данные о студентах:
# # строки — студенты, столбцы — оценки по предметам
# scores = np.array([[85, 90, 78],
#                    [62, 75, 88],
#                    [95, 92, 89],
#                    [45, 60, 55]])

# # Средняя оценка КАЖДОГО СТУДЕНТА (по строкам)
# student_avg = np.mean(scores, axis=1)
# print("Средняя оценка каждого студента:", student_avg)
# # [84.33, 75, 92, 53.33]

# # Средняя оценка по КАЖДОМУ ПРЕДМЕТУ (по столбцам)
# subject_avg = np.mean(scores, axis=0)
# print("Средняя оценка по предметам:", subject_avg)
# # [71.75, 79.25, 77.5]

# # Нормализация (стандартизация) — вычитаем среднее каждого столбца
# # (очень частая операция в ML!)
# normalized = scores - np.mean(scores, axis=0)
# print("Нормализованные данные:")
# print(normalized)

# import pandas as pd

# heros = pd.Series([100, 200, 300], index=["Такеда", "Хонда", "Ода"])
# print(heros)

# import numpy as np

# # Доходности 3 активов за 5 дней
# returns = np.array([
#     [0.05, 0.02, 0.01],
#     [0.04, 0.03, 0.02],
#     [0.06, 0.01, 0.03],
#     [0.03, 0.04, 0.02],
#     [0.05, 0.02, 0.04]
# ])

# # Ковариационная матрица (риски и корреляции)
# cov_matrix = np.cov(returns.T)
# print("Ковариационная матрица:")
# print(cov_matrix)

# # Определитель (близок к 0 → активы сильно связаны)
# det_cov = np.linalg.det(cov_matrix)
# print(f"Определитель: {det_cov:.6f}")

# # Оптимальные веса портфеля (пример)
# weights = np.linalg.solve(cov_matrix, np.ones(3))
# weights = weights / np.sum(weights)
# print(f"Оптимальные веса: {weights}")


import numpy as np

# Матрица признаков (3 объекта, у каждого по 2 признака: например, доход и кредитный рейтинг)
X = np.array([
    [100, 700], 
    [50, 650], 
    [120, 800]
])

# Веса модели (насколько важен каждый признак)
weights = np.array([0.5, 0.1])
bias = -10

# Матричное умножение: X @ weights + bias
predictions = np.dot(X, weights) + bias

print(f"Прогнозы модели: {predictions}")
# Каждое число здесь — это прогноз для конкретного клиента/актива


import numpy as np

# Реальные цены акций
y_true = np.array([100, 150, 200])

# То, что нагадала наша модель
y_pred = np.array([90, 160, 210])

# Считаем MSE вручную через NumPy
error = y_true - y_pred
mse = np.mean(error**2)

print(f"Ошибка MSE: {mse}") 
# (10^2 + 10^2 + 10^2) / 3 = 100.0

import numpy as np

a = np.array([2, -1.3])
b = np.array([4, -2.6])

# Длины (нормы)
norm_a = np.linalg.norm(a)
norm_b = np.linalg.norm(b)

print(f"Длина a: {norm_a:.3f}")
print(f"Длина b: {norm_b:.3f}")

# Проверка на сонаправленность через косинусное расстояние
# Если косинус угла между ними = 1, они сонаправлены
cos_sim = np.dot(a, b) / (norm_a * norm_b)
print(f"Косинус угла: {cos_sim}") # Будет 1.0

a = np.array([2, 1, 0])
b = np.array([1, 3, 2])
cross = np.cross(a, b)
length = np.linalg.norm(cross)
print(length)
