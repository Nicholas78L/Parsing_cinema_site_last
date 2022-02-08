import csv
from time import sleep
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

dataAll = []
ag = str()
links_genres = []
genres = []
x = 1  # variable (first page for searching)
y = 3  # variable ("n" page for searching)

#   #   #   #   #   #    Create a base of all genres    #   #   #   #   #   #

url = f'https://kinobar.vip/'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
categories = soup.find('ul', class_='cats_menu').find_all('a')
print('type(categories)', type(categories), categories)
for cat in categories:
    stop = 20  # variable (which points how many films do we need)
    a = 0
    data = []
    # genre = cat.find('a').find('title')
    films0 = soup.find('div', id='dle-content').findAll('div', class_='main_news') # For find out capacity
    nfop = len(films0[:])   # The number of films on the one page => 14 (without the movie of the day)
    genre = cat.get('title')[:-7]
    link_genre = cat.get('href').strip('/')  # in string format
    link_genre_l = link_genre.split()
    links_genres += link_genre_l
    names_folders_genres = link_genre.strip('/')
    genre = genre.split(';')
    genres += genre
    url_genre = url + link_genre
    # print('capacity', type(capacity), capacity)
# print('genres', len(genres), genres)
#     print('link_genre', type(link_genre), link_genre)
# print('links_genres', len(links_genres), type(links_genres), links_genres)
# print(type(genre), 'genre', genre)
# print(type(names_folders_genres), names_folders_genres)
    for page in range(round(stop/nfop + 1)):
        k = round((stop/nfop + 1))
        print('k', type(k), k)
        url1 = url + link_genre + f'/page/{page}'
        r1 = requests.get(url1)
        sleep(1)
        soup1 = BeautifulSoup(r1.text, "lxml")
        films = soup1.findAll('div', class_='main_news')
        numer = len(films[:])  # The number of movies on the one page (14)
        print('numer', type(numer), numer)
        # print('films', type(films), films)
        # print(films)
        for film in films:
            if len(data) <= (stop-1):
                link = film.find('div', class_='mn_left_img').find('a', class_='link img').get('href')[:]
                name = film.find('h2', class_='zagolovok').text.rstrip()
                genre1 = film.find('ul', class_='teaser_ads').text.split('\n')[2].split(':')[1].strip()
                director = film.find('div', class_='mn_text').find('li', id='teaser_rej').text.split(":")[1].strip()
                year = film.find('ul', class_='teaser_ads').text.split(':')[1].split()[0]
                appearance = film.find('ul', class_='mn_links').text.split('\n')[1]
                data.append([link, name, genre1, director, year, appearance])
                dataAll.append([link, name, genre1, director, year, appearance])
                # a += 1
            else:
                break
            print('data', len(data), type(data), data)

  #   #   #   #   #    Create the csv files for each genre    #   #   #   #   #   #
for b in range(0, len(links_genres)):
    with open('film_database/cinema_'+links_genres[b]+'_.csv', 'w') as template_file:
        writer = csv.writer(template_file)
        writer.writerow(
            ('link', 'name', 'genre', 'director', 'year', 'appearance')
        )
        template_file.close()

#   #   #   #   #   #    Create the csv file for all movies together    #   #   #   #   #   #
# header = ['link', 'name', 'genre', 'director', 'year', 'appearance']
# df = pd.DataFrame(data, columns=header)
# df.to_csv('film_database/cinema_parsing_all_in_one.csv', sep=';', encoding='utf-8')

with open('film_database/cinema_parsing_all_in_one.csv', 'w') as general_file:
    writer = csv.writer(general_file)
    writer.writerow(
        ('link', 'name', 'genre', 'director', 'year', 'appearance')
    )
    general_file.close()

for items in dataAll:
    with open('film_database/cinema_parsing_all_in_one.csv', 'a') as general_file:
        writer = csv.writer(general_file)
        writer.writerow(
            items
        )

together_dict = dict(zip(links_genres, genres))
new_list = together_dict.values()

# print(type(together_dict.keys()), together_dict)
# keys = together_dict.keys()
# print('together_dict.values()', type(together_dict.values()), together_dict.values())
#
#
# print('together_dict', type(together_dict), together_dict)
# print(list(together_dict.values()))

#   #   #   #   #   #    Fill the csv files for each genre with movies    #   #   #   #   #   #
for g in range(0, len(links_genres)):
    count = 0
    for f in range(0, len(dataAll)):
        if list(new_list)[g] in dataAll[f][2] and count <= (stop-1):
            with open('film_database/cinema_' + links_genres[g] + '_.csv', 'a') as final_file:
                writer = csv.writer(final_file)
                writer.writerow(
                    dataAll[f][:]
                )
                count += 1
        else:
            continue



            #     print(len(data))
            #     count += 1
            #     print(count)
            # else:
            #     break

#     print('type(genre)', type(genre), genre)
# print(len(genres), 'type(genres)', type(genres), genres)

# gl = genres.split(';')
# print('type(gl)', type(gl), gl)

# <li><a href="/trillery/" title="Триллеры онлайн">Триллеры</a></li>
# <li><a href="/multfilmy/" title="Мультфильмы онлайн">Мультфильмы</a></li>
# <li><a href="/fantastika/" title="Фантастика онлайн">Фантастика</a></li>
# <li><a href="/semeynyy/" title="Cемейный онлайн">Cемейный</a></li>

# for p0 in range(x, y):
#     print(p0)
#     url0 = f"https://kinobar.vip/detektiv/page/{p0}"
#     r0 = requests.get(url0)
#     sleep(1)
#     soup0 = BeautifulSoup(r0.text, "lxml")
#     films0 = soup0.findAll('div', class_='main_news')
#
#     for film0 in films0:
#         genre0 = film0.find('ul', class_='teaser_ads').text.split('\n')[2].split(':')[1].strip()
#         print('type(genre0)', type(genre0), genre0)
#         genreAll = film0.find('ul', class_='cats_menu').text.split('\n')[2].split(':')[1].strip()
# print('type(genreAll)', type(genreAll), genreAll)
#         try:
#             genre0 = film0.find('ul', class_='teaser_ads').text.split('\n')[2].split(':')[1].strip()
#         except:
#             genre0 = '-'
# print('type(genre0)', type(genre0), genre0)
#         ag += ', ' + genre0          # ag => variable (all genres)
#
# agl = ag.split(',')             # agl => variable (all genres <type = list>)
#
# for i in range(len(agl)):
#     agl[i] = agl[i].strip()
#
# ag_set = set(agl)               # ag_set => variable (all genres <type = set>)
# ag_set.pop()                    # crutch to remove first empty item in variable genre
# agl_cl = list(ag_set)           # agl_cl => variable (all genres list cleaned)
# print('agl_cl', len(agl_cl), type(agl_cl), agl_cl)
#
# #   #   #   #   #   #    Create a base of all movies (data)    #   #   #   #   #   #
# for p in range(x, y):
#     print(p)
#     url = f"https://kinobar.vip/detektiv/page/{p}"
#     r = requests.get(url)
#     sleep(2)
#     soup = BeautifulSoup(r.text, "lxml")
#     films = soup.findAll('div', class_='main_news')
#     for film in films:
#         link = film.find('div', class_='mn_left_img').find('a', class_='link img').get('href')[:]
#         name = film.find('h2', class_='zagolovok').text.rstrip()
#         try:
#             genre = film.find('ul', class_='teaser_ads').text.split('\n')[2].split(':')[1].strip()
#         except:
#             genre = '-'
#         director = film.find('div', class_='mn_text').find('li', id='teaser_rej').text.split(":")[1].strip()
#         year = film.find('ul', class_='teaser_ads').text.split(':')[1].split()[0]
#         appearance = film.find('ul', class_='mn_links').text.split('\n')[1]
#
#         data.append([link, name, genre, director, year, appearance])
# print('len(data)', len(data), type(data))
#
# #   #   #   #   #   #    Create the csv files for each genre    #   #   #   #   #   #
# for d in range(0, len(agl_cl)):
#     with open('film_database/cinema_'+agl_cl[d]+'_.csv', 'w') as template_file:
#         writer = csv.writer(template_file)
#         writer.writerow(
#             ('link', 'name', 'genre', 'director', 'year', 'appearance')
#         )
#         template_file.close()
#
# #   #   #   #   #   #    Create the csv file for all movies together    #   #   #   #   #   #
# # header = ['link', 'name', 'genre', 'director', 'year', 'appearance']
# # df = pd.DataFrame(data, columns=header)
# # df.to_csv('film_database/cinema_parsing_all_in_one.csv', sep=';', encoding='utf-8')
#
# with open('film_database/cinema_parsing_all_in_one.csv', 'w') as general_file:
#     writer = csv.writer(general_file)
#     writer.writerow(
#         ('link', 'name', 'genre', 'director', 'year', 'appearance')
#     )
#     general_file.close()
#
# for items in data:
#     with open('film_database/cinema_parsing_all_in_one.csv', 'a') as general_file:
#         writer = csv.writer(general_file)
#         writer.writerow(
#             items
#         )
#
# #   #   #   #   #   #    Fill the csv files for each genre with movies    #   #   #   #   #   #
# for g in range(0, len(agl_cl)):
#     count = 1
#     for f in range(0, len(data)):
#         if agl_cl[g] in data[f][2] and count <= stop:
#             with open('film_database/cinema_' + agl_cl[g] + '_.csv', 'a') as final_file:
#                 writer = csv.writer(final_file)
#                 writer.writerow(
#                     data[f][:]
#                 )
#                 count += 1
#         else:
#             continue
#
#
