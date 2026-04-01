# ============================================
# ТИТАНИК: ПРЕДСКАЗАНИЕ ВЫЖИВАНИЯ
# ============================================

# 1. ИМПОРТ БИБЛИОТЕК
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import warnings
import plotly.express as px
warnings.filterwarnings('ignore')

# 2. СОЗДАЕМ ДАННЫЕ ВРУЧНУЮ (чтобы не скачивать файлы)
# Это 10 пассажиров Титаника
data = {
    'pclass': [1, 3, 1, 3, 3, 2, 3, 1, 3, 2],        # класс билета (1 - первый, 3 - третий)
    'sex': ['male', 'female', 'female', 'male', 'male', 'female', 'male', 'male', 'female', 'female'],  # пол
    'age': [29, 35, 18, 26, 32, 24, 19, 42, 22, 30],  # возраст
    'sibsp': [0, 1, 0, 0, 0, 1, 0, 1, 0, 0],         # кол-во братьев/сестер/супругов на борту
    'parch': [0, 0, 0, 1, 0, 0, 2, 0, 0, 0],         # кол-во родителей/детей на борту
    'fare': [80, 12, 53, 8, 7, 20, 16, 73, 10, 18],   # цена билета
    'embarked': ['C', 'S', 'C', 'S', 'S', 'Q', 'S', 'C', 'S', 'S'],  # порт посадки (C=Cherbourg, S=Southampton, Q=Queenstown)
    'survived': [1, 0, 1, 0, 0, 1, 0, 1, 1, 0]       # выжил? (1 - да, 0 - нет) - ЭТО НАША ЦЕЛЬ
}

# 3. ПРЕВРАЩАЕМ В ТАБЛИЦУ (DataFrame)
df = pd.DataFrame(data)
# Сохраняем копию с текстовыми полями для графиков
df_original = df.copy()
df_original['sex_original'] = data['sex']  # восстанавливаем исходный пол
print("=" * 50)
print("ПЕРВЫЕ 5 СТРОК ДАННЫХ:")
print("=" * 50)
print(df.head())
print()

# 4. ПРЕОБРАЗУЕМ ТЕКСТ В ЧИСЛА (модели понимают только числа)
# Пол: male -> 0, female -> 1
df['sex'] = df['sex'].map({'male': 0, 'female': 1})

# Порт посадки: S -> 0, C -> 1, Q -> 2
df['embarked'] = df['embarked'].map({'S': 0, 'C': 1, 'Q': 2})

print("=" * 50)
print("ДАННЫЕ ПОСЛЕ ПРЕОБРАЗОВАНИЯ ТЕКСТА В ЧИСЛА:")
print("=" * 50)
print(df.head())
print()

# 5. ОТДЕЛЯЕМ ПРИЗНАКИ (X) ОТ ЦЕЛИ (y)
X = df.drop('survived', axis=1)  # все колонки кроме survived
y = df['survived']               # только survived

print("=" * 50)
print("ПРИЗНАКИ (X) - то, по чему учится модель:")
print("=" * 50)
print(X.head())
print()
print("=" * 50)
print("ЦЕЛЬ (y) - что предсказываем:")
print("=" * 50)
print(y.head())
print()

# 6. ДЕЛИМ НА ОБУЧАЮЩУЮ И ТЕСТОВУЮ ВЫБОРКИ
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

print("=" * 50)
print("РАЗМЕРЫ ВЫБОРОК:")
print("=" * 50)
print(f"Обучающих примеров: {len(X_train)}")
print(f"Тестовых примеров: {len(X_test)}")
print()

# 7. СОЗДАЕМ МОДЕЛЬ
# Вот здесь МОЖНО МЕНЯТЬ МОДЕЛЬ!
model = RandomForestClassifier(n_estimators=10, random_state=42)
# Другие варианты (раскомментируй, чтобы попробовать):
# model = LogisticRegression()  # логистическая регрессия
# model = KNeighborsClassifier() # метод ближайших соседей

print("=" * 50)
print(f"ИСПОЛЬЗУЕМАЯ МОДЕЛЬ: {type(model).__name__}")
print("=" * 50)

# 8. ОБУЧАЕМ МОДЕЛЬ
model.fit(X_train, y_train)

# 9. ДЕЛАЕМ ПРЕДСКАЗАНИЯ
predictions = model.predict(X_test)

# 10. ОЦЕНИВАЕМ ТОЧНОСТЬ
accuracy = accuracy_score(y_test, predictions)

print("\n" + "=" * 50)
print("РЕЗУЛЬТАТЫ:")
print("=" * 50)
print(f"Реальные значения:    {list(y_test)}")
print(f"Предсказанные значения: {list(predictions)}")
print(f"Точность модели: {accuracy:.2f} ({accuracy*100:.0f}%)")
print()

# 11. ПРОВЕРЯЕМ НА НОВОМ ПАССАЖИРЕ
# Создаем нового пассажира: первый класс, женщина, 25 лет, одна, без детей, дорогой билет, из Шербура
new_passenger = pd.DataFrame({
    'pclass': [1],
    'sex': [1],        # 1 = female
    'age': [25],
    'sibsp': [0],
    'parch': [0],
    'fare': [100],
    'embarked': [1]    # 1 = C (Cherbourg)
})

new_prediction = model.predict(new_passenger)
print("=" * 50)
print("ПРЕДСКАЗАНИЕ ДЛЯ НОВОГО ПАССАЖИРА:")
print("=" * 50)
print(f"Пассажир: 1 класс, женщина, 25 лет, билет 100$, из Шербура")
print(f"Модель предсказывает: {'ВЫЖИВЕТ' if new_prediction[0] == 1 else 'НЕ ВЫЖИВЕТ'}")
print()

# 12. СМОТРИМ, КАКИЕ ПРИЗНАКИ ВАЖНЫЕ (для RandomForest)
if type(model).__name__ == "RandomForestClassifier":
    feature_importance = pd.DataFrame({
        'feature': X.columns,
        'importance': model.feature_importances_
    }).sort_values('importance', ascending=False)
    
    print("=" * 50)
    print("ВАЖНОСТЬ ПРИЗНАКОВ (что больше всего влияет на выживание):")
    print("=" * 50)
    print(feature_importance)

# ============================================
# ВИЗУАЛИЗАЦИЯ (ГРАФИКИ)
# ============================================
import matplotlib.pyplot as plt
import seaborn as sns

# Настраиваем стиль графиков
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 8)

# 1. ГРАФИК ВЫЖИВАЕМОСТИ ПО ПОЛУ
plt.subplot(2, 2, 1)  # 2 строки, 2 колонки, первая позиция
sns.countplot(x='sex_original', hue='survived', data=df_original)
plt.title('Выживаемость по полу', fontsize=14)
plt.xlabel('Пол')
plt.ylabel('Количество')
plt.legend(['Не выжил', 'Выжил'], loc='upper right')
# Вместо 0/1 подписываем male/female
plt.xticks(ticks=[0, 1], labels=['Мужчины', 'Женщины'])

# 2. ГРАФИК ВЫЖИВАЕМОСТИ ПО КЛАССУ
plt.subplot(2, 2, 2)
sns.countplot(x='pclass', hue='survived', data=df)
plt.title('Выживаемость по классу билета', fontsize=14)
plt.xlabel('Класс')
plt.ylabel('Количество')
plt.legend(['Не выжил', 'Выжил'])
plt.xticks(ticks=[1, 2, 3], labels=['1-й класс', '2-й класс', '3-й класс'])

# 3. ВОЗРАСТНОЕ РАСПРЕДЕЛЕНИЕ
plt.subplot(2, 2, 3)
plt.hist([df[df['survived']==0]['age'], df[df['survived']==1]['age']], 
         bins=10, label=['Не выжили', 'Выжили'], alpha=0.7)
plt.title('Распределение возраста выживших и погибших', fontsize=14)
plt.xlabel('Возраст')
plt.ylabel('Количество')
plt.legend()

# 4. ЦЕНА БИЛЕТА VS ВЫЖИВАЕМОСТЬ
plt.subplot(2, 2, 4)
sns.boxplot(x='survived', y='fare', data=df)
plt.title('Цена билета у выживших и погибших', fontsize=14)
plt.xlabel('Выживание')
plt.ylabel('Цена билета')
plt.xticks(ticks=[0, 1], labels=['Погибли', 'Выжили'])

plt.tight_layout()  # чтобы графики не налезали друг на друга
plt.show()

# 5. ТЕПЛОВАЯ КАРТА КОРРЕЛЯЦИИ
plt.figure(figsize=(10, 8))
correlation = df.corr()
sns.heatmap(correlation, annot=True, cmap='coolwarm', center=0)
plt.title('Корреляция между признаками', fontsize=16)
plt.show()

# 6. СРАВНЕНИЕ РЕАЛЬНЫХ И ПРЕДСКАЗАННЫХ ЗНАЧЕНИЙ
# (для тестовой выборки)
plt.figure(figsize=(14, 5))

plt.subplot(1, 2, 1)
# Реальные значения
sns.countplot(x=y_test, color='skyblue', alpha=0.7)
plt.title('Реальные значения (тестовая выборка)', fontsize=14)
plt.xlabel('Выживание')
plt.ylabel('Количество')
plt.xticks(ticks=[0, 1], labels=['Погибли', 'Выжили'])

plt.subplot(1, 2, 2)
# Предсказанные значения
sns.countplot(x=predictions, color='salmon', alpha=0.7)
plt.title('Предсказания модели (тестовая выборка)', fontsize=14)
plt.xlabel('Выживание')
plt.ylabel('Количество')
plt.xticks(ticks=[0, 1], labels=['Погибли', 'Выжили'])

plt.tight_layout()
plt.show()

fig = px.bar(df_original, x='sex_original', color='survived', barmode='group')
fig.show()
plt.savefig('titanic_plot.png')