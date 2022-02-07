import csv
from time import sleep
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

ag = str()
data = []
genres = []
x = 1         # variable (first page for searching)
y = 3       # variable ("n" page for searching)
stop = 10    # variable (which points how many films do we need)

#   #   #   #   #   #    Create a base of all genres    #   #   #   #   #   #

url = f'https://kinobar.vip/'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
categories = soup.find('ul', class_='cats_menu').find_all('a')
# print('type(categories)', type(categories), categories)
for cat in categories:
    count = 1
    # genre = cat.find('a').find('title')
    genre = cat.get('title')[:-7]
    link_genre = cat.get('href')
    names_folders_genres = link_genre.strip('/')
    genre = genre.split(';')
    genres += genre
    url_genre = url + link_genre
    # print(link_genre)
    # print(names_folders_genres)
    # print('link_genre', type(link_genre), link_genre)
    print(url_genre)
    for page in range(x, y):
        url1 = url + link_genre + f'/page/{page}'
        r1 = requests.get(url1)
        sleep(2)
        soup1 = BeautifulSoup(r1.text, "lxml")
        films = soup1.findAll('div', class_='main_news')
        if count <= 1:
            for film in films:
                link = film.find('div', class_='mn_left_img').find('a', class_='link img').get('href')[:]
                name = film.find('h2', class_='zagolovok').text.rstrip()
                genre1 = film.find('ul', class_='teaser_ads').text.split('\n')[2].split(':')[1].strip()
                director = film.find('div', class_='mn_text').find('li', id='teaser_rej').text.split(":")[1].strip()
                year = film.find('ul', class_='teaser_ads').text.split(':')[1].split()[0]
                appearance = film.find('ul', class_='mn_links').text.split('\n')[1]
                if len(data) <= 10:
                    data.append([link, name, genre1, director, year, appearance])
                    print(len(data))
                    count += 1
                    print(count)
                else:
                    break


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
# #   #   #   #   #   #    Create the csv files for each genres    #   #   #   #   #   #
# for d in range(0, len(agl_cl)):
#     with open('film_base/cinema_'+agl_cl[d]+'_.csv', 'w') as template_file:
#         writer = csv.writer(template_file)
#         writer.writerow(
#             ('link', 'name', 'genre', 'director', 'year', 'appearance')
#         )
#         template_file.close()
#
# #   #   #   #   #   #    Create the csv file for all movies together    #   #   #   #   #   #
# # header = ['link', 'name', 'genre', 'director', 'year', 'appearance']
# # df = pd.DataFrame(data, columns=header)
# # df.to_csv('film_base/cinema_parsing_all_in_one.csv', sep=';', encoding='utf-8')
#
# with open('film_base/cinema_parsing_all_in_one.csv', 'w') as general_file:
#     writer = csv.writer(general_file)
#     writer.writerow(
#         ('link', 'name', 'genre', 'director', 'year', 'appearance')
#     )
#     general_file.close()
#
# for items in data:
#     with open('film_base/cinema_parsing_all_in_one.csv', 'a') as general_file:
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
#             with open('film_base/cinema_' + agl_cl[g] + '_.csv', 'a') as final_file:
#                 writer = csv.writer(final_file)
#                 writer.writerow(
#                     data[f][:]
#                 )
#                 count += 1
#         else:
#             continue
#
#

