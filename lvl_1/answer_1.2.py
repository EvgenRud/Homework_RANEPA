# Решение задачи 1.2.

# Пункт A. 
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут

import random

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

my_favorite_songs = random.sample(my_favorite_songs, 3)

my_favorite_songs = list(my_favorite_songs)

songs_time = my_favorite_songs[0][1] + my_favorite_songs[1][1]  + my_favorite_songs[2][1]

print(f'Три песни звучат {songs_time:.2f} минут')


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

# Сортируем словарь по значениям и получаем список

my_sorted = sorted(my_favorite_songs_dict.values())

# Кладём 3 рандомные значения в список

my_sorted = random.sample(my_sorted, 3)

# Складываем песни (по индексам)

songs_time_dict = my_sorted[0] + my_sorted[1] + my_sorted[2]

print(f'Три песни звучат {songs_time_dict:.2f} минут')



# Дополнительно для пунктов A и B
# Пункт C.
# Сгенерируйте случайные песни с помощью модуля random
# import random

# Дополнительно 
# Пункт D.
# Переведите минуты и секунды в формат времени. Используйте модуль datetime 

