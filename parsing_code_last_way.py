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

#   #   #   #   #   #    Create a base of all genres    #   #   #   #   #   #

url = f'https://kinobar.vip/'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
categories = soup.find('ul', class_='cats_menu').find_all('a')
print('type(categories)', type(categories), categories)
for cat in categories:
    stop = 100  # variable (which points how many films do we need)
    data = []
    # genre = cat.find('a').find('title')
    films0 = soup.find('div', id='dle-content').findAll('div', class_='main_news') # For find out nfop
    nfop = len(films0[:])   # The number of films on the one page => 14 (without the movie of the day)
    genre = cat.get('title')[:-7]
    link_genre = cat.get('href').strip('/')  # in string format
    link_genre_l = link_genre.split()
    links_genres += link_genre_l
    names_folders_genres = link_genre.strip('/')
    genre = genre.split(';')
    genres += genre
    url_genre = url + link_genre

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
            else:
                break
            print('data', len(data), type(data), data)

  #   #   #   #   #    Create the csv files for each genre    #   #   #   #   #   #
for b in range(0, len(links_genres)):
    with open('film_base/cinema_'+links_genres[b]+'_.csv', 'w') as template_file:
        writer = csv.writer(template_file)
        writer.writerow(
            ('link', 'name', 'genre', 'director', 'year', 'appearance')
        )
        template_file.close()

#   #   #   #   #   #    Create the csv file for all movies together    #   #   #   #   #   #
# header = ['link', 'name', 'genre', 'director', 'year', 'appearance']
# df = pd.DataFrame(data, columns=header)
# df.to_csv('film_base/cinema_parsing_all_in_one.csv', sep=';', encoding='utf-8')

with open('film_base/cinema_parsing_all_in_one.csv', 'w') as general_file:
    writer = csv.writer(general_file)
    writer.writerow(
        ('link', 'name', 'genre', 'director', 'year', 'appearance')
    )
    general_file.close()

for items in dataAll:
    with open('film_base/cinema_parsing_all_in_one.csv', 'a') as general_file:
        writer = csv.writer(general_file)
        writer.writerow(
            items
        )

#   #   #   #   #   #    Fill the csv files for each genre with movies    #   #   #   #   #   #
together_dict = dict(zip(links_genres, genres))
new_list = together_dict.values()

for g in range(0, len(links_genres)):
    count = 0
    for f in range(0, len(dataAll)):
        if list(new_list)[g] in dataAll[f][2] and count <= (stop-1):
            with open('film_base/cinema_' + links_genres[g] + '_.csv', 'a') as final_file:
                writer = csv.writer(final_file)
                writer.writerow(
                    dataAll[f][:]
                )
                count += 1
        else:
            continue
