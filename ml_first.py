# 1. Импортируем библиотеки
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

# 2. Создаем простые данные (в реальности ты будешь загружать из файла)
# Признаки: площадь, этаж, количество комнат, год постройки
data = {
    'площадь': [45, 60, 35, 80, 50, 42, 70, 55, 63, 47],
    'этаж': [3, 5, 2, 7, 4, 2, 9, 5, 4, 3],
    'комнаты': [2, 3, 1, 4, 2, 2, 3, 3, 3, 2],
    'год': [2005, 2010, 1995, 2020, 2000, 1998, 2015, 2008, 2012, 2003],
    'цена': [6500000, 8500000, 4800000, 12000000, 7200000, 5900000, 9500000, 7800000, 8900000, 6800000]
}

# 3. Превращаем в DataFrame
df = pd.DataFrame(data)
print("Данные загружены:")
print(df.head())

# 4. Отделяем признаки (X) от цели (y)
X = df.drop('цена', axis=1)  # все колонки кроме цены
y = df['цена']               # только цена

# 5. Делим на обучающую и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 6. Создаем и обучаем модель
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 7. Делаем предсказания на тестовых данных
predictions = model.predict(X_test)

# 8. Сравниваем с реальными значениями
print("\nРеальные цены:", y_test.values)
print("Предсказанные цены:", [int(x) for x in predictions])

# 9. Считаем ошибку
mae = mean_absolute_error(y_test, predictions)
print(f"\nСредняя ошибка предсказания: {mae:.0f} рублей")

# 10. Проверяем на новой квартире (например, 52 м², 4 этаж, 2 комнаты, 2018 год)
new_apartment = pd.DataFrame({
    'площадь': [52],
    'этаж': [4],
    'комнаты': [2],
    'год': [2018]
})

price = model.predict(new_apartment)
print(f"\nПредсказанная цена новой квартиры: {int(price[0])} рублей")

import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.plot(range(len(y_test)), y_test.values, 'ro-', label='Реальные цены')
plt.plot(range(len(predictions)), predictions, 'bo-', label='Предсказанные цены')
plt.xlabel('Номер квартиры')
plt.ylabel('Цена (рубли)')
plt.title('Сравнение реальных и предсказанных цен')
plt.legend()
plt.grid(True)
plt.show()