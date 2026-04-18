# import matplotlib.pyplot as plt
# import pandas as pd
# import seaborn as sns

# # Данные для примера
# x = [1, 2, 3, 4, 5]
# y = [2, 4, 1, 3, 5]

# # Строим график
# plt.plot(x, y)
# plt.title("Мой первый график в VS Code")
# plt.show()

from pprint import pprint

# Как создать матрицу 3x3 из нулей так, чтобы изменение matrix[0][0] не затронуло другие строки?
#[
#    [0, 0, 0],
#    [0, 0, 0],
#    [0, 0, 0],
#]

matrix = [[0, 0, 0 ]] * 3
pprint(matrix)