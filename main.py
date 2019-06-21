#%%
import matplotlib
#%%
import pandas as pd
import numpy as np
data_file = 'CoffeeAndCode.csv'

data_frame = pd.read_csv(data_file, encoding="UTF-8")
data_frame['AgeRange'] = data_frame['AgeRange'].fillna('18 to 29')
data_frame.head()
# All table
#%%
ds = data_frame
print(ds.dtypes)
#%%
#%%
# Количество людей по возрасту
age_range = ds.groupby('AgeRange').count().CodingHours
print(age_range)
#%%
# Колисество людей по времени программирования в день
coding_hours = ds.groupby('CodingHours').count().CoffeeTime
print(coding_hours)
#%%
# Частота людей по возрасту
age_range_frequency = age_range.apply(lambda x: x/100)
print(age_range_frequency)
age_range_frequency = age_range_frequency.reindex([age_range_frequency.index[new_index] for new_index in [4, 0, 1, 2, 3]])
print(age_range_frequency)
#%%
# Частота людей по времени программирования
coding_hours_frequency = coding_hours.apply(lambda x: x/100)
#%%
import matplotlib.pyplot as plt
figure, axis = plt.subplots()
position = [pos for pos in range(1, 11)]
rects = axis.bar(position, coding_hours.CoffeeTime, 0.9, color="#7E1946")
axis.set_xlabel('Время программирования, ч')
axis.set_ylabel('Количество программистов')
axis.set_xticks(position)
axis.set_yticks([tick for tick in range(0, max(coding_hours.CoffeeTime)+1)])
plt.title('Диаграмма частот времени работы программистов')

def autolabel(rects, axis, xpos='center'):
    """
    Attach a text label above each bar in *rects*, displaying its height.

    *xpos* indicates which side to place the text w.r.t. the center of
    the bar. It can be one of the following {'center', 'right', 'left'}.
    """

    ha = {'center': 'center', 'right': 'left', 'left': 'right'}
    offset = {'center': 0, 'right': 1, 'left': -1}

    for rect in rects:
        height = rect.get_height()
        axis.annotate('{}'.format(height),
                      xy=(rect.get_x() + rect.get_width() / 2, height),
                      xytext=(offset[xpos]*3, 3),  # use 3 points offset
                      textcoords="offset points",  # in both directions
                      ha=ha[xpos], va='bottom',
                      )


autolabel(rects, axis)
figure.tight_layout()
plt.show()
#%%
age_range['CoffeeTime'].sort_values()[::-1].plot(kind='bar')
plt.title('Диаграмма частот распределения возраста программистов')
plt.xlabel('Возраст программистов')
plt.show()
#%%
coding_hours_frequency['CoffeeTime'].plot(kind='bar')
plt.title('Диаграмма частот времени работы программистов')
plt.xlabel('Время программирования, ч')
plt.show()
#%%
empirical_coding_hours = pd.DataFrame({"CodingHours": [coding_hours_frequency[:limit]['CoffeeTime'].sum() for limit in range(0, 11)]})
#%%
figure, axis = plt.subplots()
position = [pos for pos in range(0, 11)]
values = [round(value * 100) / 100 for value in empirical_coding_hours['CodingHours']]
rects = axis.bar(position, values, 0.9, color="#F18F01")
axis.set_xlabel('Время программирования, ч')
axis.set_xticks(position)
autolabel(rects, axis)
figure.tight_layout()
plt.show()
#%%
empirical_age_range = pd.DataFrame({"AgeRange": [round(age_range_frequency[:limit].sum() * 100) / 100 for limit in range(1, 6)]})
figure, axis = plt.subplots()
position = [pos for pos in range(5)]
rects = axis.bar(position, empirical_age_range['AgeRange'], 0.9, color="#60D394")
axis.set_xlabel('Возраст')
axis.set_xticks(position)


def print_headers():
    plot_text = list(age_range_frequency.index)
    ha = {'center': 'center', 'right': 'left', 'left': 'right'}
    offset = {'center': 0, 'right': 1, 'left': -1}

    for rect in rects:
        height = rect.get_height()
        axis.annotate('{column_name}({height})'.format(column_name=plot_text.pop(0), height=height),
                      xy=(rect.get_x() + rect.get_width() / 2, height),
                      xytext=(offset['center'] * 3, 3),  # use 3 points offset
                      textcoords="offset points",  # in both directions
                      ha=ha['center'], va='bottom'
                      )


print_headers()

figure.tight_layout()
plt.show()
#%%
print('Время программирования:')
print('Дисперсия: ', ds.CodingHours.var())
print('Стандартное отклонение: ', ds.CodingHours.std())
print('Мат. ожидание: ', ds.CodingHours.mean())
print('Среднее значение: ', ds.CodingHours.sum()/ds.CodingHours.count())
print('Соотношение мат. ожидания и дисперсии: ', ds.CodingHours.mean()/ds.CodingHours.var())
print('Среднее значение: ', ds.CodingHours.sum()/ds.CodingHours.count())
print('Мода: ', ds.CodingHours.mode().values[0])
print('Медиана: ', ds.CodingHours.median())
print('Ассиметрия: ', ds.CodingHours.skew())
print('Эксцесс: ', ds.CodingHours.kurtosis())
#%%
print('Количество выпитых кружек кофе в день:')
print('Дисперсия: ', ds.CoffeeCupsPerDay.var())
print('Стандартное отклонение: ', ds.CoffeeCupsPerDay.std())
print('Мат. ожидание: ', ds.CoffeeCupsPerDay.mean())
print('Среднее значение', ds.CoffeeCupsPerDay.sum()/ds.CoffeeCupsPerDay.count())
print('Соотношение мат. ожидания и дисперсии: ', ds.CoffeeCupsPerDay.mean()/ds.CoffeeCupsPerDay.var())
print('Среднее значение: ', ds.CoffeeCupsPerDay.sum()/ds.CoffeeCupsPerDay.count())
print('Мода: ', ds.CoffeeCupsPerDay.mode().values[0])
print('Медиана: ', ds.CoffeeCupsPerDay.median())
print('Ассиметрия: ', ds.CoffeeCupsPerDay.skew())
print('Эксцесс: ', ds.CoffeeCupsPerDay.kurtosis())

