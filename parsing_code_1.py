import csv
from time import sleep
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

ag = str()
data = []
count = 0

url0 = f'https://kinobar.vip/'
r0 = requests.get(url0)
soup0 = BeautifulSoup(r0.text, 'lxml')

x = 1                       # variable (first page for searching)
y = 3                      # variable ("n" page for searching)

#   #   #   #   #   #    Create a base of all genres    #   #   #   #   #   #
for p0 in range(x, y):
    print(p0)
    url0 = f"https://kinobar.vip/detektiv/page/{p0}"
    r0 = requests.get(url0)
    sleep(2)
    soup0 = BeautifulSoup(r0.text, "lxml")
    films0 = soup0.findAll('div', class_='main_news')

    for film0 in films0:
        try:
            genre0 = film0.find('ul', class_='teaser_ads').text.split('\n')[2].split(':')[1].strip()
        except:
            genre0 = '-'
        ag += ', ' + genre0          # ag => variable (all genres)

agl = ag.split(',')             # agl => variable (all genres list)

for i in range(len(agl)):
    agl[i] = agl[i].strip()

ag_set = set(agl)               # ag_set => variable (all genres set)
ag_set.pop()                    # crutch to remove first empty item in variable genre
agl_cl = list(ag_set)           # agl_cl => variable (all genres list cleaned)
print('agl_cl', len(agl_cl), type(agl_cl), agl_cl)

#   #   #   #   #   #    Create a base of all movies (data)    #   #   #   #   #   #
for p in range(x, y):
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
print('len(data)', len(data), type(data))

#   #   #   #   #   #    Create the csv files for each genres    #   #   #   #   #   #
for d in range(0, len(agl_cl)):
    with open('cinema_'+agl_cl[d]+'_.csv', 'w') as template_file:
        writer = csv.writer(template_file)
        writer.writerow(
            ('link', 'name', 'genre', 'director', 'year', 'appearance')
        )

#   #   #   #   #   #    Create the csv file for all movies together    #   #   #   #   #   #
header = ['link', 'name', 'genre', 'director', 'year', 'appearance']
df = pd.DataFrame(data, columns=header)
df.to_csv('cinema_parsing_all_in_one.csv', sep=';', encoding='utf-8')

#   #   #   #   #   #    Fill the csv files for each genre with movies    #   #   #   #   #   #
for g in range(0, len(agl_cl)):
    for f in range(0, len(data)):
        if agl_cl[g] in data[f][2]:
            with open('cinema_' + agl_cl[g] + '_.csv', 'a', ) as final_file:
                writer = csv.writer(final_file)
                writer.writerow(
                    data[f][:]
                )
