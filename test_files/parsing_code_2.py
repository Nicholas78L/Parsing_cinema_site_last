from time import sleep
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

z = set()
ag = str()
data = []
data_boevik =[]
data_drama =[]

for p in range(1, 3):
    print(p)
    url = f"https://kinobar.vip/detektiv/page/{p}"
    r = requests.get(url)
    sleep(2)
    soup = BeautifulSoup(r.text, "lxml")
    films = soup.findAll('div', class_='main_news')

    for film in films:
        link = film.find('div', class_='mn_left_img').find('a', class_='link img').get('href')[:]
        name = film.find('h2', class_='zagolovok').text.rstrip()
        try:
            genre = film.find('ul', class_='teaser_ads').text.split('\n')[2].split(':')[1].strip()
        except:
            genre = '-'
        director = film.find('div', class_='mn_text').find('li', id='teaser_rej').text.split(":")[1].strip()
        year = film.find('ul', class_='teaser_ads').text.split(':')[1].split()[0]
        appearance = film.find('ul', class_='mn_links').text.split('\n')[1]

        data.append([link, name, genre, director, year, appearance])


ag_1 = ''     # variable (all genres)
ag_list = []  # variable (all genres list)
ags = {}      # variable (all genres set)
ag_cl = []    # variable (all genres cleaned list)
for n in range(0, len(data)):
    ag_1 += ', ' + data[n][2]
print('ag_1', 'type(ag_1)', type(ag_1), ag_1)
ag_list = ag_1.split(',')
ags = set(ag_list)
ags.pop()
ag_cl = list(ags)
print('type(ag_cl)', type(ag_cl), 'len(ag_cl)', len(ag_cl), ag_cl)
print('data', type(data), len(data), '\n', data)
print('data[0][2]', type(data[0][2]), data[0][2])
print('ag_cl[n]', type(ag_cl[1]), ag_cl[1])
#
# for k in range(0, len(ag_cl)):
#     for t in range(0, len(data)):
#         if ag_cl[k] in data[t][2]:
#             data+{k} = data.append()


#
# ag += ', ' + genre          # ag => variable (all genres)
#
# print('type(ag)', type(ag), ag)
#
# agl = ag.split(',')             # agl => variable (all genres list)
# print('agl', type(agl), agl)
#
# for i in range(len(agl)):
#     agl[i] = agl[i].strip()
# print(agl)
#
# ag_set = set(agl)               # ag_set => variable (all genres set)
# ag_set.pop()                    # crutch to remove first empty item in variable genre
# agl_cl = list(ag_set)           # agl_cl => variable (all genres list cleaned)
# print('agl_cl', len(agl_cl), type(agl_cl), agl_cl)
# print('agl_cl[0]', agl_cl[0])
#
# print('type(genre0)', type(genre), genre)
# print(data)
# print('len(data)', len(data))
#
# for n in range(0, len(agl_cl)):








        # if genre == 'Боевики':
        #     data_boevik.append([link, name, genre, director, year, appearance])
        #     # print("OK")
        #     # print('type(genre)', type(genre))
        # if genre == 'Драмы':
        #     data_drama.append([link, name, genre, director, year, appearance])

        # header = ['link', 'name', 'genre', 'director', 'year', 'appearance']
        # df = pd.DataFrame(data, columns=header)
        # df.to_csv('kino_parsing.csv', sep=';', encoding='utf-8')

#
# #
#         ag += ', ' + genre          # ag => variable (all genres)
#
# print('type(ag)', type(ag), ag)
#
# agl = ag.split(',')             # agl => variable (all genres list)
# print('agl', type(agl), agl)
#
# for i in range(len(agl)):
#     agl[i] = agl[i].strip()
# print(agl)
#
# ag_set = set(agl)               # ag_set => variable (all genres set)
# ag_set.pop()                    # crutch to remove first empty item in variable genre
# agl_cl = list(ag_set)           # agl_cl => variable (all genres list cleaned)
# print('agl_cl', len(agl_cl), type(agl_cl), agl_cl)
# print('agl_cl[0]', agl_cl[0])
#
# print('type(genre)', type(genre), genre)
