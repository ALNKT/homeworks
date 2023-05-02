# Задача 1.1.

# Есть строка с перечислением песен

my_favorite_songs = 'Waste a Moment, Staying\' Alive, A Sorta Fairytale, Start Me Up, New Salvation'

# Выведите на консоль с помощью индексации строки, последовательно: первый трек, последний, второй, второй с конца
# Нельзя переопределять my_favorite_songs и запятая не должна выводиться.


first_track = my_favorite_songs[:14]
last_track = my_favorite_songs[-13:]
second_track = my_favorite_songs[16:30]
second_from_end_track = my_favorite_songs[-26:-15]

print(first_track, last_track, second_track, second_from_end_track, sep='; ')
