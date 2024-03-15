import requests
import textwrap

API = 'EXJ45X6-NF9MGN7-JA5CJJQ-M14FMA9'
URL = 'https://api.kinopoisk.dev/v1.4/movie/random'


def get_random_series(years, genres, url=URL):
    headers = {'X-API-KEY': API}
    params = {
        'notNullFields': ['name', 'description'],
        'type': ['tv-series'],
        'rating.kp': ['7-10'],
        'releaseYears.start': years,
        'genres.name': genres
    }
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        name = data['name']
        description = data['description']
        series_lenght = data['seriesLength']
        age_rating = data['ageRating']

        print(f'Название: {name}')
        print()
        print(f'Описание: {textwrap.fill(description, 100)}')
        print()
        print(f'Продолжительность одной серии: {series_lenght}')
        print(f'Возрастной рейтинг: {age_rating}')

    else:
        print('Не удалось подключиться')


series_years = [input('Введите год начала выпуска: ')]
series_genres = input('Введите через запятую какие жанры предпочитаете: ').split(', ')
print()
get_random_series(series_years, series_genres)




'''
изначально я делала эту лабу для хэд хантера, но у них нет API в открытом доступе. Для того, чтобы его получить надо сделать заявку на приложение. Я ее сделала, но ответа так и не получила, поэтому переделала свой код для кинопоиска
import requests
import textwrap

API = ''
URL = 'https://api.hh.ru/resumes/similar_vacancies'


def get_vacancy(area, salary, url=URL):
    headers = {'X-API-KEY': API}
    params = {
        'notNullFields': ['industry', 'department.description'],
        'experience': ['between1And3'],
        'area.name': area,
        'salary.from': salary
    }
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        industry = data['industry']
        description = data['department.description']
        schedule = data['schedule.name']
        employment = data['employment.name']

        print(f'Индустрия компании: {industry}')
        print()
        print(f'Описание работадателя: {textwrap.fill(description, 50)}')
        print()
        print(f'График работы {schedule}')
        print(f'Занятость: {employment}')

    else:
        print('Не удалось подключиться:(')


vacancy_area = [input('Введите область поиска вакансии: ')]
vacancy_salary = [input('Введите минимальную желаемую зарплату : ')]
print()
get_vacancy()
'''
