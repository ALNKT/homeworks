# Задача 1.2.
import random
import datetime

# Пункт A. 
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]

songs = random.sample(my_favorite_songs, 3)

time_of_songs = [str(i_song[1]).split('.') for i_song in songs]

tmp_time = datetime.timedelta(minutes=0)

for i_time in time_of_songs:
    i_time = [int(i) for i in i_time]
    tmp_time += datetime.timedelta(hours=0, minutes=i_time[0], seconds=i_time[1])

print(f'Три песни звучат {tmp_time} мин.')


# Пункт B. 
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.

my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}

time_of_songs = random.sample(list(my_favorite_songs_dict.values()), 3)
time_of_songs = [str(i_song).split('.') for i_song in time_of_songs]

tmp_time = datetime.timedelta(minutes=0)

for i_time in time_of_songs:
    i_time = [int(i) for i in i_time]
    tmp_time += datetime.timedelta(hours=0, minutes=i_time[0], seconds=i_time[1])

print(f'Три песни звучат {tmp_time} мин.')


# Дополнительно для пунктов A и B
# Пункт C.
# Сгенерируйте случайные песни с помощью модуля random
# import random

# Дополнительно 
# Пункт D.
# Переведите минуты и секунды в формат времени. Используйте модуль datetime 
