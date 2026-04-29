import pandas as pd
import glob

# Путь к папке с файлами XLSX
folder_path = "C:/Practic Python/wb_data/"

# Выходной файл (сохраним в правильной кодировке)
output_file = "wb_sales_daily.csv"

# Все xlsx файлы
files = glob.glob(folder_path + "*.xlsx")
files.sort()

print(f"Найдено файлов: {len(files)}")

all_data = []

for file in files:
    print(f"Обрабатываю: {file}")
    
    df = pd.read_excel(file)
    
    cols = ['Дата продажи', 'Код номенклатуры', 'Тип документа', 'Кол-во', 'Цена розничная']
    
    if not all(c in df.columns for c in cols):
        print(f"  Пропускаю: нет нужных колонок")
        continue
    
    df = df[cols]
    
    # Продажи
    sales = df[df['Тип документа'] == 'Продажа'].groupby(
        ['Дата продажи', 'Код номенклатуры']
    ).agg(
        sales=('Кол-во', 'sum'),
        avg_price=('Цена розничная', 'mean')
    ).reset_index()
    
    # Возвраты
    returns = df[df['Тип документа'] == 'Возврат'].groupby(
        ['Дата продажи', 'Код номенклатуры']
    )['Кол-во'].sum().reset_index(name='returns')
    
    # Объединяем
    daily = sales.merge(returns, on=['Дата продажи', 'Код номенклатуры'], how='left')
    daily['returns'] = daily['returns'].fillna(0)
    daily['net_sales'] = daily['sales'] - daily['returns']
    
    all_data.append(daily)

# Склеиваем всё
final_df = pd.concat(all_data, ignore_index=True)

# Агрегация
final_df = final_df.groupby(['Дата продажи', 'Код номенклатуры']).agg({
    'sales': 'sum',
    'returns': 'sum',
    'net_sales': 'sum',
    'avg_price': 'mean'
}).reset_index()

# 🧹 ФИЛЬТРАЦИЯ (убираем мусор)
final_df = final_df[final_df['Код номенклатуры'] != 0]  # убираем код 0
final_df = final_df[final_df['sales'] > 0]  # убираем строки без продаж (оставляем только дни с продажами)

# Сортируем
final_df = final_df.sort_values(['Дата продажи', 'Код номенклатуры'])

# 💾 Сохраняем с правильной кодировкой UTF-8 (чтобы русские буквы не ломались)
final_df.to_csv(output_file, index=False, encoding='utf-8-sig')

print(f"✅ Готово! Сохранено в {output_file}")
print(f"Всего строк: {len(final_df)}")
print(f"Диапазон дат: {final_df['Дата продажи'].min()} - {final_df['Дата продажи'].max()}")