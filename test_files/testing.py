links_genres = ['novinki-kino', 'serialy', 'serialy-s-kazahstanskih-telekanalov', 'tv-shou-peredachi', 'aziatskie-serialy', 'tureckie-serialy', 'komedii', 'melodramy', 'dramy', 'boeviki', 'priklyucheniya', 'trillery', 'multfilmy', 'fantastika', 'semeynyy', 'biografiya', 'myuzikl', 'fentezi', 'dokumentalnye', 'uzhasyy', 'detektiv', 'mistika', 'vesterny', 'voennyy', 'istoriya', 'kriminal', 'sport', 'anime', 'na-inostrannom-yazyke', 'goblinskiy-perevod', 'kazahstanskoe-kino', 'rossiyskoe-kino']
genres = ['Новинки кино', 'Сериалы', 'Сериалы с Каз.ТВ сериалы', 'ТВ-шоу, передачи сериалы', 'Азиатские сериалы', 'Турецкие сериалы', 'Комедии', 'Мелодрамы', 'Драмы', 'Боевики', 'Приключения', 'Триллеры', 'Мультфильмы', 'Фантастика', 'Cемейный', 'Биография', 'Мюзикл', 'Фэнтези', 'Документальные', 'Ужасы', 'Детектив', 'Мистика', 'Вестерны', 'Военный', 'История', 'Криминал', 'Спорт', 'Аниме', 'На иностранном языке', 'Гоблинский Перевод', 'Казахстанское кино', 'Российское кино']

together_dict = dict(zip(links_genres, genres))
print('together_dict', type(together_dict), together_dict)
new_list = together_dict.values()
print('new_list', type(new_list), new_list)


# dataAll[f][2] <class 'str'> Сериалы, Драмы, Триллеры, Криминал, Сериалы с Каз.ТВ
# genres[2] <class 'str'> Сериалы с Каз.ТВ сериалы



# print(type(together_dict.keys()), together_dict)
# keys = together_dict.keys()
# print('together_dict.values()', type(together_dict.values()), together_dict.values())
#
#
# print('together_dict', type(together_dict), together_dict)
# print(list(together_dict.values()))
# new_list = together_dict.values()
# print('new_list', type(new_list), new_list)
# print(list(new_list)[2])
# for g in range(0, len(links_genres)):
#     count = 0
#     for f in range(0, len(dataAll)):
#         if links_genres[g] in dataAll[f][2] and count <= stop:
#             with open('film_database/cinema_' + links_genres[g] + '_.csv', 'a') as final_file:
#                 writer = csv.writer(final_file)
#                 writer.writerow(
#                     dataAll[f][:]
#                 )
#                 count += 1
#         else:
#             continue