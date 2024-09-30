from create_tables import connect_to_db
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

    start_time = time.time()

    cursor.execute(id_query, (id,))

    execution_time = time.time() - start_time

    result = cursor.fetchall()

    return execution_time, result


def select_by_range(cursor, rating_min: float, rating_max: float):

    start_time = time.time()

    cursor.execute(range_query, (rating_min, rating_max))

    execution_time = time.time() - start_time

    result = cursor.fetchall()

    return execution_time, result


def join_movies_and_ratings(cursor, rating_min: float, rating_max: float):

    start_time = time.time()

    cursor.execute(join_query, (rating_min, rating_max))

    execution_time = time.time() - start_time

    result = cursor.fetchall()

    return execution_time, result


def group_by_title(cursor):

    start_time = time.time()

    cursor.execute(group_query)

    execution_time = time.time() - start_time

    result = cursor.fetchall()

    return execution_time, result


def select_by_genres(cursor, genres: list[str]):

    start = time.time()

    cursor.execute(genres_query, (genres,))

    execution_time = time.time() - start

    result = cursor.fetchall()

    return execution_time, result
