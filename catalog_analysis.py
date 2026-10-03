movies = [
    {"title": "The Dune Chronicles", "year": 2021, "genres": {"sci-fi", "drama"},
     "rating": 8.6, "duration_min": 155, "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]},
    {"title": "Kitchen Stories", "year": 2019, "genres": {"comedy", "drama"},
     "rating": 7.1, "duration_min": 98, "actors": ["A. Novak", "M. Ferguson"]},
    {"title": "silent hours", "year": 2016, "genres": {"thriller", "drama"},
     "rating": 6.4, "duration_min": 112, "actors": ["J. Bloom", "K. Lee"]},
    {"title": "Comet Racers", "year": 2023, "genres": {"sci-fi", "action"},
     "rating": 5.9, "duration_min": 101, "actors": ["O. Isaac", "P. Diaz"]},
    {"title": "The Last Bakery", "year": 2014, "genres": {"comedy"},
     "rating": 7.8, "duration_min": 89, "actors": ["A. Novak", "T. Chalamet"]},
    {"title": "midnight in oslo", "year": 2020, "genres": {"thriller", "mystery"},
     "rating": 8.9, "duration_min": 124, "actors": ["K. Lee", "R. Ferguson"]},
    {"title": "Garden of Static", "year": 2022, "genres": {"drama"},
     "rating": 4.8, "duration_min": 137, "actors": ["P. Diaz", "J. Bloom"]},
    {"title": "The Quiet Algorithm", "year": 2024, "genres": {"sci-fi", "drama"},
     "rating": 9.2, "duration_min": 118, "actors": ["M. Ferguson", "O. Isaac"]},
    {"title": "Two Left Shoes", "year": 2011, "genres": {"comedy"},
     "rating": 6.0, "duration_min": 95, "actors": ["A. Novak", "K. Lee"]},
    {"title": "Red Harbor", "year": 2018, "genres": {"action", "thriller"},
     "rating": 7.3, "duration_min": 129, "actors": ["P. Diaz", "T. Chalamet"]},
]

def average_rating(movies: list[dict]) -> float:
    '''возвращает среднюю оценку по каталогу, округленную до одного знака (round)'''
    if not movies:
        return 0.00
    #проход по словарям внутри списка и сразу ищу сумму оценок
    sum_rate = sum(film['rating'] for film in movies)
    return round(sum_rate / len(movies), 1)

import math

def catalog_age_stats(movies: list[dict], current_year: int = 2026) -> tuple[int, int, int]:
    '''возвращает кортеж (самый старый фильм в годах, самый новый фильм в годах,
     среднее), где среднее округлено вверх до целого с помощью math.ceil.'''
    if not movies:
        return (0, 0, 0)

    movies_ages = [current_year - film['year'] for film in movies]
    #print(movies_ages)
    oldest = max(movies_ages)
    newest = min(movies_ages)
    average_age = math.ceil(sum(movies_ages) / len(movies_ages))

    return (oldest, newest, average_age)

def duration_in_hours(minutes: int) -> str:
    '''переводит минуты в формат "2ч 35м", используя целочисленное деление
    и остаток от деления.'''
    if not minutes:
        return 0
    hours = minutes // 60
    mins = minutes % 60
    return(f'{hours}ч {mins}м')

def rating_tier(rating: float) -> str:
    '''по оценке возвращает категорию: "шедевр" (≥9), "хорошо" (7–8.9),
    "средне" (5–6.9), "слабо" (<5)'''

    return 'шедевр' if rating >= 9 else ('хорошо' if rating >=7 
                                         else ('средне' if rating >=5 
                                               else 'слабо'))

def decade_label(year):
    '''возвращает метку "новые" (после 2020), "недавние" (2015–2020)
    или "старые" (раньше 2015)'''
    match year:
        case _ if year > 2020:
            return 'новые'
        case _ if 2015 <= year <= 2020:
            return 'недавние'
        case _ if year < 2015:
            return 'старые'

for film in movies:
    if 'comedy' in film['genres']:
        continue
    print(film['title'])

i = 0
while i < len(movies):
    if movies[i]['rating'] > 9.0:
        print(movies[i]['title'])
        break
    i += 1
else:
    print('Шедевров не найдено')

def count_long_movies(movies: list[dict], threshold: int = 120) -> int:
    '''считает количество фильмов длиннее threshold минут'''
    result = 0
    for film in movies:
        if film['duration_min'] > threshold:
            result += 1
    return result

def normalize_title(title:str) -> str:
    '''приводит строку к формату Title Case'''
    title_split = title.split()

    title_case = []
    for word in title_split:
        if not word:
            continue

        title_case.append(word[0].upper() + word[1:])

    result = ' '.join(title_case)
    return result

def make_slug(title:str) -> str:
    '''превращает нормализованное название в «слаг» 
    вида the-quiet-algorithm'''
    slug_title = title.lower().replace(' ', '-')
    return slug_title

def format_report_line(movie: dict) -> str:
    '''возвращает единую строку с описанием фильма.'''
    title = normalize_title(movie.get('title', '')) #обработка заголовков с мал буквы
    year = movie.get('year')
    rate = movie.get('rating')
    duration = duration_in_hours(movie.get('duration_min'))
    unsorted_genres = movie.get('genres', [])
    sorted_genres = ', '.join(sorted(unsorted_genres)) if unsorted_genres else 'жанр не определен'

    return f'"{title}" ({year}) — {rate}/10, {duration}, жанры: {sorted_genres}'




