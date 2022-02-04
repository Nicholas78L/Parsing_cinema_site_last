import csv
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

url0 = f'https://kinobar.vip/'
r0 = requests.get(url0)
soup0 = BeautifulSoup(r0.text, 'lxml')

x = 1
y = 20

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

print('type(ag)', type(ag), ag)

agl = ag.split(',')             # agl => variable (all genres list)
print('agl', type(agl), agl)

for i in range(len(agl)):
    agl[i] = agl[i].strip()
print(agl)

ag_set = set(agl)               # ag_set => variable (all genres set)
ag_set.pop()                    # crutch to remove first empty item in variable genre
agl_cl = list(ag_set)           # agl_cl => variable (all genres list cleaned)
print('agl_cl', len(agl_cl), type(agl_cl), agl_cl)
print('agl_cl[0]', agl_cl[0])

print('type(genre0)', type(genre0), genre0)

count = 0
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


for d in range(0, len(agl_cl)):
    with open('cinema_'+agl_cl[d]+'_.csv', 'w') as template_file:
        writer = csv.writer(template_file)
        writer.writerow(
            ('link', 'name', 'genre', 'director', 'year', 'appearance')
        )

for k in range(0, len(agl_cl)):
    for t in range(0, len(data)):
        if agl_cl[k] in data[t][2]:
            with open('cinema_'+agl_cl[k]+'_.csv', 'a') as final_file:
                writer = csv.writer(final_file)
                writer.writerow(
                    data[t][:]
                )
