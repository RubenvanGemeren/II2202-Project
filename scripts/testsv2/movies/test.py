from connect_postgres import connect_to_db
from queries import get_id_array
import json
import re
from decimal import Decimal


range_query = """
explain analyze 
SELECT *
FROM ratings
WHERE rating BETWEEN %s AND %s
ORDER BY ratings.rating DESC
"""

join_query = """
explain analyze
SELECT *
FROM movies
JOIN ratings 
ON ratings.movieId = movies.movieId
"""

genres_query = """
explain analyze 
SELECT *
FROM movies
WHERE genres @> %s::varchar[]
"""


conn = connect_to_db()
cursor = conn.cursor()

id = get_id_array(cursor)

cursor.execute(genres_query, (["action", "comedy"],))

result = cursor.fetchall()

execution_time_str = result[len(result) - 1][0]
execution_time = Decimal(re.findall(r"\d+\.\d+", execution_time_str)[0])

print(execution_time)
