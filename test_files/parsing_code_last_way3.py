import csv
from time import sleep
import requests
from bs4 import BeautifulSoup
import random
import pandas as pd
import re

buffer = []
dataAll = []
links_genres = []
genres = []
t = 0                  # счётчик прохождения выполнения кода (для наглядности)

#   #   #   #   #   #    Create a base of all genres    #   #   #   #   #   #

url = f'https://kinobar.vip/'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
categories = soup.find('ul', class_='cats_menu').find_all('a')

# Цикл для извлечения из главной страницы полного перечня жанров предлагаемых сайтом фильмов
for cat in categories:
    stop = 5  # число фильмов, которое нужно отобрать по каждому жанру.
    data = []
    films0 = soup.find('div', id='dle-content').findAll('div', class_='main_news')   # To find out the variable 'capacity'
    capacity = len(films0[:])   # Число фильмо, представленных на каждой странице (без фильма дня на главной) = 14 фильмов.
    genre = cat.text                                # каждый жанр в формате строки кириллицей
    link_genre = cat.get('href').strip('/')         # каждый жанр в формате строки латиницей
    link_genre_l = link_genre.split()               # каждый жанр в формате списка латиницей
    links_genres += link_genre_l                    # Список жанров на латинице (все жанры)
    genre = genre.split(';')                        # каждый жанр в формате списка кириллицей
    genres += genre                                 # Список всех жанров на кириллице

# Цикл для извлечения общей инф-ции по фильмам из кол-ва страниц на единицу больше нежели необходимо
    for page in range(0, round(stop / capacity + 1)):     # 'stop' - искомое число фильмов, 'capacity' - число фильмов на одной странице сайта (14)
        url1 = url + link_genre + f'/page/{page}'
        r1 = requests.get(url1)
        sleep(random.randint(3, 5))                       # пауза в запросах, чтобы сервер не заблокировал выполнение программы
        soup1 = BeautifulSoup(r1.text, "lxml")
        films = soup1.findAll('div', class_='main_news')

# Цикл для извлечения частной инф-ции по каждому фильму
        for film in films:
            t += 1                                        # счётчик прохождения выполнения кода (для наглядности)
            print(t)
            if len(data) < stop:
                link = film.find('div', class_='mn_left_img').find('a', class_='link img').get('href')[:]               # ссылка на фильм
                name = film.find('h2', class_='zagolovok').text.rstrip()                                                # название фильма
                try:
                    genre1 = film.find('ul', class_='teaser_ads').text.split('\n')[2].split(':')[1].strip()             # жанр фильма
                except:
                    genre1 = '-'
                director = film.find('div', class_='mn_text').find('li', id='teaser_rej').text.split(":")[1].strip()    # режиссер фильма
                year = film.find('ul', class_='teaser_ads').text.split(':')[1].split()[0]                               # год выпуска фильма
                appearance = film.find('ul', class_='mn_links').text.split('\n')[1]                                     # дата появления на сайте
                buffer = link.split(';') + name.split(';') + genre1.split(';') + director.split(';') + year.split(';') + appearance.split(';')
                if buffer in data:  # исключаем попадание в базы данных повторений фильмов
                    break
                else:
                    data.append([link, name, genre1, director, year, appearance])  # база данных для одного фильма
                if buffer in dataAll:
                    break
                else:
                    dataAll.append([link, name, genre1, director, year, appearance])  # база данных для всех фильмов
            else:
                break

                    #   #   #   #   #   #    Create the empty csv files for each genre    #   #   #   #   #   #
# Создаю пустые csv файлы с методом .close() для очистки их же при каждом следующем запуске программы, т.о. пользователю
# будут доступны только "свежие" данные о фильмах.
for b in range(0, len(links_genres)):              # кол-во повторений = длине списка жанров на латинице
    with open('film_databaseTest_3/cinema_'+links_genres[b]+'_.csv', 'w') as template_file:
        writer = csv.writer(template_file)
        writer.writerow(
            ('link', 'name', 'genre', 'director', 'year', 'appearance')
        )
        template_file.close()

#   #   #   #   #   #    Create the csv file for all movies together    #   #   #   #   #   #
# Создаю пустой общий csv файл с методом .close() для очистки его же при каждом следующем запуске программы, т.о. пользователю
# будут доступны только "свежие" данные о фильмах.
with open('film_databaseTest_3/cinema_parsing_all_in_one.csv', 'w') as general_file:
    writer = csv.writer(general_file)
    writer.writerow(
        ('link', 'name', 'genre', 'director', 'year', 'appearance')
    )
    general_file.close()

# заполняем файл из базы данных для всех выбраных фильмов
for items in dataAll:
    with open('film_databaseTest_3/cinema_parsing_all_in_one.csv', 'a') as general_file:
        writer = csv.writer(general_file)
        writer.writerow(
            items
        )

# #   #   #   #   #   #    Fill the csv files for each genre with movies    #   #   #   #   #   #
# заполняем csv файлы из базы данных для всех выбраных фильмов
for g in range(0, len(links_genres)):                       # Цикл перебора названий жанров из их кол-ва (32)
    count = 0                                               # Счётчик для ограничения поиска (соотв-й условию не более - 'stop')
    for f in range(0, len(dataAll)):                        # Цикл перебора каждого фильма из общей базы данных
        if genres[g] in dataAll[f][2] and count < stop:     # Проверяем наличие названия жанра (кириллицей) в общей базе данных
            with open('film_databaseTest_3/cinema_' + links_genres[g] + '_.csv', 'a') as final_file:      # заполняем csv файлы
                writer = csv.writer(final_file)
                writer.writerow(
                    dataAll[f][:]
                )
                count += 1
        else:
            continue
