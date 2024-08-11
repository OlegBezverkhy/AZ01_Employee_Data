import pandas as pd

data_file = 'employee_data.csv'
head_string = 5

df = pd.read_csv(data_file)
print(f'Первые 5 строк данных из файла {data_file} :')
print(df.head(head_string))
print(f'Информация о данных в файле {data_file} :')
print((df.info))
print(f'Статистическое описание файла {data_file} :')
print(df.describe())
