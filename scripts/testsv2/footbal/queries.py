from create_tables import connect_to_db
import time


id_query = """
SELECT *
FROM game_lineups
WHERE id = %s
"""

range_query = """
SELECT *
FROM game_lineups
WHERE date BETWEEN %s AND %s
ORDER BY game_lineups.date DESC
"""

# range_query = """
# SELECT *
# FROM games
# WHERE season BETWEEN %s AND %s
# order by games.date DESC
# """

join_query = """
SELECT *
FROM game_lineups
JOIN players
ON game_lineups.player_id = players.id
WHERE game_lineups.date = '2013-07-27';
"""

# join_query = """
# SELECT *
# FROM game_lineups
# JOIN games
# ON game_lineups.game_id = games.id
# """

group_query = """
SELECT games.season, game_lineups.id
FROM game_lineups
JOIN games
ON game_lineups.game_id = games.id
WHERE games.season = '2013'
GROUP BY game_lineups.id, games.season;
"""

player_query = """
SELECT *
FROM players
WHERE name LIKE %s
"""


def get_id_array(cursor):

    cursor.execute("SELECT id FROM game_lineups")

    result = cursor.fetchall()

    id_array = [row[0] for row in result]

    return id_array


def select_by_id(cursor, id: int):

    start_time = time.time()

    cursor.execute(id_query, (id,))

    execution_time = time.time() - start_time

    result = cursor.fetchall()

    return execution_time, result


def select_by_range(cursor, date_min: str, date_max: str):

    start_time = time.time()

    cursor.execute(range_query, (date_min, date_max))

    execution_time = time.time() - start_time

    result = cursor.fetchall()

    return execution_time, result


def join_game_lineups_and_players(cursor):

    start_time = time.time()

    cursor.execute(join_query)

    execution_time = time.time() - start_time

    result = cursor.fetchall()

    return execution_time, result


def group_by_season(cursor):

    start_time = time.time()

    cursor.execute(group_query)

    execution_time = time.time() - start_time

    result = cursor.fetchall()

    return execution_time, result


def select_by_name(cursor, name: str):

    start = time.time()

    cursor.execute(player_query, (name,))

    execution_time = time.time() - start

    result = cursor.fetchall()

    return execution_time, result
