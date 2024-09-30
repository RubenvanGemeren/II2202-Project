from create_tables import connect_to_db


id_query = """
SELECT * 
FROM ratings
WHERE movieId = %s
"""

range_query = """
SELECT *
FROM ratings
WHERE rating BETWEEN %s AND %s
"""

join_query = """
SELECT *
FROM movies
JOIN ratings 
ON movies.movieId = ratings.movieId
WHERE avg_rating BETWEEN %s AND %s
ORDER BY avg_rating DESC
"""

group_query = """
SELECT *
FROM ratings
JOIN movies
ON ratings.movieId = movies.movieId
GROUP BY movies.title
"""


def select_by_id(id: str):
    con = connect_to_db()
    cursor = con.cursor()

    cursor.execute(id_query, (id,))

    result = cursor.fetchall()

    return result


def select_by_range(budget_min: int, budget_max: int):
    con = connect_to_db()
    cursor = con.cursor()

    cursor.execute(range_query, (budget_min, budget_max))

    result = cursor.fetchall()

    return result


def join_movies_and_ratings(rating_min: float, rating_max: float):
    con = connect_to_db()
    cursor = con.cursor()

    cursor.execute(join_query, (rating_min, rating_max))

    result = cursor.fetchall()

    return result


def group_by_title():
    con = connect_to_db()
    cursor = con.cursor()

    cursor.execute(group_query)

    result = cursor.fetchall()

    return result
