# Задача 40: Работать с файлом california_housing_train.csv, который находится в папке sample_data.
# Определить среднюю стоимость дома, где кол-во людей от 0 до 500 (population).

import pandas as pd
df = pd.read_csv('sample_data/california_housing_train.csv')
df[df['population'] > 500]['median_house_value'].median()

# Задача 42: Узнать какая максимальная households в зоне минимального значения population.

import pandas as pd
df = pd.read_csv('sample_data/california_housing_train.csv')
min_pop = df['population'].min()
mins_pops = df[df['population'] == min_pop]
max_households = mins_pops['households'].max()
print(max_households)