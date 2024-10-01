from connect_postgres import connect_to_db


# Home club id and away club id could be used to join with clubs table
create_games_table = """
CREATE TABLE games(
    id INTEGER PRIMARY KEY,
    season INTEGER,
    date DATE
);
"""

# Current club id could be used to join with clubs table
create_players_table = """
CREATE TABLE players(
    id INTEGER PRIMARY KEY,
    name VARCHAR,
    last_season INTEGER
);
"""
# Club id could be used to join with clubs table
create_game_lineups_table = """
CREATE TABLE game_lineups(
    id VARCHAR PRIMARY KEY,
    date DATE,
    game_id INTEGER REFERENCES games(id),
    player_id INTEGER REFERENCES players(id)
);
"""
# Club id could be used to join with clubs table
# create_clubs_table = """
# CREATE TABLE clubs(
#     id INTEGER PRIMARY KEY,
#     squad_size INTEGER
# );
# """


conn = connect_to_db()
cursor = conn.cursor()

# cursor.execute(create_games_table)
# cursor.execute(create_players_table)
# cursor.execute(create_game_lineups_table)
# cursor.execute(create_clubs_table)