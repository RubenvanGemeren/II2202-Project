import time


id_query = """
SELECT * 
FROM ratings
WHERE movieId = %s
"""

range_query = """
SELECT *
FROM ratings
WHERE rating BETWEEN %s AND %s
ORDER BY ratings.rating DESC
"""

join_query = """
SELECT *
FROM ratings
JOIN movies 
ON ratings.movieId = movies.movieId
WHERE ratings.rating between 2 and 5
"""

group_query = """
SELECT ratings.movieId, movies.title, AVG(ratings.rating) as avg_rating
FROM ratings
JOIN movies
ON ratings.movieId = movies.movieId
GROUP BY ratings.movieId, movies.title
"""

genres_query = """
SELECT *
FROM movies
WHERE genres @> %s::varchar[]
"""


def get_id_array(cursor):

    cursor.execute("SELECT movieId FROM movies")

    result = cursor.fetchall()

    id_array = [row[0] for row in result]

    return id_array


def select_by_id(cursor, id: int):

    cursor.execute("BEGIN")
    start_time = time.perf_counter()

    cursor.execute(id_query, (id,))

    execution_time = time.perf_counter() - start_time

    cursor.execute("COMMIT")

    return execution_time


def select_by_range(cursor, rating_min: float, rating_max: float):

    cursor.execute("BEGIN")
    start_time = time.perf_counter()

    cursor.execute(range_query, (rating_min, rating_max))

    execution_time = time.perf_counter() - start_time

    return execution_time


def join_movies_and_ratings(cursor):

    cursor.execute("BEGIN")
    start_time = time.perf_counter()

    cursor.execute(join_query)

    execution_time = time.perf_counter() - start_time

    cursor.execute("COMMIT")

    return execution_time


def group_by_title(cursor):

    cursor.execute("BEGIN")
    start_time = time.perf_counter()

    cursor.execute(group_query)

    execution_time = time.perf_counter() - start_time

    cursor.execute("COMMIT")
    return execution_time


def select_by_genres(cursor, genres: list[str]):

    cursor.execute("BEGIN")

    start = time.perf_counter()

    cursor.execute(genres_query, (genres,))

    execution_time = time.perf_counter() - start

    cursor.execute("COMMIT")

    return execution_time
