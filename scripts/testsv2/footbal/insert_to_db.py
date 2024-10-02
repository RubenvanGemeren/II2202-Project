from read import read_csv
import json
from connect_postgres import connect_to_db


games_path = "C:/Users/rvang/Documents/GitHub/II2202-Project/data/games.csv"
players_path = "C:/Users/rvang/Documents/GitHub/II2202-Project/data/players.csv"
line_ups_path = "C:/Users/rvang/Documents/GitHub/II2202-Project/data/game_lineups.csv"

insert_games_query = """
INSERT INTO games (id, season, date)
VALUES (%s, %s, %s)
ON CONFLICT (id) DO UPDATE
SET
    season = excluded.season,
    date = excluded.date
"""

insert_players_query = """
INSERT INTO players (id, name, last_season)
VALUES (%s, %s, %s)
ON CONFLICT (id) DO UPDATE
SET
    name = excluded.name,
    last_season = excluded.last_season
"""

insert_game_lineups_query = """
INSERT INTO game_lineups (id, date, game_id, player_id)
VALUES (%s, %s, %s, %s)
ON CONFLICT (id) DO UPDATE
SET
    date = excluded.date,
    game_id = excluded.game_id,
    player_id = excluded.player_id
"""

# Read data
games_df = read_csv(games_path)
players_df = read_csv(players_path)
game_line_ups_df = read_csv(line_ups_path)

# Get all player ids
player_ids = players_df["player_id"].unique()

# Remove all game_lineups that do not have a player_id in the players ids list
game_line_ups_df = game_line_ups_df[game_line_ups_df["player_id"].isin(player_ids)]

# Select columns
games_cols = ["game_id", "season", "date"]
games_modified = games_df[games_cols]

players_cols = ["player_id", "name", "last_season"]
players_modified = players_df[players_cols]

line_ups_cols = ["game_lineups_id", "date", "game_id", "player_id"]
line_ups_modified = game_line_ups_df[line_ups_cols]

# Drop rows with missing values
games_modified = games_modified.dropna(subset=["game_id", "season", "date"])
players_modified = players_modified.dropna(subset=["player_id", "name", "last_season"])
line_ups_modified = line_ups_modified.dropna(subset=["game_lineups_id", "date", "game_id", "player_id"])

# Drop duplicates
games_modified = games_modified.drop_duplicates(subset=["game_id"])
players_modified = players_modified.drop_duplicates(subset=["player_id"])
line_ups_modified = line_ups_modified.drop_duplicates(subset=["game_lineups_id"])

print(line_ups_modified.count())

conn = connect_to_db()
cursor = conn.cursor()

for index, row in games_modified.iterrows():
    cursor.execute(
        insert_games_query,
        (
            row["game_id"],
            row["season"],
            row["date"],
        ),
    )

print("Games inserted")

for index, row in players_modified.iterrows():
    cursor.execute(
        insert_players_query,
        (
            row["player_id"],
            row["name"],
            row["last_season"],
        ),
    )

print("Players inserted")

for index, row in line_ups_modified.iterrows():
    cursor.execute(
        insert_game_lineups_query,
        (
            row["game_lineups_id"],
            row["date"],
            row["game_id"],
            row["player_id"],
        ),
    )

print("Game lineups inserted")

conn.commit()
cursor.close()
conn.close()