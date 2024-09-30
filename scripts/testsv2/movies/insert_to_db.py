from read import read_csv
import json
from connect_postgres import connect_to_db


movies_path = "../../../data/movies/movies_metadata.csv"
ratings_path = "../../../data/movies/ratings.csv"
links_path = "../../../data/movies/links.csv"

insert_movies_query = """
INSERT INTO movies (movieId, title, budget, genres)
VALUES (%s, %s, %s, %s)
ON CONFLICT (movieId) DO UPDATE
SET
    title = excluded.title,
    budget = excluded.budget,
    genres = excluded.genres
"""

insert_ratings_query = """
INSERT INTO ratings (userId, movieId, rating)
VALUES (%s, %s, %s)
"""

# Get mapping of movieId to rating Id
links_df = read_csv(links_path)
links_df = links_df.dropna(subset=["movieId", "tmdbId"])
links_df = links_df.drop_duplicates(subset=["movieId"])

# Create dictionary mapping tmdbId to movieId
tmdb_movie_dict = dict(
    zip(links_df["tmdbId"].astype(int), links_df["movieId"].astype(int))
)

# Read data
movies_df = read_csv(movies_path)

# Drop rows that was read incorrectly
movies_df = movies_df[movies_df["id"].astype(str).str.isdigit()]
movies_df["id"] = movies_df["id"].astype(int)

# Select columns
cols = ["id", "title", "genres", "budget"]
movies_modified = movies_df[cols]

# Map tmdbId to movieId
movies_modified = movies_modified.rename(columns={"id": "tmdbId"})
movies_modified["tmdbId"] = movies_modified["tmdbId"].astype(int).map(tmdb_movie_dict)
# Rename id column to movieId
movies_modified = movies_modified.rename(columns={"tmdbId": "movieId"})

# Drop rows with missing values
movies_modified = movies_modified.dropna(
    subset=["movieId", "title", "budget", "genres"]
)
# Drop duplicates
movies_modified = movies_modified.drop_duplicates(subset=["movieId"])

# Convert genres to list of strings
movies_modified["genres"] = (
    movies_modified["genres"]
    .apply(lambda x: json.loads(x.replace("'", '"')))
    .apply(lambda x: [i["name"] for i in x])
)

print(movies_modified.head())

ratings_df = read_csv(ratings_path)
ratings_df = ratings_df.drop(columns=["timestamp"])
ratings_df = ratings_df.head(int(len(ratings_df) * 0.003))

ratings_df = ratings_df[ratings_df["movieId"].isin(movies_modified["movieId"])]

print(ratings_df.head())

conn = connect_to_db()
cursor = conn.cursor()

for index, row in movies_modified.iterrows():
    cursor.execute(
        insert_movies_query,
        (
            row["movieId"],
            row["title"],
            row["budget"],
            row["genres"],
        ),
    )

print("Movies inserted")

ratings_inserted = 0

for index, row in ratings_df.iterrows():
    cursor.execute(
        insert_ratings_query,
        (
            row["userId"],
            row["movieId"],
            row["rating"],
        ),
    )
    ratings_inserted += 1
    if ratings_inserted % 100_000 == 0:
        print(f"{ratings_inserted} ratings inserted")
