import pandas as pd
import numpy as np

# # Создаём и сохраняем файл
# np.random.seed(42)
# df = pd.DataFrame({
#     'employee': [f'Person_{i}' for i in range(1, 101)],
#     'department': np.random.choice(['IT', 'Sales', 'HR', 'Marketing'], 100),
#     'salary': np.random.randint(40000, 120000, 100),
#     'experience': np.random.randint(0, 20, 100)
# })

# # Добавляем бонус (зависит от зарплаты и опыта)
# df['bonus'] = df['salary'] * 0.05 + df['experience'] * 500

# # Сохраняем
# df.to_excel('practice_data.xlsx', index=False)
# print("✅ 'practice_data.xlsx' создан! 100 строк данных.")

# # Анализ
# df = pd.read_excel('practice_data.xlsx')

# print("=== ОТЧЁТ ===")
# print(f"Всего сотрудников: {len(df)}")
# print(f"Средняя зарплата: ${df['salary'].mean():,.0f}")
# print(f"Средний бонус: ${df['bonus'].mean():,.0f}")

# print("\n=== ПО ОТДЕЛАМ ===")
# dept_stats = df.groupby('department').agg({
#     'salary': ['mean', 'min', 'max'],
#     'employee': 'count'
# })
# print(dept_stats)

# print("\n=== ТОП-5 ПО ЗАРПЛАТЕ ===")
# print(df.nlargest(5, 'salary')[['employee', 'department', 'salary', 'bonus']])

# import pandas as pd
# import numpy as np
# df = pd.DataFrame({'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
#                    'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
#                    'name': ['Murzik', 'Pushok', 'Kaa', 'Bobik', 'Strelka', 'Vaska', 'Kaa2', 'Murka', 'Graf', 'Muhtar'],
#                    'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
#                    'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']},
#                     index = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])
# age_between = [2, 4]

# low, high = age_between[0], age_between[1]
# result = df[(df["age"] >= low) & (df['age'] <= high)]
# print(result)


import pandas as pd

# # Сначала создадим данные и сохраним в JSON
# data = {
#     'name': ['Alice', 'Bob', 'Charlie'],
#     'age': [25, 30, 35],
#     'city': ['NY', 'LA', 'Chicago']
# }

# df_original = pd.DataFrame(data)
# df_original.to_json('people.json', orient='records', force_ascii=False)

# print("✅ Файл people.json создан!")

# # Теперь читаем JSON файл
# df_loaded = pd.read_json('people.json')

# print("\nПрочитанный файл:")
# print(df_loaded)


df = pd.read_csv('train.csv')

mean_age = df['Age'].mean()
survived_count = df["Survived"].sum()
first_class_count = df[df['Pclass'] == 1].shape[0]
most_freq = df['Embarked'].mode()[0]
count = (df['Embarked'] == most_freq).sum()
df['Embarked'] = df['Embarked'].fillna(most_freq)

df['Embarked'] = df['Embarked'].fillna(most_freq)
print(most_freq, count)

# Проверяем, что пропусков больше нет
print(df['Embarked'].isnull().sum())  # 0

# Проверяем новое количество S (стало больше на 2 пропуска)
print(df['Embarked'].value_counts())
# S    646  (было 644 + 2 пропуска)
# C    168
# Q     77

average_ticket = df.groupby('Pclass')['Fare'].mean()
average_age_sex = df.groupby('Sex')['Age'].mean()
pp = df.groupby(['Sex', 'Pclass'])['Age'].size()
agg = df.groupby('Pclass')['Fare'].agg(['min', 'max', 'mean', 'median'])
pass_count = df.isnull().sum().sum()

print(df.shape)
print(mean_age)
print(survived_count)
print(first_class_count)
print(pass_count)
print("Date:", average_ticket)
print("Age:", average_age_sex)
print("PP:", pp)
print("agg:", agg)