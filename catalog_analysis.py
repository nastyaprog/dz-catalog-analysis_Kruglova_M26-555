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

def print_non_comedy_titles(movies):
    '''печатает фильмы не комедии'''
    for film in movies:
        if 'comedy' in film['genres']:
            continue
        print(film['title'])

def find_first_masterpiece(movies):
    '''печатает первый шедевр с оценкой от 9'''
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

def titles_sorted_by_rating(movies):
    '''возвращает список названий фильмов, отсортированных по убыванию рейтинга'''
    sorted_movies = sorted(movies,
                           key = lambda film: film.get('rating'),
                           reverse = True)
    return [film.get('title', 'Нет названия') for film in sorted_movies]


def top_n_by_rating(movies: list[dict], n: int = 3) -> list[tuple[str, float | int]]:
    '''возвращает список из n кортежей (title, rating) — топ по рейтингу.'''
    sorted_movies = sorted(movies,
                           key = lambda film: film.get('rating'),
                           reverse = True)

    top_movies = sorted_movies[:n]

    return [(film.get('title', 'Нет названия'),
             film.get('rating', 'Нет оценки'))
            for film in top_movies
            ]

def count_by_genre(movies: list[dict]) -> dict[str, int]:
    '''возвращает словарь из жанра и количества фильмов'''
    genre_counts = {}
    for film in movies:
        genres = film.get('genres', [])

        for genre in genres:
            genre_counts[genre] = genre_counts.get(genre, 0) + 1

    return genre_counts


def actor_filmography(movies: list[dict]) -> dict[str, list[str]]:
    '''возвращает актера и список фильмов с ним в виде словаря'''
    actors_movies = {}
    for film in movies:
        actors = film.get('actors', [])
        title = film.get('title', 'Нет названия')

        for actor in actors:
            if actor not in actors_movies:
                actors_movies[actor] = []
            actors_movies[actor].append(title)
    return actors_movies

def all_genres(movies: list[dict]) -> set[str]:
    '''возвращает множество всех уникальных жанров каталога.'''
    result = set()

    for movie in movies:
        genres = movie.get('genres', [])
        result.update(genres)
    return result

def common_actors(movie1: dict, movie2: dict) -> set[str]:
    '''возвращает множество актеров, снимавшихся в обоих фильмах.'''
    actors_1 = set(movie1.get('actors', []))
    actors_2 = set(movie2.get('actors', []))
    result = actors_1 & actors_2

    return result

def genres_only_in_one(movies_a: list[dict], movies_b: list[dict]) -> set[str]:
    '''возвращает жанры, встречающиеся в movies_a, но не встречающиеся в movies_b'''

    genres_a = set()
    for film_a in movies_a:
        genres_a.update(film_a.get('genres', []))

    genres_b = set()
    for film_b in movies_b:
        genres_b.update(film_b.get('genres', []))

    return genres_a - genres_b


def iter_high_rated(movies, min_rating=8.0):
    '''отдает фильмы с рейтингом не ниже min_rating'''
    for film in movies:
        if film.get('rating', 0) >= min_rating:
            yield film

def show_high_rated_movies(movies, min_rating=8.0):
    """
    Демонстрирует работу генератора iter_high_rated: 
    печатает фильмы с рейтингом >= min_rating.
    """
    for film in iter_high_rated(movies, min_rating):
        print(format_report_line(film))

def total_duration_high_rated(movies, min_rating=7.0):
    """
    Возвращает суммарную длительность (в минутах) фильмов с рейтингом 
    не ниже min_rating.
    """
    return sum(
        film["duration_min"]
        for film in movies
        if film["rating"] > min_rating
    )

def build_report(movies):
    '''Собирает отчёт по каталогу из результатов всех предыдущих этапов.'''

    print("ОТЧеТ ПО КАТАЛОГУ")
    print(f"Средний рейтинг: {average_rating(movies)}")
    print(f"Средний возраст фильмов: {catalog_age_stats(movies, current_year=2026)[2]} лет")

    print("\nТоп-3 фильма:")
    #для каждого фильма m в списке movies сделаем запись, где ключ — название фильма, а значение — сам словарь фильма
    #так как top_n_by_rating возвращает только кортежи, а в format_report_line нужен словарь
    by_title = {m["title"]: m for m in movies}
    for title, _ in top_n_by_rating(movies, n=3):
        #передаём словарь в функцию
        print("  " + format_report_line(by_title[title]))

    print("\nФильмов по жанрам:")

    for genre, cnt in sorted(count_by_genre(movies).items(), 
    #У нас два критерия: Сначала — по количеству, по убыванию.
    #Решение: для количества используем минус, чтобы убывание стало возрастанием 
    #отрицательных чисел, а для названия оставляем как есть.
                             key = lambda item: (-item[1], item[0])):
        print(f"  {genre} — {cnt}")

    print(f'\nВсе жанры каталога: {", ".join(sorted(all_genres(movies)))}')


if __name__ == "__main__":
    build_report(movies)