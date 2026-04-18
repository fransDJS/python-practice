import pandas as pd
import numpy as np

# Создаём и сохраняем файл
np.random.seed(42)
df = pd.DataFrame({
    'employee': [f'Person_{i}' for i in range(1, 101)],
    'department': np.random.choice(['IT', 'Sales', 'HR', 'Marketing'], 100),
    'salary': np.random.randint(40000, 120000, 100),
    'experience': np.random.randint(0, 20, 100)
})

# Добавляем бонус (зависит от зарплаты и опыта)
df['bonus'] = df['salary'] * 0.05 + df['experience'] * 500

# Сохраняем
df.to_excel('practice_data.xlsx', index=False)
print("✅ 'practice_data.xlsx' создан! 100 строк данных.")

# Анализ
df = pd.read_excel('practice_data.xlsx')

print("=== ОТЧЁТ ===")
print(f"Всего сотрудников: {len(df)}")
print(f"Средняя зарплата: ${df['salary'].mean():,.0f}")
print(f"Средний бонус: ${df['bonus'].mean():,.0f}")

print("\n=== ПО ОТДЕЛАМ ===")
dept_stats = df.groupby('department').agg({
    'salary': ['mean', 'min', 'max'],
    'employee': 'count'
})
print(dept_stats)

print("\n=== ТОП-5 ПО ЗАРПЛАТЕ ===")
print(df.nlargest(5, 'salary')[['employee', 'department', 'salary', 'bonus']])