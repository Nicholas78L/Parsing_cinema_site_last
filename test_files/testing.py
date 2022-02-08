links_genres = ['novinki-kino', 'serialy', 'serialy-s-kazahstanskih-telekanalov', 'tv-shou-peredachi', 'aziatskie-serialy', 'tureckie-serialy', 'komedii', 'melodramy', 'dramy', 'boeviki', 'priklyucheniya', 'trillery', 'multfilmy', 'fantastika', 'semeynyy', 'biografiya', 'myuzikl', 'fentezi', 'dokumentalnye', 'uzhasyy', 'detektiv', 'mistika', 'vesterny', 'voennyy', 'istoriya', 'kriminal', 'sport', 'anime', 'na-inostrannom-yazyke', 'goblinskiy-perevod', 'kazahstanskoe-kino', 'rossiyskoe-kino']
genres = ['Новинки кино', 'Сериалы', 'Сериалы с Каз.ТВ сериалы', 'ТВ-шоу, передачи сериалы', 'Азиатские сериалы', 'Турецкие сериалы', 'Комедии', 'Мелодрамы', 'Драмы', 'Боевики', 'Приключения', 'Триллеры', 'Мультфильмы', 'Фантастика', 'Cемейный', 'Биография', 'Мюзикл', 'Фэнтези', 'Документальные', 'Ужасы', 'Детектив', 'Мистика', 'Вестерны', 'Военный', 'История', 'Криминал', 'Спорт', 'Аниме', 'На иностранном языке', 'Гоблинский Перевод', 'Казахстанское кино', 'Российское кино']

# together_dict = dict(zip(links_genres, genres))
# print('together_dict', type(together_dict), together_dict)
# new_list = together_dict.values()
# print('new_list', type(new_list), new_list)

x = ['https://kinobar.vip/25476-den-slepogo-valentina.html', 'День слепого Валентина', 'Комедии, Мелодрамы, Новинки кино, Российское кино, Фильмы 2022', 'Александр Баршак', '2022', 'Сегодня, 12:49']
y = ['d', 'e', 'f']
z = x + y
# print('x', type(x), x)
# print('z', type(z), z)

# data <class 'list'> [['https://kinobar.vip/25476-den-slepogo-valentina.html', 'День слепого Валентина', 'Комедии, Мелодрамы, Новинки кино, Российское кино, Фильмы 2022', 'Александр Баршак', '2022', 'Сегодня, 12:49'], ['https://kinobar.vip/16992-u-nee-drugoe-imya-v3.html', 'Другое имя', 'Драмы, Триллеры, Новинки кино, Российское кино, Фильмы 2022', 'Вета Гераськина', '2022', 'Сегодня, 12:47'], ['https://kinobar.vip/15686-zvezdnyy-razum-v2.html', 'Звёздный разум', 'Приключения, Триллеры, Фантастика, Новинки кино, Российское кино, Фильмы 2021', 'Вячеслав Лисневский', '2021', 'Вчера, 17:34'], ['https://kinobar.vip/24307-padenie-luny.html', 'Падение Луны', 'Боевики, Фантастика, Новинки кино, Фильмы 2022', 'Роланд Эммерих', '2022', '6 февраля 2022'], ['https://kinobar.vip/24583-mariya.html', 'Мария. Спасти Москву', 'Драмы, Военный, Новинки кино, Российское кино, Фильмы 2021', 'Вера Сторожева', '2021', '6 февраля 2022'], ['https://kinobar.vip/24424-kazn.html', 'Казнь', 'Триллеры, Новинки кино, Российское кино, Фильмы 2021', 'Ладо Кватания', '2021', '6 февраля 2022'], ['https://kinobar.vip/25755-iz-moego-okna.html', 'Из моего окна', 'Комедии, Мелодрамы, Драмы, Новинки кино, Фильмы 2022', 'Марсаль Форес', '2022', '5 февраля 2022'], ['https://kinobar.vip/25584-aferist-iz-tinder.html', 'Аферист из Tinder', 'Документальные, Криминал, Новинки кино, Фильмы 2022', 'Фелисити Моррис', '2022', '4 февраля 2022'], ['https://kinobar.vip/24230-svingery.html', 'Свингеры', 'Комедии, Мелодрамы, Новинки кино, Российское кино, Фильмы 2021', 'Андрейс Экис', '2021', '4 февраля 2022'], ['https://kinobar.vip/25389-lyubov-kak-bestseller.html', 'Любовь как бестселлер', 'Комедии, Мелодрамы, Новинки кино, Фильмы 2022', 'Аналейне Каль-и-Майор', '2022', '4 февраля 2022']]
dataAll = [['https://kinobar.vip/25476-den-slepogo-valentina.html', 'День слепого Валентина', 'Комедии, Мелодрамы, Новинки кино, Российское кино, Фильмы 2022', 'Александр Баршак', '2022', 'Сегодня, 12:49'], ['https://kinobar.vip/16992-u-nee-drugoe-imya-v3.html', 'Другое имя', 'Драмы, Триллеры, Новинки кино, Российское кино, Фильмы 2022', 'Вета Гераськина', '2022', 'Сегодня, 12:47'], ['https://kinobar.vip/15686-zvezdnyy-razum-v2.html', 'Звёздный разум', 'Приключения, Триллеры, Фантастика, Новинки кино, Российское кино, Фильмы 2021', 'Вячеслав Лисневский', '2021', 'Вчера, 17:34'], ['https://kinobar.vip/24307-padenie-luny.html', 'Падение Луны', 'Боевики, Фантастика, Новинки кино, Фильмы 2022', 'Роланд Эммерих', '2022', '6 февраля 2022'], ['https://kinobar.vip/24583-mariya.html', 'Мария. Спасти Москву', 'Драмы, Военный, Новинки кино, Российское кино, Фильмы 2021', 'Вера Сторожева', '2021', '6 февраля 2022'], ['https://kinobar.vip/24424-kazn.html', 'Казнь', 'Триллеры, Новинки кино, Российское кино, Фильмы 2021', 'Ладо Кватания', '2021', '6 февраля 2022'], ['https://kinobar.vip/25755-iz-moego-okna.html', 'Из моего окна', 'Комедии, Мелодрамы, Драмы, Новинки кино, Фильмы 2022', 'Марсаль Форес', '2022', '5 февраля 2022'], ['https://kinobar.vip/25584-aferist-iz-tinder.html', 'Аферист из Tinder', 'Документальные, Криминал, Новинки кино, Фильмы 2022', 'Фелисити Моррис', '2022', '4 февраля 2022'], ['https://kinobar.vip/24230-svingery.html', 'Свингеры', 'Комедии, Мелодрамы, Новинки кино, Российское кино, Фильмы 2021', 'Андрейс Экис', '2021', '4 февраля 2022'], ['https://kinobar.vip/25389-lyubov-kak-bestseller.html', 'Любовь как бестселлер', 'Комедии, Мелодрамы, Новинки кино, Фильмы 2022', 'Аналейне Каль-и-Майор', '2022', '4 февраля 2022']]
if x in dataAll:
    print("OK")



# stop = 4
# nfop = 14
#
# k = round((stop / nfop + 1))
# print('k', type(k), k)

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