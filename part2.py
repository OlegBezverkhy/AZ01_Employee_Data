import pandas as pd

data_file = 'dz.csv'
df = pd.read_csv(data_file)

# Получаем представление о данных по первым 5 строкам
print('Первые пять строк таблицы:')
print(df.head(5))
print('Средняя заработная плата(Salary) по городам')
print(df.groupby('City')['Salary'].mean())
