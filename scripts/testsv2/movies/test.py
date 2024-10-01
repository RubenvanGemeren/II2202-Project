from connect_postgres import connect_to_db
from queries import get_id_array
import json


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


conn = connect_to_db()
cursor = conn.cursor()

id = get_id_array(cursor)

cursor.execute(join_query)

result = cursor.fetchall()

print(result)
# print(result[len(result) - 1][0])
