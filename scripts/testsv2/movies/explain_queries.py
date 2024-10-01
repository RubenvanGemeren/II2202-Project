import time
from decimal import Decimal
import re

id_query = """
EXPLAIN ANALYZE
SELECT * 
FROM ratings
WHERE movieId = %s
"""

range_query = """
EXPLAIN ANALYZE
SELECT *
FROM ratings
WHERE rating BETWEEN %s AND %s
ORDER BY ratings.rating DESC
"""

join_query = """
EXPLAIN ANALYZE
SELECT *
FROM ratings
JOIN movies 
ON ratings.movieId = movies.movieId
"""

group_query = """
EXPLAIN ANALYZE
SELECT ratings.movieId, movies.title, AVG(ratings.rating) as avg_rating
FROM ratings
JOIN movies
ON ratings.movieId = movies.movieId
GROUP BY ratings.movieId, movies.title
"""

genres_query = """
EXPLAIN ANALYZE
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

    cursor.execute(id_query, (id,))

    result = cursor.fetchall()
    execution_time_str = result[len(result) - 1][0]
    execution_time = Decimal(re.findall(r"\d+\.\d+", execution_time_str)[0])

    return execution_time


def select_by_range(cursor, rating_min: float, rating_max: float):

    cursor.execute(range_query, (rating_min, rating_max))

    result = cursor.fetchall()
    execution_time_str = result[len(result) - 1][0]
    execution_time = Decimal(re.findall(r"\d+\.\d+", execution_time_str)[0])

    return execution_time


def join_movies_and_ratings(cursor):

    cursor.execute(join_query)

    result = cursor.fetchall()
    execution_time_str = result[len(result) - 1][0]
    execution_time = Decimal(re.findall(r"\d+\.\d+", execution_time_str)[0])

    return execution_time


def group_by_title(cursor):

    cursor.execute(group_query)

    result = cursor.fetchall()
    execution_time_str = result[len(result) - 1][0]
    execution_time = Decimal(re.findall(r"\d+\.\d+", execution_time_str)[0])

    return execution_time


def select_by_genres(cursor, genres: list[str]):

    cursor.execute(genres_query, (genres,))

    result = cursor.fetchall()
    execution_time_str = result[len(result) - 1][0]
    execution_time = Decimal(re.findall(r"\d+\.\d+", execution_time_str)[0])

    return execution_time
